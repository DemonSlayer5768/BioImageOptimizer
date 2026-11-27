import unittest

import numpy as np
from PyQt6.QtGui import QImage

from algorithms.segmentacion.segmentacion import segmentar


def crear_imagen_gris(valores: np.ndarray) -> QImage:
    alto, ancho = valores.shape
    imagen = QImage(ancho, alto, QImage.Format.Format_Grayscale8)
    bits = imagen.bits()
    bits.setsize(imagen.sizeInBytes())
    pixeles = np.frombuffer(bits, dtype=np.uint8).reshape(
        alto, imagen.bytesPerLine()
    )
    pixeles[:, :ancho] = valores
    return imagen


def leer_pixeles(imagen: QImage, canales: int = 1) -> np.ndarray:
    bits = imagen.constBits()
    bits.setsize(imagen.sizeInBytes())
    datos = np.frombuffer(bits, dtype=np.uint8).reshape(
        imagen.height(), imagen.bytesPerLine()
    )
    if canales == 1:
        return datos[:, :imagen.width()].copy()
    return datos[:, :imagen.width() * canales].reshape(
        imagen.height(), imagen.width(), canales
    ).copy()


class SegmentarTests(unittest.TestCase):
    def test_umbral_aplica_rango_inclusivo_y_opcion_invertir(self):
        imagen = crear_imagen_gris(
            np.array([[10, 100, 200, 250]], dtype=np.uint8)
        )

        resultado = segmentar(
            imagen,
            "Umbralizacion",
            umbral_min=100,
            umbral_max=200,
        )
        invertido = segmentar(
            imagen,
            "Umbralizacion",
            umbral_min=100,
            umbral_max=200,
            invertir=True,
        )

        np.testing.assert_array_equal(
            leer_pixeles(resultado),
            [[0, 255, 255, 0]],
        )
        np.testing.assert_array_equal(
            leer_pixeles(invertido),
            [[255, 0, 0, 255]],
        )

    def test_umbral_adaptativo_produce_mascara_binaria(self):
        valores = np.tile(np.arange(16, dtype=np.uint8) * 16, (8, 1))

        resultado = segmentar(
            crear_imagen_gris(valores),
            "Umbralización adaptativa",
            tamano_bloque=5,
            constante=0,
        )

        self.assertEqual(resultado.format(), QImage.Format.Format_Grayscale8)
        self.assertTrue(set(np.unique(leer_pixeles(resultado))) <= {0, 255})

    def test_watershed_devuelve_regiones_rgb(self):
        valores = np.zeros((24, 32), dtype=np.uint8)
        valores[5:19, 3:13] = 220
        valores[5:19, 19:29] = 220

        resultado = segmentar(
            crear_imagen_gris(valores),
            "Watershed",
            umbral_min=200,
            umbral_max=255,
            distancia_min=1,
            distancia_max=255,
            conectividad=8,
            kernel=3,
        )

        self.assertEqual(resultado.format(), QImage.Format.Format_RGB888)
        self.assertGreater(
            len(np.unique(leer_pixeles(resultado, 3).reshape(-1, 3), axis=0)),
            2,
        )

    def test_kmeans_separa_dos_colores(self):
        valores = np.zeros((8, 12), dtype=np.uint8)
        valores[:, 6:] = 255

        resultado = segmentar(
            crear_imagen_gris(valores),
            "K-means",
            numero_clusters=2,
        )

        salida = leer_pixeles(resultado, 3)
        self.assertEqual(resultado.format(), QImage.Format.Format_RGB888)
        self.assertTrue(np.all(salida[:, :6] == 0))
        self.assertTrue(np.all(salida[:, 6:] == 255))

    def test_region_growing_usa_semilla_y_tolerancia(self):
        valores = np.full((5, 6), 200, dtype=np.uint8)
        valores[:, :3] = 40

        resultado = segmentar(
            crear_imagen_gris(valores),
            "Region Growing",
            semilla=(1, 2),
            tolerancia=0,
            conectividad=4,
        )

        np.testing.assert_array_equal(
            leer_pixeles(resultado),
            np.array(
                [[255, 255, 255, 0, 0, 0]] * 5,
                dtype=np.uint8,
            ),
        )

    def test_region_growing_requiere_semilla(self):
        imagen = crear_imagen_gris(np.zeros((3, 3), dtype=np.uint8))

        with self.assertRaisesRegex(ValueError, "semilla"):
            segmentar(imagen, "Region Growing")

    def test_slic_devuelve_imagen_rgb(self):
        valores = np.zeros((16, 16), dtype=np.uint8)
        valores[4:12, 4:12] = 180

        resultado = segmentar(
            crear_imagen_gris(valores),
            "SLIC (Superpixeles)",
            numero_superpixeles=8,
        )

        self.assertEqual(resultado.format(), QImage.Format.Format_RGB888)
        self.assertEqual((resultado.width(), resultado.height()), (16, 16))


if __name__ == "__main__":
    unittest.main()
