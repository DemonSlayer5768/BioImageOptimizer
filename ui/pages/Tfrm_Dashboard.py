from PyQt6.QtWidgets import QWidget
from PyQt6 import uic


class Frm_Dashboard(QWidget):

    def __init__(self):
        super().__init__()

        uic.loadUi(
            "ui/pages/Tfrm_Dashboard.ui",
            self
        )