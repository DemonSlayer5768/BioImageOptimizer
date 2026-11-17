from PyQt6.QtWidgets import QMainWindow
from PyQt6 import uic

from ui.pages.Tfrm_Dashboard import Frm_Dashboard
from ui.pages.Tfrm_Galeria import Frm_Galeria
from ui.pages.Tfrm_Optimizacion import Frm_Optimizacion
from ui.pages.Tfrm_Procesamiento import Frm_Procesamiento
from ui.pages.Tfrm_Restauracion import Frm_Restauracion
from ui.pages.Tfrm_Segmentacion import Frm_Segmentacion
from ui.pages.Tfrm_Binarizacion import Frm_Binarizacion
from ui.pages.Tfrm_Configuracion import Frm_Configuracion
# from ui.pages.Tfrm_Evaluacion import Frm_Evaluacion
from ui.pages.Tfrm_Historial import Frm_Historial




class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        uic.loadUi("ui/MainWindow.ui", self)

        # Crear paginas
        self.dashboard = Frm_Dashboard()
        self.galeria = Frm_Galeria()
        self.optimizacion = Frm_Optimizacion()
        self.procesamiento = Frm_Procesamiento()
        self.restauracion = Frm_Restauracion()
        self.segmentacion = Frm_Segmentacion()
        self.binarizacion = Frm_Binarizacion()
        self.configuracion = Frm_Configuracion()
        self.historial = Frm_Historial()
        # self.evaluacion = Frm_Evaluacion()

        self.binarizacion.solicitar_galeria.connect(
            self.abrir_galeria_para_binarizacion
        )
        self.galeria.imagen_seleccionada.connect(
            self.cargar_imagen_en_binarizacion
        )

        # Agregar paginas al Stack
        self.stackedWidget.addWidget(self.dashboard)
        self.stackedWidget.addWidget(self.galeria)
        self.stackedWidget.addWidget(self.optimizacion)
        self.stackedWidget.addWidget(self.procesamiento)
        self.stackedWidget.addWidget(self.restauracion)
        self.stackedWidget.addWidget(self.segmentacion)
        self.stackedWidget.addWidget(self.binarizacion)
        self.stackedWidget.addWidget(self.configuracion)
        self.stackedWidget.addWidget(self.historial)
        # self.stackedWidget.addWidget(self.evaluacion)

        # Conectar botones SideBar
        self.btn_dashboard.clicked.connect(
            lambda: self.navegar_sidebar(self.dashboard)
        )
        self.btn_galeria.clicked.connect(
            lambda: self.navegar_sidebar(self.galeria)
        )
        self.btn_optimizacion.clicked.connect(
            lambda: self.navegar_sidebar(self.optimizacion)
        )
        self.btn_procesamiento.clicked.connect(
            lambda: self.navegar_sidebar(self.procesamiento)
        )
        self.btn_restauracion.clicked.connect(
            lambda: self.navegar_sidebar(self.restauracion)
        )
        self.btn_segmentacion.clicked.connect(
            lambda: self.navegar_sidebar(self.segmentacion)
        )
        self.btn_binarizacion.clicked.connect(
            lambda: self.navegar_sidebar(self.binarizacion)
        )
        self.btn_configuracion.clicked.connect(
            lambda: self.navegar_sidebar(self.configuracion)
        )
        self.btn_historial.clicked.connect(
            lambda: self.navegar_sidebar(self.historial)
        )
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
        self.limpiar_formularios()
        self.change_page(page)

    def limpiar_formularios(self):
        self.binarizacion.limpiar_formulario()
        self.galeria.limpiar_formulario()

    def abrir_galeria_para_binarizacion(self):
        self.galeria.set_modo_seleccion(True)
        self.change_page(self.galeria)

    def cargar_imagen_en_binarizacion(self, ruta):
        self.galeria.set_modo_seleccion(False)
        self.binarizacion.cargar_imagen(ruta)
        self.change_page(self.binarizacion)