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
            lambda: self.change_page(self.dashboard)
        )
        self.btn_galeria.clicked.connect(
            lambda: self.change_page(self.galeria)
        )
        self.btn_optimizacion.clicked.connect(
            lambda: self.change_page(self.optimizacion)
        )
        self.btn_procesamiento.clicked.connect(
            lambda: self.change_page(self.procesamiento)
        )
        self.btn_restauracion.clicked.connect(
            lambda: self.change_page(self.restauracion)
        )
        self.btn_segmentacion.clicked.connect(
            lambda: self.change_page(self.segmentacion)
        )
        self.btn_binarizacion.clicked.connect(
            lambda: self.change_page(self.binarizacion)
        )
        self.btn_configuracion.clicked.connect(
            lambda: self.change_page(self.configuracion)
        )
        self.btn_historial.clicked.connect(
            lambda: self.change_page(self.historial)
        )
        # self.btn_evaluacion.clicked.connect(
        #     lambda: self.change_page(self.evaluacion)
        # )


        #Boton salir
        self.btn_salir.clicked.connect(self.close)




        # Página inicial
        self.change_page(self.dashboard)

    def change_page(self, page):

        self.stackedWidget.setCurrentWidget(page)