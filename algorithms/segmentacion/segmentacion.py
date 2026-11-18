from __future__ import annotations

import numpy as np
from PyQt6.QtGui import QImage
from scipy import ndimage
from skimage.feature import peak_local_max
from skimage.filters import threshold_local
from skimage.segmentation import flood, slic, watershed


_METODO_UMBRAL = "Umbralizacion"
_METODO_ADAPTATIVO = "Umbralización adaptativa"
_METODO_WATERSHED = "Watershed"
_METODO_KMEANS = "K-means"
_METODO_REGION_GROWING = "Region Growing"
_METODO_SLIC = "SLIC (Superpixeles)"


def segmentar(
    imagen: QImage,
    metodo: str,
    umbral_min: int = 127,
    umbral_max: int = 255,
    tamano_bloque: int = 11,
    constante: float = 2.0,
    invertir: bool = False,
    distancia_min: int = 3,
    distancia_max: int = 255,
    conectividad: int = 8,
    kernel: int = 3,
    tolerancia: int = 20,
    semilla: tuple[int, int] | None = None,
    numero_clusters: int = 3,
    numero_superpixeles: int = 200,
    compactness: float = 10.0,
) -> QImage:
    if imagen.isNull():
        raise ValueError("La imagen está vacía.")
    if not 0 <= umbral_min <= umbral_max <= 255:
        raise ValueError("El rango de umbrales no es válido.")
    if metodo == _METODO_WATERSHED:
        if not 1 <= distancia_min <= distancia_max <= 255:
            raise ValueError("El rango de distancias no es válido.")
        if conectividad not in (4, 8):
            raise ValueError("La conectividad debe ser de 4 u 8 vecinos.")
        if kernel not in (3, 5, 7):
            raise ValueError("El kernel debe ser de 3, 5 o 7.")
    if metodo == _METODO_REGION_GROWING:
        if conectividad not in (4, 8):
            raise ValueError("La conectividad debe ser de 4 u 8 vecinos.")
        if not 0 <= tolerancia <= 255:
            raise ValueError("La tolerancia debe estar entre 0 y 255.")
    if metodo == _METODO_KMEANS and numero_clusters < 1:
        raise ValueError("El número de clusters debe ser mayor que 0.")
    if metodo == _METODO_SLIC:
        if numero_superpixeles < 1:
            raise ValueError("El número de superpíxeles debe ser mayor que 0.")
        if compactness <= 0:
            raise ValueError("Compactness debe ser mayor que 0.")

    gris = _leer_gris(imagen)
    if metodo == _METODO_UMBRAL:
        mascara = (gris >= umbral_min) & (gris <= umbral_max)
        if invertir:
            mascara = ~mascara
        return _crear_imagen_mascara(mascara)

    if metodo == _METODO_ADAPTATIVO:
        bloque = max(3, tamano_bloque)
        if bloque % 2 == 0:
            bloque += 1
        umbral_local = threshold_local(
            gris,
            block_size=bloque,
            method="mean",
            offset=constante,
        )
        mascara = gris > umbral_local
        if invertir:
            mascara = ~mascara
        return _crear_imagen_mascara(mascara)

    rgb = _leer_rgb(imagen)
    if metodo == _METODO_WATERSHED:
        etiquetas = _segmentar_watershed(
            gris,
            umbral_min,
            umbral_max,
            distancia_min,
            distancia_max,
            conectividad,
            kernel,
        )
        return _crear_imagen_rgb(_colorear_etiquetas(etiquetas, rgb))

    if metodo == _METODO_KMEANS:
        return _crear_imagen_rgb(
            _segmentar_kmeans(rgb, numero_clusters)
        )

    if metodo == _METODO_REGION_GROWING:
        if semilla is None:
            raise ValueError(
                "Selecciona una semilla haciendo clic en la imagen original."
            )
        x, y = semilla
        if not 0 <= x < gris.shape[1] or not 0 <= y < gris.shape[0]:
            raise ValueError("La semilla está fuera de la imagen.")
        mascara = flood(
            gris,
            (y, x),
            connectivity=1 if conectividad == 4 else 2,
            tolerance=tolerancia,
        )
        if invertir:
            mascara = ~mascara
        return _crear_imagen_mascara(mascara)

    if metodo == _METODO_SLIC:
        etiquetas = slic(
            rgb.astype(np.float32) / 255.0,
            n_segments=numero_superpixeles,
            compactness=compactness,
            start_label=1,
            channel_axis=-1,
        )
        return _crear_imagen_rgb(_colorear_etiquetas(etiquetas, rgb))

    raise ValueError(f"Método de segmentación desconocido: {metodo}")


def _leer_gris(imagen: QImage) -> np.ndarray:
    gris = imagen.convertToFormat(QImage.Format.Format_Grayscale8)
    bits = gris.bits()
    bits.setsize(gris.sizeInBytes())
    return np.frombuffer(bits, dtype=np.uint8).reshape(
        gris.height(), gris.bytesPerLine()
    )[:, :gris.width()].copy()


def _leer_rgb(imagen: QImage) -> np.ndarray:
    rgb = imagen.convertToFormat(QImage.Format.Format_RGB888)
    bits = rgb.bits()
    bits.setsize(rgb.sizeInBytes())
    datos = np.frombuffer(bits, dtype=np.uint8).reshape(
        rgb.height(), rgb.bytesPerLine()
    )
    return datos[:, :rgb.width() * 3].reshape(
        rgb.height(), rgb.width(), 3
    ).copy()


def _crear_imagen_mascara(mascara: np.ndarray) -> QImage:
    mascara_uint8 = np.asarray(mascara, dtype=np.uint8) * 255
    alto, ancho = mascara_uint8.shape
    imagen = QImage(ancho, alto, QImage.Format.Format_Grayscale8)
    bits = imagen.bits()
    bits.setsize(imagen.sizeInBytes())
    salida = np.frombuffer(bits, dtype=np.uint8).reshape(
        alto, imagen.bytesPerLine()
    )
    salida[:, :ancho] = mascara_uint8
    return imagen


def _crear_imagen_rgb(pixeles: np.ndarray) -> QImage:
    alto, ancho, _ = pixeles.shape
    imagen = QImage(ancho, alto, QImage.Format.Format_RGB888)
    bits = imagen.bits()
    bits.setsize(imagen.sizeInBytes())
    salida = np.frombuffer(bits, dtype=np.uint8).reshape(
        alto, imagen.bytesPerLine()
    )
    salida[:, :ancho * 3] = pixeles.reshape(alto, ancho * 3)
    return imagen


def _segmentar_watershed(
    gris: np.ndarray,
    umbral_min: int,
    umbral_max: int,
    distancia_min: int,
    distancia_max: int,
    conectividad: int,
    kernel: int,
) -> np.ndarray:
    mascara = (gris >= umbral_min) & (gris <= umbral_max)
    if not np.any(mascara):
        return np.zeros(gris.shape, dtype=np.int32)

    estructura = ndimage.generate_binary_structure(
        2, 1 if conectividad == 4 else 2
    )
    distancia = ndimage.distance_transform_edt(mascara)
    sigma = max(0.5, kernel / 6.0)
    distancia = ndimage.gaussian_filter(distancia, sigma=sigma)
    coords = peak_local_max(
        distancia,
        min_distance=max(1, distancia_min),
        threshold_abs=max(0, distancia_min),
        labels=mascara,
        exclude_border=False,
    )
    if distancia_max > 0 and len(coords):
        valores = distancia[coords[:, 0], coords[:, 1]]
        coords = coords[valores <= distancia_max]

    marcadores = np.zeros(gris.shape, dtype=np.int32)
    if len(coords):
        marcadores[coords[:, 0], coords[:, 1]] = np.arange(
            1, len(coords) + 1
        )
    else:
        componentes, cantidad = ndimage.label(mascara, structure=estructura)
        indices = np.arange(1, cantidad + 1)
        posiciones = ndimage.maximum_position(
            distancia,
            labels=componentes,
            index=indices,
        )
        for componente, posicion in zip(indices, posiciones):
            marcadores[posicion] = componente

    return watershed(
        -distancia,
        marcadores,
        connectivity=estructura,
        mask=mascara,
    )


def _colorear_etiquetas(
    etiquetas: np.ndarray,
    rgb: np.ndarray,
) -> np.ndarray:
    if not np.any(etiquetas):
        return np.zeros_like(rgb)
    paleta = np.random.default_rng(0).integers(
        48,
        256,
        size=(int(etiquetas.max()) + 1, 3),
        dtype=np.uint8,
    )
    paleta[0] = 0
    coloreada = (
        rgb.astype(np.float32) * 0.55
        + paleta[etiquetas].astype(np.float32) * 0.45
    )
    coloreada[etiquetas == 0] = rgb[etiquetas == 0]
    return np.clip(np.round(coloreada), 0, 255).astype(np.uint8)


def _segmentar_kmeans(rgb: np.ndarray, numero_clusters: int) -> np.ndarray:
    pixeles = rgb.reshape(-1, 3).astype(np.float32)
    cantidad = len(pixeles)
    clusters = min(numero_clusters, cantidad)
    rng = np.random.default_rng(0)
    muestra = pixeles[
        rng.choice(cantidad, size=min(cantidad, 30_000), replace=False)
    ]
    centros = _inicializar_centros(muestra, clusters, rng)

    for _ in range(25):
        distancias = np.sum(
            (muestra[:, None, :] - centros[None, :, :]) ** 2,
            axis=2,
        )
        etiquetas = np.argmin(distancias, axis=1)
        conteos = np.bincount(etiquetas, minlength=clusters)
        nuevos_centros = centros.copy()
        for canal in range(3):
            sumas = np.bincount(
                etiquetas,
                weights=muestra[:, canal],
                minlength=clusters,
            )
            activos = conteos > 0
            nuevos_centros[activos, canal] = (
                sumas[activos] / conteos[activos]
            )
        if np.allclose(nuevos_centros, centros, atol=0.1):
            centros = nuevos_centros
            break
        centros = nuevos_centros

    salida = np.empty_like(pixeles)
    tamano_lote = 100_000
    for inicio in range(0, cantidad, tamano_lote):
        fin = min(cantidad, inicio + tamano_lote)
        lote = pixeles[inicio:fin]
        distancias = np.sum(
            (lote[:, None, :] - centros[None, :, :]) ** 2,
            axis=2,
        )
        salida[inicio:fin] = centros[np.argmin(distancias, axis=1)]

    return np.clip(np.round(salida), 0, 255).astype(np.uint8).reshape(rgb.shape)


def _inicializar_centros(
    muestra: np.ndarray,
    cantidad: int,
    rng: np.random.Generator,
) -> np.ndarray:
    centros = np.empty((cantidad, muestra.shape[1]), dtype=np.float32)
    centros[0] = muestra[rng.integers(len(muestra))]
    distancias = np.sum((muestra - centros[0]) ** 2, axis=1)

    for indice in range(1, cantidad):
        total = float(distancias.sum())
        siguiente = (
            int(rng.choice(len(muestra), p=distancias / total))
            if total > 0
            else int(rng.integers(len(muestra)))
        )
        centros[indice] = muestra[siguiente]
        nuevas_distancias = np.sum(
            (muestra - centros[indice]) ** 2,
            axis=1,
        )
        distancias = np.minimum(distancias, nuevas_distancias)

    return centros