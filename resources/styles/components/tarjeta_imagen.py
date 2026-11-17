from PyQt6.QtWidgets import (
    QVBoxLayout,
    QFrame,
    QLabel,
    QHBoxLayout
)
from PyQt6.QtCore import Qt, QSize



class TarjetaImagen(QFrame):

    def __init__(self, ruta, pixmap, categoria):
        super().__init__()

        self.setObjectName("tarjeta_imagen")
        self.setCursor(Qt.CursorShape.PointingHandCursor)
        self.setProperty("selected", False)

        layout = QVBoxLayout(self)
        layout.setContentsMargins(10, 10, 10, 10)
        layout.setSpacing(6)

        # Nombre de la imagen (arriba)
        nombre = QLabel(ruta.name)
        nombre.setObjectName("nombre_imagen")
        nombre.setWordWrap(True)
        nombre.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter)

        # Miniatura
        imagen = QLabel()
        imagen.setObjectName("miniatura_imagen")
        imagen.setAlignment(Qt.AlignmentFlag.AlignCenter)

        miniatura = pixmap.scaled(
            QSize(200, 155),                          # ← más ancha
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation
        )
        imagen.setPixmap(miniatura)

        # Badge abajo a la derecha
        texto_badge = "Original" if categoria == "Originales" else "Procesada"

        badge = QLabel(texto_badge)
        badge.setObjectName(
            "badge_original" if categoria == "Originales"
            else "badge_procesada"
        )
        
        badge.setAlignment(Qt.AlignmentFlag.AlignCenter)
        badge.setFixedHeight(22)

        # Fila inferior solo con el badge alineado a la derecha
        fila_inferior = QHBoxLayout()
        fila_inferior.setContentsMargins(0, 0, 0, 0)
        fila_inferior.addStretch()          # empuja el badge a la derecha
        fila_inferior.addWidget(badge)

        # Montaje
        layout.addWidget(nombre)
        layout.addWidget(imagen, 1)
        layout.addLayout(fila_inferior)

        self.setStyleSheet("""
            QFrame#tarjeta_imagen {
                background-color: #111a2e;
                border: 1px solid #2f3e56;
                border-radius: 10px;
            }

            QFrame#tarjeta_imagen:hover {
                background-color: #1b2a41;
                border: 1px solid #65D6C6;
            }

            QFrame#tarjeta_imagen[selected="true"],
            QFrame#tarjeta_imagen[selected="true"]:hover {
                background-color: #1b2a41;
                border: 2px solid #65D6C6;
            }

            QLabel#nombre_imagen {
                color: #c8d3e0;
                font-size: 11px;
                font-weight: 600;
            }

            QLabel#badge_original {
                background-color: #1b2a41;
                color: #65D6C6;
                border: 1px solid #65D6C6;
                border-radius: 6px;
                padding: 3px 8px;
                font-size: 9px;
                font-weight: bold;
            }

            QLabel#badge_procesada {
                background-color: #3b2a1a;          /* fondo oscuro cálido */
                color: #f59e0b;                     /* ámbar */
                border: 1px solid #f59e0b;
                border-radius: 6px;
                padding: 3px 8px;
                font-size: 9px;
                font-weight: bold;
            }
        """)

    def set_selected(self, selected):
        self.setProperty("selected", selected)
        self.style().unpolish(self)
        self.style().polish(self)
        self.update()
