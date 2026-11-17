import sys
from PyQt6.QtWidgets import QApplication
from ui.MainWindow import MainWindow
from core.styles.styles_manager import StyleManager
 

if __name__ == "__main__":

    app = QApplication(sys.argv)

    # Cargar estilos globales
    style_manager = StyleManager()
    style_manager.load_styles(app)


    #iniciar ventana principal
    window = MainWindow()
    window.show()

    sys.exit(app.exec())