
from pathlib import Path
import shutil
from ui.components.tarjeta_imagen import TarjetaImagen

from PyQt6 import uic
from PyQt6.QtWidgets import (
    QFileDialog,
    QWidget,
    QListWidgetItem,
    QMessageBox,
    QInputDialog,
)
from PyQt6.QtGui import QPixmap, QIcon
from PyQt6.QtCore import Qt, QSize


class Frm_Galeria(QWidget):

    def __init__(self):
        super().__init__()

        uic.loadUi("ui/pages/Tfrm_Galeria.ui", self)

        # Directorios de imágenes
        self.BASE_DIR = Path(__file__).resolve().parents[2]

        self.DIR_ORIGINALS = (
            self.BASE_DIR / "data" / "images" / "originals"
        )

        self.DIR_PROCESSED = (
            self.BASE_DIR / "data" / "images" / "processed"
        )

        self.formatos = {
            ".png", ".jpg", ".jpeg",
            ".bmp", ".tif", ".tiff", ".webp"
        }


        self.cmb_categoria.setCursor(
             Qt.CursorShape.PointingHandCursor
        )

        self.cmb_categoria.view().setCursor(
            Qt.CursorShape.PointingHandCursor
        )


        # Configuración de componentes
        self.configurar_galeria()
        self.configurar_combobox(self.cmb_categoria)

        # Eventos y datos
        self.conectar_eventos()
        self.cargar_imagenes()
       

    # ----------------------------------
    # CONFIGURACIÓN DEL LISTWIDGET
    # ----------------------------------

    def configurar_galeria(self):

        self.listWidget_imagenes.setViewMode(
            self.listWidget_imagenes.ViewMode.IconMode
        )

        self.listWidget_imagenes.setFlow(
            self.listWidget_imagenes.Flow.LeftToRight
        )

        self.listWidget_imagenes.setResizeMode(
            self.listWidget_imagenes.ResizeMode.Adjust
        )

        self.listWidget_imagenes.setMovement(
            self.listWidget_imagenes.Movement.Static
        )

        self.listWidget_imagenes.setWrapping(True)

        self.listWidget_imagenes.setSpacing(8)

        self.listWidget_imagenes.setSelectionMode(
            self.listWidget_imagenes.SelectionMode.SingleSelection
        )

        self.listWidget_imagenes.setHorizontalScrollBarPolicy(
            Qt.ScrollBarPolicy.ScrollBarAlwaysOff
        )

        self.listWidget_imagenes.setVerticalScrollBarPolicy(
            Qt.ScrollBarPolicy.ScrollBarAsNeeded
        )

    # ----------------------------------
    # CONECTAR EVENTOS
    # ----------------------------------

    def conectar_eventos(self):

        self.lineEdit_buscar.textChanged.connect(
        self.filtrar_imagenes
         )

        self.cmb_categoria.currentTextChanged.connect(
            self.filtrar_imagenes
        )

        self.btn_agregar.clicked.connect(
            self.agregar_imagen
        )

        self.btn_eliminar.clicked.connect(
            self.eliminar_imagen
        )

        self.btn_modificar.clicked.connect(
            self.modificar_imagen
        )

    # ----------------------------------
    # OBTENER IMÁGENES
    # ----------------------------------

    def obtener_imagenes(self):

        imagenes = []

        directorios = [
            self.DIR_ORIGINALS,
            self.DIR_PROCESSED
        ]

        for directorio in directorios:

            if not directorio.exists():
                continue

            for archivo in directorio.rglob("*"):

                if (
                    archivo.is_file()
                    and archivo.suffix.lower() in self.formatos
                ):
                    imagenes.append(archivo)

        return sorted(
            imagenes,
            key=lambda archivo: archivo.name.lower()
        )

    # ----------------------------------
    # CARGAR IMÁGENES EN LA GALERÍA
    # ----------------------------------

    def cargar_imagenes(self):

        self.listWidget_imagenes.clear()

        imagenes = self.obtener_imagenes()

        for ruta in imagenes:

            pixmap = QPixmap(str(ruta))

            if pixmap.isNull():
                continue

            if ruta.is_relative_to(self.DIR_ORIGINALS):
                categoria = "Originales"
            else:
                categoria = "Procesadas"

            item = QListWidgetItem()

            item.setData(
                Qt.ItemDataRole.UserRole,
                str(ruta)
            )

            tarjeta = TarjetaImagen(
                ruta,
                pixmap,
                categoria
            )

            item.setSizeHint(QSize(210, 220))

            self.listWidget_imagenes.addItem(item)

            self.listWidget_imagenes.setItemWidget(
                item,
                tarjeta
            )

        self.filtrar_imagenes()

    # ----------------------------------
    # FILTRAR IMÁGENES
    # ----------------------------------

    def filtrar_imagenes(self):

        texto = self.lineEdit_buscar.text().strip().lower()

        categoria = self.cmb_categoria.currentText()

        for i in range(self.listWidget_imagenes.count()):

            item = self.listWidget_imagenes.item(i)

            ruta = Path(
                item.data(Qt.ItemDataRole.UserRole)
            )

            # Filtro por nombre
            coincide_nombre = texto in item.text().lower()

            # Filtro por categoría
            coincide_categoria = True

            # if categoria == self.cmb_categoria.itemText(-1):  # "Todas"
            #     coincide_categoria = True

            if categoria == self.cmb_categoria.itemText(1):  # "Originales" 
                coincide_categoria = ruta.is_relative_to(
                    self.DIR_ORIGINALS
                )
 
            elif categoria == self.cmb_categoria.itemText(2):  # "Procesadas" 
                coincide_categoria = ruta.is_relative_to(
                    self.DIR_PROCESSED
                )

           

            # Aplicar ambos filtros
            item.setHidden(
                not (coincide_nombre and coincide_categoria)
            )

    # ----------------------------------
    # AGREGAR IMÁGENES
    # ----------------------------------

    def agregar_imagen(self):

        archivos, _ = QFileDialog.getOpenFileNames(
            self,
            "Seleccionar imágenes",
            "",
            "Imágenes (*.png *.jpg *.jpeg *.bmp *.tif *.tiff *.webp)"
        )

        if not archivos:
            return

        self.DIR_ORIGINALS.mkdir(
            parents=True,
            exist_ok=True
        )

        agregadas = 0
        omitidas = 0

        for archivo in archivos:

            origen = Path(archivo)
            destino = self.DIR_ORIGINALS / origen.name

            # Evitar sobrescribir archivos
            if destino.exists():
                omitidas += 1
                continue

            try:
                shutil.copy2(origen, destino)
                agregadas += 1

            except OSError as error:
                print(f"Error al copiar {origen.name}: {error}")
                omitidas += 1

        self.cargar_imagenes()

        QMessageBox.information(
            self,
            "Agregar imágenes",
            f"Imágenes agregadas: {agregadas}\n"
            f"Imágenes omitidas: {omitidas}"
        )

    # ----------------------------------
    # MODIFICAR IMAGEN
    # ----------------------------------

    def modificar_imagen(self):

        item = self.listWidget_imagenes.currentItem()

        if item is None:
            QMessageBox.warning(
                self,
                "Modificar imagen",
                "Selecciona una imagen de la galería."
            )
            return

        ruta_actual = Path(
            item.data(Qt.ItemDataRole.UserRole)
        )

        if not ruta_actual.exists():

            QMessageBox.warning(
                self,
                "Archivo no encontrado",
                "La imagen ya no existe en el directorio."
            )

            self.cargar_imagenes()
            return

        # Determinar categoría actual
        if ruta_actual.is_relative_to(self.DIR_ORIGINALS):
            categoria_actual = "Originales"

        elif ruta_actual.is_relative_to(self.DIR_PROCESSED):
            categoria_actual = "Procesadas"

        else:
            QMessageBox.warning(
                self,
                "Ubicación desconocida",
                "La imagen no pertenece a una categoría válida."
            )
            return

        # ------------------------------
        # CAMBIAR NOMBRE
        # ------------------------------

        nuevo_nombre, aceptar = QInputDialog.getText(
            self,
            "Modificar nombre",
            "Introduce el nuevo nombre:",
            text=ruta_actual.stem
        )

        if not aceptar:
            return

        nuevo_nombre = nuevo_nombre.strip()

        if not nuevo_nombre:
            QMessageBox.warning(
                self,
                "Nombre inválido",
                "El nombre no puede estar vacío."
            )
            return

        # Validar caracteres no permitidos en Windows
        caracteres_invalidos = '<>:"/\\|?*'

        if any(c in nuevo_nombre for c in caracteres_invalidos):

            QMessageBox.warning(
                self,
                "Nombre inválido",
                "El nombre contiene caracteres no permitidos."
            )
            return

        # ------------------------------
        # CAMBIAR CATEGORÍA
        # ------------------------------

        categorias = ["Originales", "Procesadas"]

        nueva_categoria, aceptar = QInputDialog.getItem(
            self,
            "Modificar categoría",
            "Selecciona la categoría:",
            categorias,
            categorias.index(categoria_actual),
            False
        )

        if not aceptar:
            return

        # Determinar directorio destino
        if nueva_categoria == "Originales":
            nuevo_directorio = self.DIR_ORIGINALS

        else:
            nuevo_directorio = self.DIR_PROCESSED

        # Construir nueva ruta
        nuevo_archivo = (
            nuevo_nombre + ruta_actual.suffix
        )

        nueva_ruta = nuevo_directorio / nuevo_archivo

        # ------------------------------
        # VALIDAR DESTINO
        # ------------------------------

        if nueva_ruta != ruta_actual and nueva_ruta.exists():

            QMessageBox.warning(
                self,
                "Archivo existente",
                "Ya existe una imagen con ese nombre en la categoría seleccionada."
            )
            return

        # ------------------------------
        # RENOMBRAR / MOVER
        # ------------------------------

        try:

            if nueva_ruta != ruta_actual:

                nuevo_directorio.mkdir(
                    parents=True,
                    exist_ok=True
                )

                ruta_actual.rename(nueva_ruta)

            self.cargar_imagenes()

            QMessageBox.information(
                self,
                "Imagen modificada",
                "Los cambios se realizaron correctamente."
            )

        except OSError as error:

            QMessageBox.critical(
                self,
                "Error al modificar",
                f"No se pudo modificar la imagen:\n{error}"
            )



        # ----------------------------------
        # ELIMINAR IMAGEN
        # ----------------------------------

    # ----------------------------------
    # ELIMINAR IMAGEN
    # ----------------------------------

    def eliminar_imagen(self):

        item = self.listWidget_imagenes.currentItem()

        if item is None:
            QMessageBox.warning(
                self,
                "Eliminar imagen",
                "Selecciona una imagen de la galería."
            )
            return

        ruta = Path(
            item.data(Qt.ItemDataRole.UserRole)
        )

        respuesta = QMessageBox.question(
            self,
            "Confirmar eliminación",
            f"¿Deseas eliminar permanentemente esta imagen?\n\n"
            f"{ruta.name}",
            QMessageBox.StandardButton.Yes |
            QMessageBox.StandardButton.No,
            QMessageBox.StandardButton.No
        )

        if respuesta != QMessageBox.StandardButton.Yes:
            return

        try:

            if not ruta.exists():
                raise FileNotFoundError("El archivo ya no existe.")

            ruta.unlink()

            self.cargar_imagenes()

            QMessageBox.information(
                self,
                "Imagen eliminada",
                "La imagen se eliminó correctamente."
            )

        except OSError as error:

            QMessageBox.critical(
                self,
                "Error",
                f"No se pudo eliminar la imagen:\n{error}"
            )

    # ----------------------------------
    # CONFIGURACIÓN DEL COMBOBOX
    # ----------------------------------
        
    def configurar_combobox(self, combo):

        combo.setCursor(Qt.CursorShape.PointingHandCursor)

        vista = combo.view()

        vista.setCursor(Qt.CursorShape.PointingHandCursor)
        vista.viewport().setCursor(Qt.CursorShape.PointingHandCursor)

        vista.setMouseTracking(True)
        vista.viewport().setMouseTracking(True)




