from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QSlider, QApplication


# Modificacion de QSlider para cambiar el cursor al pasar sobre el slider y mientras se arrastra
def configurar_sliders(self):
    for slider in self.findChildren(QSlider):
        # Cursor al pasar sobre el slider
        slider.setCursor(Qt.CursorShape.OpenHandCursor)

        # Cursor mientras se arrastra
        slider.sliderPressed.connect(
            lambda s=slider: s.setCursor(Qt.CursorShape.ClosedHandCursor)
        )

        # Restaurar cursor al soltar
        slider.sliderReleased.connect(
            lambda s=slider: s.setCursor(Qt.CursorShape.OpenHandCursor)
        )


def centrar_ventana(self):
    pantalla = QApplication.primaryScreen()
    geometria = pantalla.availableGeometry()

    # Tamaño inicial
    self.resize(1024, 768)

    # Tamaño mínimo permitido
    self.setMinimumSize(1024, 768)

    # Obtener pantalla
    pantalla = self.screen().availableGeometry()

    x = (geometria.width() - self.width()) // 2
    y = (geometria.height() - self.height()) // 2

    self.move(x, y)