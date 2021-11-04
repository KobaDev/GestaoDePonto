# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tela_menurITCNn.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import icons_rc

class Ui_MainWindow(QObject):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1028, 777)
        MainWindow.setMinimumSize(1024, 768)
        MainWindow.setStyleSheet(u"border: none;\n"
"background-color: rgb(255, 255, 255);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_top_menu = QFrame(self.centralwidget)
        self.frame_top_menu.setObjectName(u"frame_top_menu")
        self.frame_top_menu.setStyleSheet(u"background-color: rgb(16, 49, 100);")
        self.frame_top_menu.setFrameShape(QFrame.StyledPanel)
        self.frame_top_menu.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_top_menu)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_11 = QFrame(self.frame_top_menu)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.frame = QFrame(self.frame_11)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(50, 50))
        self.label_4.setPixmap(QPixmap(u":/icons/Desing_MODERN-UI/telas_Novas_UI - (Jadson implementa\u00e7\u00e3o)/telas e icons/icons/Bianca/Icones e Imagens/IconeFotoNavBar.svg"))
        self.label_4.setScaledContents(True)
        self.label_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_4)


        self.horizontalLayout_2.addWidget(self.frame)

        self.frame_19 = QFrame(self.frame_11)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_19)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_5 = QLabel(self.frame_19)
        self.label_5.setObjectName(u"label_5")
        font = QFont()
        font.setFamily(u"Lucida Console")
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_2.addWidget(self.label_5)

        self.label_6 = QLabel(self.frame_19)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font)

        self.verticalLayout_2.addWidget(self.label_6)


        self.horizontalLayout_2.addWidget(self.frame_19)


        self.horizontalLayout.addWidget(self.frame_11)

        self.frame_10 = QFrame(self.frame_top_menu)
        self.frame_10.setObjectName(u"frame_10")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_10.sizePolicy().hasHeightForWidth())
        self.frame_10.setSizePolicy(sizePolicy)
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_3.setSpacing(5)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_18 = QFrame(self.frame_10)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_18)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.home_btn = QPushButton(self.frame_18)
        self.home_btn.setObjectName(u"home_btn")
        self.home_btn.setStyleSheet(u"color: rgb(255, 255, 255);")
        icon = QIcon()
        icon.addFile(u":/icons/Desing_MODERN-UI/telas_Novas_UI - (Jadson implementa\u00e7\u00e3o)/telas e icons/icons/Bianca/Icones e Imagens/IconeHome.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.home_btn.setIcon(icon)
        self.home_btn.setIconSize(QSize(50, 50))
        self.home_btn.setFlat(True)

        self.verticalLayout_8.addWidget(self.home_btn)


        self.horizontalLayout_3.addWidget(self.frame_18)

        self.frame_16 = QFrame(self.frame_10)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_16)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.meus_dados1_btn = QPushButton(self.frame_16)
        self.meus_dados1_btn.setObjectName(u"meus_dados1_btn")
        font1 = QFont()
        font1.setFamily(u"Lucida Console")
        font1.setPointSize(11)
        font1.setBold(True)
        font1.setWeight(75)
        self.meus_dados1_btn.setFont(font1)
        self.meus_dados1_btn.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.meus_dados1_btn.setFlat(True)

        self.verticalLayout_7.addWidget(self.meus_dados1_btn)


        self.horizontalLayout_3.addWidget(self.frame_16)

        self.frame_14 = QFrame(self.frame_10)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_14)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.marcaponto_btn1 = QPushButton(self.frame_14)
        self.marcaponto_btn1.setObjectName(u"marcaponto_btn1")
        self.marcaponto_btn1.setFont(font1)
        self.marcaponto_btn1.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.marcaponto_btn1.setFlat(True)

        self.verticalLayout_6.addWidget(self.marcaponto_btn1)


        self.horizontalLayout_3.addWidget(self.frame_14)

        self.frame_13 = QFrame(self.frame_10)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_13)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.relatorio_btn1 = QPushButton(self.frame_13)
        self.relatorio_btn1.setObjectName(u"relatorio_btn1")
        self.relatorio_btn1.setFont(font1)
        self.relatorio_btn1.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.relatorio_btn1.setFlat(True)

        self.verticalLayout_5.addWidget(self.relatorio_btn1)


        self.horizontalLayout_3.addWidget(self.frame_13)

        self.frame_12 = QFrame(self.frame_10)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_12)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.sair_btn = QPushButton(self.frame_12)
        self.sair_btn.setObjectName(u"sair_btn")
        self.sair_btn.setStyleSheet(u"color: rgb(255, 255, 255);")
        icon1 = QIcon()
        icon1.addFile(u":/icons/Desing_MODERN-UI/telas_Novas_UI - (Jadson implementa\u00e7\u00e3o)/telas e icons/icons/Bianca/Icones e Imagens/IconeSair.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.sair_btn.setIcon(icon1)
        self.sair_btn.setIconSize(QSize(50, 50))
        self.sair_btn.setFlat(True)

        self.verticalLayout_4.addWidget(self.sair_btn)


        self.horizontalLayout_3.addWidget(self.frame_12)


        self.horizontalLayout.addWidget(self.frame_10)


        self.verticalLayout.addWidget(self.frame_top_menu, 0, Qt.AlignTop)

        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"background-color: rgb(222, 222, 222);")
        self.main_pg = QWidget()
        self.main_pg.setObjectName(u"main_pg")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.main_pg.sizePolicy().hasHeightForWidth())
        self.main_pg.setSizePolicy(sizePolicy1)
        self.main_pg.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.verticalLayout_12 = QVBoxLayout(self.main_pg)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.escolha_primaria = QFrame(self.main_pg)
        self.escolha_primaria.setObjectName(u"escolha_primaria")
        sizePolicy1.setHeightForWidth(self.escolha_primaria.sizePolicy().hasHeightForWidth())
        self.escolha_primaria.setSizePolicy(sizePolicy1)
        self.escolha_primaria.setFrameShape(QFrame.StyledPanel)
        self.escolha_primaria.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.escolha_primaria)
        self.horizontalLayout_4.setSpacing(10)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(150, 150, 150, 150)
        self.user_data_grid = QFrame(self.escolha_primaria)
        self.user_data_grid.setObjectName(u"user_data_grid")
        self.user_data_grid.setMinimumSize(QSize(0, 0))
        self.user_data_grid.setFrameShape(QFrame.StyledPanel)
        self.user_data_grid.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.user_data_grid)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.user_data_grid)
        self.label.setObjectName(u"label")
        self.label.setPixmap(QPixmap(u":/icons/Desing_MODERN-UI/telas_Novas_UI - (Jadson implementa\u00e7\u00e3o)/telas e icons/icons/Bianca/Icones e Imagens/IconeMeusDados.svg"))
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_9.addWidget(self.label)

        self.meus_dados2_btn = QPushButton(self.user_data_grid)
        self.meus_dados2_btn.setObjectName(u"meus_dados2_btn")
        self.meus_dados2_btn.setMaximumSize(QSize(210, 100))
        font2 = QFont()
        font2.setFamily(u"Lucida Console")
        font2.setPointSize(12)
        font2.setBold(True)
        font2.setWeight(75)
        self.meus_dados2_btn.setFont(font2)
        self.meus_dados2_btn.setStyleSheet(u"background-color: rgb(13, 28, 122);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 30px;\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-color: rgb(120, 120, 120);")

        self.verticalLayout_9.addWidget(self.meus_dados2_btn)


        self.horizontalLayout_4.addWidget(self.user_data_grid)

        self.user_marc_grid = QFrame(self.escolha_primaria)
        self.user_marc_grid.setObjectName(u"user_marc_grid")
        self.user_marc_grid.setFrameShape(QFrame.StyledPanel)
        self.user_marc_grid.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.user_marc_grid)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.user_marc_grid)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setPixmap(QPixmap(u":/icons/Desing_MODERN-UI/telas_Novas_UI - (Jadson implementa\u00e7\u00e3o)/telas e icons/icons/Bianca/Icones e Imagens/IconeMarcarPonto.svg"))
        self.label_2.setScaledContents(False)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_10.addWidget(self.label_2)

        self.marcaponto_btn2 = QPushButton(self.user_marc_grid)
        self.marcaponto_btn2.setObjectName(u"marcaponto_btn2")
        self.marcaponto_btn2.setMaximumSize(QSize(210, 100))
        self.marcaponto_btn2.setFont(font2)
        self.marcaponto_btn2.setStyleSheet(u"background-color: rgb(13, 28, 122);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 30px;\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-color: rgb(120, 120, 120);")

        self.verticalLayout_10.addWidget(self.marcaponto_btn2)


        self.horizontalLayout_4.addWidget(self.user_marc_grid)

        self.user_report_grid = QFrame(self.escolha_primaria)
        self.user_report_grid.setObjectName(u"user_report_grid")
        self.user_report_grid.setFrameShape(QFrame.StyledPanel)
        self.user_report_grid.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.user_report_grid)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.user_report_grid)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setPixmap(QPixmap(u":/icons/Desing_MODERN-UI/telas_Novas_UI - (Jadson implementa\u00e7\u00e3o)/telas e icons/icons/Bianca/Icones e Imagens/IconeRelat\u00f3rio.svg"))
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_11.addWidget(self.label_3)

        self.relatorio_btn2 = QPushButton(self.user_report_grid)
        self.relatorio_btn2.setObjectName(u"relatorio_btn2")
        self.relatorio_btn2.setMaximumSize(QSize(210, 100))
        self.relatorio_btn2.setFont(font2)
        self.relatorio_btn2.setStyleSheet(u"background-color: rgb(13, 28, 122);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 30px;\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-color: rgb(120, 120, 120);")

        self.verticalLayout_11.addWidget(self.relatorio_btn2)


        self.horizontalLayout_4.addWidget(self.user_report_grid)


        self.verticalLayout_12.addWidget(self.escolha_primaria)

        self.stackedWidget.addWidget(self.main_pg)
        self.data_view_pg = QWidget()
        self.data_view_pg.setObjectName(u"data_view_pg")
        self.horizontalLayout_5 = QHBoxLayout(self.data_view_pg)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.data_view_pg)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(365, 0))
        self.frame_2.setMaximumSize(QSize(350, 16777215))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.frame_2)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.title_data_grid = QFrame(self.frame_2)
        self.title_data_grid.setObjectName(u"title_data_grid")
        self.title_data_grid.setMaximumSize(QSize(350, 50))
        self.title_data_grid.setFrameShape(QFrame.StyledPanel)
        self.title_data_grid.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.title_data_grid)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(40, 0, -1, 0)
        self.meus_dados_text = QLabel(self.title_data_grid)
        self.meus_dados_text.setObjectName(u"meus_dados_text")
        font3 = QFont()
        font3.setFamily(u"Lucida Console")
        font3.setPointSize(18)
        font3.setBold(True)
        font3.setWeight(75)
        self.meus_dados_text.setFont(font3)

        self.verticalLayout_17.addWidget(self.meus_dados_text)


        self.verticalLayout_16.addWidget(self.title_data_grid)

        self.user_icon_gride = QFrame(self.frame_2)
        self.user_icon_gride.setObjectName(u"user_icon_gride")
        self.user_icon_gride.setMaximumSize(QSize(350, 16777215))
        self.user_icon_gride.setFrameShape(QFrame.StyledPanel)
        self.user_icon_gride.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.user_icon_gride)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.user_icon = QLabel(self.user_icon_gride)
        self.user_icon.setObjectName(u"user_icon")
        self.user_icon.setMaximumSize(QSize(250, 250))
        self.user_icon.setPixmap(QPixmap(u":/icons/Desing_MODERN-UI/telas_Novas_UI - (Jadson implementa\u00e7\u00e3o)/telas e icons/icons/Bianca/Icones e Imagens/IconeFotoFuncionarioAmpliada.svg"))
        self.user_icon.setScaledContents(True)
        self.user_icon.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_6.addWidget(self.user_icon)


        self.verticalLayout_16.addWidget(self.user_icon_gride)


        self.horizontalLayout_5.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.data_view_pg)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setStyleSheet(u"background-color: rgb(222, 222, 222);")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_3)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.inferior_adequa = QFrame(self.frame_3)
        self.inferior_adequa.setObjectName(u"inferior_adequa")
        self.inferior_adequa.setMaximumSize(QSize(16777215, 50))
        self.inferior_adequa.setFrameShape(QFrame.StyledPanel)
        self.inferior_adequa.setFrameShadow(QFrame.Raised)

        self.verticalLayout_13.addWidget(self.inferior_adequa)

        self.frame_9 = QFrame(self.frame_3)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 25px;\n"
"border-style: outset;\n"
"")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.frame_9)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.frame_6 = QFrame(self.frame_9)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_6)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(30)
        self.gridLayout.setVerticalSpacing(0)
        self.gridLayout.setContentsMargins(30, 30, 30, 30)
        self.label_11 = QLabel(self.frame_6)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font)

        self.gridLayout.addWidget(self.label_11, 2, 0, 1, 1)

        self.label_17 = QLabel(self.frame_6)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_17, 3, 1, 1, 1)

        self.label_10 = QLabel(self.frame_6)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font)

        self.gridLayout.addWidget(self.label_10, 1, 0, 1, 1)

        self.label_15 = QLabel(self.frame_6)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_15, 2, 1, 1, 1)

        self.label_9 = QLabel(self.frame_6)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font)

        self.gridLayout.addWidget(self.label_9, 0, 0, 1, 1)

        self.label_18 = QLabel(self.frame_6)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_18, 1, 1, 1, 1)

        self.label_16 = QLabel(self.frame_6)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setLayoutDirection(Qt.RightToLeft)
        self.label_16.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_16, 0, 1, 1, 1)

        self.label_12 = QLabel(self.frame_6)
        self.label_12.setObjectName(u"label_12")
        font4 = QFont()
        font4.setFamily(u"Lucida Console")
        font4.setPointSize(10)
        font4.setBold(False)
        font4.setWeight(50)
        self.label_12.setFont(font4)

        self.gridLayout.addWidget(self.label_12, 3, 0, 1, 1)


        self.verticalLayout_14.addWidget(self.frame_6)

        self.frame_7 = QFrame(self.frame_9)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMaximumSize(QSize(16777215, 100))
        self.frame_7.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.frame_7)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(120, 0, 120, 0)
        self.data_edit_btn = QPushButton(self.frame_7)
        self.data_edit_btn.setObjectName(u"data_edit_btn")
        self.data_edit_btn.setMaximumSize(QSize(210, 45))
        font5 = QFont()
        font5.setFamily(u"Lucida Console")
        font5.setPointSize(14)
        font5.setBold(False)
        font5.setWeight(50)
        self.data_edit_btn.setFont(font5)
        self.data_edit_btn.setStyleSheet(u"background-color: rgb(152, 4, 39);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 20px;\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-color: rgb(120, 120, 120);")

        self.verticalLayout_15.addWidget(self.data_edit_btn)


        self.verticalLayout_14.addWidget(self.frame_7)


        self.verticalLayout_13.addWidget(self.frame_9)

        self.superior_adequar = QFrame(self.frame_3)
        self.superior_adequar.setObjectName(u"superior_adequar")
        self.superior_adequar.setMaximumSize(QSize(16777215, 50))
        self.superior_adequar.setStyleSheet(u"background-color: rgb(222, 222, 222);")
        self.superior_adequar.setFrameShape(QFrame.StyledPanel)
        self.superior_adequar.setFrameShadow(QFrame.Raised)

        self.verticalLayout_13.addWidget(self.superior_adequar)


        self.horizontalLayout_5.addWidget(self.frame_3)

        self.stackedWidget.addWidget(self.data_view_pg)
        self.data_change_pg1 = QWidget()
        self.data_change_pg1.setObjectName(u"data_change_pg1")
        self.horizontalLayout_7 = QHBoxLayout(self.data_change_pg1)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.data_chance_title_grid = QFrame(self.data_change_pg1)
        self.data_chance_title_grid.setObjectName(u"data_chance_title_grid")
        self.data_chance_title_grid.setMinimumSize(QSize(350, 0))
        self.data_chance_title_grid.setFrameShape(QFrame.StyledPanel)
        self.data_chance_title_grid.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.data_chance_title_grid)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.data_change_txt_grid = QFrame(self.data_chance_title_grid)
        self.data_change_txt_grid.setObjectName(u"data_change_txt_grid")
        self.data_change_txt_grid.setMaximumSize(QSize(16777215, 50))
        self.data_change_txt_grid.setFrameShape(QFrame.StyledPanel)
        self.data_change_txt_grid.setFrameShadow(QFrame.Raised)
        self.verticalLayout_25 = QVBoxLayout(self.data_change_txt_grid)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.verticalLayout_25.setContentsMargins(40, -1, -1, 0)
        self.meus_dados_text2 = QLabel(self.data_change_txt_grid)
        self.meus_dados_text2.setObjectName(u"meus_dados_text2")
        self.meus_dados_text2.setFont(font3)

        self.verticalLayout_25.addWidget(self.meus_dados_text2)


        self.verticalLayout_18.addWidget(self.data_change_txt_grid)

        self.data_chance_icon_grid = QFrame(self.data_chance_title_grid)
        self.data_chance_icon_grid.setObjectName(u"data_chance_icon_grid")
        self.data_chance_icon_grid.setFrameShape(QFrame.StyledPanel)
        self.data_chance_icon_grid.setFrameShadow(QFrame.Raised)
        self.verticalLayout_26 = QVBoxLayout(self.data_chance_icon_grid)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.user_icon2 = QLabel(self.data_chance_icon_grid)
        self.user_icon2.setObjectName(u"user_icon2")
        self.user_icon2.setMaximumSize(QSize(250, 250))
        self.user_icon2.setPixmap(QPixmap(u":/icons/Desing_MODERN-UI/telas_Novas_UI - (Jadson implementa\u00e7\u00e3o)/telas e icons/icons/Bianca/Icones e Imagens/IconeFotoFuncionarioAmpliada.svg"))
        self.user_icon2.setScaledContents(True)
        self.user_icon2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_26.addWidget(self.user_icon2)


        self.verticalLayout_18.addWidget(self.data_chance_icon_grid)


        self.horizontalLayout_7.addWidget(self.data_chance_title_grid)

        self.user_data_change_grid = QFrame(self.data_change_pg1)
        self.user_data_change_grid.setObjectName(u"user_data_change_grid")
        self.user_data_change_grid.setFrameShape(QFrame.StyledPanel)
        self.user_data_change_grid.setFrameShadow(QFrame.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.user_data_change_grid)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.superior_adequar_2 = QFrame(self.user_data_change_grid)
        self.superior_adequar_2.setObjectName(u"superior_adequar_2")
        self.superior_adequar_2.setMaximumSize(QSize(16777215, 50))
        self.superior_adequar_2.setFrameShape(QFrame.StyledPanel)
        self.superior_adequar_2.setFrameShadow(QFrame.Raised)

        self.verticalLayout_19.addWidget(self.superior_adequar_2)

        self.change_grid = QFrame(self.user_data_change_grid)
        self.change_grid.setObjectName(u"change_grid")
        self.change_grid.setMinimumSize(QSize(623, 457))
        self.change_grid.setMaximumSize(QSize(623, 457))
        self.change_grid.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 25px;\n"
"border-style: outset;\n"
"")
        self.change_grid.setFrameShape(QFrame.StyledPanel)
        self.change_grid.setFrameShadow(QFrame.Raised)
        self.verticalLayout_20 = QVBoxLayout(self.change_grid)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.user_name_email_grid = QFrame(self.change_grid)
        self.user_name_email_grid.setObjectName(u"user_name_email_grid")
        self.user_name_email_grid.setMinimumSize(QSize(601, 96))
        self.user_name_email_grid.setMaximumSize(QSize(601, 96))
        self.user_name_email_grid.setFrameShape(QFrame.StyledPanel)
        self.user_name_email_grid.setFrameShadow(QFrame.Raised)
        self.verticalLayout_21 = QVBoxLayout(self.user_name_email_grid)
        self.verticalLayout_21.setSpacing(10)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(30, 0, 30, 0)
        self.lineEdit = QLineEdit(self.user_name_email_grid)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(0, 35))
        font6 = QFont()
        font6.setFamily(u"Lucida Console")
        font6.setPointSize(12)
        font6.setBold(False)
        font6.setWeight(50)
        self.lineEdit.setFont(font6)
        self.lineEdit.setStyleSheet(u"background-color: rgb(244, 247, 248);\n"
"border-radius: 10px;\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-color: rgb(120, 120, 120);")
        self.lineEdit.setAlignment(Qt.AlignCenter)

        self.verticalLayout_21.addWidget(self.lineEdit)

        self.lineEdit_2 = QLineEdit(self.user_name_email_grid)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setMinimumSize(QSize(0, 35))
        self.lineEdit_2.setFont(font6)
        self.lineEdit_2.setStyleSheet(u"background-color: rgb(244, 247, 248);\n"
"border-radius: 10px;\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-color: rgb(120, 120, 120);")
        self.lineEdit_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_21.addWidget(self.lineEdit_2)

        self.lineEdit_2.raise_()
        self.lineEdit.raise_()

        self.verticalLayout_20.addWidget(self.user_name_email_grid)

        self.frame_23 = QFrame(self.change_grid)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setMinimumSize(QSize(601, 97))
        self.frame_23.setMaximumSize(QSize(601, 97))
        self.frame_23.setFrameShape(QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_23)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.frame_21 = QFrame(self.frame_23)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.verticalLayout_22 = QVBoxLayout(self.frame_21)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.label_7 = QLabel(self.frame_21)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font5)

        self.verticalLayout_22.addWidget(self.label_7, 0, Qt.AlignLeft)


        self.horizontalLayout_8.addWidget(self.frame_21)

        self.frame_17 = QFrame(self.frame_23)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.verticalLayout_27 = QVBoxLayout(self.frame_17)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.data_alterar_senha_btn = QPushButton(self.frame_17)
        self.data_alterar_senha_btn.setObjectName(u"data_alterar_senha_btn")
        self.data_alterar_senha_btn.setMinimumSize(QSize(180, 40))
        self.data_alterar_senha_btn.setMaximumSize(QSize(180, 16777215))
        font7 = QFont()
        font7.setFamily(u"Lucida Console")
        font7.setPointSize(14)
        font7.setBold(True)
        font7.setWeight(75)
        self.data_alterar_senha_btn.setFont(font7)
        self.data_alterar_senha_btn.setStyleSheet(u"background-color: rgb(13, 28, 122);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-color: rgb(120, 120, 120);")

        self.verticalLayout_27.addWidget(self.data_alterar_senha_btn)


        self.horizontalLayout_8.addWidget(self.frame_17, 0, Qt.AlignRight)


        self.verticalLayout_20.addWidget(self.frame_23)

        self.frame_24 = QFrame(self.change_grid)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setMinimumSize(QSize(601, 125))
        self.frame_24.setMaximumSize(QSize(601, 125))
        self.frame_24.setFrameShape(QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QFrame.Raised)
        self.verticalLayout_23 = QVBoxLayout(self.frame_24)
        self.verticalLayout_23.setSpacing(15)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.verticalLayout_23.setContentsMargins(30, 0, 30, 0)

        self.verticalLayout_20.addWidget(self.frame_24)

        self.frame_25 = QFrame(self.change_grid)
        self.frame_25.setObjectName(u"frame_25")
        self.frame_25.setMinimumSize(QSize(601, 96))
        self.frame_25.setMaximumSize(QSize(601, 96))
        self.frame_25.setFrameShape(QFrame.StyledPanel)
        self.frame_25.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_25)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(120, 0, 120, 10)
        self.data_salvar_btn1 = QPushButton(self.frame_25)
        self.data_salvar_btn1.setObjectName(u"data_salvar_btn1")
        self.data_salvar_btn1.setMinimumSize(QSize(0, 40))
        self.data_salvar_btn1.setMaximumSize(QSize(250, 40))
        self.data_salvar_btn1.setFont(font7)
        self.data_salvar_btn1.setStyleSheet(u"background-color: rgb(152, 4, 39);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-color: rgb(120, 120, 120);")

        self.horizontalLayout_9.addWidget(self.data_salvar_btn1)


        self.verticalLayout_20.addWidget(self.frame_25)


        self.verticalLayout_19.addWidget(self.change_grid, 0, Qt.AlignVCenter)

        self.inferior_adequar = QFrame(self.user_data_change_grid)
        self.inferior_adequar.setObjectName(u"inferior_adequar")
        self.inferior_adequar.setMaximumSize(QSize(16777215, 50))
        self.inferior_adequar.setFrameShape(QFrame.StyledPanel)
        self.inferior_adequar.setFrameShadow(QFrame.Raised)

        self.verticalLayout_19.addWidget(self.inferior_adequar)


        self.horizontalLayout_7.addWidget(self.user_data_change_grid)

        self.stackedWidget.addWidget(self.data_change_pg1)
        self.data_change_pg2 = QWidget()
        self.data_change_pg2.setObjectName(u"data_change_pg2")
        self.horizontalLayout_12 = QHBoxLayout(self.data_change_pg2)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.frame_5 = QFrame(self.data_change_pg2)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMinimumSize(QSize(350, 0))
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_33 = QVBoxLayout(self.frame_5)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.data_change_txt_grid_2 = QFrame(self.frame_5)
        self.data_change_txt_grid_2.setObjectName(u"data_change_txt_grid_2")
        self.data_change_txt_grid_2.setMaximumSize(QSize(16777215, 50))
        self.data_change_txt_grid_2.setFrameShape(QFrame.StyledPanel)
        self.data_change_txt_grid_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_34 = QVBoxLayout(self.data_change_txt_grid_2)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.verticalLayout_34.setContentsMargins(40, -1, -1, 0)
        self.meus_dados_text2_2 = QLabel(self.data_change_txt_grid_2)
        self.meus_dados_text2_2.setObjectName(u"meus_dados_text2_2")
        self.meus_dados_text2_2.setFont(font3)

        self.verticalLayout_34.addWidget(self.meus_dados_text2_2)


        self.verticalLayout_33.addWidget(self.data_change_txt_grid_2)

        self.data_chance_icon_grid_2 = QFrame(self.frame_5)
        self.data_chance_icon_grid_2.setObjectName(u"data_chance_icon_grid_2")
        self.data_chance_icon_grid_2.setFrameShape(QFrame.StyledPanel)
        self.data_chance_icon_grid_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_35 = QVBoxLayout(self.data_chance_icon_grid_2)
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.user_icon2_2 = QLabel(self.data_chance_icon_grid_2)
        self.user_icon2_2.setObjectName(u"user_icon2_2")
        self.user_icon2_2.setMaximumSize(QSize(250, 250))
        self.user_icon2_2.setPixmap(QPixmap(u":/icons/Desing_MODERN-UI/telas_Novas_UI - (Jadson implementa\u00e7\u00e3o)/telas e icons/icons/Bianca/Icones e Imagens/IconeFotoFuncionarioAmpliada.svg"))
        self.user_icon2_2.setScaledContents(True)
        self.user_icon2_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_35.addWidget(self.user_icon2_2)


        self.verticalLayout_33.addWidget(self.data_chance_icon_grid_2)


        self.horizontalLayout_12.addWidget(self.frame_5)

        self.frame_26 = QFrame(self.data_change_pg2)
        self.frame_26.setObjectName(u"frame_26")
        self.frame_26.setFrameShape(QFrame.StyledPanel)
        self.frame_26.setFrameShadow(QFrame.Raised)
        self.verticalLayout_24 = QVBoxLayout(self.frame_26)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.superior_adequar_3 = QFrame(self.frame_26)
        self.superior_adequar_3.setObjectName(u"superior_adequar_3")
        self.superior_adequar_3.setMaximumSize(QSize(16777215, 50))
        self.superior_adequar_3.setFrameShape(QFrame.StyledPanel)
        self.superior_adequar_3.setFrameShadow(QFrame.Raised)

        self.verticalLayout_24.addWidget(self.superior_adequar_3)

        self.frame_27 = QFrame(self.frame_26)
        self.frame_27.setObjectName(u"frame_27")
        self.frame_27.setMinimumSize(QSize(623, 457))
        self.frame_27.setMaximumSize(QSize(623, 457))
        self.frame_27.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 25px;\n"
"border-style: outset;\n"
"")
        self.frame_27.setFrameShape(QFrame.StyledPanel)
        self.frame_27.setFrameShadow(QFrame.Raised)
        self.verticalLayout_28 = QVBoxLayout(self.frame_27)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.frame_28 = QFrame(self.frame_27)
        self.frame_28.setObjectName(u"frame_28")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.frame_28.sizePolicy().hasHeightForWidth())
        self.frame_28.setSizePolicy(sizePolicy2)
        self.frame_28.setMinimumSize(QSize(601, 96))
        self.frame_28.setMaximumSize(QSize(601, 96))
        self.frame_28.setFrameShape(QFrame.StyledPanel)
        self.frame_28.setFrameShadow(QFrame.Raised)
        self.verticalLayout_29 = QVBoxLayout(self.frame_28)
        self.verticalLayout_29.setSpacing(10)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.verticalLayout_29.setContentsMargins(30, 0, 30, 0)
        self.lineEdit_6 = QLineEdit(self.frame_28)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        self.lineEdit_6.setMinimumSize(QSize(0, 35))
        font8 = QFont()
        font8.setFamily(u"Lucida Console")
        font8.setPointSize(12)
        self.lineEdit_6.setFont(font8)
        self.lineEdit_6.setStyleSheet(u"background-color: rgb(244, 247, 248);\n"
"border-radius: 10px;\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-color: rgb(120, 120, 120);")
        self.lineEdit_6.setAlignment(Qt.AlignCenter)

        self.verticalLayout_29.addWidget(self.lineEdit_6)

        self.lineEdit_7 = QLineEdit(self.frame_28)
        self.lineEdit_7.setObjectName(u"lineEdit_7")
        self.lineEdit_7.setMinimumSize(QSize(0, 35))
        self.lineEdit_7.setFont(font8)
        self.lineEdit_7.setStyleSheet(u"background-color: rgb(244, 247, 248);\n"
"border-radius: 10px;\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-color: rgb(120, 120, 120);")
        self.lineEdit_7.setAlignment(Qt.AlignCenter)

        self.verticalLayout_29.addWidget(self.lineEdit_7)


        self.verticalLayout_28.addWidget(self.frame_28)

        self.frame_29 = QFrame(self.frame_27)
        self.frame_29.setObjectName(u"frame_29")
        self.frame_29.setMinimumSize(QSize(601, 97))
        self.frame_29.setMaximumSize(QSize(601, 97))
        self.frame_29.setFrameShape(QFrame.StyledPanel)
        self.frame_29.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_29)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.frame_30 = QFrame(self.frame_29)
        self.frame_30.setObjectName(u"frame_30")
        self.frame_30.setFrameShape(QFrame.StyledPanel)
        self.frame_30.setFrameShadow(QFrame.Raised)
        self.verticalLayout_30 = QVBoxLayout(self.frame_30)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.label_8 = QLabel(self.frame_30)
        self.label_8.setObjectName(u"label_8")
        font9 = QFont()
        font9.setFamily(u"Lucida Console")
        font9.setPointSize(14)
        self.label_8.setFont(font9)

        self.verticalLayout_30.addWidget(self.label_8, 0, Qt.AlignLeft)


        self.horizontalLayout_10.addWidget(self.frame_30)

        self.frame_31 = QFrame(self.frame_29)
        self.frame_31.setObjectName(u"frame_31")
        self.frame_31.setFrameShape(QFrame.StyledPanel)
        self.frame_31.setFrameShadow(QFrame.Raised)
        self.verticalLayout_31 = QVBoxLayout(self.frame_31)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.pushButton_12 = QPushButton(self.frame_31)
        self.pushButton_12.setObjectName(u"pushButton_12")
        self.pushButton_12.setMinimumSize(QSize(180, 40))
        self.pushButton_12.setMaximumSize(QSize(180, 16777215))
        self.pushButton_12.setFont(font7)
        self.pushButton_12.setStyleSheet(u"background-color: rgb(13, 28, 122);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-color: rgb(120, 120, 120);")

        self.verticalLayout_31.addWidget(self.pushButton_12)


        self.horizontalLayout_10.addWidget(self.frame_31, 0, Qt.AlignRight)


        self.verticalLayout_28.addWidget(self.frame_29)

        self.frame_32 = QFrame(self.frame_27)
        self.frame_32.setObjectName(u"frame_32")
        self.frame_32.setMinimumSize(QSize(601, 125))
        self.frame_32.setMaximumSize(QSize(601, 125))
        self.frame_32.setFrameShape(QFrame.StyledPanel)
        self.frame_32.setFrameShadow(QFrame.Raised)
        self.verticalLayout_32 = QVBoxLayout(self.frame_32)
        self.verticalLayout_32.setSpacing(10)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.verticalLayout_32.setContentsMargins(30, 0, 30, 0)
        self.lineEdit_8 = QLineEdit(self.frame_32)
        self.lineEdit_8.setObjectName(u"lineEdit_8")
        self.lineEdit_8.setMinimumSize(QSize(0, 35))
        self.lineEdit_8.setFont(font8)
        self.lineEdit_8.setStyleSheet(u"background-color: rgb(244, 247, 248);\n"
"border-radius: 10px;\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-color: rgb(120, 120, 120);")
        self.lineEdit_8.setEchoMode(QLineEdit.Password)
        self.lineEdit_8.setAlignment(Qt.AlignCenter)

        self.verticalLayout_32.addWidget(self.lineEdit_8)

        self.lineEdit_9 = QLineEdit(self.frame_32)
        self.lineEdit_9.setObjectName(u"lineEdit_9")
        self.lineEdit_9.setMinimumSize(QSize(0, 35))
        self.lineEdit_9.setFont(font8)
        self.lineEdit_9.setStyleSheet(u"background-color: rgb(244, 247, 248);\n"
"border-radius: 10px;\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-color: rgb(120, 120, 120);")
        self.lineEdit_9.setEchoMode(QLineEdit.Password)
        self.lineEdit_9.setAlignment(Qt.AlignCenter)

        self.verticalLayout_32.addWidget(self.lineEdit_9)

        self.lineEdit_10 = QLineEdit(self.frame_32)
        self.lineEdit_10.setObjectName(u"lineEdit_10")
        self.lineEdit_10.setMinimumSize(QSize(0, 35))
        self.lineEdit_10.setFont(font8)
        self.lineEdit_10.setStyleSheet(u"background-color: rgb(244, 247, 248);\n"
"border-radius: 10px;\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-color: rgb(120, 120, 120);")
        self.lineEdit_10.setEchoMode(QLineEdit.Password)
        self.lineEdit_10.setAlignment(Qt.AlignCenter)

        self.verticalLayout_32.addWidget(self.lineEdit_10)


        self.verticalLayout_28.addWidget(self.frame_32)

        self.frame_33 = QFrame(self.frame_27)
        self.frame_33.setObjectName(u"frame_33")
        self.frame_33.setMinimumSize(QSize(601, 96))
        self.frame_33.setMaximumSize(QSize(601, 96))
        self.frame_33.setFrameShape(QFrame.StyledPanel)
        self.frame_33.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_33)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(120, 0, 120, 10)
        self.data_salvar_btn2 = QPushButton(self.frame_33)
        self.data_salvar_btn2.setObjectName(u"data_salvar_btn2")
        self.data_salvar_btn2.setMinimumSize(QSize(0, 40))
        self.data_salvar_btn2.setMaximumSize(QSize(250, 40))
        self.data_salvar_btn2.setFont(font7)
        self.data_salvar_btn2.setStyleSheet(u"background-color: rgb(152, 4, 39);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-color: rgb(120, 120, 120);")

        self.horizontalLayout_11.addWidget(self.data_salvar_btn2)


        self.verticalLayout_28.addWidget(self.frame_33)


        self.verticalLayout_24.addWidget(self.frame_27, 0, Qt.AlignVCenter)

        self.inferior_adequar_2 = QFrame(self.frame_26)
        self.inferior_adequar_2.setObjectName(u"inferior_adequar_2")
        self.inferior_adequar_2.setMaximumSize(QSize(16777215, 50))
        self.inferior_adequar_2.setFrameShape(QFrame.StyledPanel)
        self.inferior_adequar_2.setFrameShadow(QFrame.Raised)

        self.verticalLayout_24.addWidget(self.inferior_adequar_2)


        self.horizontalLayout_12.addWidget(self.frame_26)

        self.stackedWidget.addWidget(self.data_change_pg2)
        self.user_marcaponto_pg = QWidget()
        self.user_marcaponto_pg.setObjectName(u"user_marcaponto_pg")
        self.horizontalLayout_13 = QHBoxLayout(self.user_marcaponto_pg)
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.frame_35 = QFrame(self.user_marcaponto_pg)
        self.frame_35.setObjectName(u"frame_35")
        self.frame_35.setStyleSheet(u"")
        self.frame_35.setFrameShape(QFrame.StyledPanel)
        self.frame_35.setFrameShadow(QFrame.Raised)
        self.verticalLayout_40 = QVBoxLayout(self.frame_35)
        self.verticalLayout_40.setSpacing(0)
        self.verticalLayout_40.setObjectName(u"verticalLayout_40")
        self.verticalLayout_40.setContentsMargins(50, 50, 50, 50)
        self.info_bar_grid = QFrame(self.frame_35)
        self.info_bar_grid.setObjectName(u"info_bar_grid")
        self.info_bar_grid.setMinimumSize(QSize(924, 100))
        self.info_bar_grid.setMaximumSize(QSize(924, 100))
        self.info_bar_grid.setFrameShape(QFrame.StyledPanel)
        self.info_bar_grid.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.info_bar_grid)
        self.horizontalLayout_16.setSpacing(0)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.title_marc_grid = QFrame(self.info_bar_grid)
        self.title_marc_grid.setObjectName(u"title_marc_grid")
        self.title_marc_grid.setFrameShape(QFrame.StyledPanel)
        self.title_marc_grid.setFrameShadow(QFrame.Raised)
        self.verticalLayout_43 = QVBoxLayout(self.title_marc_grid)
        self.verticalLayout_43.setSpacing(0)
        self.verticalLayout_43.setObjectName(u"verticalLayout_43")
        self.verticalLayout_43.setContentsMargins(50, 0, 0, 0)
        self.title_marc_text = QLabel(self.title_marc_grid)
        self.title_marc_text.setObjectName(u"title_marc_text")
        self.title_marc_text.setFont(font3)

        self.verticalLayout_43.addWidget(self.title_marc_text, 0, Qt.AlignTop)


        self.horizontalLayout_16.addWidget(self.title_marc_grid)

        self.func_info_grid = QFrame(self.info_bar_grid)
        self.func_info_grid.setObjectName(u"func_info_grid")
        self.func_info_grid.setMinimumSize(QSize(0, 0))
        self.func_info_grid.setMaximumSize(QSize(300, 16777215))
        self.func_info_grid.setFrameShape(QFrame.StyledPanel)
        self.func_info_grid.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.func_info_grid)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.frame_37 = QFrame(self.func_info_grid)
        self.frame_37.setObjectName(u"frame_37")
        self.frame_37.setMaximumSize(QSize(90, 16777215))
        self.frame_37.setFrameShape(QFrame.StyledPanel)
        self.frame_37.setFrameShadow(QFrame.Raised)
        self.verticalLayout_42 = QVBoxLayout(self.frame_37)
        self.verticalLayout_42.setSpacing(0)
        self.verticalLayout_42.setObjectName(u"verticalLayout_42")
        self.verticalLayout_42.setContentsMargins(0, 0, 0, 0)
        self.user_icon3 = QLabel(self.frame_37)
        self.user_icon3.setObjectName(u"user_icon3")
        self.user_icon3.setMinimumSize(QSize(75, 75))
        self.user_icon3.setMaximumSize(QSize(75, 75))
        self.user_icon3.setPixmap(QPixmap(u":/icons/Desing_MODERN-UI/telas_Novas_UI - (Jadson implementa\u00e7\u00e3o)/telas e icons/icons/Bianca/Icones e Imagens/IconeFuncionario.svg"))
        self.user_icon3.setScaledContents(True)
        self.user_icon3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_42.addWidget(self.user_icon3)


        self.horizontalLayout_15.addWidget(self.frame_37, 0, Qt.AlignHCenter)

        self.user_info = QFrame(self.func_info_grid)
        self.user_info.setObjectName(u"user_info")
        self.user_info.setFrameShape(QFrame.StyledPanel)
        self.user_info.setFrameShadow(QFrame.Raised)
        self.verticalLayout_41 = QVBoxLayout(self.user_info)
        self.verticalLayout_41.setObjectName(u"verticalLayout_41")
        self.verticalLayout_41.setContentsMargins(0, 0, 0, 0)
        self.username_txt = QLabel(self.user_info)
        self.username_txt.setObjectName(u"username_txt")
        self.username_txt.setFont(font4)

        self.verticalLayout_41.addWidget(self.username_txt)

        self.cargo_txt = QLabel(self.user_info)
        self.cargo_txt.setObjectName(u"cargo_txt")
        self.cargo_txt.setFont(font)

        self.verticalLayout_41.addWidget(self.cargo_txt)

        self.matricula_txt = QLabel(self.user_info)
        self.matricula_txt.setObjectName(u"matricula_txt")
        self.matricula_txt.setFont(font)

        self.verticalLayout_41.addWidget(self.matricula_txt)


        self.horizontalLayout_15.addWidget(self.user_info)


        self.horizontalLayout_16.addWidget(self.func_info_grid)


        self.verticalLayout_40.addWidget(self.info_bar_grid)

        self.frame_marc_grid = QFrame(self.frame_35)
        self.frame_marc_grid.setObjectName(u"frame_marc_grid")
        self.frame_marc_grid.setFrameShape(QFrame.StyledPanel)
        self.frame_marc_grid.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.frame_marc_grid)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.esq_adequar = QFrame(self.frame_marc_grid)
        self.esq_adequar.setObjectName(u"esq_adequar")
        self.esq_adequar.setMinimumSize(QSize(20, 652))
        self.esq_adequar.setMaximumSize(QSize(20, 652))
        self.esq_adequar.setFrameShape(QFrame.StyledPanel)
        self.esq_adequar.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_14.addWidget(self.esq_adequar)

        self.frame_15 = QFrame(self.frame_marc_grid)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 25px;\n"
"border-style: outset;\n"
"")
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.verticalLayout_36 = QVBoxLayout(self.frame_15)
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.frame_20 = QFrame(self.frame_15)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.verticalLayout_38 = QVBoxLayout(self.frame_20)
        self.verticalLayout_38.setObjectName(u"verticalLayout_38")
        self.label_14 = QLabel(self.frame_20)
        self.label_14.setObjectName(u"label_14")
        font10 = QFont()
        font10.setFamily(u"Lucida Console")
        font10.setPointSize(18)
        self.label_14.setFont(font10)
        self.label_14.setAlignment(Qt.AlignCenter)

        self.verticalLayout_38.addWidget(self.label_14, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.verticalLayout_36.addWidget(self.frame_20)

        self.frame_22 = QFrame(self.frame_15)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setFrameShape(QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Raised)
        self.verticalLayout_37 = QVBoxLayout(self.frame_22)
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")
        self.label_13 = QLabel(self.frame_22)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setMinimumSize(QSize(150, 150))
        font11 = QFont()
        font11.setFamily(u"Lucida Bright")
        font11.setPointSize(14)
        self.label_13.setFont(font11)
        self.label_13.setStyleSheet(u"border-radius: 60px;\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-color: rgb(16, 49, 100)")
        self.label_13.setAlignment(Qt.AlignCenter)

        self.verticalLayout_37.addWidget(self.label_13, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.verticalLayout_36.addWidget(self.frame_22)

        self.frame_34 = QFrame(self.frame_15)
        self.frame_34.setObjectName(u"frame_34")
        self.frame_34.setFont(font9)
        self.frame_34.setFrameShape(QFrame.StyledPanel)
        self.frame_34.setFrameShadow(QFrame.Raised)
        self.verticalLayout_39 = QVBoxLayout(self.frame_34)
        self.verticalLayout_39.setSpacing(0)
        self.verticalLayout_39.setObjectName(u"verticalLayout_39")
        self.verticalLayout_39.setContentsMargins(0, 25, 0, 0)
        self.pushButton_14 = QPushButton(self.frame_34)
        self.pushButton_14.setObjectName(u"pushButton_14")
        self.pushButton_14.setMinimumSize(QSize(180, 45))
        self.pushButton_14.setMaximumSize(QSize(180, 45))
        font12 = QFont()
        font12.setPointSize(14)
        self.pushButton_14.setFont(font12)
        self.pushButton_14.setStyleSheet(u"background-color: rgb(152, 4, 39);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 20px;\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-color: rgb(120, 120, 120);")

        self.verticalLayout_39.addWidget(self.pushButton_14, 0, Qt.AlignHCenter|Qt.AlignTop)


        self.verticalLayout_36.addWidget(self.frame_34)


        self.horizontalLayout_14.addWidget(self.frame_15)

        self.dir_adequar = QFrame(self.frame_marc_grid)
        self.dir_adequar.setObjectName(u"dir_adequar")
        self.dir_adequar.setMinimumSize(QSize(20, 652))
        self.dir_adequar.setMaximumSize(QSize(20, 652))
        self.dir_adequar.setFrameShape(QFrame.StyledPanel)
        self.dir_adequar.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_14.addWidget(self.dir_adequar)


        self.verticalLayout_40.addWidget(self.frame_marc_grid)


        self.horizontalLayout_13.addWidget(self.frame_35)

        self.stackedWidget.addWidget(self.user_marcaponto_pg)
        self.relatorio_fr_pg = QWidget()
        self.relatorio_fr_pg.setObjectName(u"relatorio_fr_pg")
        self.relatorio_fr_pg.setStyleSheet(u"border: none;")
        self.verticalLayout_52 = QVBoxLayout(self.relatorio_fr_pg)
        self.verticalLayout_52.setSpacing(0)
        self.verticalLayout_52.setObjectName(u"verticalLayout_52")
        self.verticalLayout_52.setContentsMargins(0, 0, 0, 0)
        self.frame_36 = QFrame(self.relatorio_fr_pg)
        self.frame_36.setObjectName(u"frame_36")
        self.frame_36.setStyleSheet(u"")
        self.frame_36.setFrameShape(QFrame.StyledPanel)
        self.frame_36.setFrameShadow(QFrame.Raised)
        self.verticalLayout_44 = QVBoxLayout(self.frame_36)
        self.verticalLayout_44.setSpacing(0)
        self.verticalLayout_44.setObjectName(u"verticalLayout_44")
        self.verticalLayout_44.setContentsMargins(50, 50, 50, 50)
        self.info_bar_grid_2 = QFrame(self.frame_36)
        self.info_bar_grid_2.setObjectName(u"info_bar_grid_2")
        self.info_bar_grid_2.setMinimumSize(QSize(924, 100))
        self.info_bar_grid_2.setMaximumSize(QSize(924, 100))
        self.info_bar_grid_2.setFrameShape(QFrame.StyledPanel)
        self.info_bar_grid_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.info_bar_grid_2)
        self.horizontalLayout_17.setSpacing(0)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.title_marc_grid_2 = QFrame(self.info_bar_grid_2)
        self.title_marc_grid_2.setObjectName(u"title_marc_grid_2")
        self.title_marc_grid_2.setFrameShape(QFrame.StyledPanel)
        self.title_marc_grid_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_45 = QVBoxLayout(self.title_marc_grid_2)
        self.verticalLayout_45.setSpacing(0)
        self.verticalLayout_45.setObjectName(u"verticalLayout_45")
        self.verticalLayout_45.setContentsMargins(50, 0, 0, 0)
        self.title_marc_text_2 = QLabel(self.title_marc_grid_2)
        self.title_marc_text_2.setObjectName(u"title_marc_text_2")
        self.title_marc_text_2.setFont(font3)

        self.verticalLayout_45.addWidget(self.title_marc_text_2, 0, Qt.AlignTop)


        self.horizontalLayout_17.addWidget(self.title_marc_grid_2)

        self.func_info_grid_2 = QFrame(self.info_bar_grid_2)
        self.func_info_grid_2.setObjectName(u"func_info_grid_2")
        self.func_info_grid_2.setMinimumSize(QSize(0, 0))
        self.func_info_grid_2.setMaximumSize(QSize(300, 16777215))
        self.func_info_grid_2.setFrameShape(QFrame.StyledPanel)
        self.func_info_grid_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.func_info_grid_2)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.frame_38 = QFrame(self.func_info_grid_2)
        self.frame_38.setObjectName(u"frame_38")
        self.frame_38.setMaximumSize(QSize(90, 16777215))
        self.frame_38.setFrameShape(QFrame.StyledPanel)
        self.frame_38.setFrameShadow(QFrame.Raised)
        self.verticalLayout_46 = QVBoxLayout(self.frame_38)
        self.verticalLayout_46.setSpacing(0)
        self.verticalLayout_46.setObjectName(u"verticalLayout_46")
        self.verticalLayout_46.setContentsMargins(0, 0, 0, 0)
        self.user_icon3_2 = QLabel(self.frame_38)
        self.user_icon3_2.setObjectName(u"user_icon3_2")
        self.user_icon3_2.setMinimumSize(QSize(75, 75))
        self.user_icon3_2.setMaximumSize(QSize(75, 75))
        self.user_icon3_2.setPixmap(QPixmap(u":/icons/Desing_MODERN-UI/telas_Novas_UI - (Jadson implementa\u00e7\u00e3o)/telas e icons/icons/Bianca/Icones e Imagens/IconeFuncionario.svg"))
        self.user_icon3_2.setScaledContents(True)
        self.user_icon3_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_46.addWidget(self.user_icon3_2)


        self.horizontalLayout_18.addWidget(self.frame_38, 0, Qt.AlignHCenter)

        self.user_info_2 = QFrame(self.func_info_grid_2)
        self.user_info_2.setObjectName(u"user_info_2")
        self.user_info_2.setFrameShape(QFrame.StyledPanel)
        self.user_info_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_47 = QVBoxLayout(self.user_info_2)
        self.verticalLayout_47.setObjectName(u"verticalLayout_47")
        self.verticalLayout_47.setContentsMargins(0, 0, 0, 0)
        self.username_txt_2 = QLabel(self.user_info_2)
        self.username_txt_2.setObjectName(u"username_txt_2")
        self.username_txt_2.setFont(font4)

        self.verticalLayout_47.addWidget(self.username_txt_2)

        self.cargo_txt_2 = QLabel(self.user_info_2)
        self.cargo_txt_2.setObjectName(u"cargo_txt_2")
        self.cargo_txt_2.setFont(font)

        self.verticalLayout_47.addWidget(self.cargo_txt_2)

        self.matricula_txt_2 = QLabel(self.user_info_2)
        self.matricula_txt_2.setObjectName(u"matricula_txt_2")
        self.matricula_txt_2.setFont(font)

        self.verticalLayout_47.addWidget(self.matricula_txt_2)


        self.horizontalLayout_18.addWidget(self.user_info_2)


        self.horizontalLayout_17.addWidget(self.func_info_grid_2)


        self.verticalLayout_44.addWidget(self.info_bar_grid_2)

        self.frame_report_date_grid = QFrame(self.frame_36)
        self.frame_report_date_grid.setObjectName(u"frame_report_date_grid")
        self.frame_report_date_grid.setFrameShape(QFrame.StyledPanel)
        self.frame_report_date_grid.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_19 = QHBoxLayout(self.frame_report_date_grid)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.esq_adequar_2 = QFrame(self.frame_report_date_grid)
        self.esq_adequar_2.setObjectName(u"esq_adequar_2")
        self.esq_adequar_2.setMinimumSize(QSize(20, 652))
        self.esq_adequar_2.setMaximumSize(QSize(20, 652))
        self.esq_adequar_2.setFrameShape(QFrame.StyledPanel)
        self.esq_adequar_2.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_19.addWidget(self.esq_adequar_2)

        self.date_report_grid = QFrame(self.frame_report_date_grid)
        self.date_report_grid.setObjectName(u"date_report_grid")
        self.date_report_grid.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 25px;\n"
"border-style: outset;\n"
"")
        self.date_report_grid.setFrameShape(QFrame.StyledPanel)
        self.date_report_grid.setFrameShadow(QFrame.Raised)
        self.verticalLayout_48 = QVBoxLayout(self.date_report_grid)
        self.verticalLayout_48.setSpacing(10)
        self.verticalLayout_48.setObjectName(u"verticalLayout_48")
        self.verticalLayout_48.setContentsMargins(100, 0, 100, 1)
        self.incial_time_grid = QFrame(self.date_report_grid)
        self.incial_time_grid.setObjectName(u"incial_time_grid")
        self.incial_time_grid.setFrameShape(QFrame.StyledPanel)
        self.incial_time_grid.setFrameShadow(QFrame.Raised)
        self.verticalLayout_49 = QVBoxLayout(self.incial_time_grid)
        self.verticalLayout_49.setObjectName(u"verticalLayout_49")
        self.frame_4 = QFrame(self.incial_time_grid)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_53 = QVBoxLayout(self.frame_4)
        self.verticalLayout_53.setObjectName(u"verticalLayout_53")
        self.label_19 = QLabel(self.frame_4)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setFont(font10)
        self.label_19.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_53.addWidget(self.label_19)


        self.verticalLayout_49.addWidget(self.frame_4)

        self.frame_8 = QFrame(self.incial_time_grid)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_20 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(0, -1, 100, -1)
        self.lineEdit_3 = QLineEdit(self.frame_8)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setMinimumSize(QSize(100, 0))
        self.lineEdit_3.setMaximumSize(QSize(100, 80))
        font13 = QFont()
        font13.setPointSize(10)
        self.lineEdit_3.setFont(font13)
        self.lineEdit_3.setStyleSheet(u"background-color: rgb(244, 247, 248);\n"
"border-radius: 10px;\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-color: rgb(120, 120, 120);")
        self.lineEdit_3.setEchoMode(QLineEdit.Password)
        self.lineEdit_3.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_20.addWidget(self.lineEdit_3)

        self.lineEdit_5 = QLineEdit(self.frame_8)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setMaximumSize(QSize(100, 80))
        self.lineEdit_5.setFont(font13)
        self.lineEdit_5.setStyleSheet(u"background-color: rgb(244, 247, 248);\n"
"border-radius: 10px;\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-color: rgb(120, 120, 120);")
        self.lineEdit_5.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_20.addWidget(self.lineEdit_5)

        self.lineEdit_11 = QLineEdit(self.frame_8)
        self.lineEdit_11.setObjectName(u"lineEdit_11")
        self.lineEdit_11.setMinimumSize(QSize(100, 20))
        self.lineEdit_11.setMaximumSize(QSize(100, 80))
        self.lineEdit_11.setFont(font13)
        self.lineEdit_11.setStyleSheet(u"background-color: rgb(244, 247, 248);\n"
"border-radius: 10px;\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-color: rgb(120, 120, 120);")
        self.lineEdit_11.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_20.addWidget(self.lineEdit_11)


        self.verticalLayout_49.addWidget(self.frame_8, 0, Qt.AlignLeft)


        self.verticalLayout_48.addWidget(self.incial_time_grid)

        self.final_time_grid = QFrame(self.date_report_grid)
        self.final_time_grid.setObjectName(u"final_time_grid")
        self.final_time_grid.setFrameShape(QFrame.StyledPanel)
        self.final_time_grid.setFrameShadow(QFrame.Raised)
        self.verticalLayout_50 = QVBoxLayout(self.final_time_grid)
        self.verticalLayout_50.setObjectName(u"verticalLayout_50")
        self.frame_43 = QFrame(self.final_time_grid)
        self.frame_43.setObjectName(u"frame_43")
        self.frame_43.setFrameShape(QFrame.StyledPanel)
        self.frame_43.setFrameShadow(QFrame.Raised)
        self.verticalLayout_54 = QVBoxLayout(self.frame_43)
        self.verticalLayout_54.setObjectName(u"verticalLayout_54")
        self.label_21 = QLabel(self.frame_43)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setFont(font10)
        self.label_21.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_54.addWidget(self.label_21)


        self.verticalLayout_50.addWidget(self.frame_43)

        self.frame_44 = QFrame(self.final_time_grid)
        self.frame_44.setObjectName(u"frame_44")
        self.frame_44.setFrameShape(QFrame.StyledPanel)
        self.frame_44.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_21 = QHBoxLayout(self.frame_44)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_21.setContentsMargins(0, -1, 0, -1)
        self.lineEdit_4 = QLineEdit(self.frame_44)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setMinimumSize(QSize(100, 0))
        self.lineEdit_4.setMaximumSize(QSize(100, 80))
        self.lineEdit_4.setFont(font13)
        self.lineEdit_4.setStyleSheet(u"background-color: rgb(244, 247, 248);\n"
"border-radius: 10px;\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-color: rgb(120, 120, 120);")
        self.lineEdit_4.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_21.addWidget(self.lineEdit_4)

        self.lineEdit_12 = QLineEdit(self.frame_44)
        self.lineEdit_12.setObjectName(u"lineEdit_12")
        self.lineEdit_12.setMinimumSize(QSize(100, 0))
        self.lineEdit_12.setMaximumSize(QSize(100, 80))
        self.lineEdit_12.setFont(font13)
        self.lineEdit_12.setStyleSheet(u"background-color: rgb(244, 247, 248);\n"
"border-radius: 10px;\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-color: rgb(120, 120, 120);")
        self.lineEdit_12.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_21.addWidget(self.lineEdit_12)

        self.lineEdit_13 = QLineEdit(self.frame_44)
        self.lineEdit_13.setObjectName(u"lineEdit_13")
        self.lineEdit_13.setMinimumSize(QSize(100, 0))
        self.lineEdit_13.setMaximumSize(QSize(100, 80))
        self.lineEdit_13.setFont(font13)
        self.lineEdit_13.setStyleSheet(u"background-color: rgb(244, 247, 248);\n"
"border-radius: 10px;\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-color: rgb(120, 120, 120);")
        self.lineEdit_13.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_21.addWidget(self.lineEdit_13)


        self.verticalLayout_50.addWidget(self.frame_44, 0, Qt.AlignLeft)


        self.verticalLayout_48.addWidget(self.final_time_grid)

        self.frame_42 = QFrame(self.date_report_grid)
        self.frame_42.setObjectName(u"frame_42")
        self.frame_42.setFont(font9)
        self.frame_42.setFrameShape(QFrame.StyledPanel)
        self.frame_42.setFrameShadow(QFrame.Raised)
        self.verticalLayout_51 = QVBoxLayout(self.frame_42)
        self.verticalLayout_51.setSpacing(0)
        self.verticalLayout_51.setObjectName(u"verticalLayout_51")
        self.verticalLayout_51.setContentsMargins(0, 25, 0, 0)
        self.pushButton_15 = QPushButton(self.frame_42)
        self.pushButton_15.setObjectName(u"pushButton_15")
        self.pushButton_15.setMinimumSize(QSize(180, 45))
        self.pushButton_15.setMaximumSize(QSize(180, 45))
        self.pushButton_15.setFont(font12)
        self.pushButton_15.setStyleSheet(u"background-color: rgb(152, 4, 39);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 20px;\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-color: rgb(120, 120, 120);")

        self.verticalLayout_51.addWidget(self.pushButton_15, 0, Qt.AlignHCenter|Qt.AlignTop)


        self.verticalLayout_48.addWidget(self.frame_42)


        self.horizontalLayout_19.addWidget(self.date_report_grid)

        self.dir_adequar_2 = QFrame(self.frame_report_date_grid)
        self.dir_adequar_2.setObjectName(u"dir_adequar_2")
        self.dir_adequar_2.setMinimumSize(QSize(20, 652))
        self.dir_adequar_2.setMaximumSize(QSize(20, 652))
        self.dir_adequar_2.setFrameShape(QFrame.StyledPanel)
        self.dir_adequar_2.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_19.addWidget(self.dir_adequar_2)


        self.verticalLayout_44.addWidget(self.frame_report_date_grid)


        self.verticalLayout_52.addWidget(self.frame_36)

        self.stackedWidget.addWidget(self.relatorio_fr_pg)
        self.Em_edicao = QWidget()
        self.Em_edicao.setObjectName(u"Em_edicao")
        self.stackedWidget.addWidget(self.Em_edicao)

        self.verticalLayout.addWidget(self.stackedWidget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_4.setText("")
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Seja Bem vindo!", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Nome do funcion\u00e1rio", None))
        self.home_btn.setText("")
        self.meus_dados1_btn.setText(QCoreApplication.translate("MainWindow", u"Meus Dados", None))
        self.marcaponto_btn1.setText(QCoreApplication.translate("MainWindow", u"Marcar Ponto", None))
        self.relatorio_btn1.setText(QCoreApplication.translate("MainWindow", u"Relat\u00f3rio", None))
        self.sair_btn.setText("")
        self.label.setText("")
        self.meus_dados2_btn.setText(QCoreApplication.translate("MainWindow", u"MEUS DADOS", None))
        self.label_2.setText("")
        self.marcaponto_btn2.setText(QCoreApplication.translate("MainWindow", u"MARCAR PONTO", None))
        self.label_3.setText("")
        self.relatorio_btn2.setText(QCoreApplication.translate("MainWindow", u"RELAT\u00d3RIO", None))
        self.meus_dados_text.setText(QCoreApplication.translate("MainWindow", u"Meus Dados", None))
        self.user_icon.setText("")
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Matr\u00edcula", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Cargo/Fun\u00e7\u00e3o", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Nome do Funcion\u00e1rio", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"E-mail", None))
        self.data_edit_btn.setText(QCoreApplication.translate("MainWindow", u"Editar", None))
        self.meus_dados_text2.setText(QCoreApplication.translate("MainWindow", u"Meus Dados", None))
        self.user_icon2.setText("")
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Nome completo", None))
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"E-mail", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Senha", None))
        self.data_alterar_senha_btn.setText(QCoreApplication.translate("MainWindow", u"Alterar", None))
        self.data_salvar_btn1.setText(QCoreApplication.translate("MainWindow", u"Salvar", None))
        self.meus_dados_text2_2.setText(QCoreApplication.translate("MainWindow", u"Meus Dados", None))
        self.user_icon2_2.setText("")
        self.lineEdit_6.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Nome completo", None))
        self.lineEdit_7.setPlaceholderText(QCoreApplication.translate("MainWindow", u"E-mail", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Senha", None))
        self.pushButton_12.setText(QCoreApplication.translate("MainWindow", u"Alterar", None))
        self.lineEdit_8.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Senha atual", None))
        self.lineEdit_9.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Senha nova", None))
        self.lineEdit_10.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Confirar senha", None))
        self.data_salvar_btn2.setText(QCoreApplication.translate("MainWindow", u"Salvar", None))
        self.title_marc_text.setText(QCoreApplication.translate("MainWindow", u"Marca\u00e7\u00e3o de Ponto", None))
        self.user_icon3.setText("")
        self.username_txt.setText(QCoreApplication.translate("MainWindow", u"Nome do funcion\u00e1rio", None))
        self.cargo_txt.setText(QCoreApplication.translate("MainWindow", u"Cargo", None))
        self.matricula_txt.setText(QCoreApplication.translate("MainWindow", u"Matr\u00edcula", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Dia da semana, DD/MM/AAAA", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"data", None))
        self.pushButton_14.setText(QCoreApplication.translate("MainWindow", u"Marcar Ponto", None))
        self.title_marc_text_2.setText(QCoreApplication.translate("MainWindow", u"Relat\u00f3rio de Frequ\u00eancia", None))
        self.user_icon3_2.setText("")
        self.username_txt_2.setText(QCoreApplication.translate("MainWindow", u"Nome do funcion\u00e1rio", None))
        self.cargo_txt_2.setText(QCoreApplication.translate("MainWindow", u"Cargo", None))
        self.matricula_txt_2.setText(QCoreApplication.translate("MainWindow", u"Matr\u00edcula", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Per\u00edodo inicial", None))
        self.lineEdit_3.setPlaceholderText(QCoreApplication.translate("MainWindow", u"DD", None))
        self.lineEdit_5.setPlaceholderText(QCoreApplication.translate("MainWindow", u"MM", None))
        self.lineEdit_11.setPlaceholderText(QCoreApplication.translate("MainWindow", u"AAAA", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Per\u00edodo final", None))
        self.lineEdit_4.setPlaceholderText(QCoreApplication.translate("MainWindow", u"DD", None))
        self.lineEdit_12.setPlaceholderText(QCoreApplication.translate("MainWindow", u"MM", None))
        self.lineEdit_13.setPlaceholderText(QCoreApplication.translate("MainWindow", u"AAAA", None))
        self.pushButton_15.setText(QCoreApplication.translate("MainWindow", u"Gerar", None))
    # retranslateUi

