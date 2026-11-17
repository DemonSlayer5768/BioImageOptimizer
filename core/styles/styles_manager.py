
from pathlib import Path


class StyleManager:

    def __init__(self):
        self.styles_path = (
            Path(__file__).resolve().parents[2]
            / "resources"
            / "styles"
        )

    def load_styles(self, app):

        components = [

            #carpeta global
            "global.qss",

            #carpeta components
            "components/QLabel.qss",
            "components/QPushButton.qss",
            "components/QComboBox.qss",
            "components/QLineEdit.qss",
            "components/QCheckBox.qss",
            "components/QSlider.qss",
            "components/QSpinBox.qss",
            "components/QGroupBox.qss",

        ]

        stylesheet = ""

        for file in components:

            file_path = self.styles_path / file

            if file_path.exists():

                with open(file_path, "r", encoding="utf-8") as f:
                    stylesheet += f.read() + "\n"

            else:
                print(f"[STYLE] Archivo no encontrado: {file_path}")

        app.setStyleSheet(stylesheet)

        print("[STYLE] Estilos cargados correctamente.")
