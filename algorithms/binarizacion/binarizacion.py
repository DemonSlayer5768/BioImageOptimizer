from array import array
from math import sqrt

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
    pixeles = bytes(bits)

    if metodo in _METODOS_UMBRAL_GLOBAL:
        if metodo == "Fixed":
            umbral_aplicado = umbral
        else:
            histograma = [0] * 256
            for y in range(alto):
                inicio = y * stride
                for x in range(ancho):
                    histograma[pixeles[inicio + x]] += 1
            if metodo == "Otsu":
                umbral_aplicado = _umbral_otsu(histograma)
            else:
                umbral_aplicado = _umbral_triangle(histograma)

        medias_locales = None
    elif metodo == "Adaptive Mean":
        bloque = _normalizar_bloque(tamano_bloque)
        medias_locales = _medias_adaptativas(
            pixeles, ancho, alto, stride, bloque
        )
        umbral_aplicado = None
    elif metodo == "Adaptive Gaussian":
        bloque = _normalizar_bloque(tamano_bloque)
        medias_locales = _medias_gaussianas(
            pixeles, ancho, alto, stride, bloque
        )
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
    buffer_salida = memoryview(salida)
    stride_salida = resultado.bytesPerLine()

    for y in range(alto):
        inicio = y * stride
        inicio_salida = y * stride_salida
        for x in range(ancho):
            indice = inicio + x
            if medias_locales is None:
                limite = umbral_aplicado
            else:
                limite = medias_locales[y * ancho + x] - constante
            es_blanco = pixeles[indice] > limite
            if invertir:
                es_blanco = not es_blanco
            buffer_salida[inicio_salida + x] = 255 if es_blanco else 0

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
    pixeles: bytes,
    ancho: int,
    alto: int,
    stride: int,
    bloque: int,
) -> array:
    columnas = ancho + 1
    integral = array("Q", [0]) * (columnas * (alto + 1))

    for y in range(alto):
        suma_fila = 0
        inicio = y * stride
        fila_integral = (y + 1) * columnas
        fila_anterior = y * columnas
        for x in range(ancho):
            suma_fila += pixeles[inicio + x]
            integral[fila_integral + x + 1] = (
                integral[fila_anterior + x + 1] + suma_fila
            )

    radio = bloque // 2
    medias = array("d", [0.0]) * (ancho * alto)
    for y in range(alto):
        arriba = max(0, y - radio)
        abajo = min(alto, y + radio + 1)
        for x in range(ancho):
            izquierda = max(0, x - radio)
            derecha = min(ancho, x + radio + 1)
            suma = (
                integral[abajo * columnas + derecha]
                - integral[arriba * columnas + derecha]
                - integral[abajo * columnas + izquierda]
                + integral[arriba * columnas + izquierda]
            )
            area = (abajo - arriba) * (derecha - izquierda)
            medias[y * ancho + x] = suma / area

    return medias


def _medias_gaussianas(
    pixeles: bytes,
    ancho: int,
    alto: int,
    stride: int,
    bloque: int,
) -> array:
    sigma = max(0.5, 0.3 * ((bloque - 1) * 0.5 - 1) + 0.8)
    ancho_caja = max(3, round(sqrt(4 * sigma * sigma + 1)))
    if ancho_caja % 2 == 0:
        ancho_caja += 1
    radio = ancho_caja // 2

    suavizados = array("d", [0.0]) * (ancho * alto)
    for y in range(alto):
        inicio = y * stride
        fila = y * ancho
        for x in range(ancho):
            suavizados[fila + x] = pixeles[inicio + x]

    for _ in range(3):
        horizontal = array("d", [0.0]) * (ancho * alto)
        for y in range(alto):
            fila = y * ancho
            suma = sum(
                suavizados[fila + min(ancho - 1, max(0, x))]
                for x in range(-radio, radio + 1)
            )
            for x in range(ancho):
                horizontal[fila + x] = suma / ancho_caja
                sale = min(ancho - 1, max(0, x - radio))
                entra = min(ancho - 1, max(0, x + radio + 1))
                suma += (
                    suavizados[fila + entra] - suavizados[fila + sale]
                )

        vertical = array("d", [0.0]) * (ancho * alto)
        for x in range(ancho):
            suma = sum(
                horizontal[min(alto - 1, max(0, y)) * ancho + x]
                for y in range(-radio, radio + 1)
            )
            for y in range(alto):
                vertical[y * ancho + x] = suma / ancho_caja
                sale = min(alto - 1, max(0, y - radio))
                entra = min(alto - 1, max(0, y + radio + 1))
                suma += (
                    horizontal[entra * ancho + x]
                    - horizontal[sale * ancho + x]
                )
        suavizados = vertical

    return suavizados
