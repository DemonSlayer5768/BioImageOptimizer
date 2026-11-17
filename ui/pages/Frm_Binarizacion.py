from pathlib import Path

from PyQt6 import uic
from PyQt6.QtCore import Qt, pyqtSignal
from PyQt6.QtGui import QImage, QPixmap
from PyQt6.QtWidgets import (
    QBoxLayout,
    QFileDialog,
    QMessageBox,
    QWidget,
)

from algorithms.binarizacion.binarizacion import binarizar


class Frm_Binarizacion(QWidget):
    solicitar_galeria = pyqtSignal()

    def __init__(self):
        super().__init__()

        uic.loadUi("ui/pages/Tfrm_Binarizacion.ui", self)

        self._imagen_original = QImage()
        self._imagen_binaria = QImage()
        self._ruta_imagen = None

        self.configurar_controles()
        self.conectar_eventos()
        self.actualizar_parametros_metodo()

    def configurar_controles(self):
        self.lb_img_orignal.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lb_img_bin.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lb_img_orignal.setScaledContents(False)
        self.lb_img_bin.setScaledContents(False)
        self.lb_img_orignal.setToolTip("Imagen original")
        self.lb_img_bin.setToolTip("Resultado binarizado")

        self.spin_tamano_bloque.setRange(3, 255)
        self.spin_tamano_bloque.setSingleStep(2)
        self.spin_tamano_bloque.setValue(11)
        self.doubleSpinBox.setRange(-50.0, 50.0)
        self.doubleSpinBox.setDecimals(1)
        self.doubleSpinBox.setSingleStep(0.5)
        self.doubleSpinBox.setValue(2.0)

        self.btn_eliminar.setEnabled(False)
        self.btn_reset.setEnabled(False)
        self.btn_guardar.setEnabled(False)
        self.chk_mascara.setEnabled(False)
        self.chk_mascara.setToolTip(
            "La aplicación todavía no tiene una máscara previa para aplicar."
        )

    def conectar_eventos(self):
        self.btn_importar.clicked.connect(self.solicitar_galeria.emit)
        self.btn_eliminar.clicked.connect(self.quitar_imagen)
        self.btn_reset.clicked.connect(self.reiniciar_parametros)
        self.btn_guardar.clicked.connect(self.guardar_resultado)

        self.cmb_metodo.currentTextChanged.connect(
            self.actualizar_parametros_metodo
        )
        self.cmb_metodo.currentTextChanged.connect(
            self.actualizar_resultado_si_preview
        )
        self.spin_umbral.valueChanged.connect(self.slider_umbral.setValue)
        self.slider_umbral.valueChanged.connect(self.spin_umbral.setValue)
        self.slider_umbral.valueChanged.connect(
            self.actualizar_resultado_si_preview
        )
        self.spin_tamano_bloque.valueChanged.connect(
            self.normalizar_tamano_bloque
        )
        self.spin_tamano_bloque.valueChanged.connect(
            self.actualizar_resultado_si_preview
        )
        self.doubleSpinBox.valueChanged.connect(
            self.actualizar_resultado_si_preview
        )
        self.chk_invertir.toggled.connect(
            self.actualizar_resultado_si_preview
        )
        self.chk_preview.toggled.connect(self.alternar_vista_previa)
        self.chk_ver_original.toggled.connect(
            self.actualizar_visibilidad_imagenes
        )
        self.actualizar_visibilidad_imagenes(
            self.chk_ver_original.isChecked()
        )

    def actualizar_visibilidad_imagenes(self, mostrar_original: bool):
        self.grp_original.setVisible(mostrar_original)
        self.grp_bin.setVisible(True)

    def cargar_imagen(self, ruta: str):
        imagen = QImage(ruta)
        if imagen.isNull():
            QMessageBox.warning(
                self,
                "No se pudo abrir la imagen",
                f"El archivo no es una imagen válida:\n{ruta}",
            )
            return

        self._imagen_original = imagen
        self._ruta_imagen = Path(ruta)
        self.btn_eliminar.setEnabled(True)
        self.btn_reset.setEnabled(True)
        self.btn_guardar.setEnabled(True)
        self.actualizar_vistas()
        self.aplicar_binarizacion()

    def quitar_imagen(self):
        self._imagen_original = QImage()
        self._imagen_binaria = QImage()
        self._ruta_imagen = None
        self.lb_img_orignal.clear()
        self.lb_img_bin.clear()
        self.btn_eliminar.setEnabled(False)
        self.btn_reset.setEnabled(False)
        self.btn_guardar.setEnabled(False)

    def reiniciar_parametros(self):
        self.cmb_metodo.setCurrentIndex(0)
        self.spin_umbral.setValue(127)
        self.spin_tamano_bloque.setValue(11)
        self.doubleSpinBox.setValue(2.0)
        self.chk_invertir.setChecked(False)
        self.chk_mascara.setChecked(False)
        self.chk_preview.setChecked(False)
        self.chk_ver_original.setChecked(True)
        self.aplicar_binarizacion()

    def limpiar_formulario(self):
        self.quitar_imagen()
        self.reiniciar_parametros()

    def actualizar_parametros_metodo(self):
        metodo = self.cmb_metodo.currentText()
        es_fijo = metodo == "Fixed"
        es_adaptativo = metodo in ("Adaptive Mean", "Adaptive Gaussian")
        self.spin_umbral.setEnabled(es_fijo)
        self.slider_umbral.setEnabled(es_fijo)
        self.spin_tamano_bloque.setEnabled(es_adaptativo)
        self.doubleSpinBox.setEnabled(es_adaptativo)

    def normalizar_tamano_bloque(self, valor: int):
        if valor % 2 == 0:
            self.spin_tamano_bloque.setValue(
                valor + 1 if valor < self.spin_tamano_bloque.maximum()
                else valor - 1
            )

    def actualizar_resultado_si_preview(self):
        if self.chk_preview.isChecked():
            self.aplicar_binarizacion()

    def alternar_vista_previa(self, activa: bool):
        if activa:
            self.aplicar_binarizacion()

    def aplicar_binarizacion(self):
        if self._imagen_original.isNull():
            return

        self._imagen_binaria = binarizar(
            self._imagen_original,
            self.cmb_metodo.currentText(),
            self.spin_umbral.value(),
            self.spin_tamano_bloque.value(),
            self.doubleSpinBox.value(),
            self.chk_invertir.isChecked(),
        )
        self.actualizar_vistas()

    def guardar_resultado(self):
        if self._imagen_original.isNull():
            QMessageBox.warning(
                self,
                "Guardar resultado",
                "Primero importa una imagen.",
            )
            return

        self.aplicar_binarizacion()
        nombre = (
            f"{self._ruta_imagen.stem}_binarizada.png"
            if self._ruta_imagen
            else "imagen_binarizada.png"
        )
        directorio = (
            Path(__file__).resolve().parents[2]
            / "data"
            / "images"
            / "processed"
        )
        ruta, _ = QFileDialog.getSaveFileName(
            self,
            "Guardar imagen binarizada",
            str(directorio / nombre),
            "Imagen PNG (*.png)",
        )
        if not ruta:
            return

        if not ruta.lower().endswith(".png"):
            ruta += ".png"
        if not self._imagen_binaria.save(ruta, "PNG"):
            QMessageBox.warning(
                self,
                "Error al guardar",
                f"No se pudo guardar la imagen en:\n{ruta}",
            )
            return

        QMessageBox.information(
            self,
            "Imagen guardada",
            f"El resultado se guardó en:\n{ruta}",
        )

    def actualizar_vistas(self):
        self._actualizar_label(self.lb_img_orignal, self._imagen_original)
        self._actualizar_label(self.lb_img_bin, self._imagen_binaria)

    @staticmethod
    def _actualizar_label(etiqueta, imagen: QImage):
        if imagen.isNull() or etiqueta.size().isEmpty():
            etiqueta.clear()
            return

        pixmap = QPixmap.fromImage(imagen).scaled(
            etiqueta.size(),
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation,
        )
        etiqueta.setPixmap(pixmap)

    def resizeEvent(self, evento):
        super().resizeEvent(evento)
        ventana = self.window()
        ancho_suficiente = self.panel_imagen.width() >= 700
        direccion = (
            QBoxLayout.Direction.LeftToRight
            if ventana.isMaximized() or ancho_suficiente
            else QBoxLayout.Direction.TopToBottom
        )
        if self.verticalLayout_4.direction() != direccion:
            self.verticalLayout_4.setDirection(direccion)
        self.actualizar_vistas()
