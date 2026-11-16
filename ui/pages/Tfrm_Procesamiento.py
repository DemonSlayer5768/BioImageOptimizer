from PyQt6.QtWidgets import QWidget
from PyQt6 import uic


class Frm_Procesamiento(QWidget):

    def __init__(self):
        super().__init__()

        uic.loadUi(
            "ui/pages/Tfrm_Procesamiento.ui",
            self
        )