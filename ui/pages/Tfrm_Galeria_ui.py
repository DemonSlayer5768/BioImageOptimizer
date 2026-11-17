# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Tfrm_Galeria.ui'
##
## Created by: Qt User Interface Compiler version 6.12.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QLineEdit, QListView,
    QListWidget, QListWidgetItem, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_Frm_Galeria(object):
    def setupUi(self, Frm_Galeria):
        if not Frm_Galeria.objectName():
            Frm_Galeria.setObjectName(u"Frm_Galeria")
        Frm_Galeria.resize(950, 820)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Frm_Galeria.sizePolicy().hasHeightForWidth())
        Frm_Galeria.setSizePolicy(sizePolicy)
        Frm_Galeria.setMinimumSize(QSize(950, 820))
        Frm_Galeria.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.horizontalLayout_2 = QHBoxLayout(Frm_Galeria)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.Panel_container = QFrame(Frm_Galeria)
        self.Panel_container.setObjectName(u"Panel_container")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.Panel_container.sizePolicy().hasHeightForWidth())
        self.Panel_container.setSizePolicy(sizePolicy1)
        self.Panel_container.setMinimumSize(QSize(950, 820))
        self.Panel_container.setStyleSheet(u"")
        self.Panel_container.setFrameShape(QFrame.Shape.StyledPanel)
        self.Panel_container.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.Panel_container)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.Panel_Head = QFrame(self.Panel_container)
        self.Panel_Head.setObjectName(u"Panel_Head")
        self.Panel_Head.setMaximumSize(QSize(16777215, 100))
        self.Panel_Head.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.Panel_Head.setFrameShape(QFrame.Shape.NoFrame)
        self.Panel_Head.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.Panel_Head)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.Separator = QFrame(self.Panel_Head)
        self.Separator.setObjectName(u"Separator")
        self.Separator.setMaximumSize(QSize(10, 16777215))
        self.Separator.setStyleSheet(u"background-color : rgb(101, 214, 198);")
        self.Separator.setFrameShape(QFrame.Shape.NoFrame)
        self.Separator.setFrameShadow(QFrame.Shadow.Plain)

        self.horizontalLayout_5.addWidget(self.Separator)

        self.Layout_vertical = QVBoxLayout()
        self.Layout_vertical.setObjectName(u"Layout_vertical")
        self.lb_titulo = QLabel(self.Panel_Head)
        self.lb_titulo.setObjectName(u"lb_titulo")
        self.lb_titulo.setStyleSheet(u"")

        self.Layout_vertical.addWidget(self.lb_titulo)

        self.lb_descripcion = QLabel(self.Panel_Head)
        self.lb_descripcion.setObjectName(u"lb_descripcion")
        self.lb_descripcion.setStyleSheet(u"")

        self.Layout_vertical.addWidget(self.lb_descripcion)


        self.horizontalLayout_5.addLayout(self.Layout_vertical)


        self.verticalLayout.addWidget(self.Panel_Head)

        self.Card_body = QFrame(self.Panel_container)
        self.Card_body.setObjectName(u"Card_body")
        self.Card_body.setStyleSheet(u"")
        self.Card_body.setFrameShape(QFrame.Shape.StyledPanel)
        self.Card_body.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.Card_body)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(15, 0, 15, 0)
        self.Layout_grid = QGridLayout()
        self.Layout_grid.setObjectName(u"Layout_grid")
        self.Layout_grid.setHorizontalSpacing(25)
        self.Layout_grid.setVerticalSpacing(9)
        self.Layout_grid.setContentsMargins(9, 9, 9, 9)
        self.lineEdit_buscar = QLineEdit(self.Card_body)
        self.lineEdit_buscar.setObjectName(u"lineEdit_buscar")
        self.lineEdit_buscar.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.lineEdit_buscar.setStyleSheet(u"")
        self.lineEdit_buscar.setClearButtonEnabled(False)

        self.Layout_grid.addWidget(self.lineEdit_buscar, 2, 2, 1, 1)

        self.label = QLabel(self.Card_body)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"")

        self.Layout_grid.addWidget(self.label, 1, 2, 1, 1)

        self.cmb_categoria = QComboBox(self.Card_body)
        self.cmb_categoria.addItem("")
        self.cmb_categoria.addItem("")
        self.cmb_categoria.addItem("")
        self.cmb_categoria.setObjectName(u"cmb_categoria")
        self.cmb_categoria.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.cmb_categoria.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.cmb_categoria.setStyleSheet(u"")
        self.cmb_categoria.setEditable(False)
        self.cmb_categoria.setLabelDrawingMode(QComboBox.LabelDrawingMode.UseStyle)

        self.Layout_grid.addWidget(self.cmb_categoria, 2, 0, 1, 1)

        self.label_2 = QLabel(self.Card_body)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"")

        self.Layout_grid.addWidget(self.label_2, 1, 0, 1, 1)

        self.Layout_grid.setColumnStretch(0, 3)
        self.Layout_grid.setColumnStretch(1, 2)
        self.Layout_grid.setColumnStretch(2, 5)

        self.verticalLayout_2.addLayout(self.Layout_grid)

        self.listWidget_imagenes = QListWidget(self.Card_body)
        self.listWidget_imagenes.setObjectName(u"listWidget_imagenes")
        self.listWidget_imagenes.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.listWidget_imagenes.setStyleSheet(u"/* GALER\u00cdA */\n"
"\n"
"/* ===================== GALER\u00cdA ===================== */\n"
"QListWidget {\n"
"    background-color: #0b0f1a;\n"
"    border: none;\n"
"    outline: none;\n"
"    padding: 14px;\n"
"    color: #c8d3e0;\n"
"}\n"
"\n"
"/* ===================== ITEMS ===================== */\n"
"QListWidget::item {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"    border-radius: 12px;\n"
"    padding: 4px;\n"
"    margin: 6px;\n"
"}\n"
"\n"
"QListWidget::item:hover {\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"QListWidget::item:selected {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"}\n"
"\n"
"")
        self.listWidget_imagenes.setFrameShape(QFrame.Shape.NoFrame)
        self.listWidget_imagenes.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.listWidget_imagenes.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.listWidget_imagenes.setIconSize(QSize(150, 120))
        self.listWidget_imagenes.setMovement(QListView.Movement.Static)
        self.listWidget_imagenes.setResizeMode(QListView.ResizeMode.Adjust)
        self.listWidget_imagenes.setSpacing(8)
        self.listWidget_imagenes.setGridSize(QSize(210, 220))
        self.listWidget_imagenes.setViewMode(QListView.ViewMode.IconMode)
        self.listWidget_imagenes.setUniformItemSizes(True)
        self.listWidget_imagenes.setWordWrap(True)

        self.verticalLayout_2.addWidget(self.listWidget_imagenes)

        self.Layout_horizontal = QHBoxLayout()
        self.Layout_horizontal.setSpacing(9)
        self.Layout_horizontal.setObjectName(u"Layout_horizontal")
        self.Layout_horizontal.setContentsMargins(9, 15, 9, 15)
        self.btn_abrir = QPushButton(self.Card_body)
        self.btn_abrir.setObjectName(u"btn_abrir")
        self.btn_abrir.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_abrir.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.btn_abrir.setStyleSheet(u"")
        self.btn_abrir.setIconSize(QSize(15, 15))
        self.btn_abrir.setAutoRepeat(False)

        self.Layout_horizontal.addWidget(self.btn_abrir)

        self.btn_eliminar = QPushButton(self.Card_body)
        self.btn_eliminar.setObjectName(u"btn_eliminar")
        self.btn_eliminar.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_eliminar.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.btn_eliminar.setStyleSheet(u"")
        icon = QIcon()
        icon.addFile(u"../../resources/Icons/Icons_rojos/delete.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_eliminar.setIcon(icon)
        self.btn_eliminar.setIconSize(QSize(20, 20))
        self.btn_eliminar.setAutoRepeat(False)

        self.Layout_horizontal.addWidget(self.btn_eliminar)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.Layout_horizontal.addItem(self.horizontalSpacer)

        self.btn_guardar = QPushButton(self.Card_body)
        self.btn_guardar.setObjectName(u"btn_guardar")
        self.btn_guardar.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_guardar.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.btn_guardar.setStyleSheet(u"")
        icon1 = QIcon()
        icon1.addFile(u"../../resources/Icons/Icons_amarillos/saved.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_guardar.setIcon(icon1)
        self.btn_guardar.setIconSize(QSize(20, 20))

        self.Layout_horizontal.addWidget(self.btn_guardar)

        self.btn_modificar = QPushButton(self.Card_body)
        self.btn_modificar.setObjectName(u"btn_modificar")
        self.btn_modificar.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_modificar.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.btn_modificar.setStyleSheet(u"")
        icon2 = QIcon()
        icon2.addFile(u"../../resources/Icons/Icons_azules/edit.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_modificar.setIcon(icon2)
        self.btn_modificar.setIconSize(QSize(20, 20))
        self.btn_modificar.setAutoRepeat(False)

        self.Layout_horizontal.addWidget(self.btn_modificar)

        self.btn_agregar = QPushButton(self.Card_body)
        self.btn_agregar.setObjectName(u"btn_agregar")
        self.btn_agregar.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_agregar.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.btn_agregar.setStyleSheet(u"")
        icon3 = QIcon()
        icon3.addFile(u"../../resources/Icons/Icons_verdes/add_icon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_agregar.setIcon(icon3)
        self.btn_agregar.setIconSize(QSize(20, 20))
        self.btn_agregar.setAutoRepeat(False)

        self.Layout_horizontal.addWidget(self.btn_agregar)

        self.Layout_horizontal.setStretch(1, 1)
        self.Layout_horizontal.setStretch(2, 2)
        self.Layout_horizontal.setStretch(3, 1)
        self.Layout_horizontal.setStretch(4, 1)
        self.Layout_horizontal.setStretch(5, 1)

        self.verticalLayout_2.addLayout(self.Layout_horizontal)


        self.verticalLayout.addWidget(self.Card_body)


        self.horizontalLayout_2.addWidget(self.Panel_container)


        self.retranslateUi(Frm_Galeria)

        self.cmb_categoria.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Frm_Galeria)
    # setupUi

    def retranslateUi(self, Frm_Galeria):
        Frm_Galeria.setWindowTitle(QCoreApplication.translate("Frm_Galeria", u"Form", None))
        self.Panel_container.setProperty(u"cssClass", QCoreApplication.translate("Frm_Galeria", u"Background", None))
#if QT_CONFIG(tooltip)
        self.Panel_Head.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.Panel_Head.setProperty(u"cssClass", QCoreApplication.translate("Frm_Galeria", u"Surface", None))
        self.lb_titulo.setText(QCoreApplication.translate("Frm_Galeria", u"Dashboard", None))
        self.lb_titulo.setProperty(u"cssClass", QCoreApplication.translate("Frm_Galeria", u"Tittle", None))
        self.lb_descripcion.setText(QCoreApplication.translate("Frm_Galeria", u"Resumen General", None))
        self.lb_descripcion.setProperty(u"cssClass", QCoreApplication.translate("Frm_Galeria", u"Description", None))
        self.Card_body.setProperty(u"cssClass", QCoreApplication.translate("Frm_Galeria", u"Card", None))
        self.lineEdit_buscar.setText("")
        self.lineEdit_buscar.setPlaceholderText(QCoreApplication.translate("Frm_Galeria", u"Buscar ... ", None))
        self.label.setText(QCoreApplication.translate("Frm_Galeria", u"Nombre ", None))
        self.label.setProperty(u"cssClass", QCoreApplication.translate("Frm_Galeria", u"Mediana", None))
        self.cmb_categoria.setItemText(0, QCoreApplication.translate("Frm_Galeria", u"Todas", None))
        self.cmb_categoria.setItemText(1, QCoreApplication.translate("Frm_Galeria", u"Original", None))
        self.cmb_categoria.setItemText(2, QCoreApplication.translate("Frm_Galeria", u"Procesada", None))

        self.cmb_categoria.setPlaceholderText("")
        self.label_2.setText(QCoreApplication.translate("Frm_Galeria", u"Categor\u00eda", None))
        self.label_2.setProperty(u"cssClass", QCoreApplication.translate("Frm_Galeria", u"Mediana", None))
        self.listWidget_imagenes.setProperty(u"cssClass", QCoreApplication.translate("Frm_Galeria", u"List_galeria", None))
        self.btn_abrir.setText(QCoreApplication.translate("Frm_Galeria", u"Seleccionar", None))
        self.btn_abrir.setProperty(u"cssClass", QCoreApplication.translate("Frm_Galeria", u"AquaButton", None))
        self.btn_eliminar.setText(QCoreApplication.translate("Frm_Galeria", u"Eliminar", None))
        self.btn_eliminar.setProperty(u"cssClass", QCoreApplication.translate("Frm_Galeria", u"RedButton", None))
        self.btn_guardar.setText(QCoreApplication.translate("Frm_Galeria", u"Guardar", None))
        self.btn_guardar.setProperty(u"cssClass", QCoreApplication.translate("Frm_Galeria", u"YellowButton", None))
        self.btn_modificar.setText(QCoreApplication.translate("Frm_Galeria", u"Modificar", None))
        self.btn_modificar.setProperty(u"cssClass", QCoreApplication.translate("Frm_Galeria", u"BlueButton", None))
        self.btn_agregar.setText(QCoreApplication.translate("Frm_Galeria", u"Agregar", None))
        self.btn_agregar.setProperty(u"cssClass", QCoreApplication.translate("Frm_Galeria", u"GreenButton", None))
    # retranslateUi

