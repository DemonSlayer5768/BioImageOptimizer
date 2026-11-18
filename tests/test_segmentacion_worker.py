import os
import time
import unittest
from unittest.mock import patch

os.environ.setdefault("QT_QPA_PLATFORM", "offscreen")

from PyQt6.QtCore import QEventLoop, QPoint, QTimer, Qt
from PyQt6.QtGui import QImage
from PyQt6.QtWidgets import QApplication
from PyQt6.QtTest import QTest

from ui.pages.Frm_Segmentacion import Frm_Segmentacion


class SegmentacionWorkerTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.app = QApplication.instance() or QApplication([])

    def test_worker_deja_responder_a_la_interfaz(self):
        form = Frm_Segmentacion()
        form.chk_preview.setChecked(False)
        form._imagen_original = QImage(
            32,
            32,
            QImage.Format.Format_RGB32,
        )
        form._imagen_original.fill(0xFF808080)
        form.btn_ejecutar.setEnabled(True)

        def segmentar_lentamente(imagen, metodo, **parametros):
            time.sleep(0.15)
            if metodo != "Umbralizacion" or parametros["umbral_min"] < 0:
                return QImage()
            return imagen.copy()

        pulsos = []
        temporizador = QTimer()
        temporizador.setInterval(5)
        temporizador.timeout.connect(lambda: pulsos.append(True))
        temporizador.start()

        with patch(
            "ui.pages.Frm_Segmentacion.segmentar",
            side_effect=segmentar_lentamente,
        ):
            form.btn_ejecutar.click()
            bucle = QEventLoop()
            sondeo = QTimer()
            sondeo.setInterval(5)
            sondeo.timeout.connect(
                lambda: bucle.quit() if form._worker is None else None
            )
            sondeo.start()
            QTimer.singleShot(5000, bucle.quit)
            bucle.exec()

        temporizador.stop()
        sondeo.stop()
        form.esperar_procesamiento()
        self.app.processEvents()

        self.assertGreater(len(pulsos), 2)
        self.assertIsNone(form._worker)
        self.assertFalse(form._imagen_segmentada.isNull())
        self.assertTrue(form.btn_ejecutar.isEnabled())
        form.deleteLater()

    def test_preview_debounce_conserva_resultado_hasta_terminar(self):
        form = Frm_Segmentacion()
        form._imagen_original = QImage(
            32,
            32,
            QImage.Format.Format_RGB32,
        )
        form._imagen_original.fill(0xFF808080)
        form._imagen_segmentada = QImage(
            32,
            32,
            QImage.Format.Format_RGB32,
        )
        form._imagen_segmentada.fill(0xFFFF0000)

        llamadas = []

        def segmentar_lentamente(imagen, metodo, **parametros):
            if metodo != "Umbralizacion":
                raise AssertionError(f"Metodo inesperado: {metodo}")
            llamadas.append(parametros["umbral_min"])
            time.sleep(0.1)
            return imagen.copy()

        with patch(
            "ui.pages.Frm_Segmentacion.segmentar",
            side_effect=segmentar_lentamente,
        ):
            form.slider_umbral_min.setValue(100)
            form.slider_umbral_min.setValue(110)
            form.slider_umbral_min.setValue(120)

            self.assertEqual(
                form._imagen_segmentada.pixelColor(0, 0).red(),
                255,
            )
            self.assertTrue(form._preview_timer.isActive())

            bucle = QEventLoop()
            sondeo = QTimer()
            sondeo.setInterval(10)

            def terminar_al_completar():
                if (
                    not form._preview_timer.isActive()
                    and form._worker is None
                    and llamadas
                ):
                    bucle.quit()

            sondeo.timeout.connect(terminar_al_completar)
            sondeo.start()
            QTimer.singleShot(5000, bucle.quit)
            bucle.exec()
            sondeo.stop()

        self.assertEqual(llamadas, [120])
        self.assertFalse(form._imagen_segmentada.isNull())
        form.esperar_procesamiento()
        form.deleteLater()

    def test_slider_no_cambia_valor_al_mover_el_cursor(self):
        form = Frm_Segmentacion()
        form.show()
        slider = form.slider_umbral_min
        valor_inicial = slider.value()

        QTest.mouseMove(
            slider,
            QPoint(slider.width() // 2, slider.height() // 2),
        )
        self.app.processEvents()

        self.assertEqual(slider.value(), valor_inicial)
        self.assertEqual(slider.cursor().shape(), Qt.CursorShape.ArrowCursor)
        form.deleteLater()


if __name__ == "__main__":
    unittest.main()
