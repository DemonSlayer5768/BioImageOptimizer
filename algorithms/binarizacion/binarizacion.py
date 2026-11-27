from math import sqrt

import numpy as np
from PyQt6.QtGui import QImage


_METODOS_UMBRAL_GLOBAL = {"Otsu", "Fixed", "Triangle"}


def binarizar(
    imagen: QImage,
    metodo: str,
    umbral: int,
    tamano_bloque: int,
    constante: float,
    invertir: bool,
) -> QImage:
    if imagen.isNull():
        raise ValueError("La imagen está vacía.")

    gris = imagen.convertToFormat(QImage.Format.Format_Grayscale8)
    ancho = gris.width()
    alto = gris.height()
    stride = gris.bytesPerLine()
    bits = gris.bits()
    bits.setsize(gris.sizeInBytes())
    pixeles = np.frombuffer(bits, dtype=np.uint8).reshape(alto, stride)
    pixeles = pixeles[:, :ancho]

    if metodo in _METODOS_UMBRAL_GLOBAL:
        if metodo == "Fixed":
            umbral_aplicado = umbral
        else:
            histograma = np.bincount(
                pixeles.ravel(), minlength=256
            ).tolist()
            if metodo == "Otsu":
                umbral_aplicado = _umbral_otsu(histograma)
            else:
                umbral_aplicado = _umbral_triangle(histograma)

        medias_locales = None
    elif metodo == "Adaptive Mean":
        bloque = _normalizar_bloque(tamano_bloque)
        medias_locales = _medias_adaptativas(pixeles, bloque)
        umbral_aplicado = None
    elif metodo == "Adaptive Gaussian":
        bloque = _normalizar_bloque(tamano_bloque)
        medias_locales = _medias_gaussianas(pixeles, bloque)
        umbral_aplicado = None
    else:
        raise ValueError(f"Método de binarización desconocido: {metodo}")

    resultado = QImage(
        ancho,
        alto,
        QImage.Format.Format_Grayscale8
    )
    resultado.fill(0)
    salida = resultado.bits()
    salida.setsize(resultado.sizeInBytes())
    stride_salida = resultado.bytesPerLine()
    buffer_salida = np.frombuffer(salida, dtype=np.uint8).reshape(
        alto, stride_salida
    )

    limite = (
        umbral_aplicado
        if medias_locales is None
        else medias_locales - constante
    )
    es_blanco = pixeles > limite
    if invertir:
        np.logical_not(es_blanco, out=es_blanco)
    buffer_salida[:, :ancho] = es_blanco * 255

    return resultado


def _normalizar_bloque(tamano: int) -> int:
    bloque = max(3, tamano)
    if bloque % 2 == 0:
        bloque += 1
    return bloque


def _umbral_otsu(histograma: list[int]) -> int:
    total = sum(histograma)
    suma_total = sum(indice * cantidad
                     for indice, cantidad in enumerate(histograma))
    peso_fondo = 0
    suma_fondo = 0
    mejor_varianza = -1.0
    mejor_umbral = 0

    for nivel, cantidad in enumerate(histograma):
        peso_fondo += cantidad
        if peso_fondo == 0:
            continue

        peso_frente = total - peso_fondo
        if peso_frente == 0:
            break

        suma_fondo += nivel * cantidad
        media_fondo = suma_fondo / peso_fondo
        media_frente = (suma_total - suma_fondo) / peso_frente
        varianza = (
            peso_fondo
            * peso_frente
            * (media_fondo - media_frente) ** 2
        )
        if varianza > mejor_varianza:
            mejor_varianza = varianza
            mejor_umbral = nivel

    return mejor_umbral


def _umbral_triangle(histograma: list[int]) -> int:
    niveles = [i for i, cantidad in enumerate(histograma) if cantidad]
    if not niveles:
        return 0

    extremo = niveles[0]
    pico = max(range(256), key=histograma.__getitem__)
    final = niveles[-1]
    invertir_histograma = pico - extremo < final - pico
    if invertir_histograma:
        histograma = histograma[::-1]
        extremo = 255 - final
        pico = 255 - pico

    altura_extremo = histograma[extremo]
    altura_pico = histograma[pico]
    delta_x = pico - extremo
    delta_y = altura_pico - altura_extremo
    distancia_maxima = -1.0
    mejor_nivel = extremo

    for nivel in range(extremo, pico + 1):
        distancia = abs(
            delta_y * nivel - delta_x * histograma[nivel]
            + pico * altura_extremo - extremo * altura_pico
        )
        if distancia > distancia_maxima:
            distancia_maxima = distancia
            mejor_nivel = nivel

    return 255 - mejor_nivel if invertir_histograma else mejor_nivel


def _medias_adaptativas(
    pixeles: np.ndarray,
    bloque: int,
) -> np.ndarray:
    alto, ancho = pixeles.shape
    radio = bloque // 2
    integral = np.zeros((alto + 1, ancho + 1), dtype=np.uint64)
    integral[1:, 1:] = np.cumsum(
        np.cumsum(pixeles, axis=0, dtype=np.uint64),
        axis=1,
        dtype=np.uint64,
    )

    arriba = np.maximum(0, np.arange(alto) - radio)
    abajo = np.minimum(alto, np.arange(alto) + radio + 1)
    izquierda = np.maximum(0, np.arange(ancho) - radio)
    derecha = np.minimum(ancho, np.arange(ancho) + radio + 1)

    sumas = (
        integral[abajo[:, None], derecha[None, :]]
        - integral[arriba[:, None], derecha[None, :]]
        - integral[abajo[:, None], izquierda[None, :]]
        + integral[arriba[:, None], izquierda[None, :]]
    )
    areas = (
        (abajo - arriba)[:, None]
        * (derecha - izquierda)[None, :]
    )
    return sumas / areas


def _medias_gaussianas(
    pixeles: np.ndarray,
    bloque: int,
) -> np.ndarray:
    sigma = max(0.5, 0.3 * ((bloque - 1) * 0.5 - 1) + 0.8)
    ancho_caja = max(3, round(sqrt(4 * sigma * sigma + 1)))
    if ancho_caja % 2 == 0:
        ancho_caja += 1
    radio = ancho_caja // 2

    suavizados = pixeles.astype(np.float64)
    for _ in range(3):
        horizontal_padded = np.pad(
            suavizados, ((0, 0), (radio, radio)), mode="edge"
        )
        horizontal_sumas = np.pad(
            np.cumsum(horizontal_padded, axis=1),
            ((0, 0), (1, 0)),
        )
        horizontal = (
            horizontal_sumas[:, ancho_caja:]
            - horizontal_sumas[:, :-ancho_caja]
        ) / ancho_caja

        vertical_padded = np.pad(
            horizontal, ((radio, radio), (0, 0)), mode="edge"
        )
        vertical_sumas = np.pad(
            np.cumsum(vertical_padded, axis=0),
            ((1, 0), (0, 0)),
        )
        suavizados = (
            vertical_sumas[ancho_caja:, :]
            - vertical_sumas[:-ancho_caja, :]
        ) / ancho_caja

    return suavizados
