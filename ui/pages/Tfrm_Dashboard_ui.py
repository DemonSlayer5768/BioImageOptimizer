# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Tfrm_Dashboard.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QLayout, QPushButton, QSizePolicy, QSpacerItem,
    QToolButton, QVBoxLayout, QWidget)

class Ui_Frm_Dashboard(object):
    def setupUi(self, Frm_Dashboard):
        if not Frm_Dashboard.objectName():
            Frm_Dashboard.setObjectName(u"Frm_Dashboard")
        Frm_Dashboard.resize(954, 828)
        Frm_Dashboard.setMinimumSize(QSize(950, 820))
        Frm_Dashboard.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.verticalLayout_2 = QVBoxLayout(Frm_Dashboard)
        self.verticalLayout_2.setSpacing(1)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.Panel_container = QFrame(Frm_Dashboard)
        self.Panel_container.setObjectName(u"Panel_container")
        self.Panel_container.setMinimumSize(QSize(950, 800))
        self.Panel_container.setStyleSheet(u"")
        self.Panel_container.setFrameShape(QFrame.Shape.StyledPanel)
        self.Panel_container.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.Panel_container)
        self.verticalLayout.setSpacing(9)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(9, 9, 9, 0)
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

        self.Panel_1 = QFrame(self.Panel_container)
        self.Panel_1.setObjectName(u"Panel_1")
        self.Panel_1.setMinimumSize(QSize(0, 0))
        self.Panel_1.setMaximumSize(QSize(16777215, 125))
        self.Panel_1.setFrameShape(QFrame.Shape.NoFrame)
        self.Panel_1.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.Panel_1)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(9, 0, -1, 0)
        self.Card_cantidad_imgs = QFrame(self.Panel_1)
        self.Card_cantidad_imgs.setObjectName(u"Card_cantidad_imgs")
        self.Card_cantidad_imgs.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.Card_cantidad_imgs.setStyleSheet(u"")
        self.Card_cantidad_imgs.setFrameShape(QFrame.Shape.StyledPanel)
        self.Card_cantidad_imgs.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.Card_cantidad_imgs)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.lb_img = QLabel(self.Card_cantidad_imgs)
        self.lb_img.setObjectName(u"lb_img")
        self.lb_img.setMinimumSize(QSize(28, 28))
        self.lb_img.setMaximumSize(QSize(28, 28))
        self.lb_img.setPixmap(QPixmap(u"../../resources/Icons/Icons_aqua/image.png"))
        self.lb_img.setScaledContents(True)
        self.lb_img.setWordWrap(False)

        self.verticalLayout_6.addWidget(self.lb_img)

        self.lb_Img_count = QLabel(self.Card_cantidad_imgs)
        self.lb_Img_count.setObjectName(u"lb_Img_count")
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(28)
        font.setWeight(QFont.DemiBold)
        font.setItalic(False)
        self.lb_Img_count.setFont(font)
        self.lb_Img_count.setStyleSheet(u"color: rgb(101, 214, 198);\n"
"font: 700 28pt \"Arial\";\n"
"font-weight: 600;\n"
"")

        self.verticalLayout_6.addWidget(self.lb_Img_count)

        self.lb_primary_2 = QLabel(self.Card_cantidad_imgs)
        self.lb_primary_2.setObjectName(u"lb_primary_2")
        font1 = QFont()
        font1.setBold(True)
        font1.setItalic(False)
        self.lb_primary_2.setFont(font1)
        self.lb_primary_2.setStyleSheet(u"")

        self.verticalLayout_6.addWidget(self.lb_primary_2)


        self.horizontalLayout_2.addWidget(self.Card_cantidad_imgs)

        self.Card_cantidad_procesos = QFrame(self.Panel_1)
        self.Card_cantidad_procesos.setObjectName(u"Card_cantidad_procesos")
        self.Card_cantidad_procesos.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.Card_cantidad_procesos.setStyleSheet(u"")
        self.Card_cantidad_procesos.setFrameShape(QFrame.Shape.StyledPanel)
        self.Card_cantidad_procesos.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.Card_cantidad_procesos)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.lb_img_3 = QLabel(self.Card_cantidad_procesos)
        self.lb_img_3.setObjectName(u"lb_img_3")
        self.lb_img_3.setMinimumSize(QSize(28, 28))
        self.lb_img_3.setMaximumSize(QSize(28, 28))
        self.lb_img_3.setPixmap(QPixmap(u"../../resources/Icons/Icons_aqua/folder.png"))
        self.lb_img_3.setScaledContents(True)
        self.lb_img_3.setWordWrap(False)

        self.verticalLayout_5.addWidget(self.lb_img_3)

        self.lb_exp_count = QLabel(self.Card_cantidad_procesos)
        self.lb_exp_count.setObjectName(u"lb_exp_count")
        self.lb_exp_count.setFont(font)
        self.lb_exp_count.setStyleSheet(u"color: rgb(101, 214, 198);\n"
"font: 700 28pt \"Arial\";\n"
"font-weight: 600;\n"
"")

        self.verticalLayout_5.addWidget(self.lb_exp_count)

        self.lb_primary = QLabel(self.Card_cantidad_procesos)
        self.lb_primary.setObjectName(u"lb_primary")
        self.lb_primary.setFont(font1)
        self.lb_primary.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.lb_primary.setStyleSheet(u"")

        self.verticalLayout_5.addWidget(self.lb_primary)


        self.horizontalLayout_2.addWidget(self.Card_cantidad_procesos)

        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 1)

        self.verticalLayout.addWidget(self.Panel_1)

        self.Panel_2 = QFrame(self.Panel_container)
        self.Panel_2.setObjectName(u"Panel_2")
        self.Panel_2.setMaximumSize(QSize(16777215, 150))
        self.Panel_2.setFrameShape(QFrame.Shape.NoFrame)
        self.Panel_2.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.Panel_2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(9, 0, 9, 0)
        self.Card_accesos_rapidos = QFrame(self.Panel_2)
        self.Card_accesos_rapidos.setObjectName(u"Card_accesos_rapidos")
        self.Card_accesos_rapidos.setMaximumSize(QSize(16777215, 200))
        self.Card_accesos_rapidos.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.Card_accesos_rapidos.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.Card_accesos_rapidos.setStyleSheet(u"")
        self.Card_accesos_rapidos.setFrameShape(QFrame.Shape.StyledPanel)
        self.Card_accesos_rapidos.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.Card_accesos_rapidos)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.Layout_horizontal = QHBoxLayout()
        self.Layout_horizontal.setObjectName(u"Layout_horizontal")
        self.Layout_horizontal.setContentsMargins(9, 9, 0, 0)
        self.lb_img_2 = QLabel(self.Card_accesos_rapidos)
        self.lb_img_2.setObjectName(u"lb_img_2")
        self.lb_img_2.setMinimumSize(QSize(28, 28))
        self.lb_img_2.setMaximumSize(QSize(28, 28))
        self.lb_img_2.setPixmap(QPixmap(u"../../resources/Icons/Icons_aqua/flash_on.png"))
        self.lb_img_2.setScaledContents(True)
        self.lb_img_2.setWordWrap(False)

        self.Layout_horizontal.addWidget(self.lb_img_2)

        self.lb_primary_4 = QLabel(self.Card_accesos_rapidos)
        self.lb_primary_4.setObjectName(u"lb_primary_4")
        self.lb_primary_4.setFont(font1)
        self.lb_primary_4.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.lb_primary_4.setStyleSheet(u"")

        self.Layout_horizontal.addWidget(self.lb_primary_4)

        self.Layout_horizontal.setStretch(0, 1)
        self.Layout_horizontal.setStretch(1, 1)

        self.verticalLayout_3.addLayout(self.Layout_horizontal)

        self.Layout_horizontal_2 = QHBoxLayout()
        self.Layout_horizontal_2.setObjectName(u"Layout_horizontal_2")
        self.Tbtn_Importar_Imagenes = QToolButton(self.Card_accesos_rapidos)
        self.Tbtn_Importar_Imagenes.setObjectName(u"Tbtn_Importar_Imagenes")
        self.Tbtn_Importar_Imagenes.setMinimumSize(QSize(150, 50))
        self.Tbtn_Importar_Imagenes.setMaximumSize(QSize(300, 16777215))
        self.Tbtn_Importar_Imagenes.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.Tbtn_Importar_Imagenes.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.Tbtn_Importar_Imagenes.setAutoFillBackground(False)
        self.Tbtn_Importar_Imagenes.setStyleSheet(u"")
        icon = QIcon()
        icon.addFile(u"../../resources/Icons/Icons_aqua/image.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.Tbtn_Importar_Imagenes.setIcon(icon)
        self.Tbtn_Importar_Imagenes.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)

        self.Layout_horizontal_2.addWidget(self.Tbtn_Importar_Imagenes)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.Layout_horizontal_2.addItem(self.horizontalSpacer)

        self.Tbtn_CompararImgs = QToolButton(self.Card_accesos_rapidos)
        self.Tbtn_CompararImgs.setObjectName(u"Tbtn_CompararImgs")
        self.Tbtn_CompararImgs.setMinimumSize(QSize(150, 50))
        self.Tbtn_CompararImgs.setMaximumSize(QSize(300, 16777215))
        self.Tbtn_CompararImgs.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.Tbtn_CompararImgs.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.Tbtn_CompararImgs.setAutoFillBackground(False)
        self.Tbtn_CompararImgs.setStyleSheet(u"")
        icon1 = QIcon()
        icon1.addFile(u"../../resources/Icons/Icons_aqua/page.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.Tbtn_CompararImgs.setIcon(icon1)
        self.Tbtn_CompararImgs.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)

        self.Layout_horizontal_2.addWidget(self.Tbtn_CompararImgs)

        self.Tbtn_Resultados = QToolButton(self.Card_accesos_rapidos)
        self.Tbtn_Resultados.setObjectName(u"Tbtn_Resultados")
        self.Tbtn_Resultados.setMinimumSize(QSize(150, 50))
        self.Tbtn_Resultados.setMaximumSize(QSize(300, 16777215))
        self.Tbtn_Resultados.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.Tbtn_Resultados.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.Tbtn_Resultados.setAutoFillBackground(False)
        self.Tbtn_Resultados.setStyleSheet(u"")
        icon2 = QIcon()
        icon2.addFile(u"../../resources/Icons/Icons_aqua/bar-chart.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.Tbtn_Resultados.setIcon(icon2)
        self.Tbtn_Resultados.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)

        self.Layout_horizontal_2.addWidget(self.Tbtn_Resultados)


        self.verticalLayout_3.addLayout(self.Layout_horizontal_2)

        self.verticalLayout_3.setStretch(0, 1)
        self.verticalLayout_3.setStretch(1, 9)

        self.horizontalLayout_3.addWidget(self.Card_accesos_rapidos)


        self.verticalLayout.addWidget(self.Panel_2)

        self.Panel_3 = QFrame(self.Panel_container)
        self.Panel_3.setObjectName(u"Panel_3")
        self.Panel_3.setFrameShape(QFrame.Shape.NoFrame)
        self.Panel_3.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.Panel_3)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.Card_historial = QFrame(self.Panel_3)
        self.Card_historial.setObjectName(u"Card_historial")
        self.Card_historial.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.Card_historial.setStyleSheet(u"")
        self.Card_historial.setFrameShape(QFrame.Shape.StyledPanel)
        self.Card_historial.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.Card_historial)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.Layout_horizontal_3 = QHBoxLayout()
        self.Layout_horizontal_3.setObjectName(u"Layout_horizontal_3")
        self.lb_img_4 = QLabel(self.Card_historial)
        self.lb_img_4.setObjectName(u"lb_img_4")
        self.lb_img_4.setMinimumSize(QSize(28, 28))
        self.lb_img_4.setMaximumSize(QSize(28, 28))
        self.lb_img_4.setPixmap(QPixmap(u"../../resources/Icons/Icons_aqua/bar-chart.png"))
        self.lb_img_4.setScaledContents(True)
        self.lb_img_4.setWordWrap(False)

        self.Layout_horizontal_3.addWidget(self.lb_img_4)

        self.lb_primary_3 = QLabel(self.Card_historial)
        self.lb_primary_3.setObjectName(u"lb_primary_3")
        self.lb_primary_3.setFont(font1)
        self.lb_primary_3.setStyleSheet(u"")

        self.Layout_horizontal_3.addWidget(self.lb_primary_3)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.Layout_horizontal_3.addItem(self.horizontalSpacer_2)

        self.btn_verTodos = QPushButton(self.Card_historial)
        self.btn_verTodos.setObjectName(u"btn_verTodos")
        self.btn_verTodos.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_verTodos.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.btn_verTodos.setStyleSheet(u"color: #65D6C6;")
        icon3 = QIcon()
        icon3.addFile(u"../../resources/Icons/Icons_aqua/chevron_right.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_verTodos.setIcon(icon3)
        self.btn_verTodos.setFlat(True)

        self.Layout_horizontal_3.addWidget(self.btn_verTodos)


        self.verticalLayout_4.addLayout(self.Layout_horizontal_3)

        self.Card_actividad_reciente = QFrame(self.Card_historial)
        self.Card_actividad_reciente.setObjectName(u"Card_actividad_reciente")
        self.Card_actividad_reciente.setStyleSheet(u"")
        self.Card_actividad_reciente.setFrameShape(QFrame.Shape.StyledPanel)
        self.Card_actividad_reciente.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.Card_actividad_reciente)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(-1, 0, -1, 15)

        self.verticalLayout_4.addWidget(self.Card_actividad_reciente)

        self.verticalLayout_4.setStretch(0, 1)
        self.verticalLayout_4.setStretch(1, 7)

        self.horizontalLayout_4.addWidget(self.Card_historial)


        self.verticalLayout.addWidget(self.Panel_3)

        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 2)
        self.verticalLayout.setStretch(2, 3)
        self.verticalLayout.setStretch(3, 6)

        self.verticalLayout_2.addWidget(self.Panel_container)


        self.retranslateUi(Frm_Dashboard)

        QMetaObject.connectSlotsByName(Frm_Dashboard)
    # setupUi

    def retranslateUi(self, Frm_Dashboard):
        Frm_Dashboard.setWindowTitle(QCoreApplication.translate("Frm_Dashboard", u"Form", None))
#if QT_CONFIG(accessibility)
        self.Panel_container.setAccessibleName(QCoreApplication.translate("Frm_Dashboard", u"BackGround", None))
#endif // QT_CONFIG(accessibility)
        self.Panel_container.setProperty(u"cssClass", QCoreApplication.translate("Frm_Dashboard", u"Background", None))
#if QT_CONFIG(tooltip)
        self.Panel_Head.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.Panel_Head.setProperty(u"cssClass", QCoreApplication.translate("Frm_Dashboard", u"Surface", None))
        self.lb_titulo.setText(QCoreApplication.translate("Frm_Dashboard", u"Dashboard", None))
        self.lb_titulo.setProperty(u"cssClass", QCoreApplication.translate("Frm_Dashboard", u"Tittle", None))
        self.lb_descripcion.setText(QCoreApplication.translate("Frm_Dashboard", u"Resumen General", None))
        self.lb_descripcion.setProperty(u"cssClass", QCoreApplication.translate("Frm_Dashboard", u"Description", None))
        self.Panel_1.setProperty(u"cssClass", QCoreApplication.translate("Frm_Dashboard", u"Surface", None))
        self.Card_cantidad_imgs.setProperty(u"cssClass", QCoreApplication.translate("Frm_Dashboard", u"Card", None))
        self.lb_img.setText("")
        self.lb_Img_count.setText(QCoreApplication.translate("Frm_Dashboard", u"0", None))
        self.lb_primary_2.setText(QCoreApplication.translate("Frm_Dashboard", u"Imagenes", None))
        self.lb_primary_2.setProperty(u"cssClass", QCoreApplication.translate("Frm_Dashboard", u"Grande", None))
        self.Card_cantidad_procesos.setProperty(u"cssClass", QCoreApplication.translate("Frm_Dashboard", u"Card", None))
        self.lb_img_3.setText("")
        self.lb_exp_count.setText(QCoreApplication.translate("Frm_Dashboard", u"0", None))
        self.lb_primary.setText(QCoreApplication.translate("Frm_Dashboard", u"Imagenes procesadas", None))
        self.lb_primary.setProperty(u"cssClass", QCoreApplication.translate("Frm_Dashboard", u"Grande", None))
        self.Panel_2.setProperty(u"cssClass", QCoreApplication.translate("Frm_Dashboard", u"Surface", None))
        self.Card_accesos_rapidos.setProperty(u"cssClass", QCoreApplication.translate("Frm_Dashboard", u"Card", None))
        self.lb_img_2.setText("")
        self.lb_primary_4.setText(QCoreApplication.translate("Frm_Dashboard", u"Accesos Rapidos", None))
        self.lb_primary_4.setProperty(u"cssClass", QCoreApplication.translate("Frm_Dashboard", u"Mediana", None))
#if QT_CONFIG(accessibility)
        self.Tbtn_Importar_Imagenes.setAccessibleDescription("")
#endif // QT_CONFIG(accessibility)
        self.Tbtn_Importar_Imagenes.setText(QCoreApplication.translate("Frm_Dashboard", u"Cargar Imagen", None))
        self.Tbtn_Importar_Imagenes.setProperty(u"cssClass", QCoreApplication.translate("Frm_Dashboard", u"Primary", None))
#if QT_CONFIG(accessibility)
        self.Tbtn_CompararImgs.setAccessibleDescription("")
#endif // QT_CONFIG(accessibility)
        self.Tbtn_CompararImgs.setText(QCoreApplication.translate("Frm_Dashboard", u"Comparar Imagenes", None))
        self.Tbtn_CompararImgs.setProperty(u"cssClass", QCoreApplication.translate("Frm_Dashboard", u"Primary", None))
#if QT_CONFIG(accessibility)
        self.Tbtn_Resultados.setAccessibleDescription("")
#endif // QT_CONFIG(accessibility)
        self.Tbtn_Resultados.setText(QCoreApplication.translate("Frm_Dashboard", u"Ver Resultados", None))
        self.Tbtn_Resultados.setProperty(u"cssClass", QCoreApplication.translate("Frm_Dashboard", u"Primary", None))
        self.Panel_3.setProperty(u"cssClass", QCoreApplication.translate("Frm_Dashboard", u"Surface", None))
        self.Card_historial.setProperty(u"cssClass", QCoreApplication.translate("Frm_Dashboard", u"Card", None))
        self.lb_img_4.setText("")
        self.lb_primary_3.setText(QCoreApplication.translate("Frm_Dashboard", u"Actividad Reciente", None))
        self.lb_primary_3.setProperty(u"cssClass", QCoreApplication.translate("Frm_Dashboard", u"Mediana", None))
        self.btn_verTodos.setText(QCoreApplication.translate("Frm_Dashboard", u"Ver todos", None))
        self.Card_actividad_reciente.setProperty(u"cssClass", QCoreApplication.translate("Frm_Dashboard", u"Card", None))
    # retranslateUi

