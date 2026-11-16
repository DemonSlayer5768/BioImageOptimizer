from PyQt6.QtWidgets import QMainWindow
from PyQt6 import uic

from ui.pages.Tfrm_Dashboard import Frm_Dashboard
from ui.pages.Tfrm_Galeria import Frm_Galeria



class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        uic.loadUi("ui/MainWindow.ui", self)

        # Crear paginas
        self.dashboard = Frm_Dashboard()
        self.galeria = Frm_Galeria()

        # Agregar paginas al Stack
        self.stackedWidget.addWidget(self.dashboard)
        self.stackedWidget.addWidget(self.galeria)
     

        # Conectar botones SideBar
        self.btn_dashboard.clicked.connect(
            lambda: self.change_page(self.dashboard)
        )
        self.btn_Galeria.clicked.connect(
            lambda: self.change_page(self.galeria)
        )

        #Boton salir
        self.btn_salir.clicked.connect(self.close)




        # Página inicial
        self.change_page(self.dashboard)

    def change_page(self, page):

        self.stackedWidget.setCurrentWidget(page)