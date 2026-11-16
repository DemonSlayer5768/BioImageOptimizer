
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

        self._candidatos_filtro = []
        self._texto_filtro_anterior = ""
        self._categoria_filtro_anterior = None

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
        self.aplicar_estilo_scrollbar(
            self.listWidget_imagenes.verticalScrollBar()    
        )


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
            self.listWidget_imagenes.SelectionMode.ExtendedSelection
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

        self.listWidget_imagenes.itemSelectionChanged.connect(
            self.actualizar_seleccion_tarjetas
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

        self._candidatos_filtro = []
        self._texto_filtro_anterior = ""
        self._categoria_filtro_anterior = None
        self.listWidget_imagenes.clear()

        imagenes = self.obtener_imagenes()

        for ruta in imagenes:

            pixmap = QPixmap(str(ruta))

            if pixmap.isNull():
                continue

            es_original = ruta.is_relative_to(self.DIR_ORIGINALS)
            if es_original:
                categoria = "Originales"
            else:
                categoria = "Procesadas"

            item = QListWidgetItem()

            item.setData(
                Qt.ItemDataRole.UserRole,
                str(ruta)
            )

            item.setData(
                Qt.ItemDataRole.UserRole + 1,
                ruta.name.casefold()
            )
            item.setData(
                Qt.ItemDataRole.UserRole + 2,
                es_original
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
        self.actualizar_seleccion_tarjetas()

    def actualizar_seleccion_tarjetas(self):

        self.btn_agregar.setEnabled(
            not self.listWidget_imagenes.selectedItems()
        )

        for i in range(self.listWidget_imagenes.count()):

            item = self.listWidget_imagenes.item(i)
            tarjeta = self.listWidget_imagenes.itemWidget(item)

            if tarjeta is not None:
                tarjeta.set_selected(item.isSelected())

    # ----------------------------------
    # FILTRAR IMÁGENES
    # ----------------------------------

    def filtrar_imagenes(self):

        texto = self.lineEdit_buscar.text().strip().casefold()
        indice_categoria = self.cmb_categoria.currentIndex()

        es_busqueda_incremental = (
            indice_categoria == self._categoria_filtro_anterior
            and texto.startswith(self._texto_filtro_anterior)
        )

        if es_busqueda_incremental:
            candidatos = self._candidatos_filtro
        else:
            candidatos = [
                self.listWidget_imagenes.item(i)
                for i in range(self.listWidget_imagenes.count())
            ]

        coincidencias = []
        for item in candidatos:
            nombre = item.data(Qt.ItemDataRole.UserRole + 1)
            es_original = item.data(Qt.ItemDataRole.UserRole + 2)

            coincide_nombre = nombre.startswith(texto)

            if indice_categoria == 1:
                coincide_categoria = es_original
            elif indice_categoria == 2:
                coincide_categoria = not es_original
            else:
                coincide_categoria = True

            coincide = coincide_nombre and coincide_categoria
            item.setHidden(not coincide)
            if coincide:
                coincidencias.append(item)

        self._candidatos_filtro = coincidencias
        self._texto_filtro_anterior = texto
        self._categoria_filtro_anterior = indice_categoria

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

        items = self.listWidget_imagenes.selectedItems()

        if not items:
            QMessageBox.warning(
                self,
                "Modificar imagen",
                "Selecciona una o más imágenes de la galería."
            )
            return

        rutas = [
            Path(item.data(Qt.ItemDataRole.UserRole))
            for item in items
        ]

        nuevo_nombre, aceptar = QInputDialog.getText(
            self,
            "Modificar nombre",
            "Introduce el nombre base para las imágenes seleccionadas:",
            text=rutas[0].stem
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

        if any(not ruta.exists() for ruta in rutas):
            QMessageBox.warning(
                self,
                "Archivo no encontrado",
                "Una o más imágenes ya no existen. Se actualizará la galería."
            )
            self.cargar_imagenes()
            return

        categorias = ["Originales", "Procesadas"]

        ruta_actual = rutas[0]
        if ruta_actual.is_relative_to(self.DIR_ORIGINALS):
            indice_categoria = 0
        elif ruta_actual.is_relative_to(self.DIR_PROCESSED):
            indice_categoria = 1
        else:
            QMessageBox.warning(
                self,
                "Ubicación desconocida",
                "La imagen no pertenece a una categoría válida."
            )
            return

        nueva_categoria, aceptar = QInputDialog.getItem(
            self,
            "Modificar categoría",
            "Selecciona la categoría para todas las imágenes:",
            categorias,
            indice_categoria,
            False
        )

        if not aceptar:
            return

        if nueva_categoria == "Originales":
            nuevo_directorio = self.DIR_ORIGINALS
        else:
            nuevo_directorio = self.DIR_PROCESSED

        for ruta in rutas:
            if not (
                ruta.is_relative_to(self.DIR_ORIGINALS)
                or ruta.is_relative_to(self.DIR_PROCESSED)
            ):
                QMessageBox.warning(
                    self,
                    "Ubicación desconocida",
                    f"{ruta.name} no pertenece a una categoría válida."
                )
                return

        try:
            nuevo_directorio.mkdir(parents=True, exist_ok=True)
            reservados = {
                str(ruta.resolve()).casefold()
                for ruta in nuevo_directorio.iterdir()
                if ruta.is_file()
            }

            destinos = []
            for ruta in rutas:
                numero = 1
                while True:
                    sufijo = "" if numero == 1 else f"_{numero}"
                    destino = nuevo_directorio / (
                        f"{nuevo_nombre}{sufijo}{ruta.suffix}"
                    )
                    clave_destino = str(destino.resolve()).casefold()

                    if (
                        clave_destino not in reservados
                        or clave_destino == str(ruta.resolve()).casefold()
                    ):
                        destinos.append((ruta, destino))
                        reservados.add(clave_destino)
                        break

                    numero += 1
        except OSError as error:
            QMessageBox.warning(
                self,
                "Error al modificar",
                f"No se pudo preparar la categoría seleccionada:\n{error}"
            )
            return

        errores = []
        modificadas = 0

        for ruta, destino in destinos:
            try:
                if ruta != destino:
                    ruta.rename(destino)
                modificadas += 1
            except OSError as error:
                errores.append(f"{ruta.name}: {error}")

        self.cargar_imagenes()

        if errores:
            QMessageBox.warning(
                self,
                "Modificación incompleta",
                f"Imágenes modificadas: {modificadas}\n\n"
                "No se pudieron modificar:\n" + "\n".join(errores)
            )
        else:
            QMessageBox.information(
                self,
                "Imágenes modificadas",
                f"Imágenes modificadas: {modificadas}"
            )

    # ----------------------------------
    # ELIMINAR IMAGEN
    # ----------------------------------

    def eliminar_imagen(self):

        items = self.listWidget_imagenes.selectedItems()

        if not items:
            QMessageBox.warning(
                self,
                "Eliminar imagen",
                "Selecciona una o más imágenes de la galería."
            )
            return

        rutas = [
            Path(item.data(Qt.ItemDataRole.UserRole))
            for item in items
        ]

        respuesta = QMessageBox.question(
            self,
            "Confirmar eliminación",
            "¿Deseas eliminar permanentemente estas imágenes?\n\n"
            + "\n".join(ruta.name for ruta in rutas),
            QMessageBox.StandardButton.Yes |
            QMessageBox.StandardButton.No,
            QMessageBox.StandardButton.No
        )

        if respuesta != QMessageBox.StandardButton.Yes:
            return

        eliminadas = 0
        errores = []

        for ruta in rutas:
            try:
                if not ruta.exists():
                    raise FileNotFoundError("El archivo ya no existe.")
                ruta.unlink()
                eliminadas += 1
            except OSError as error:
                errores.append(f"{ruta.name}: {error}")

        self.cargar_imagenes()

        if errores:
            QMessageBox.warning(
                self,
                "Eliminación incompleta",
                f"Imágenes eliminadas: {eliminadas}\n\n"
                "No se pudieron eliminar:\n" + "\n".join(errores)
            )
        else:
            QMessageBox.information(
                self,
                "Imágenes eliminadas",
                f"Imágenes eliminadas: {eliminadas}"
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



    # ----------------------------------
    # ESTILO DE LA SCROLLBAR VERTICAL
    # ----------------------------------

    def aplicar_estilo_scrollbar(self, scrollbar):

      scrollbar.setStyleSheet("""
                 QScrollBar:vertical {
                     background-color: #0b0f1a;
                     width: 8px;
                     margin: 4px 2px 4px 0;
                     border: none;
                     border-radius: 4px;
                 }
     
                 QScrollBar::handle:vertical {
                     background-color: #2f3e56;
                     border-radius: 4px;
                     min-height: 40px;
                 }
     
                 QScrollBar::handle:vertical:hover {
                     background-color: #65D6C6;
                 }
     
                 QScrollBar::add-line:vertical,
                 QScrollBar::sub-line:vertical {
                     height: 0px;
                     background: none;
                 }
     
                 QScrollBar::add-page:vertical,
                 QScrollBar::sub-page:vertical {
                     background: none;
                 }
             """)
      

