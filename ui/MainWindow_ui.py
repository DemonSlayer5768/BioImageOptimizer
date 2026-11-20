# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
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
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QStackedWidget, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 878)
        MainWindow.setMinimumSize(QSize(800, 600))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_sideBar = QFrame(self.centralwidget)
        self.frame_sideBar.setObjectName(u"frame_sideBar")
        self.frame_sideBar.setMinimumSize(QSize(200, 0))
        self.frame_sideBar.setStyleSheet(u"/*\n"
"QFrame{ \n"
"background-color: #111a2e;\n"
"}\n"
"\n"
"*/\n"
"\n"
"\n"
"\n"
"QPushButton {\n"
"    background-color: #111a2e;\n"
"    color: #c8d3e0;\n"
"\n"
"    border: 1px solid #1b2a41;\n"
"    border-radius: 8px;\n"
"\n"
"    padding: 10px 14px;\n"
"\n"
"    font-size: 14px;\n"
"    font-weight: 600;\n"
"\n"
"    text-align: left;\n"
"}\n"
"\n"
"/* Hover */\n"
"QPushButton:hover {\n"
"    background-color: #1b2a41;\n"
"    border: 1px solid #2f3e56;\n"
"    color: #65D6C6;\n"
"}\n"
"\n"
"/* Pressed */\n"
"QPushButton:pressed {\n"
"    background-color: #0b0f1a;\n"
"    border: 1px solid #65D6C6;\n"
"\n"
"    padding-top: 11px;\n"
"    padding-bottom: 9px;\n"
"}\n"
"\n"
"/* Disabled */\n"
"QPushButton:disabled {\n"
"    background-color: #0b0f1a;\n"
"    color: #59677a;\n"
"    border: 1px solid #111a2e;\n"
"}\n"
"")
        self.frame_sideBar.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_sideBar.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_sideBar)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(-1, 20, -1, 20)
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.lb_n1 = QLabel(self.frame_sideBar)
        self.lb_n1.setObjectName(u"lb_n1")
        font = QFont()
        font.setFamilies([u"Segoe UI Light"])
        font.setPointSize(25)
        self.lb_n1.setFont(font)
        self.lb_n1.setStyleSheet(u"\n"
"QLabel#sectionTitle {\n"
"    background-color: transparent;\n"
"    color: #c8d3e0;\n"
"\n"
"    border: none;\n"
"\n"
"    font-size: 17px;\n"
"    font-weight: 700;\n"
"\n"
"    padding: 4px 0px;\n"
"}\n"
"")

        self.verticalLayout_3.addWidget(self.lb_n1)

        self.lb_n2 = QLabel(self.frame_sideBar)
        self.lb_n2.setObjectName(u"lb_n2")
        self.lb_n2.setFont(font)
        self.lb_n2.setStyleSheet(u"\n"
"QLabel#sectionTitle {\n"
"    background-color: transparent;\n"
"    color: #c8d3e0;\n"
"\n"
"    border: none;\n"
"\n"
"    font-size: 17px;\n"
"    font-weight: 700;\n"
"\n"
"    padding: 4px 0px;\n"
"}\n"
"")

        self.verticalLayout_3.addWidget(self.lb_n2)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_3)

        self.verticalLayout_3.setStretch(0, 1)
        self.verticalLayout_3.setStretch(1, 2)

        self.verticalLayout_7.addLayout(self.verticalLayout_3)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer_4)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(10)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.btn_dashboard = QPushButton(self.frame_sideBar)
        self.btn_dashboard.setObjectName(u"btn_dashboard")
        self.btn_dashboard.setEnabled(True)
        font1 = QFont()
        font1.setFamilies([u"Arial"])
        font1.setWeight(QFont.DemiBold)
        self.btn_dashboard.setFont(font1)
        self.btn_dashboard.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_dashboard.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btn_dashboard.setAutoFillBackground(False)
        self.btn_dashboard.setStyleSheet(u"")
        icon = QIcon()
        icon.addFile(u"../resources/Icons/Icons_blancos/home.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_dashboard.setIcon(icon)
        self.btn_dashboard.setIconSize(QSize(25, 25))

        self.verticalLayout_2.addWidget(self.btn_dashboard)

        self.btn_galeria = QPushButton(self.frame_sideBar)
        self.btn_galeria.setObjectName(u"btn_galeria")
        self.btn_galeria.setEnabled(True)
        self.btn_galeria.setFont(font1)
        self.btn_galeria.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_galeria.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btn_galeria.setAutoFillBackground(False)
        self.btn_galeria.setStyleSheet(u"")
        icon1 = QIcon()
        icon1.addFile(u"../resources/Icons/Icons_blancos/image.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_galeria.setIcon(icon1)
        self.btn_galeria.setIconSize(QSize(25, 25))

        self.verticalLayout_2.addWidget(self.btn_galeria)

        self.btn_binarizacion = QPushButton(self.frame_sideBar)
        self.btn_binarizacion.setObjectName(u"btn_binarizacion")
        self.btn_binarizacion.setEnabled(True)
        self.btn_binarizacion.setFont(font1)
        self.btn_binarizacion.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_binarizacion.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btn_binarizacion.setAutoFillBackground(False)
        self.btn_binarizacion.setStyleSheet(u"")
        icon2 = QIcon()
        icon2.addFile(u"../resources/Icons/Icons_blancos/binarizacion.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_binarizacion.setIcon(icon2)
        self.btn_binarizacion.setIconSize(QSize(25, 25))

        self.verticalLayout_2.addWidget(self.btn_binarizacion)

        self.btn_segmentacion = QPushButton(self.frame_sideBar)
        self.btn_segmentacion.setObjectName(u"btn_segmentacion")
        self.btn_segmentacion.setEnabled(True)
        self.btn_segmentacion.setFont(font1)
        self.btn_segmentacion.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_segmentacion.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btn_segmentacion.setAutoFillBackground(False)
        self.btn_segmentacion.setStyleSheet(u"")
        icon3 = QIcon()
        icon3.addFile(u"../resources/Icons/Icons_blancos/segmentacion.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_segmentacion.setIcon(icon3)
        self.btn_segmentacion.setIconSize(QSize(25, 25))

        self.verticalLayout_2.addWidget(self.btn_segmentacion)

        self.btn_restauracion = QPushButton(self.frame_sideBar)
        self.btn_restauracion.setObjectName(u"btn_restauracion")
        self.btn_restauracion.setEnabled(True)
        self.btn_restauracion.setFont(font1)
        self.btn_restauracion.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_restauracion.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btn_restauracion.setAutoFillBackground(False)
        self.btn_restauracion.setStyleSheet(u"")
        icon4 = QIcon()
        icon4.addFile(u"../resources/Icons/Icons_blancos/restauracion.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_restauracion.setIcon(icon4)
        self.btn_restauracion.setIconSize(QSize(25, 25))

        self.verticalLayout_2.addWidget(self.btn_restauracion)

        self.btn_optimizacion = QPushButton(self.frame_sideBar)
        self.btn_optimizacion.setObjectName(u"btn_optimizacion")
        self.btn_optimizacion.setEnabled(False)
        self.btn_optimizacion.setFont(font1)
        self.btn_optimizacion.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_optimizacion.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btn_optimizacion.setAutoFillBackground(False)
        self.btn_optimizacion.setStyleSheet(u"")
        icon5 = QIcon()
        icon5.addFile(u"../resources/Icons/Icons_blancos/optimizacion.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_optimizacion.setIcon(icon5)
        self.btn_optimizacion.setIconSize(QSize(25, 25))

        self.verticalLayout_2.addWidget(self.btn_optimizacion)

        self.btn_procesamiento = QPushButton(self.frame_sideBar)
        self.btn_procesamiento.setObjectName(u"btn_procesamiento")
        self.btn_procesamiento.setEnabled(False)
        self.btn_procesamiento.setFont(font1)
        self.btn_procesamiento.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_procesamiento.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btn_procesamiento.setAutoFillBackground(False)
        self.btn_procesamiento.setStyleSheet(u"")
        icon6 = QIcon()
        icon6.addFile(u"../resources/Icons/Icons_blancos/procesamiento.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_procesamiento.setIcon(icon6)
        self.btn_procesamiento.setIconSize(QSize(25, 25))

        self.verticalLayout_2.addWidget(self.btn_procesamiento)


        self.verticalLayout_7.addLayout(self.verticalLayout_2)

        self.frame_line_2 = QFrame(self.frame_sideBar)
        self.frame_line_2.setObjectName(u"frame_line_2")
        self.frame_line_2.setMaximumSize(QSize(16777215, 5))
        self.frame_line_2.setStyleSheet(u"   QFrame {\n"
"        background-color: #2f3e56;\n"
"    }")
        self.frame_line_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_line_2.setFrameShadow(QFrame.Shadow.Raised)

        self.verticalLayout_7.addWidget(self.frame_line_2)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.btn_historial = QPushButton(self.frame_sideBar)
        self.btn_historial.setObjectName(u"btn_historial")
        self.btn_historial.setEnabled(True)
        self.btn_historial.setFont(font1)
        self.btn_historial.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_historial.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btn_historial.setAutoFillBackground(False)
        self.btn_historial.setStyleSheet(u"")
        icon7 = QIcon()
        icon7.addFile(u"../resources/Icons/Icons_blancos/history.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_historial.setIcon(icon7)
        self.btn_historial.setIconSize(QSize(25, 25))

        self.verticalLayout_4.addWidget(self.btn_historial)

        self.btn_configuracion = QPushButton(self.frame_sideBar)
        self.btn_configuracion.setObjectName(u"btn_configuracion")
        self.btn_configuracion.setEnabled(True)
        self.btn_configuracion.setFont(font1)
        self.btn_configuracion.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_configuracion.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btn_configuracion.setAutoFillBackground(False)
        self.btn_configuracion.setStyleSheet(u"")
        icon8 = QIcon()
        icon8.addFile(u"../resources/Icons/Icons_blancos/setting.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_configuracion.setIcon(icon8)
        self.btn_configuracion.setIconSize(QSize(25, 25))

        self.verticalLayout_4.addWidget(self.btn_configuracion)


        self.verticalLayout_7.addLayout(self.verticalLayout_4)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer_2)

        self.frame_line = QFrame(self.frame_sideBar)
        self.frame_line.setObjectName(u"frame_line")
        self.frame_line.setMaximumSize(QSize(16777215, 5))
        self.frame_line.setStyleSheet(u"   QFrame {\n"
"        background-color: #2f3e56;\n"
"    }")
        self.frame_line.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_line.setFrameShadow(QFrame.Shadow.Raised)

        self.verticalLayout_7.addWidget(self.frame_line)

        self.btn_salir = QPushButton(self.frame_sideBar)
        self.btn_salir.setObjectName(u"btn_salir")
        self.btn_salir.setEnabled(True)
        self.btn_salir.setFont(font1)
        self.btn_salir.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_salir.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btn_salir.setAutoFillBackground(False)
        self.btn_salir.setStyleSheet(u"")
        icon9 = QIcon()
        icon9.addFile(u"../resources/Icons/Icons_blancos/logout.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_salir.setIcon(icon9)
        self.btn_salir.setIconSize(QSize(25, 25))

        self.verticalLayout_7.addWidget(self.btn_salir)

        self.verticalLayout_7.setStretch(0, 1)
        self.verticalLayout_7.setStretch(3, 1)
        self.verticalLayout_7.setStretch(5, 2)
        self.verticalLayout_7.setStretch(6, 1)
        self.verticalLayout_7.setStretch(7, 2)
        self.verticalLayout_7.setStretch(8, 2)

        self.horizontalLayout.addWidget(self.frame_sideBar)

        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy)
        self.stackedWidget.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.stackedWidget.setAutoFillBackground(False)
        self.stackedWidget.setFrameShadow(QFrame.Shadow.Plain)
        self.page_DashBoard = QWidget()
        self.page_DashBoard.setObjectName(u"page_DashBoard")
        sizePolicy.setHeightForWidth(self.page_DashBoard.sizePolicy().hasHeightForWidth())
        self.page_DashBoard.setSizePolicy(sizePolicy)
        self.page_DashBoard.setMaximumSize(QSize(16777215, 16777215))
        self.page_DashBoard.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.page_DashBoard.setAutoFillBackground(False)
        self.verticalLayout_6 = QVBoxLayout(self.page_DashBoard)
        self.verticalLayout_6.setSpacing(1)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget.addWidget(self.page_DashBoard)
        self.page_Galeria = QWidget()
        self.page_Galeria.setObjectName(u"page_Galeria")
        self.verticalLayout_8 = QVBoxLayout(self.page_Galeria)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget.addWidget(self.page_Galeria)
        self.page_Optimizacion = QWidget()
        self.page_Optimizacion.setObjectName(u"page_Optimizacion")
        self.stackedWidget.addWidget(self.page_Optimizacion)
        self.page_Binarizacion = QWidget()
        self.page_Binarizacion.setObjectName(u"page_Binarizacion")
        self.stackedWidget.addWidget(self.page_Binarizacion)
        self.page_Segmentacion = QWidget()
        self.page_Segmentacion.setObjectName(u"page_Segmentacion")
        self.stackedWidget.addWidget(self.page_Segmentacion)
        self.page_Procesamiento = QWidget()
        self.page_Procesamiento.setObjectName(u"page_Procesamiento")
        self.stackedWidget.addWidget(self.page_Procesamiento)
        self.page_Restauracion = QWidget()
        self.page_Restauracion.setObjectName(u"page_Restauracion")
        self.stackedWidget.addWidget(self.page_Restauracion)
        self.page_Historial = QWidget()
        self.page_Historial.setObjectName(u"page_Historial")
        self.stackedWidget.addWidget(self.page_Historial)
        self.page_configuracion = QWidget()
        self.page_configuracion.setObjectName(u"page_configuracion")
        self.stackedWidget.addWidget(self.page_configuracion)

        self.horizontalLayout.addWidget(self.stackedWidget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.btn_dashboard.setDefault(False)
        self.btn_galeria.setDefault(False)
        self.btn_binarizacion.setDefault(False)
        self.btn_segmentacion.setDefault(False)
        self.btn_restauracion.setDefault(False)
        self.btn_optimizacion.setDefault(False)
        self.btn_procesamiento.setDefault(False)
        self.btn_historial.setDefault(False)
        self.btn_configuracion.setDefault(False)
        self.btn_salir.setDefault(False)
        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.frame_sideBar.setProperty(u"cssClass", QCoreApplication.translate("MainWindow", u"Background", None))
        self.lb_n1.setText(QCoreApplication.translate("MainWindow", u"BioImage", None))
        self.lb_n2.setText(QCoreApplication.translate("MainWindow", u"Optimizer", None))
        self.btn_dashboard.setText(QCoreApplication.translate("MainWindow", u"Dashboard", None))
        self.btn_galeria.setText(QCoreApplication.translate("MainWindow", u"Galeria", None))
        self.btn_binarizacion.setText(QCoreApplication.translate("MainWindow", u"Binarizaci\u00f3n", None))
        self.btn_segmentacion.setText(QCoreApplication.translate("MainWindow", u"Segmentaci\u00f3n", None))
        self.btn_restauracion.setText(QCoreApplication.translate("MainWindow", u"Restauraci\u00f3n", None))
        self.btn_optimizacion.setText(QCoreApplication.translate("MainWindow", u"Optimizaci\u00f3n", None))
        self.btn_procesamiento.setText(QCoreApplication.translate("MainWindow", u"Procesamiento", None))
        self.btn_historial.setText(QCoreApplication.translate("MainWindow", u"Historial", None))
        self.btn_configuracion.setText(QCoreApplication.translate("MainWindow", u"Configuraci\u00f3n", None))
        self.btn_salir.setText(QCoreApplication.translate("MainWindow", u"Salir", None))
#if QT_CONFIG(statustip)
        self.stackedWidget.setStatusTip("")
#endif // QT_CONFIG(statustip)
        self.stackedWidget.setAccessibleIdentifier("")
    # retranslateUi

