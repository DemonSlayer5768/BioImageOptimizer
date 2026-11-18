from PyQt6.QtWidgets import QMainWindow
from PyQt6 import uic

from ui.pages.Frm_Dashboard import Frm_Dashboard
from ui.pages.Frm_Galeria import Frm_Galeria
from ui.pages.Frm_Binarizacion import Frm_Binarizacion
from ui.pages.Frm_Segmentacion import Frm_Segmentacion





class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        uic.loadUi("ui/MainWindow.ui", self)

        # Crear paginas
        self.dashboard = Frm_Dashboard()
        self.galeria = Frm_Galeria()
        self.binarizacion = Frm_Binarizacion()
        self.segmentacion = Frm_Segmentacion()
        self._destino_galeria = None
       
        # self.evaluacion = Frm_Evaluacion()

        self.binarizacion.solicitar_galeria.connect(
            self.abrir_galeria_para_binarizacion
        )
        self.segmentacion.solicitar_galeria.connect(
            self.abrir_galeria_para_segmentacion
        )
        self.galeria.imagen_seleccionada.connect(
            self.cargar_imagen_seleccionada
        )

        # Agregar paginas al Stack
        self.stackedWidget.addWidget(self.dashboard)
        self.stackedWidget.addWidget(self.galeria)
        self.stackedWidget.addWidget(self.binarizacion)
        self.stackedWidget.addWidget(self.segmentacion)

        # Conectar botones SideBar
        self.btn_dashboard.clicked.connect(
            lambda: self.navegar_sidebar(self.dashboard)
        )
        self.btn_galeria.clicked.connect(
            lambda: self.navegar_sidebar(self.galeria)
        )
        self.btn_binarizacion.clicked.connect(
            lambda: self.navegar_sidebar(self.binarizacion)
        )
        self.btn_segmentacion.clicked.connect(
            lambda: self.navegar_sidebar(self.segmentacion)
        )
        # self.btn_optimizacion.clicked.connect(
        #     lambda: self.navegar_sidebar(self.optimizacion)
        # )
        # self.btn_procesamiento.clicked.connect(
        #     lambda: self.navegar_sidebar(self.procesamiento)
        # )
        # self.btn_restauracion.clicked.connect(
        #     lambda: self.navegar_sidebar(self.restauracion)
        # )
        # self.btn_segmentacion.clicked.connect(
        #     lambda: self.navegar_sidebar(self.segmentacion)
        # )
        # self.btn_configuracion.clicked.connect(
        #     lambda: self.navegar_sidebar(self.configuracion)
        # )
        # self.btn_historial.clicked.connect(
        #     lambda: self.navegar_sidebar(self.historial)
        # )
        # self.btn_evaluacion.clicked.connect(
        #     lambda: self.change_page(self.evaluacion)
        # )


        #Boton salir
        self.btn_salir.clicked.connect(self.close)




        # Página inicial
        self.change_page(self.dashboard)

    def change_page(self, page):
        if page is not self.galeria:
            self.galeria.set_modo_seleccion(False)
        else:
            self.galeria.actualizar_al_entrar()

        self.stackedWidget.setCurrentWidget(page)

    def navegar_sidebar(self, page):
        self._destino_galeria = None
        self.limpiar_formularios()
        self.change_page(page)

    def limpiar_formularios(self):
        self.binarizacion.limpiar_formulario()
        self.segmentacion.limpiar_formulario()
        self.galeria.limpiar_formulario()

    def abrir_galeria_para_binarizacion(self):
        self._destino_galeria = "binarizacion"
        self.galeria.set_modo_seleccion(True)
        self.change_page(self.galeria)

    def abrir_galeria_para_segmentacion(self):
        self._destino_galeria = "segmentacion"
        self.galeria.set_modo_seleccion(True)
        self.change_page(self.galeria)

    def cargar_imagen_seleccionada(self, ruta):
        if self._destino_galeria == "segmentacion":
            self.cargar_imagen_en_segmentacion(ruta)
        else:
            self.cargar_imagen_en_binarizacion(ruta)
        self._destino_galeria = None

    def cargar_imagen_en_binarizacion(self, ruta):
        self.galeria.set_modo_seleccion(False)
        self.binarizacion.cargar_imagen(ruta)
        self.change_page(self.binarizacion)

    def cargar_imagen_en_segmentacion(self, ruta):
        self.galeria.set_modo_seleccion(False)
        self.segmentacion.cargar_imagen(ruta)
        self.change_page(self.segmentacion)

    def closeEvent(self, evento):
        self.segmentacion.esperar_procesamiento()
        super().closeEvent(evento)