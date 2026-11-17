
from PyQt6.QtWidgets import QWidget, QFileDialog, QMessageBox
from PyQt6 import uic

from core.image_manager import import_images


class Frm_Dashboard(QWidget):

    def __init__(self):
        super().__init__()

        uic.loadUi("ui/pages/Tfrm_Dashboard.ui", self)

        self.conectar_eventos()

    # Conectar botones del Dashboard
    def conectar_eventos(self):

        self.Tbtn_Importar_Imagenes.clicked.connect(
            self.importar_imagenes
        )

    # Función para importar imágenes
    def importar_imagenes(self):

        file_paths, _ = QFileDialog.getOpenFileNames(
            self,
            "Seleccionar imágenes",
            "",
            "Imágenes (*.png *.jpg *.jpeg *.bmp *.tif *.tiff *.webp)"
        )

        if not file_paths:
            return

        imported = import_images(file_paths)

        if imported:
            QMessageBox.information(
                self,
                "Imagen Guardada",
                f"Se importaron {len(imported)} imágenes correctamente."
            )
        else:
            QMessageBox.warning(
                self,
                "Importación",
                "No se pudo importar ninguna imagen."
            )
