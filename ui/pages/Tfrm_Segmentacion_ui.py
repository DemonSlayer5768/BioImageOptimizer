# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Tfrm_Segmentacion.ui'
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
    QHBoxLayout, QLabel, QPushButton, QRadioButton,
    QSizePolicy, QSlider, QSpacerItem, QSpinBox,
    QVBoxLayout, QWidget)

class Ui_Frm_Segmentacion(object):
    def setupUi(self, Frm_Segmentacion):
        if not Frm_Segmentacion.objectName():
            Frm_Segmentacion.setObjectName(u"Frm_Segmentacion")
        Frm_Segmentacion.resize(949, 820)
        Frm_Segmentacion.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.verticalLayout = QVBoxLayout(Frm_Segmentacion)
        self.verticalLayout.setSpacing(1)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.Panel_container = QFrame(Frm_Segmentacion)
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
        self.Panel_body.setMinimumSize(QSize(0, 710))
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
        self.verticalLayout_7 = QVBoxLayout(self.Card_parametros)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.lb_pantalla_2 = QLabel(self.Card_parametros)
        self.lb_pantalla_2.setObjectName(u"lb_pantalla_2")
        self.lb_pantalla_2.setStyleSheet(u"")

        self.verticalLayout_7.addWidget(self.lb_pantalla_2)

        self.Line_2 = QFrame(self.Card_parametros)
        self.Line_2.setObjectName(u"Line_2")
        self.Line_2.setMaximumSize(QSize(16777215, 1))
        self.Line_2.setStyleSheet(u"background-color: rgb(49, 197, 175);")
        self.Line_2.setFrameShape(QFrame.Shape.NoFrame)
        self.Line_2.setFrameShadow(QFrame.Shadow.Raised)

        self.verticalLayout_7.addWidget(self.Line_2)

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


        self.verticalLayout_7.addLayout(self.gridLayout_2)

        self.gb_parametros = QGroupBox(self.Card_parametros)
        self.gb_parametros.setObjectName(u"gb_parametros")
        self.gb_parametros.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.gb_parametros.setStyleSheet(u"")
        self.verticalLayout_9 = QVBoxLayout(self.gb_parametros)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label = QLabel(self.gb_parametros)
        self.label.setObjectName(u"label")

        self.verticalLayout_9.addWidget(self.label)

        self.cmb_metodo = QComboBox(self.gb_parametros)
        self.cmb_metodo.addItem("")
        self.cmb_metodo.addItem("")
        self.cmb_metodo.addItem("")
        self.cmb_metodo.addItem("")
        self.cmb_metodo.addItem("")
        self.cmb_metodo.addItem("")
        self.cmb_metodo.setObjectName(u"cmb_metodo")
        self.cmb_metodo.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.cmb_metodo.setStyleSheet(u"")

        self.verticalLayout_9.addWidget(self.cmb_metodo)

        self.lb_parametros = QLabel(self.gb_parametros)
        self.lb_parametros.setObjectName(u"lb_parametros")

        self.verticalLayout_9.addWidget(self.lb_parametros)

        self.slider_umbral_min = QSlider(self.gb_parametros)
        self.slider_umbral_min.setObjectName(u"slider_umbral_min")
        self.slider_umbral_min.setCursor(QCursor(Qt.CursorShape.OpenHandCursor))
        self.slider_umbral_min.setStyleSheet(u"")
        self.slider_umbral_min.setMaximum(255)
        self.slider_umbral_min.setSliderPosition(127)
        self.slider_umbral_min.setOrientation(Qt.Orientation.Horizontal)

        self.verticalLayout_9.addWidget(self.slider_umbral_min)

        self.lb_parametros_2 = QLabel(self.gb_parametros)
        self.lb_parametros_2.setObjectName(u"lb_parametros_2")

        self.verticalLayout_9.addWidget(self.lb_parametros_2)

        self.slider_umbral_max = QSlider(self.gb_parametros)
        self.slider_umbral_max.setObjectName(u"slider_umbral_max")
        self.slider_umbral_max.setCursor(QCursor(Qt.CursorShape.OpenHandCursor))
        self.slider_umbral_max.setStyleSheet(u"")
        self.slider_umbral_max.setMaximum(255)
        self.slider_umbral_max.setSliderPosition(127)
        self.slider_umbral_max.setOrientation(Qt.Orientation.Horizontal)

        self.verticalLayout_9.addWidget(self.slider_umbral_max)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_2 = QLabel(self.gb_parametros)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_6.addWidget(self.label_2)

        self.spin_tamano_bloque = QSpinBox(self.gb_parametros)
        self.spin_tamano_bloque.setObjectName(u"spin_tamano_bloque")
        self.spin_tamano_bloque.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.spin_tamano_bloque.setStyleSheet(u"")
        self.spin_tamano_bloque.setReadOnly(False)
        self.spin_tamano_bloque.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.UpDownArrows)
        self.spin_tamano_bloque.setMinimum(3)
        self.spin_tamano_bloque.setMaximum(255)
        self.spin_tamano_bloque.setValue(11)

        self.verticalLayout_6.addWidget(self.spin_tamano_bloque)


        self.horizontalLayout_6.addLayout(self.verticalLayout_6)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_3 = QLabel(self.gb_parametros)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_8.addWidget(self.label_3)

        self.doubleSpinBox = QDoubleSpinBox(self.gb_parametros)
        self.doubleSpinBox.setObjectName(u"doubleSpinBox")
        self.doubleSpinBox.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.UpDownArrows)

        self.verticalLayout_8.addWidget(self.doubleSpinBox)


        self.horizontalLayout_6.addLayout(self.verticalLayout_8)


        self.verticalLayout_9.addLayout(self.horizontalLayout_6)

        self.chk_invertir = QCheckBox(self.gb_parametros)
        self.chk_invertir.setObjectName(u"chk_invertir")
        self.chk_invertir.setEnabled(True)
        self.chk_invertir.setMinimumSize(QSize(0, 28))
        self.chk_invertir.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.chk_invertir.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.chk_invertir.setStyleSheet(u"")
        self.chk_invertir.setChecked(False)

        self.verticalLayout_9.addWidget(self.chk_invertir)

        self.chk_mascara = QCheckBox(self.gb_parametros)
        self.chk_mascara.setObjectName(u"chk_mascara")
        self.chk_mascara.setEnabled(False)
        self.chk_mascara.setMinimumSize(QSize(0, 28))
        self.chk_mascara.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.chk_mascara.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.chk_mascara.setStyleSheet(u"")
        self.chk_mascara.setCheckable(False)
        self.chk_mascara.setChecked(False)

        self.verticalLayout_9.addWidget(self.chk_mascara)


        self.verticalLayout_7.addWidget(self.gb_parametros)

        self.gb_watershed = QGroupBox(self.Card_parametros)
        self.gb_watershed.setObjectName(u"gb_watershed")
        self.verticalLayout_2 = QVBoxLayout(self.gb_watershed)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.lb_parametros_3 = QLabel(self.gb_watershed)
        self.lb_parametros_3.setObjectName(u"lb_parametros_3")

        self.verticalLayout_2.addWidget(self.lb_parametros_3)

        self.slider_distancia_min = QSlider(self.gb_watershed)
        self.slider_distancia_min.setObjectName(u"slider_distancia_min")
        self.slider_distancia_min.setCursor(QCursor(Qt.CursorShape.OpenHandCursor))
        self.slider_distancia_min.setStyleSheet(u"")
        self.slider_distancia_min.setMaximum(255)
        self.slider_distancia_min.setSliderPosition(127)
        self.slider_distancia_min.setOrientation(Qt.Orientation.Horizontal)
        self.slider_distancia_min.setTickPosition(QSlider.TickPosition.NoTicks)

        self.verticalLayout_2.addWidget(self.slider_distancia_min)

        self.lb_parametros_4 = QLabel(self.gb_watershed)
        self.lb_parametros_4.setObjectName(u"lb_parametros_4")

        self.verticalLayout_2.addWidget(self.lb_parametros_4)

        self.slider_distancia_max = QSlider(self.gb_watershed)
        self.slider_distancia_max.setObjectName(u"slider_distancia_max")
        self.slider_distancia_max.setCursor(QCursor(Qt.CursorShape.OpenHandCursor))
        self.slider_distancia_max.setMaximum(255)
        self.slider_distancia_max.setSliderPosition(127)
        self.slider_distancia_max.setOrientation(Qt.Orientation.Horizontal)

        self.verticalLayout_2.addWidget(self.slider_distancia_max)

        self.lb_parametros_5 = QLabel(self.gb_watershed)
        self.lb_parametros_5.setObjectName(u"lb_parametros_5")

        self.verticalLayout_2.addWidget(self.lb_parametros_5)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.rd_btn_vecinos = QRadioButton(self.gb_watershed)
        self.rd_btn_vecinos.setObjectName(u"rd_btn_vecinos")

        self.horizontalLayout_2.addWidget(self.rd_btn_vecinos)

        self.rd_btn_vecinos_2 = QRadioButton(self.gb_watershed)
        self.rd_btn_vecinos_2.setObjectName(u"rd_btn_vecinos_2")
        self.rd_btn_vecinos_2.setChecked(True)

        self.horizontalLayout_2.addWidget(self.rd_btn_vecinos_2)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.lb_parametros_6 = QLabel(self.gb_watershed)
        self.lb_parametros_6.setObjectName(u"lb_parametros_6")

        self.verticalLayout_2.addWidget(self.lb_parametros_6)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.rd_btn_tres = QRadioButton(self.gb_watershed)
        self.rd_btn_tres.setObjectName(u"rd_btn_tres")

        self.horizontalLayout.addWidget(self.rd_btn_tres)

        self.rd_btn_cinco = QRadioButton(self.gb_watershed)
        self.rd_btn_cinco.setObjectName(u"rd_btn_cinco")

        self.horizontalLayout.addWidget(self.rd_btn_cinco)

        self.rd_btn_siete = QRadioButton(self.gb_watershed)
        self.rd_btn_siete.setObjectName(u"rd_btn_siete")

        self.horizontalLayout.addWidget(self.rd_btn_siete)


        self.verticalLayout_2.addLayout(self.horizontalLayout)


        self.verticalLayout_7.addWidget(self.gb_watershed)

        self.gb_kmeans = QGroupBox(self.Card_parametros)
        self.gb_kmeans.setObjectName(u"gb_kmeans")
        self.layout_kmeans = QVBoxLayout(self.gb_kmeans)
        self.layout_kmeans.setObjectName(u"layout_kmeans")
        self.label_numero_clusters = QLabel(self.gb_kmeans)
        self.label_numero_clusters.setObjectName(u"label_numero_clusters")

        self.layout_kmeans.addWidget(self.label_numero_clusters)

        self.spin_numero_clusters = QSpinBox(self.gb_kmeans)
        self.spin_numero_clusters.setObjectName(u"spin_numero_clusters")
        self.spin_numero_clusters.setMinimum(2)
        self.spin_numero_clusters.setMaximum(12)
        self.spin_numero_clusters.setValue(3)

        self.layout_kmeans.addWidget(self.spin_numero_clusters)


        self.verticalLayout_7.addWidget(self.gb_kmeans)

        self.gb_region_growing = QGroupBox(self.Card_parametros)
        self.gb_region_growing.setObjectName(u"gb_region_growing")
        self.layout_region_growing = QVBoxLayout(self.gb_region_growing)
        self.layout_region_growing.setObjectName(u"layout_region_growing")
        self.lbl_semilla = QLabel(self.gb_region_growing)
        self.lbl_semilla.setObjectName(u"lbl_semilla")

        self.layout_region_growing.addWidget(self.lbl_semilla)

        self.btn_elegir_semilla = QPushButton(self.gb_region_growing)
        self.btn_elegir_semilla.setObjectName(u"btn_elegir_semilla")
        self.btn_elegir_semilla.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.layout_region_growing.addWidget(self.btn_elegir_semilla)

        self.label_conectividad_region = QLabel(self.gb_region_growing)
        self.label_conectividad_region.setObjectName(u"label_conectividad_region")

        self.layout_region_growing.addWidget(self.label_conectividad_region)

        self.layout_conectividad_region = QHBoxLayout()
        self.layout_conectividad_region.setObjectName(u"layout_conectividad_region")
        self.rd_btn_region_vecinos = QRadioButton(self.gb_region_growing)
        self.rd_btn_region_vecinos.setObjectName(u"rd_btn_region_vecinos")

        self.layout_conectividad_region.addWidget(self.rd_btn_region_vecinos)

        self.rd_btn_region_vecinos_2 = QRadioButton(self.gb_region_growing)
        self.rd_btn_region_vecinos_2.setObjectName(u"rd_btn_region_vecinos_2")
        self.rd_btn_region_vecinos_2.setChecked(True)

        self.layout_conectividad_region.addWidget(self.rd_btn_region_vecinos_2)


        self.layout_region_growing.addLayout(self.layout_conectividad_region)

        self.label_tolerancia_region = QLabel(self.gb_region_growing)
        self.label_tolerancia_region.setObjectName(u"label_tolerancia_region")

        self.layout_region_growing.addWidget(self.label_tolerancia_region)

        self.slider_tolerancia_region = QSlider(self.gb_region_growing)
        self.slider_tolerancia_region.setObjectName(u"slider_tolerancia_region")
        self.slider_tolerancia_region.setCursor(QCursor(Qt.CursorShape.OpenHandCursor))
        self.slider_tolerancia_region.setMaximum(255)
        self.slider_tolerancia_region.setValue(20)
        self.slider_tolerancia_region.setOrientation(Qt.Orientation.Horizontal)

        self.layout_region_growing.addWidget(self.slider_tolerancia_region)


        self.verticalLayout_7.addWidget(self.gb_region_growing)

        self.gb_slic = QGroupBox(self.Card_parametros)
        self.gb_slic.setObjectName(u"gb_slic")
        self.layout_slic = QVBoxLayout(self.gb_slic)
        self.layout_slic.setObjectName(u"layout_slic")
        self.label_numero_superpixeles = QLabel(self.gb_slic)
        self.label_numero_superpixeles.setObjectName(u"label_numero_superpixeles")

        self.layout_slic.addWidget(self.label_numero_superpixeles)

        self.spin_numero_superpixeles = QSpinBox(self.gb_slic)
        self.spin_numero_superpixeles.setObjectName(u"spin_numero_superpixeles")
        self.spin_numero_superpixeles.setMinimum(10)
        self.spin_numero_superpixeles.setMaximum(5000)
        self.spin_numero_superpixeles.setValue(200)

        self.layout_slic.addWidget(self.spin_numero_superpixeles)

        self.label_compactness = QLabel(self.gb_slic)
        self.label_compactness.setObjectName(u"label_compactness")

        self.layout_slic.addWidget(self.label_compactness)

        self.slider_compactness = QSlider(self.gb_slic)
        self.slider_compactness.setObjectName(u"slider_compactness")
        self.slider_compactness.setCursor(QCursor(Qt.CursorShape.OpenHandCursor))
        self.slider_compactness.setMinimum(1)
        self.slider_compactness.setMaximum(300)
        self.slider_compactness.setValue(100)
        self.slider_compactness.setOrientation(Qt.Orientation.Horizontal)

        self.layout_slic.addWidget(self.slider_compactness)


        self.verticalLayout_7.addWidget(self.gb_slic)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer)

        self.Layout_horizontal_2 = QHBoxLayout()
        self.Layout_horizontal_2.setObjectName(u"Layout_horizontal_2")
        self.Layout_horizontal_2.setContentsMargins(-1, 9, -1, 9)
        self.btn_reset = QPushButton(self.Card_parametros)
        self.btn_reset.setObjectName(u"btn_reset")
        self.btn_reset.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_reset.setStyleSheet(u"")
        icon2 = QIcon()
        icon2.addFile(u"../../resources/Icons/Icons_aqua/reset.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_reset.setIcon(icon2)

        self.Layout_horizontal_2.addWidget(self.btn_reset)

        self.btn_guardar = QPushButton(self.Card_parametros)
        self.btn_guardar.setObjectName(u"btn_guardar")
        self.btn_guardar.setEnabled(True)
        self.btn_guardar.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_guardar.setStyleSheet(u"")
        icon3 = QIcon()
        icon3.addFile(u"../../resources/Icons/Icons_amarillos/saved.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_guardar.setIcon(icon3)

        self.Layout_horizontal_2.addWidget(self.btn_guardar)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.Layout_horizontal_2.addItem(self.horizontalSpacer)

        self.btn_ejecutar = QPushButton(self.Card_parametros)
        self.btn_ejecutar.setObjectName(u"btn_ejecutar")
        self.btn_ejecutar.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_ejecutar.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        icon4 = QIcon()
        icon4.addFile(u"../../resources/Icons/Icons_aqua/play-button-arrowhead.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_ejecutar.setIcon(icon4)

        self.Layout_horizontal_2.addWidget(self.btn_ejecutar)


        self.verticalLayout_7.addLayout(self.Layout_horizontal_2)

        self.verticalLayout_7.setStretch(2, 2)
        self.verticalLayout_7.setStretch(4, 2)
        self.verticalLayout_7.setStretch(9, 1)

        self.Layout_horizontal.addWidget(self.Card_parametros)

        self.Layout_horizontal.setStretch(0, 9)
        self.Layout_horizontal.setStretch(1, 1)

        self.verticalLayout_3.addLayout(self.Layout_horizontal)


        self.verticalLayout_5.addWidget(self.Panel_body)


        self.verticalLayout.addWidget(self.Panel_container)


        self.retranslateUi(Frm_Segmentacion)

        QMetaObject.connectSlotsByName(Frm_Segmentacion)
    # setupUi

    def retranslateUi(self, Frm_Segmentacion):
        Frm_Segmentacion.setWindowTitle(QCoreApplication.translate("Frm_Segmentacion", u"Form", None))
        self.Panel_container.setProperty(u"cssClass", QCoreApplication.translate("Frm_Segmentacion", u"Background", None))
#if QT_CONFIG(tooltip)
        self.Panel_Head.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.Panel_Head.setProperty(u"cssClass", QCoreApplication.translate("Frm_Segmentacion", u"Surface", None))
        self.lb_titulo.setText(QCoreApplication.translate("Frm_Segmentacion", u"Segmentaci\u00f3n ", None))
        self.lb_titulo.setProperty(u"cssClass", QCoreApplication.translate("Frm_Segmentacion", u"Tittle", None))
        self.lb_descripcion.setText(QCoreApplication.translate("Frm_Segmentacion", u"Segmentaci\u00f3n de imagenes", None))
        self.lb_descripcion.setProperty(u"cssClass", QCoreApplication.translate("Frm_Segmentacion", u"Description", None))
        self.Panel_body.setProperty(u"cssClass", QCoreApplication.translate("Frm_Segmentacion", u"Surface", None))
        self.panel_imagen.setProperty(u"cssClass", QCoreApplication.translate("Frm_Segmentacion", u"Card", None))
        self.grp_original.setTitle(QCoreApplication.translate("Frm_Segmentacion", u"Original", None))
        self.lb_img_orignal.setText("")
        self.grp_bin.setTitle(QCoreApplication.translate("Frm_Segmentacion", u"Result", None))
        self.lb_img_bin.setText("")
        self.Card_parametros.setProperty(u"cssClass", QCoreApplication.translate("Frm_Segmentacion", u"Card", None))
        self.lb_pantalla_2.setText(QCoreApplication.translate("Frm_Segmentacion", u"Segmentaci\u00f3n", None))
        self.lb_pantalla_2.setProperty(u"cssClass", QCoreApplication.translate("Frm_Segmentacion", u"Mediana", None))
        self.btn_importar.setText(QCoreApplication.translate("Frm_Segmentacion", u"Importar", None))
        self.btn_importar.setProperty(u"cssClass", QCoreApplication.translate("Frm_Segmentacion", u"GreenButton", None))
        self.btn_eliminar.setText(QCoreApplication.translate("Frm_Segmentacion", u"Quitar imagen", None))
        self.btn_eliminar.setProperty(u"cssClass", QCoreApplication.translate("Frm_Segmentacion", u"RedButton", None))
        self.chk_ver_original.setText(QCoreApplication.translate("Frm_Segmentacion", u"Ver original", None))
        self.chk_preview.setText(QCoreApplication.translate("Frm_Segmentacion", u"Preview", None))
        self.gb_parametros.setTitle(QCoreApplication.translate("Frm_Segmentacion", u"Par\u00e1metros", None))
        self.label.setText(QCoreApplication.translate("Frm_Segmentacion", u"M\u00e9todo de segmentaci\u00f3n", None))
        self.label.setProperty(u"cssClass", QCoreApplication.translate("Frm_Segmentacion", u"Pequena", None))
        self.cmb_metodo.setItemText(0, QCoreApplication.translate("Frm_Segmentacion", u"Umbralizacion", None))
        self.cmb_metodo.setItemText(1, QCoreApplication.translate("Frm_Segmentacion", u"Umbralizaci\u00f3n adaptativa", None))
        self.cmb_metodo.setItemText(2, QCoreApplication.translate("Frm_Segmentacion", u"Watershed", None))
        self.cmb_metodo.setItemText(3, QCoreApplication.translate("Frm_Segmentacion", u"K-means", None))
        self.cmb_metodo.setItemText(4, QCoreApplication.translate("Frm_Segmentacion", u"Region Growing", None))
        self.cmb_metodo.setItemText(5, QCoreApplication.translate("Frm_Segmentacion", u"SLIC (Superpixeles)", None))

        self.lb_parametros.setText(QCoreApplication.translate("Frm_Segmentacion", u"Umbral m\u00ednimo", None))
        self.lb_parametros.setProperty(u"cssClass", QCoreApplication.translate("Frm_Segmentacion", u"Pequena", None))
        self.lb_parametros_2.setText(QCoreApplication.translate("Frm_Segmentacion", u"Umbral m\u00e1ximo", None))
        self.lb_parametros_2.setProperty(u"cssClass", QCoreApplication.translate("Frm_Segmentacion", u"Pequena", None))
        self.label_2.setText(QCoreApplication.translate("Frm_Segmentacion", u"Tama\u00f1o de bloque", None))
        self.label_2.setProperty(u"cssClass", QCoreApplication.translate("Frm_Segmentacion", u"Pequena", None))
        self.label_3.setText(QCoreApplication.translate("Frm_Segmentacion", u"Constante C", None))
        self.label_3.setProperty(u"cssClass", QCoreApplication.translate("Frm_Segmentacion", u"Pequena", None))
        self.chk_invertir.setText(QCoreApplication.translate("Frm_Segmentacion", u"Invertir resultado", None))
        self.chk_mascara.setText(QCoreApplication.translate("Frm_Segmentacion", u"Usar m\u00e1scara previa ", None))
        self.gb_watershed.setTitle(QCoreApplication.translate("Frm_Segmentacion", u"Watershed", None))
        self.lb_parametros_3.setText(QCoreApplication.translate("Frm_Segmentacion", u"Distancia m\u00ednima", None))
        self.lb_parametros_3.setProperty(u"cssClass", QCoreApplication.translate("Frm_Segmentacion", u"Pequena", None))
        self.lb_parametros_4.setText(QCoreApplication.translate("Frm_Segmentacion", u"Distancia m\u00e1xima", None))
        self.lb_parametros_4.setProperty(u"cssClass", QCoreApplication.translate("Frm_Segmentacion", u"Pequena", None))
        self.lb_parametros_5.setText(QCoreApplication.translate("Frm_Segmentacion", u"Conectividad", None))
        self.lb_parametros_5.setProperty(u"cssClass", QCoreApplication.translate("Frm_Segmentacion", u"Pequena", None))
        self.rd_btn_vecinos.setText(QCoreApplication.translate("Frm_Segmentacion", u"4 vecinos", None))
        self.rd_btn_vecinos_2.setText(QCoreApplication.translate("Frm_Segmentacion", u"8 vecinos", None))
        self.lb_parametros_6.setText(QCoreApplication.translate("Frm_Segmentacion", u"Kernel de suavizado", None))
        self.lb_parametros_6.setProperty(u"cssClass", QCoreApplication.translate("Frm_Segmentacion", u"Pequena", None))
        self.rd_btn_tres.setText(QCoreApplication.translate("Frm_Segmentacion", u"3 x 3", None))
        self.rd_btn_tres.setProperty(u"cssClass", QCoreApplication.translate("Frm_Segmentacion", u"Badge_RadioButton", None))
        self.rd_btn_cinco.setText(QCoreApplication.translate("Frm_Segmentacion", u"5 x 5", None))
        self.rd_btn_cinco.setProperty(u"cssClass", QCoreApplication.translate("Frm_Segmentacion", u"Badge_RadioButton", None))
        self.rd_btn_siete.setText(QCoreApplication.translate("Frm_Segmentacion", u"7 x 7", None))
        self.rd_btn_siete.setProperty(u"cssClass", QCoreApplication.translate("Frm_Segmentacion", u"Badge_RadioButton", None))
        self.gb_kmeans.setTitle(QCoreApplication.translate("Frm_Segmentacion", u"K-means", None))
        self.label_numero_clusters.setText(QCoreApplication.translate("Frm_Segmentacion", u"N\u00famero de clusters", None))
        self.gb_region_growing.setTitle(QCoreApplication.translate("Frm_Segmentacion", u"Region Growing", None))
        self.lbl_semilla.setText(QCoreApplication.translate("Frm_Segmentacion", u"Sin seleccionar", None))
        self.btn_elegir_semilla.setText(QCoreApplication.translate("Frm_Segmentacion", u"Elegir semilla", None))
        self.label_conectividad_region.setText(QCoreApplication.translate("Frm_Segmentacion", u"Conectividad", None))
        self.rd_btn_region_vecinos.setText(QCoreApplication.translate("Frm_Segmentacion", u"4 vecinos", None))
        self.rd_btn_region_vecinos_2.setText(QCoreApplication.translate("Frm_Segmentacion", u"8 vecinos", None))
        self.label_tolerancia_region.setText(QCoreApplication.translate("Frm_Segmentacion", u"Tolerancia de intensidad", None))
        self.gb_slic.setTitle(QCoreApplication.translate("Frm_Segmentacion", u"SLIC (Superpixeles)", None))
        self.label_numero_superpixeles.setText(QCoreApplication.translate("Frm_Segmentacion", u"N\u00famero de superp\u00edxeles", None))
        self.label_compactness.setText(QCoreApplication.translate("Frm_Segmentacion", u"Compactness (x10)", None))
        self.btn_reset.setText(QCoreApplication.translate("Frm_Segmentacion", u"Reiniciar", None))
        self.btn_reset.setProperty(u"cssClass", QCoreApplication.translate("Frm_Segmentacion", u"AquaButton", None))
        self.btn_guardar.setText(QCoreApplication.translate("Frm_Segmentacion", u"Guardar", None))
        self.btn_guardar.setProperty(u"cssClass", QCoreApplication.translate("Frm_Segmentacion", u"YellowButton", None))
        self.btn_ejecutar.setText(QCoreApplication.translate("Frm_Segmentacion", u"Iniciar", None))
    # retranslateUi

