from dataclasses import dataclass
from pathlib import Path

from PyQt6 import uic
from PyQt6.QtCore import QEvent, QThread, QTimer, Qt, pyqtSignal
from PyQt6.QtGui import QImage, QPixmap
from PyQt6.QtWidgets import (
    QBoxLayout,
    QFileDialog,
    QMessageBox,
    QWidget,
)

from algorithms.segmentacion.segmentacion import segmentar
from resources.styles.components.md_cssClass import configurar_sliders



@dataclass(frozen=True)
class _ParametrosSegmentacion:
    metodo: str
    umbral_min: int
    umbral_max: int
    tamano_bloque: int
    constante: float
    invertir: bool
    distancia_min: int
    distancia_max: int
    conectividad: int
    kernel: int
    tolerancia: int
    semilla: tuple[int, int] | None
    numero_clusters: int
    numero_superpixeles: int
    compactness: float


class _TrabajoSegmentacion(QThread):
    resultado_disponible = pyqtSignal(int, QImage)
    error_ocurrido = pyqtSignal(int, str)

    def __init__(
        self,
        solicitud_id: int,
        imagen: QImage,
        parametros: _ParametrosSegmentacion,
    ):
        super().__init__()
        self._solicitud_id = solicitud_id
        self._imagen = imagen
        self._parametros = parametros

    def run(self):
        if self.isInterruptionRequested():
            return

        p = self._parametros
        try:
            resultado = segmentar(
                self._imagen,
                p.metodo,
                umbral_min=p.umbral_min,
                umbral_max=p.umbral_max,
                tamano_bloque=p.tamano_bloque,
                constante=p.constante,
                invertir=p.invertir,
                distancia_min=p.distancia_min,
                distancia_max=p.distancia_max,
                conectividad=p.conectividad,
                kernel=p.kernel,
                tolerancia=p.tolerancia,
                semilla=p.semilla,
                numero_clusters=p.numero_clusters,
                numero_superpixeles=p.numero_superpixeles,
                compactness=p.compactness,
            )
        except (ValueError, RuntimeError, MemoryError) as error:
            self.error_ocurrido.emit(self._solicitud_id, str(error))
            return

        self.resultado_disponible.emit(self._solicitud_id, resultado)


class Frm_Segmentacion(QWidget):
    solicitar_galeria = pyqtSignal()

    def __init__(self):
        super().__init__()

        uic.loadUi("ui/pages/Tfrm_Segmentacion.ui", self)

        self._imagen_original = QImage()
        self._imagen_segmentada = QImage()
        self._ruta_imagen: Path | None = None
        self._semilla: tuple[int, int] | None = None
        self._seleccionando_semilla = False
        self._solicitud_id = 0
        self._worker: _TrabajoSegmentacion | None = None
        self._guardar_al_terminar = False
        self._reprocesar_al_terminar = False
        self._preview_timer = QTimer(self)
        self._preview_timer.setSingleShot(True)
        self._preview_timer.setInterval(250)
        self._preview_timer.timeout.connect(self._procesar_preview_pendiente)

        self.configurar_controles()
        self.conectar_eventos()
        self.actualizar_parametros_metodo()
        configurar_sliders(self)

    def configurar_controles(self):
        self.gb_parametros.setCursor(Qt.CursorShape.ArrowCursor)
        for slider in (
            self.slider_umbral_min,
            self.slider_umbral_max,
            self.slider_distancia_min,
            self.slider_distancia_max,
            self.slider_tolerancia_region,
            self.slider_compactness,
        ):
            slider.setCursor(Qt.CursorShape.ArrowCursor)

        self.lb_img_orignal.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lb_img_bin.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lb_img_orignal.setScaledContents(False)
        self.lb_img_bin.setScaledContents(False)
        self.lb_img_orignal.setToolTip("Imagen original")
        self.lb_img_bin.setToolTip("Resultado de segmentación")
        self.lb_img_orignal.installEventFilter(self)
        self.lb_img_orignal.setMouseTracking(True)

        self.slider_umbral_min.setValue(127)
        self.slider_umbral_max.setValue(255)
        self.spin_tamano_bloque.setRange(3, 255)
        self.spin_tamano_bloque.setSingleStep(2)
        self.spin_tamano_bloque.setValue(11)
        self.doubleSpinBox.setRange(-50.0, 50.0)
        self.doubleSpinBox.setDecimals(1)
        self.doubleSpinBox.setSingleStep(0.5)
        self.doubleSpinBox.setValue(2.0)
        self.slider_distancia_min.setRange(1, 255)
        self.slider_distancia_min.setValue(3)
        self.slider_distancia_max.setRange(1, 255)
        self.slider_distancia_max.setValue(255)
        self.spin_numero_clusters.setRange(2, 12)
        self.spin_numero_clusters.setValue(3)
        self.spin_numero_superpixeles.setRange(10, 5000)
        self.spin_numero_superpixeles.setValue(200)
        self.slider_compactness.setRange(1, 300)
        self.slider_compactness.setValue(100)
        self.slider_tolerancia_region.setRange(0, 255)
        self.slider_tolerancia_region.setValue(20)

        self.rd_btn_vecinos_2.setChecked(True)
        self.rd_btn_tres.setChecked(True)
        self.rd_btn_region_vecinos_2.setChecked(True)

        self.btn_eliminar.setEnabled(False)
        self.btn_reset.setEnabled(False)
        self.btn_guardar.setEnabled(False)
        self.btn_ejecutar.setEnabled(False)
        self.chk_mascara.setEnabled(False)
        self.chk_mascara.setToolTip(
            "La aplicación todavía no tiene una máscara previa para aplicar."
        )
        self.lbl_semilla.setText("Sin seleccionar")

    def conectar_eventos(self):
        self.btn_importar.clicked.connect(self.solicitar_galeria.emit)
        self.btn_eliminar.clicked.connect(self.quitar_imagen)
        self.btn_reset.clicked.connect(self.reiniciar_parametros)
        self.btn_guardar.clicked.connect(self.guardar_resultado)
        self.btn_ejecutar.clicked.connect(
            lambda: self.aplicar_segmentacion()
        )
        self.btn_elegir_semilla.clicked.connect(self.iniciar_seleccion_semilla)

        self.cmb_metodo.currentTextChanged.connect(
            self.actualizar_parametros_metodo
        )
        self.cmb_metodo.currentTextChanged.connect(
            self.actualizar_resultado_si_preview
        )

        self.slider_umbral_min.valueChanged.connect(
            self.normalizar_umbral_minimo
        )
        self.slider_umbral_max.valueChanged.connect(
            self.normalizar_umbral_maximo
        )
        self.slider_distancia_min.valueChanged.connect(
            self.normalizar_distancia_minima
        )
        self.slider_distancia_max.valueChanged.connect(
            self.normalizar_distancia_maxima
        )
        self.slider_umbral_min.valueChanged.connect(
            self.actualizar_resultado_si_preview
        )
        self.slider_umbral_max.valueChanged.connect(
            self.actualizar_resultado_si_preview
        )
        self.spin_tamano_bloque.valueChanged.connect(
            self.normalizar_tamano_bloque
        )

        controles_valor = (
            self.spin_tamano_bloque,
            self.doubleSpinBox,
            self.slider_distancia_min,
            self.slider_distancia_max,
            self.slider_tolerancia_region,
            self.spin_numero_clusters,
            self.spin_numero_superpixeles,
            self.slider_compactness,
        )
        for control in controles_valor:
            control.valueChanged.connect(
                self.actualizar_resultado_si_preview
            )

        botones_opcion = (
            self.rd_btn_vecinos,
            self.rd_btn_vecinos_2,
            self.rd_btn_tres,
            self.rd_btn_cinco,
            self.rd_btn_siete,
            self.rd_btn_region_vecinos,
            self.rd_btn_region_vecinos_2,
        )
        for boton in botones_opcion:
            boton.toggled.connect(self.actualizar_resultado_si_preview)

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
        self._imagen_segmentada = QImage()
        self._ruta_imagen = Path(ruta)
        self._solicitud_id += 1
        self._guardar_al_terminar = False
        self._reprocesar_al_terminar = False
        self._semilla = None
        self._seleccionando_semilla = False
        self.lbl_semilla.setText("Sin seleccionar")
        self.btn_elegir_semilla.setText("Elegir semilla")
        self.btn_eliminar.setEnabled(True)
        self.btn_reset.setEnabled(True)
        self.btn_guardar.setEnabled(True)
        self.btn_ejecutar.setEnabled(True)
        self.actualizar_parametros_metodo()
        self.actualizar_vistas()
        if self.chk_preview.isChecked():
            if self._worker is not None and self._worker.isRunning():
                self._reprocesar_al_terminar = True
            else:
                self.aplicar_segmentacion(mostrar_errores=False)

    def quitar_imagen(self):
        self._solicitud_id += 1
        self._guardar_al_terminar = False
        self._reprocesar_al_terminar = False
        self._imagen_original = QImage()
        self._imagen_segmentada = QImage()
        self._ruta_imagen = None
        self._semilla = None
        self._seleccionando_semilla = False
        self.lb_img_orignal.clear()
        self.lb_img_bin.clear()
        self.lbl_semilla.setText("Sin seleccionar")
        self.btn_elegir_semilla.setText("Elegir semilla")
        self.lb_img_orignal.unsetCursor()
        self.btn_eliminar.setEnabled(False)
        self.btn_reset.setEnabled(False)
        self.btn_guardar.setEnabled(False)
        self.btn_ejecutar.setEnabled(False)

    def reiniciar_parametros(self):
        self.chk_preview.setChecked(False)
        self.cmb_metodo.setCurrentIndex(0)
        self.slider_umbral_min.setValue(127)
        self.slider_umbral_max.setValue(255)
        self.spin_tamano_bloque.setValue(11)
        self.doubleSpinBox.setValue(2.0)
        self.slider_distancia_min.setValue(3)
        self.slider_distancia_max.setValue(255)
        self.rd_btn_vecinos_2.setChecked(True)
        self.rd_btn_tres.setChecked(True)
        self.rd_btn_region_vecinos_2.setChecked(True)
        self.slider_tolerancia_region.setValue(20)
        self.spin_numero_clusters.setValue(3)
        self.spin_numero_superpixeles.setValue(200)
        self.slider_compactness.setValue(100)
        self.chk_invertir.setChecked(False)
        self.chk_mascara.setChecked(False)
        self.chk_ver_original.setChecked(True)
        self._semilla = None
        self._seleccionando_semilla = False
        self.lbl_semilla.setText("Sin seleccionar")
        self.btn_elegir_semilla.setText("Elegir semilla")
        self.lb_img_orignal.unsetCursor()
        self.actualizar_parametros_metodo()
        self.actualizar_vistas()
        if not self._imagen_original.isNull():
            self.aplicar_segmentacion(mostrar_errores=False)

    def limpiar_formulario(self):
        self.quitar_imagen()
        self.reiniciar_parametros()

    def actualizar_parametros_metodo(self):
        metodo = self.cmb_metodo.currentText()
        es_umbral = metodo == "Umbralizacion"
        es_adaptativo = metodo == "Umbralización adaptativa"
        es_watershed = metodo == "Watershed"
        es_kmeans = metodo == "K-means"
        es_region = metodo == "Region Growing"
        es_slic = metodo == "SLIC (Superpixeles)"

        for widget in (
            self.lb_parametros,
            self.slider_umbral_min,
            self.lb_parametros_2,
            self.slider_umbral_max,
        ):
            widget.setVisible(es_umbral or es_watershed)

        for widget in (
            self.label_2,
            self.spin_tamano_bloque,
            self.label_3,
            self.doubleSpinBox,
        ):
            widget.setVisible(es_adaptativo)

        self.gb_watershed.setVisible(es_watershed)
        self.gb_kmeans.setVisible(es_kmeans)
        self.gb_region_growing.setVisible(es_region)
        self.gb_slic.setVisible(es_slic)
        self.chk_invertir.setVisible(
            es_umbral or es_adaptativo or es_region
        )
        self.btn_elegir_semilla.setEnabled(
            es_region and not self._imagen_original.isNull()
        )

    def normalizar_umbral_minimo(self, valor: int):
        if valor > self.slider_umbral_max.value():
            self.slider_umbral_max.setValue(valor)

    def normalizar_umbral_maximo(self, valor: int):
        if valor < self.slider_umbral_min.value():
            self.slider_umbral_min.setValue(valor)

    def normalizar_distancia_minima(self, valor: int):
        if valor > self.slider_distancia_max.value():
            self.slider_distancia_max.setValue(valor)

    def normalizar_distancia_maxima(self, valor: int):
        if valor < self.slider_distancia_min.value():
            self.slider_distancia_min.setValue(valor)

    def normalizar_tamano_bloque(self, valor: int):
        if valor % 2 == 0:
            self.spin_tamano_bloque.setValue(
                valor + 1 if valor < self.spin_tamano_bloque.maximum()
                else valor - 1
            )

    def actualizar_resultado_si_preview(self):
        if self.chk_preview.isChecked() and not self._imagen_original.isNull():
            self._preview_timer.start()

    def alternar_vista_previa(self, activa: bool):
        if activa:
            self.actualizar_resultado_si_preview()
        else:
            self._preview_timer.stop()
            self._reprocesar_al_terminar = False

    def _procesar_preview_pendiente(self):
        if not self.chk_preview.isChecked() or self._imagen_original.isNull():
            return
        if self._worker is not None and self._worker.isRunning():
            self._reprocesar_al_terminar = True
            return
        self.aplicar_segmentacion(mostrar_errores=False)

    def aplicar_segmentacion(
        self,
        mostrar_errores: bool = True,
        guardar_al_terminar: bool = False,
    ):
        if self._imagen_original.isNull():
            return False
        if self._worker is not None and self._worker.isRunning():
            return False

        self._preview_timer.stop()
        metodo = self.cmb_metodo.currentText()
        es_region = metodo == "Region Growing"
        if es_region and self._semilla is None:
            self._imagen_segmentada = QImage()
            self.actualizar_vistas()
            if mostrar_errores:
                QMessageBox.warning(
                    self,
                    "Region Growing",
                    "Selecciona una semilla haciendo clic en la imagen original.",
                )
            return False

        cuatro_vecinos = (
            self.rd_btn_region_vecinos.isChecked()
            if es_region
            else self.rd_btn_vecinos.isChecked()
        )
        conectividad = 4 if cuatro_vecinos else 8
        kernel = (
            3 if self.rd_btn_tres.isChecked()
            else 5 if self.rd_btn_cinco.isChecked()
            else 7
        )
        parametros = _ParametrosSegmentacion(
            metodo=metodo,
            umbral_min=self.slider_umbral_min.value(),
            umbral_max=self.slider_umbral_max.value(),
            tamano_bloque=self.spin_tamano_bloque.value(),
            constante=self.doubleSpinBox.value(),
            invertir=self.chk_invertir.isChecked(),
            distancia_min=self.slider_distancia_min.value(),
            distancia_max=self.slider_distancia_max.value(),
            conectividad=conectividad,
            kernel=kernel,
            tolerancia=self.slider_tolerancia_region.value(),
            semilla=self._semilla,
            numero_clusters=self.spin_numero_clusters.value(),
            numero_superpixeles=self.spin_numero_superpixeles.value(),
            compactness=self.slider_compactness.value() / 10.0,
        )
        self._solicitud_id += 1
        solicitud_id = self._solicitud_id
        self._guardar_al_terminar = guardar_al_terminar
        self._reprocesar_al_terminar = False
        worker = _TrabajoSegmentacion(
            solicitud_id,
            self._imagen_original.copy(),
            parametros,
        )
        worker.resultado_disponible.connect(
            self._recibir_resultado_segmentacion
        )
        worker.error_ocurrido.connect(self._recibir_error_segmentacion)
        worker.finished.connect(
            lambda: self._terminar_trabajo_segmentacion(worker)
        )
        self._worker = worker
        self._actualizar_estado_procesamiento(True)
        worker.start()
        return True

    def _recibir_resultado_segmentacion(
        self,
        solicitud_id: int,
        resultado: QImage,
    ):
        if solicitud_id != self._solicitud_id:
            return
        self._imagen_segmentada = resultado
        self._actualizar_label(self.lb_img_bin, self._imagen_segmentada)

    def _recibir_error_segmentacion(
        self,
        solicitud_id: int,
        mensaje: str,
    ):
        if solicitud_id != self._solicitud_id:
            return
        self._guardar_al_terminar = False
        QMessageBox.warning(self, "Error de segmentación", mensaje)

    def _terminar_trabajo_segmentacion(self, worker: _TrabajoSegmentacion):
        es_actual = worker is self._worker
        if es_actual:
            self._worker = None
            self._actualizar_estado_procesamiento(False)
        worker.deleteLater()
        if not es_actual:
            return

        if self._reprocesar_al_terminar and not self._imagen_original.isNull():
            self._reprocesar_al_terminar = False
            self.aplicar_segmentacion(mostrar_errores=False)
            return

        self._reprocesar_al_terminar = False
        if self._guardar_al_terminar and not self._imagen_segmentada.isNull():
            self._guardar_al_terminar = False
            self._guardar_imagen_segmentada()

    def _actualizar_estado_procesamiento(self, en_proceso: bool):
        self.btn_ejecutar.setText(
            "Procesando..." if en_proceso else "Iniciar"
        )
        hay_imagen = not self._imagen_original.isNull()
        self.btn_importar.setEnabled(True)
        self.btn_eliminar.setEnabled(hay_imagen and not en_proceso)
        self.btn_reset.setEnabled(hay_imagen and not en_proceso)
        self.btn_guardar.setEnabled(hay_imagen and not en_proceso)
        self.btn_ejecutar.setEnabled(hay_imagen and not en_proceso)
        if not en_proceso:
            self.actualizar_parametros_metodo()

    def esperar_procesamiento(self):
        self._guardar_al_terminar = False
        self._reprocesar_al_terminar = False
        if self._worker is not None and self._worker.isRunning():
            self._worker.requestInterruption()
            self._worker.wait()

    def iniciar_seleccion_semilla(self):
        if self._imagen_original.isNull():
            QMessageBox.information(
                self,
                "Region Growing",
                "Primero importa una imagen.",
            )
            return

        self._seleccionando_semilla = True
        self.btn_elegir_semilla.setText("Haz clic en la imagen")
        self.lbl_semilla.setText("Selecciona un punto de la imagen original")
        self.lb_img_orignal.setCursor(Qt.CursorShape.CrossCursor)

    def eventFilter(self, watched, event):
        if (
            watched is self.lb_img_orignal
            and self._seleccionando_semilla
            and event.type() == QEvent.Type.MouseButtonPress
            and event.button() == Qt.MouseButton.LeftButton
        ):
            semilla = self._mapear_coordenadas_imagen(event.position().toPoint())
            if semilla is not None:
                self._semilla = semilla
                self._seleccionando_semilla = False
                self.btn_elegir_semilla.setText("Cambiar semilla")
                self.lbl_semilla.setText(
                    f"Semilla: x={semilla[0]}, y={semilla[1]}"
                )
                self.lb_img_orignal.unsetCursor()
                if (
                    self.chk_preview.isChecked()
                    and self.cmb_metodo.currentText() == "Region Growing"
                ):
                    self.aplicar_segmentacion(mostrar_errores=False)
                return True
        return super().eventFilter(watched, event)

    def _mapear_coordenadas_imagen(self, punto) -> tuple[int, int] | None:
        pixmap = self.lb_img_orignal.pixmap()
        if pixmap is None or pixmap.isNull():
            return None

        offset_x = (self.lb_img_orignal.width() - pixmap.width()) / 2
        offset_y = (self.lb_img_orignal.height() - pixmap.height()) / 2
        x_mostrado = punto.x() - offset_x
        y_mostrado = punto.y() - offset_y
        if not (
            0 <= x_mostrado < pixmap.width()
            and 0 <= y_mostrado < pixmap.height()
        ):
            return None

        x = int(x_mostrado * self._imagen_original.width() / pixmap.width())
        y = int(y_mostrado * self._imagen_original.height() / pixmap.height())
        return x, y

    def actualizar_visibilidad_imagenes(self, mostrar_original: bool):
        self.grp_original.setVisible(mostrar_original)
        self.grp_bin.setVisible(True)

    def guardar_resultado(self):
        if self._imagen_original.isNull():
            QMessageBox.warning(
                self,
                "Guardar resultado",
                "Primero importa una imagen.",
            )
            return
        self.aplicar_segmentacion(guardar_al_terminar=True)

    def _guardar_imagen_segmentada(self):
        nombre = (
            f"{self._ruta_imagen.stem}_segmentada.png"
            if self._ruta_imagen
            else "imagen_segmentada.png"
        )
        directorio = (
            Path(__file__).resolve().parents[2]
            / "data"
            / "images"
            / "processed"
        )
        ruta, _ = QFileDialog.getSaveFileName(
            self,
            "Guardar resultado de segmentación",
            str(directorio / nombre),
            "Imagen PNG (*.png)",
        )
        if not ruta:
            return

        if not ruta.lower().endswith(".png"):
            ruta += ".png"
        if not self._imagen_segmentada.save(ruta, "PNG"):
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
        self._actualizar_label(self.lb_img_bin, self._imagen_segmentada)

    def showEvent(self, evento):
        super().showEvent(evento)
        self.actualizar_vistas()

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
