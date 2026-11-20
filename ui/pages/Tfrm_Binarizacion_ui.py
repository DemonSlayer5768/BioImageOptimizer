# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Tfrm_Binarizacion.ui'
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
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QCheckBox, QComboBox,
    QDoubleSpinBox, QFrame, QGridLayout, QGroupBox,
    QHBoxLayout, QLabel, QPushButton, QSizePolicy,
    QSlider, QSpacerItem, QSpinBox, QVBoxLayout,
    QWidget)

class Ui_Frm_Binarizacion(object):
    def setupUi(self, Frm_Binarizacion):
        if not Frm_Binarizacion.objectName():
            Frm_Binarizacion.setObjectName(u"Frm_Binarizacion")
        Frm_Binarizacion.resize(800, 640)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Frm_Binarizacion.sizePolicy().hasHeightForWidth())
        Frm_Binarizacion.setSizePolicy(sizePolicy)
        Frm_Binarizacion.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.verticalLayout = QVBoxLayout(Frm_Binarizacion)
        self.verticalLayout.setSpacing(1)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.Panel_container = QFrame(Frm_Binarizacion)
        self.Panel_container.setObjectName(u"Panel_container")
        self.Panel_container.setStyleSheet(u"")
        self.Panel_container.setFrameShape(QFrame.Shape.StyledPanel)
        self.Panel_container.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.Panel_container)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
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


        self.verticalLayout_5.addWidget(self.Panel_Head)

        self.Panel_body = QFrame(self.Panel_container)
        self.Panel_body.setObjectName(u"Panel_body")
        self.Panel_body.setMinimumSize(QSize(0, 0))
        self.Panel_body.setStyleSheet(u"")
        self.Panel_body.setFrameShape(QFrame.Shape.StyledPanel)
        self.Panel_body.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.Panel_body)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.Layout_horizontal = QHBoxLayout()
        self.Layout_horizontal.setObjectName(u"Layout_horizontal")
        self.panel_imagen = QFrame(self.Panel_body)
        self.panel_imagen.setObjectName(u"panel_imagen")
        self.panel_imagen.setStyleSheet(u"")
        self.panel_imagen.setFrameShape(QFrame.Shape.StyledPanel)
        self.panel_imagen.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.panel_imagen)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.grp_original = QGroupBox(self.panel_imagen)
        self.grp_original.setObjectName(u"grp_original")
        self.horizontalLayout_3 = QHBoxLayout(self.grp_original)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, 25, -1, -1)
        self.lb_img_orignal = QLabel(self.grp_original)
        self.lb_img_orignal.setObjectName(u"lb_img_orignal")
        self.lb_img_orignal.setScaledContents(True)

        self.horizontalLayout_3.addWidget(self.lb_img_orignal)


        self.verticalLayout_4.addWidget(self.grp_original)

        self.grp_bin = QGroupBox(self.panel_imagen)
        self.grp_bin.setObjectName(u"grp_bin")
        self.horizontalLayout_4 = QHBoxLayout(self.grp_bin)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(-1, 25, -1, -1)
        self.lb_img_bin = QLabel(self.grp_bin)
        self.lb_img_bin.setObjectName(u"lb_img_bin")
        self.lb_img_bin.setScaledContents(True)

        self.horizontalLayout_4.addWidget(self.lb_img_bin)


        self.verticalLayout_4.addWidget(self.grp_bin)


        self.Layout_horizontal.addWidget(self.panel_imagen)

        self.Card_parametros = QFrame(self.Panel_body)
        self.Card_parametros.setObjectName(u"Card_parametros")
        self.Card_parametros.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.Card_parametros.setStyleSheet(u"")
        self.Card_parametros.setFrameShape(QFrame.Shape.StyledPanel)
        self.Card_parametros.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.Card_parametros)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, -1, -1, 9)
        self.lb_pantalla_2 = QLabel(self.Card_parametros)
        self.lb_pantalla_2.setObjectName(u"lb_pantalla_2")
        self.lb_pantalla_2.setStyleSheet(u"")

        self.verticalLayout_2.addWidget(self.lb_pantalla_2)

        self.Line_2 = QFrame(self.Card_parametros)
        self.Line_2.setObjectName(u"Line_2")
        self.Line_2.setMaximumSize(QSize(16777215, 1))
        self.Line_2.setStyleSheet(u"background-color: rgb(49, 197, 175);")
        self.Line_2.setFrameShape(QFrame.Shape.HLine)
        self.Line_2.setFrameShadow(QFrame.Shadow.Plain)

        self.verticalLayout_2.addWidget(self.Line_2)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setVerticalSpacing(9)
        self.gridLayout_2.setContentsMargins(9, 9, 9, 9)
        self.btn_importar = QPushButton(self.Card_parametros)
        self.btn_importar.setObjectName(u"btn_importar")
        self.btn_importar.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_importar.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btn_importar.setStyleSheet(u"")
        icon = QIcon()
        icon.addFile(u"../../resources/Icons/Icons_verdes/import.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_importar.setIcon(icon)

        self.gridLayout_2.addWidget(self.btn_importar, 0, 0, 1, 1)

        self.btn_eliminar = QPushButton(self.Card_parametros)
        self.btn_eliminar.setObjectName(u"btn_eliminar")
        self.btn_eliminar.setEnabled(True)
        self.btn_eliminar.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_eliminar.setStyleSheet(u"")
        icon1 = QIcon()
        icon1.addFile(u"../../resources/Icons/Icons_rojos/delete.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_eliminar.setIcon(icon1)

        self.gridLayout_2.addWidget(self.btn_eliminar, 0, 1, 1, 1)

        self.chk_ver_original = QCheckBox(self.Card_parametros)
        self.chk_ver_original.setObjectName(u"chk_ver_original")
        self.chk_ver_original.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.chk_ver_original.setStyleSheet(u"")
        self.chk_ver_original.setChecked(True)

        self.gridLayout_2.addWidget(self.chk_ver_original, 1, 0, 1, 1)

        self.chk_preview = QCheckBox(self.Card_parametros)
        self.chk_preview.setObjectName(u"chk_preview")
        self.chk_preview.setEnabled(True)
        self.chk_preview.setMinimumSize(QSize(0, 28))
        self.chk_preview.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.chk_preview.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.chk_preview.setStyleSheet(u"")
        self.chk_preview.setChecked(True)

        self.gridLayout_2.addWidget(self.chk_preview, 1, 1, 1, 1)


        self.verticalLayout_2.addLayout(self.gridLayout_2)

        self.gb_parametros = QGroupBox(self.Card_parametros)
        self.gb_parametros.setObjectName(u"gb_parametros")
        self.gb_parametros.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.gb_parametros.setStyleSheet(u"")
        self.gridLayout = QGridLayout(self.gb_parametros)
        self.gridLayout.setSpacing(9)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 9, 0, 9)
        self.label_2 = QLabel(self.gb_parametros)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 6, 0, 1, 1)

        self.lb_parametros = QLabel(self.gb_parametros)
        self.lb_parametros.setObjectName(u"lb_parametros")

        self.gridLayout.addWidget(self.lb_parametros, 2, 0, 1, 2)

        self.label_3 = QLabel(self.gb_parametros)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 6, 2, 1, 1)

        self.spin_umbral = QSpinBox(self.gb_parametros)
        self.spin_umbral.setObjectName(u"spin_umbral")
        self.spin_umbral.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.spin_umbral.setStyleSheet(u"")
        self.spin_umbral.setReadOnly(False)
        self.spin_umbral.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.UpDownArrows)
        self.spin_umbral.setMaximum(255)
        self.spin_umbral.setValue(127)

        self.gridLayout.addWidget(self.spin_umbral, 3, 2, 1, 1)

        self.spin_tamano_bloque = QSpinBox(self.gb_parametros)
        self.spin_tamano_bloque.setObjectName(u"spin_tamano_bloque")
        self.spin_tamano_bloque.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.spin_tamano_bloque.setStyleSheet(u"")
        self.spin_tamano_bloque.setReadOnly(False)
        self.spin_tamano_bloque.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.UpDownArrows)
        self.spin_tamano_bloque.setMinimum(3)
        self.spin_tamano_bloque.setMaximum(255)
        self.spin_tamano_bloque.setValue(11)

        self.gridLayout.addWidget(self.spin_tamano_bloque, 7, 0, 1, 1)

        self.cmb_metodo = QComboBox(self.gb_parametros)
        self.cmb_metodo.addItem("")
        self.cmb_metodo.addItem("")
        self.cmb_metodo.addItem("")
        self.cmb_metodo.addItem("")
        self.cmb_metodo.addItem("")
        self.cmb_metodo.setObjectName(u"cmb_metodo")
        self.cmb_metodo.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.cmb_metodo.setStyleSheet(u"")

        self.gridLayout.addWidget(self.cmb_metodo, 1, 0, 1, 3)

        self.doubleSpinBox = QDoubleSpinBox(self.gb_parametros)
        self.doubleSpinBox.setObjectName(u"doubleSpinBox")
        self.doubleSpinBox.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.UpDownArrows)

        self.gridLayout.addWidget(self.doubleSpinBox, 7, 2, 1, 1)

        self.verticalLayout_opciones = QVBoxLayout()
        self.verticalLayout_opciones.setSpacing(5)
        self.verticalLayout_opciones.setObjectName(u"verticalLayout_opciones")
        self.verticalLayout_opciones.setContentsMargins(4, 6, 4, 6)
        self.chk_invertir = QCheckBox(self.gb_parametros)
        self.chk_invertir.setObjectName(u"chk_invertir")
        self.chk_invertir.setEnabled(True)
        self.chk_invertir.setMinimumSize(QSize(0, 28))
        self.chk_invertir.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.chk_invertir.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.chk_invertir.setStyleSheet(u"")
        self.chk_invertir.setChecked(False)

        self.verticalLayout_opciones.addWidget(self.chk_invertir)

        self.chk_mascara = QCheckBox(self.gb_parametros)
        self.chk_mascara.setObjectName(u"chk_mascara")
        self.chk_mascara.setEnabled(False)
        self.chk_mascara.setMinimumSize(QSize(0, 28))
        self.chk_mascara.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.chk_mascara.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.chk_mascara.setStyleSheet(u"")
        self.chk_mascara.setCheckable(False)
        self.chk_mascara.setChecked(False)

        self.verticalLayout_opciones.addWidget(self.chk_mascara)


        self.gridLayout.addLayout(self.verticalLayout_opciones, 8, 0, 1, 3)

        self.label = QLabel(self.gb_parametros)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 3)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 9, 0, 1, 1)

        self.slider_umbral = QSlider(self.gb_parametros)
        self.slider_umbral.setObjectName(u"slider_umbral")
        self.slider_umbral.setCursor(QCursor(Qt.CursorShape.ClosedHandCursor))
        self.slider_umbral.setStyleSheet(u"")
        self.slider_umbral.setMaximum(255)
        self.slider_umbral.setSliderPosition(127)
        self.slider_umbral.setOrientation(Qt.Orientation.Horizontal)

        self.gridLayout.addWidget(self.slider_umbral, 3, 0, 1, 1)


        self.verticalLayout_2.addWidget(self.gb_parametros)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, 9, -1, 9)
        self.btn_reset = QPushButton(self.Card_parametros)
        self.btn_reset.setObjectName(u"btn_reset")
        self.btn_reset.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_reset.setStyleSheet(u"")
        icon2 = QIcon()
        icon2.addFile(u"../../resources/Icons/Icons_aqua/reset.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_reset.setIcon(icon2)

        self.horizontalLayout_2.addWidget(self.btn_reset)

        self.btn_guardar = QPushButton(self.Card_parametros)
        self.btn_guardar.setObjectName(u"btn_guardar")
        self.btn_guardar.setEnabled(True)
        self.btn_guardar.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_guardar.setStyleSheet(u"")
        icon3 = QIcon()
        icon3.addFile(u"../../resources/Icons/Icons_amarillos/saved.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_guardar.setIcon(icon3)

        self.horizontalLayout_2.addWidget(self.btn_guardar)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.verticalLayout_2.setStretch(2, 1)
        self.verticalLayout_2.setStretch(3, 9)

        self.Layout_horizontal.addWidget(self.Card_parametros)

        self.Layout_horizontal.setStretch(0, 9)
        self.Layout_horizontal.setStretch(1, 1)

        self.verticalLayout_3.addLayout(self.Layout_horizontal)


        self.verticalLayout_5.addWidget(self.Panel_body)


        self.verticalLayout.addWidget(self.Panel_container)


        self.retranslateUi(Frm_Binarizacion)

        QMetaObject.connectSlotsByName(Frm_Binarizacion)
    # setupUi

    def retranslateUi(self, Frm_Binarizacion):
        Frm_Binarizacion.setWindowTitle(QCoreApplication.translate("Frm_Binarizacion", u"Form", None))
        self.Panel_container.setProperty(u"cssClass", QCoreApplication.translate("Frm_Binarizacion", u"Background", None))
#if QT_CONFIG(tooltip)
        self.Panel_Head.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.Panel_Head.setProperty(u"cssClass", QCoreApplication.translate("Frm_Binarizacion", u"Surface", None))
        self.lb_titulo.setText(QCoreApplication.translate("Frm_Binarizacion", u"Binarizaci\u00f3n", None))
        self.lb_titulo.setProperty(u"cssClass", QCoreApplication.translate("Frm_Binarizacion", u"Tittle", None))
        self.lb_descripcion.setText(QCoreApplication.translate("Frm_Binarizacion", u"Binarizaci\u00f3n de imagenes", None))
        self.lb_descripcion.setProperty(u"cssClass", QCoreApplication.translate("Frm_Binarizacion", u"Description", None))
        self.Panel_body.setProperty(u"cssClass", QCoreApplication.translate("Frm_Binarizacion", u"Surface", None))
        self.panel_imagen.setProperty(u"cssClass", QCoreApplication.translate("Frm_Binarizacion", u"Card", None))
        self.grp_original.setTitle(QCoreApplication.translate("Frm_Binarizacion", u"Original", None))
        self.lb_img_orignal.setText("")
        self.grp_bin.setTitle(QCoreApplication.translate("Frm_Binarizacion", u"Result", None))
        self.lb_img_bin.setText("")
        self.Card_parametros.setProperty(u"cssClass", QCoreApplication.translate("Frm_Binarizacion", u"Card", None))
        self.lb_pantalla_2.setText(QCoreApplication.translate("Frm_Binarizacion", u"Binarizaci\u00f3n", None))
        self.lb_pantalla_2.setProperty(u"cssClass", QCoreApplication.translate("Frm_Binarizacion", u"Mediana", None))
        self.btn_importar.setText(QCoreApplication.translate("Frm_Binarizacion", u"Importar", None))
        self.btn_importar.setProperty(u"cssClass", QCoreApplication.translate("Frm_Binarizacion", u"GreenButton", None))
        self.btn_eliminar.setText(QCoreApplication.translate("Frm_Binarizacion", u"Quitar imagen", None))
        self.btn_eliminar.setProperty(u"cssClass", QCoreApplication.translate("Frm_Binarizacion", u"RedButton", None))
        self.chk_ver_original.setText(QCoreApplication.translate("Frm_Binarizacion", u"Ver original", None))
        self.chk_preview.setText(QCoreApplication.translate("Frm_Binarizacion", u"Preview", None))
        self.gb_parametros.setTitle(QCoreApplication.translate("Frm_Binarizacion", u"Par\u00e1metros adaptativos", None))
        self.label_2.setText(QCoreApplication.translate("Frm_Binarizacion", u"Tama\u00f1o de bloque", None))
        self.label_2.setProperty(u"cssClass", QCoreApplication.translate("Frm_Binarizacion", u"Pequena", None))
        self.lb_parametros.setText(QCoreApplication.translate("Frm_Binarizacion", u"Umbral (Threshold)", None))
        self.lb_parametros.setProperty(u"cssClass", QCoreApplication.translate("Frm_Binarizacion", u"Pequena", None))
        self.label_3.setText(QCoreApplication.translate("Frm_Binarizacion", u"Constante C", None))
        self.label_3.setProperty(u"cssClass", QCoreApplication.translate("Frm_Binarizacion", u"Pequena", None))
        self.cmb_metodo.setItemText(0, QCoreApplication.translate("Frm_Binarizacion", u"Otsu", None))
        self.cmb_metodo.setItemText(1, QCoreApplication.translate("Frm_Binarizacion", u"Fixed", None))
        self.cmb_metodo.setItemText(2, QCoreApplication.translate("Frm_Binarizacion", u"Adaptive Mean", None))
        self.cmb_metodo.setItemText(3, QCoreApplication.translate("Frm_Binarizacion", u"Adaptive Gaussian", None))
        self.cmb_metodo.setItemText(4, QCoreApplication.translate("Frm_Binarizacion", u"Triangle", None))

        self.chk_invertir.setText(QCoreApplication.translate("Frm_Binarizacion", u"Invertir resultado", None))
        self.chk_mascara.setText(QCoreApplication.translate("Frm_Binarizacion", u"Usar m\u00e1scara previa ", None))
        self.label.setText(QCoreApplication.translate("Frm_Binarizacion", u"Metodo de Binarizaci\u00f3n", None))
        self.label.setProperty(u"cssClass", QCoreApplication.translate("Frm_Binarizacion", u"Pequena", None))
        self.btn_reset.setText(QCoreApplication.translate("Frm_Binarizacion", u"Reiniciar", None))
        self.btn_reset.setProperty(u"cssClass", QCoreApplication.translate("Frm_Binarizacion", u"AquaButton", None))
        self.btn_guardar.setText(QCoreApplication.translate("Frm_Binarizacion", u"Guardar", None))
        self.btn_guardar.setProperty(u"cssClass", QCoreApplication.translate("Frm_Binarizacion", u"YellowButton", None))
    # retranslateUi

