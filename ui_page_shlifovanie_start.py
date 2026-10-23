# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_page_shlifovanie_start.ui'
##
## Created by: Qt User Interface Compiler version 6.11.1
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
from PySide6.QtWidgets import (QApplication, QDoubleSpinBox, QGroupBox, QHBoxLayout,
    QHeaderView, QLabel, QLayout, QPushButton,
    QSizePolicy, QSpacerItem, QSpinBox, QStackedWidget,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)
import res_rc

class Ui_ShlifovanieStart(object):
    def setupUi(self, ShlifovanieStart):
        if not ShlifovanieStart.objectName():
            ShlifovanieStart.setObjectName(u"ShlifovanieStart")
        ShlifovanieStart.resize(1164, 680)
        ShlifovanieStart.setStyleSheet(u"color: white;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0, stop:0 rgba(20, 40, 80, 255), stop:1 rgba(39, 73, 109, 255));\n"
"")
        self.verticalLayout = QVBoxLayout(ShlifovanieStart)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, 0, -1, -1)
        self.btn_home = QPushButton(ShlifovanieStart)
        self.btn_home.setObjectName(u"btn_home")
        font = QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.btn_home.setFont(font)
        self.btn_home.setStyleSheet(u"QPushButton {\n"
"	border-bottom: 1px solid white;\n"
"	height: 30px;\n"
"	background-color: rgba(0,0,0,0);\n"
"	padding: 5 20 5 5\n"
"\n"
"}\n"
"QPushButton:hover {\n"
"	border-radius: 10px;\n"
"	border: none;\n"
"	border-left: 1px solid rgb(58, 170, 255);\n"
"	background-color: qlineargradient(spread:pad, x1:1, y1:0.506, x2:0.517045, y2:0.528, stop:0.0340909 rgba(15, 109, 159, 0), stop:1 rgba(15, 109, 159, 64))\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: rgb(0, 53, 93)\n"
"}")
        icon = QIcon()
        icon.addFile(u":/icons/back2.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_home.setIcon(icon)
        self.btn_home.setIconSize(QSize(20, 20))

        self.horizontalLayout.addWidget(self.btn_home, 0, Qt.AlignmentFlag.AlignLeft)

        self.pushButton = QPushButton(ShlifovanieStart)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setStyleSheet(u"background: rgba(0, 0, 0, 0);")
        icon1 = QIcon()
        icon1.addFile(u":/icons/logo_cut.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton.setIcon(icon1)
        self.pushButton.setIconSize(QSize(50, 50))

        self.horizontalLayout.addWidget(self.pushButton, 0, Qt.AlignmentFlag.AlignRight)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.main = QWidget(ShlifovanieStart)
        self.main.setObjectName(u"main")
        self.main.setStyleSheet(u"#main {\n"
"border: none;\n"
"border-radius: 15px;\n"
"background: none;\n"
"}")
        self.verticalLayout_10 = QVBoxLayout(self.main)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(1, 1, 1, 1)
        self.label_7 = QLabel(self.main)
        self.label_7.setObjectName(u"label_7")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(3)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        font1 = QFont()
        font1.setWeight(QFont.DemiBold)
        self.label_7.setFont(font1)
        self.label_7.setStyleSheet(u"background-color: none;\n"
"color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(12, 123, 147, 255), stop:1 rgba(0, 168, 204, 255));\n"
"font-size: 28px;\n"
"font-weight: 600;\n"
"border: none;\n"
"width: 300px;\n"
"\n"
"")
        self.label_7.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_10.addWidget(self.label_7)

        self.group_value_start_2 = QWidget(self.main)
        self.group_value_start_2.setObjectName(u"group_value_start_2")
        self.group_value_start_2.setMouseTracking(True)
        self.group_value_start_2.setTabletTracking(False)
        self.group_value_start_2.setAutoFillBackground(False)
        self.group_value_start_2.setStyleSheet(u"QWidget { \n"
"	border: none;\n"
"	background: none;\n"
"}")
        self.verticalLayout_11 = QVBoxLayout(self.group_value_start_2)
        self.verticalLayout_11.setSpacing(10)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(150, 10, 150, 0)
        self.label_2 = QLabel(self.group_value_start_2)
        self.label_2.setObjectName(u"label_2")
        font2 = QFont()
        font2.setFamilies([u"Segoe UI Light"])
        font2.setPointSize(10)
        font2.setBold(False)
        self.label_2.setFont(font2)
        self.label_2.setStyleSheet(u"QLabel {\n"
"	background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(12, 123, 147, 255), stop:1 rgba(0, 168, 204, 255));\n"
"	padding-left: 2px;	\n"
"	color: rgb(24, 45, 76)\n"
"}\n"
"")

        self.verticalLayout_11.addWidget(self.label_2)

        self.widget_2 = QWidget(self.group_value_start_2)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setStyleSheet(u"QWidget {\n"
"	background: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0, stop:0 rgba(39, 72, 109, 129), stop:1 rgba(21, 41, 81, 129))\n"
"}")
        self.verticalLayout_6 = QVBoxLayout(self.widget_2)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 15, 0, 15)
        self.groupBox = QGroupBox(self.widget_2)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setStyleSheet(u"QGroupBox {\n"
"	border: none;\n"
"	background: none;\n"
"}\n"
"QPushButton {\n"
"	background:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(12, 123, 147, 255), stop:1 rgba(0, 168, 204, 255));\n"
"	border: none;\n"
"	font-size: 11px;\n"
"	padding: 5 10 5 10;\n"
"	width: 100px;\n"
"	border: 1px solid qradialgradient(spread:pad, cx:0.506, cy:1, radius:1.147, fx:0.494318, fy:1, stop:0 rgba(12, 123, 147, 255), stop:1 rgba(255, 255, 255, 0));\n"
"}\n"
"QPushButton:hover {\n"
"	color: rgb(0, 168, 204);\n"
"	border-left: 1px solid rgb(10, 169, 255);\n"
"	border-right: 1px solid rgb(10, 169, 255);\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.477, x2:1, y2:0.518, stop:0 rgba(15, 109, 159, 64), stop:0.505682 rgba(15, 111, 149, 0), stop:1 rgba(15, 112, 139, 58));\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: rgb(0, 53, 93)\n"
"}\n"
"QPushButton:checked {\n"
"	background: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(12, 123, 147, 177), stop:"
                        "1 rgba(39, 73, 109, 255));\n"
"	color: rgb(0, 168, 204);\n"
"}")
        self.horizontalLayout_3 = QHBoxLayout(self.groupBox)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, 0, -1, 0)
        self.btn_centr = QPushButton(self.groupBox)
        self.btn_centr.setObjectName(u"btn_centr")
        font3 = QFont()
        self.btn_centr.setFont(font3)
        self.btn_centr.setStyleSheet(u"")
        self.btn_centr.setCheckable(True)
        self.btn_centr.setChecked(True)
        self.btn_centr.setAutoExclusive(True)

        self.horizontalLayout_3.addWidget(self.btn_centr, 0, Qt.AlignmentFlag.AlignHCenter)

        self.btn_patron = QPushButton(self.groupBox)
        self.btn_patron.setObjectName(u"btn_patron")
        self.btn_patron.setFont(font3)
        self.btn_patron.setStyleSheet(u"")
        self.btn_patron.setCheckable(True)
        self.btn_patron.setAutoExclusive(True)

        self.horizontalLayout_3.addWidget(self.btn_patron, 0, Qt.AlignmentFlag.AlignHCenter)

        self.btn_opravka = QPushButton(self.groupBox)
        self.btn_opravka.setObjectName(u"btn_opravka")
        self.btn_opravka.setFont(font3)
        self.btn_opravka.setStyleSheet(u"")
        self.btn_opravka.setCheckable(True)
        self.btn_opravka.setAutoExclusive(True)

        self.horizontalLayout_3.addWidget(self.btn_opravka)


        self.verticalLayout_6.addWidget(self.groupBox, 0, Qt.AlignmentFlag.AlignHCenter)


        self.verticalLayout_11.addWidget(self.widget_2)

        self.widget = QWidget(self.group_value_start_2)
        self.widget.setObjectName(u"widget")
        self.widget.setStyleSheet(u"border: none;\n"
"background: none")
        self.verticalLayout_2 = QVBoxLayout(self.widget)
        self.verticalLayout_2.setSpacing(10)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.widget_3 = QWidget(self.widget)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setStyleSheet(u"#widget_4 {\n"
"	background: none;\n"
"}")
        self.verticalLayout_7 = QVBoxLayout(self.widget_3)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 5)
        self.stackedWidget = QStackedWidget(self.widget_3)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"background: rgba(0, 0, 0, 0)")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.page.sizePolicy().hasHeightForWidth())
        self.page.setSizePolicy(sizePolicy1)
        self.verticalLayout_3 = QVBoxLayout(self.page)
        self.verticalLayout_3.setSpacing(10)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 9)
        self.label_21 = QLabel(self.page)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setFont(font2)
        self.label_21.setStyleSheet(u"QLabel {\n"
"	background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(12, 123, 147, 255), stop:1 rgba(0, 168, 204, 255));\n"
"	padding-left: 2px;	\n"
"	color: rgb(24, 45, 76)\n"
"}\n"
"")

        self.verticalLayout_3.addWidget(self.label_21)

        self.widget_6 = QWidget(self.page)
        self.widget_6.setObjectName(u"widget_6")
        self.widget_6.setStyleSheet(u"QWidget {\n"
"	background: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0, stop:0 rgba(39, 72, 109, 129), stop:1 rgba(21, 41, 81, 129))\n"
"}")
        self.verticalLayout_13 = QVBoxLayout(self.widget_6)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(-1, 0, -1, -1)
        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_7)

        self.label_9 = QLabel(self.widget_6)
        self.label_9.setObjectName(u"label_9")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Maximum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy2)
        font4 = QFont()
        font4.setPointSize(10)
        self.label_9.setFont(font4)
        self.label_9.setStyleSheet(u"background:none;\n"
"border: none")
        self.label_9.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_7.addWidget(self.label_9)

        self.d_zazhim_centr = QDoubleSpinBox(self.widget_6)
        self.d_zazhim_centr.setObjectName(u"d_zazhim_centr")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.d_zazhim_centr.sizePolicy().hasHeightForWidth())
        self.d_zazhim_centr.setSizePolicy(sizePolicy3)
        self.d_zazhim_centr.setMinimumSize(QSize(0, 30))
        self.d_zazhim_centr.setStyleSheet(u"QDoubleSpinBox {\n"
"	padding: 2 5 2 5;	\n"
"	border: none;\n"
"	border-bottom: 1px solid white;\n"
"	border-radius: 1px;\n"
"	background: rgba(255, 255, 255, 0);\n"
"	transition: color 0.3s ease;\n"
"	transition: border-bottom 0.4s ease;\n"
"	color: rgb(204, 204, 204);\n"
"	font-size: 11pt;\n"
"}\n"
"\n"
"QDoubleSpinBox:disabled {\n"
"	color: rgb(120, 106, 107);\n"
"	background: rgba(255, 255, 255, 20);\n"
"}\n"
"\n"
"QDoubleSpinBox:hover {\n"
"	color: rgb(255, 255, 255)\n"
"}\n"
"\n"
"QDoubleSpinBox:pressed {\n"
"	border-bottom: 1px solid white;\n"
"}\n"
"")
        self.d_zazhim_centr.setMaximum(10000.000000000000000)

        self.horizontalLayout_7.addWidget(self.d_zazhim_centr, 0, Qt.AlignmentFlag.AlignHCenter)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_8)


        self.verticalLayout_13.addLayout(self.horizontalLayout_7)


        self.verticalLayout_3.addWidget(self.widget_6)

        self.label_22 = QLabel(self.page)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setFont(font2)
        self.label_22.setStyleSheet(u"QLabel {\n"
"	background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(12, 123, 147, 255), stop:1 rgba(0, 168, 204, 255));\n"
"	padding-left: 2px;	\n"
"	color: rgb(24, 45, 76)\n"
"}\n"
"")

        self.verticalLayout_3.addWidget(self.label_22)

        self.widget_7 = QWidget(self.page)
        self.widget_7.setObjectName(u"widget_7")
        self.widget_7.setStyleSheet(u"QWidget {\n"
"	background: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0, stop:0 rgba(39, 72, 109, 129), stop:1 rgba(21, 41, 81, 129))\n"
"}")
        self.verticalLayout_14 = QVBoxLayout(self.widget_7)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(-1, 0, -1, -1)
        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_9)

        self.label_10 = QLabel(self.widget_7)
        self.label_10.setObjectName(u"label_10")
        sizePolicy2.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy2)
        self.label_10.setFont(font4)
        self.label_10.setStyleSheet(u"background:none;\n"
"border: none")
        self.label_10.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_8.addWidget(self.label_10)

        self.d_vist_centr = QDoubleSpinBox(self.widget_7)
        self.d_vist_centr.setObjectName(u"d_vist_centr")
        sizePolicy3.setHeightForWidth(self.d_vist_centr.sizePolicy().hasHeightForWidth())
        self.d_vist_centr.setSizePolicy(sizePolicy3)
        self.d_vist_centr.setMinimumSize(QSize(0, 30))
        self.d_vist_centr.setStyleSheet(u"QDoubleSpinBox {\n"
"	padding: 2 5 2 5;	\n"
"	border: none;\n"
"	border-bottom: 1px solid white;\n"
"	border-radius: 1px;\n"
"	background: rgba(255, 255, 255, 0);\n"
"	transition: color 0.3s ease;\n"
"	transition: border-bottom 0.4s ease;\n"
"	color: rgb(204, 204, 204);\n"
"	font-size: 11pt;\n"
"}\n"
"\n"
"QDoubleSpinBox:disabled {\n"
"	color: rgb(120, 106, 107);\n"
"	background: rgba(255, 255, 255, 20);\n"
"}\n"
"\n"
"QDoubleSpinBox:hover {\n"
"	color: rgb(255, 255, 255)\n"
"}\n"
"\n"
"QDoubleSpinBox:pressed {\n"
"	border-bottom: 1px solid white;\n"
"}\n"
"")
        self.d_vist_centr.setMaximum(10000.000000000000000)

        self.horizontalLayout_8.addWidget(self.d_vist_centr, 0, Qt.AlignmentFlag.AlignHCenter)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_10)


        self.verticalLayout_14.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(-1, 0, -1, -1)
        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_13)

        self.label_12 = QLabel(self.widget_7)
        self.label_12.setObjectName(u"label_12")
        sizePolicy2.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy2)
        self.label_12.setFont(font4)
        self.label_12.setStyleSheet(u"background:none;\n"
"border: none")
        self.label_12.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_10.addWidget(self.label_12)

        self.d_shlifovka_centr = QDoubleSpinBox(self.widget_7)
        self.d_shlifovka_centr.setObjectName(u"d_shlifovka_centr")
        sizePolicy3.setHeightForWidth(self.d_shlifovka_centr.sizePolicy().hasHeightForWidth())
        self.d_shlifovka_centr.setSizePolicy(sizePolicy3)
        self.d_shlifovka_centr.setMinimumSize(QSize(0, 30))
        self.d_shlifovka_centr.setStyleSheet(u"QDoubleSpinBox {\n"
"	padding: 2 5 2 5;	\n"
"	border: none;\n"
"	border-bottom: 1px solid white;\n"
"	border-radius: 1px;\n"
"	background: rgba(255, 255, 255, 0);\n"
"	transition: color 0.3s ease;\n"
"	transition: border-bottom 0.4s ease;\n"
"	color: rgb(204, 204, 204);\n"
"	font-size: 11pt;\n"
"}\n"
"\n"
"QDoubleSpinBox:disabled {\n"
"	color: rgb(120, 106, 107);\n"
"	background: rgba(255, 255, 255, 20);\n"
"}\n"
"\n"
"QDoubleSpinBox:hover {\n"
"	color: rgb(255, 255, 255)\n"
"}\n"
"\n"
"QDoubleSpinBox:pressed {\n"
"	border-bottom: 1px solid white;\n"
"}\n"
"")
        self.d_shlifovka_centr.setMaximum(10000.000000000000000)

        self.horizontalLayout_10.addWidget(self.d_shlifovka_centr, 0, Qt.AlignmentFlag.AlignHCenter)

        self.horizontalSpacer_14 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_14)


        self.verticalLayout_14.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(-1, 0, -1, -1)
        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_11)

        self.label_11 = QLabel(self.widget_7)
        self.label_11.setObjectName(u"label_11")
        sizePolicy2.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy2)
        self.label_11.setFont(font4)
        self.label_11.setStyleSheet(u"background:none;\n"
"border: none")
        self.label_11.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_9.addWidget(self.label_11)

        self.bienie_centr = QDoubleSpinBox(self.widget_7)
        self.bienie_centr.setObjectName(u"bienie_centr")
        sizePolicy3.setHeightForWidth(self.bienie_centr.sizePolicy().hasHeightForWidth())
        self.bienie_centr.setSizePolicy(sizePolicy3)
        self.bienie_centr.setMinimumSize(QSize(0, 30))
        self.bienie_centr.setStyleSheet(u"QDoubleSpinBox {\n"
"	padding: 2 5 2 5;	\n"
"	border: none;\n"
"	border-bottom: 1px solid white;\n"
"	border-radius: 1px;\n"
"	background: rgba(255, 255, 255, 0);\n"
"	transition: color 0.3s ease;\n"
"	transition: border-bottom 0.4s ease;\n"
"	color: rgb(204, 204, 204);\n"
"	font-size: 11pt;\n"
"}\n"
"\n"
"QDoubleSpinBox:disabled {\n"
"	color: rgb(120, 106, 107);\n"
"	background: rgba(255, 255, 255, 20);\n"
"}\n"
"\n"
"QDoubleSpinBox:hover {\n"
"	color: rgb(255, 255, 255)\n"
"}\n"
"\n"
"QDoubleSpinBox:pressed {\n"
"	border-bottom: 1px solid white;\n"
"}\n"
"")
        self.bienie_centr.setMaximum(10000.000000000000000)

        self.horizontalLayout_9.addWidget(self.bienie_centr, 0, Qt.AlignmentFlag.AlignHCenter)

        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_12)


        self.verticalLayout_14.addLayout(self.horizontalLayout_9)


        self.verticalLayout_3.addWidget(self.widget_7)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_4)

        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        sizePolicy1.setHeightForWidth(self.page_2.sizePolicy().hasHeightForWidth())
        self.page_2.setSizePolicy(sizePolicy1)
        self.verticalLayout_4 = QVBoxLayout(self.page_2)
        self.verticalLayout_4.setSpacing(10)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, -1)
        self.label_8 = QLabel(self.page_2)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font2)
        self.label_8.setStyleSheet(u"QLabel {\n"
"	background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(12, 123, 147, 255), stop:1 rgba(0, 168, 204, 255));\n"
"	padding-left: 2px;	\n"
"	color: rgb(24, 45, 76)\n"
"}\n"
"")

        self.verticalLayout_4.addWidget(self.label_8)

        self.widget_8 = QWidget(self.page_2)
        self.widget_8.setObjectName(u"widget_8")
        self.widget_8.setStyleSheet(u"QWidget {\n"
"	background: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0, stop:0 rgba(39, 72, 109, 129), stop:1 rgba(21, 41, 81, 129))\n"
"}")
        self.verticalLayout_15 = QVBoxLayout(self.widget_8)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(-1, 0, -1, -1)
        self.horizontalSpacer_17 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_17)

        self.label_14 = QLabel(self.widget_8)
        self.label_14.setObjectName(u"label_14")
        sizePolicy2.setHeightForWidth(self.label_14.sizePolicy().hasHeightForWidth())
        self.label_14.setSizePolicy(sizePolicy2)
        self.label_14.setFont(font4)
        self.label_14.setStyleSheet(u"background:none;\n"
"border: none")
        self.label_14.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_12.addWidget(self.label_14)

        self.d_zazhim_patron = QDoubleSpinBox(self.widget_8)
        self.d_zazhim_patron.setObjectName(u"d_zazhim_patron")
        sizePolicy3.setHeightForWidth(self.d_zazhim_patron.sizePolicy().hasHeightForWidth())
        self.d_zazhim_patron.setSizePolicy(sizePolicy3)
        self.d_zazhim_patron.setMinimumSize(QSize(0, 30))
        self.d_zazhim_patron.setStyleSheet(u"QDoubleSpinBox {\n"
"	padding: 2 5 2 5;	\n"
"	border: none;\n"
"	border-bottom: 1px solid white;\n"
"	border-radius: 1px;\n"
"	background: rgba(255, 255, 255, 0);\n"
"	transition: color 0.3s ease;\n"
"	transition: border-bottom 0.4s ease;\n"
"	color: rgb(204, 204, 204);\n"
"	font-size: 11pt;\n"
"}\n"
"\n"
"QDoubleSpinBox:disabled {\n"
"	color: rgb(120, 106, 107);\n"
"	background: rgba(255, 255, 255, 20);\n"
"}\n"
"\n"
"QDoubleSpinBox:hover {\n"
"	color: rgb(255, 255, 255)\n"
"}\n"
"\n"
"QDoubleSpinBox:pressed {\n"
"	border-bottom: 1px solid white;\n"
"}\n"
"")
        self.d_zazhim_patron.setMaximum(10000.000000000000000)

        self.horizontalLayout_12.addWidget(self.d_zazhim_patron, 0, Qt.AlignmentFlag.AlignHCenter)

        self.horizontalSpacer_18 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_18)


        self.verticalLayout_15.addLayout(self.horizontalLayout_12)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(-1, 0, -1, -1)
        self.horizontalSpacer_19 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_19)

        self.label_15 = QLabel(self.widget_8)
        self.label_15.setObjectName(u"label_15")
        sizePolicy2.setHeightForWidth(self.label_15.sizePolicy().hasHeightForWidth())
        self.label_15.setSizePolicy(sizePolicy2)
        self.label_15.setFont(font4)
        self.label_15.setStyleSheet(u"background:none;\n"
"border: none")
        self.label_15.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_13.addWidget(self.label_15)

        self.length_zazhim_patron = QDoubleSpinBox(self.widget_8)
        self.length_zazhim_patron.setObjectName(u"length_zazhim_patron")
        sizePolicy3.setHeightForWidth(self.length_zazhim_patron.sizePolicy().hasHeightForWidth())
        self.length_zazhim_patron.setSizePolicy(sizePolicy3)
        self.length_zazhim_patron.setMinimumSize(QSize(0, 30))
        self.length_zazhim_patron.setStyleSheet(u"QDoubleSpinBox {\n"
"	padding: 2 5 2 5;	\n"
"	border: none;\n"
"	border-bottom: 1px solid white;\n"
"	border-radius: 1px;\n"
"	background: rgba(255, 255, 255, 0);\n"
"	transition: color 0.3s ease;\n"
"	transition: border-bottom 0.4s ease;\n"
"	color: rgb(204, 204, 204);\n"
"	font-size: 11pt;\n"
"}\n"
"\n"
"QDoubleSpinBox:disabled {\n"
"	color: rgb(120, 106, 107);\n"
"	background: rgba(255, 255, 255, 20);\n"
"}\n"
"\n"
"QDoubleSpinBox:hover {\n"
"	color: rgb(255, 255, 255)\n"
"}\n"
"\n"
"QDoubleSpinBox:pressed {\n"
"	border-bottom: 1px solid white;\n"
"}\n"
"")
        self.length_zazhim_patron.setMaximum(10000.000000000000000)

        self.horizontalLayout_13.addWidget(self.length_zazhim_patron, 0, Qt.AlignmentFlag.AlignHCenter)

        self.horizontalSpacer_20 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_20)


        self.verticalLayout_15.addLayout(self.horizontalLayout_13)


        self.verticalLayout_4.addWidget(self.widget_8)

        self.label_16 = QLabel(self.page_2)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setFont(font2)
        self.label_16.setStyleSheet(u"QLabel {\n"
"	background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(12, 123, 147, 255), stop:1 rgba(0, 168, 204, 255));\n"
"	padding-left: 2px;	\n"
"	color: rgb(24, 45, 76)\n"
"}\n"
"")

        self.verticalLayout_4.addWidget(self.label_16)

        self.widget_9 = QWidget(self.page_2)
        self.widget_9.setObjectName(u"widget_9")
        self.widget_9.setStyleSheet(u"QWidget {\n"
"	background: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0, stop:0 rgba(39, 72, 109, 129), stop:1 rgba(21, 41, 81, 129))\n"
"}")
        self.verticalLayout_17 = QVBoxLayout(self.widget_9)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(-1, 0, -1, -1)
        self.horizontalSpacer_25 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_16.addItem(self.horizontalSpacer_25)

        self.label_17 = QLabel(self.widget_9)
        self.label_17.setObjectName(u"label_17")
        sizePolicy2.setHeightForWidth(self.label_17.sizePolicy().hasHeightForWidth())
        self.label_17.setSizePolicy(sizePolicy2)
        self.label_17.setFont(font4)
        self.label_17.setStyleSheet(u"background:none;\n"
"border: none")
        self.label_17.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_16.addWidget(self.label_17)

        self.d_shlifovka_patron = QDoubleSpinBox(self.widget_9)
        self.d_shlifovka_patron.setObjectName(u"d_shlifovka_patron")
        sizePolicy3.setHeightForWidth(self.d_shlifovka_patron.sizePolicy().hasHeightForWidth())
        self.d_shlifovka_patron.setSizePolicy(sizePolicy3)
        self.d_shlifovka_patron.setMinimumSize(QSize(0, 30))
        self.d_shlifovka_patron.setStyleSheet(u"QDoubleSpinBox {\n"
"	padding: 2 5 2 5;	\n"
"	border: none;\n"
"	border-bottom: 1px solid white;\n"
"	border-radius: 1px;\n"
"	background: rgba(255, 255, 255, 0);\n"
"	transition: color 0.3s ease;\n"
"	transition: border-bottom 0.4s ease;\n"
"	color: rgb(204, 204, 204);\n"
"	font-size: 11pt;\n"
"}\n"
"\n"
"QDoubleSpinBox:disabled {\n"
"	color: rgb(120, 106, 107);\n"
"	background: rgba(255, 255, 255, 20);\n"
"}\n"
"\n"
"QDoubleSpinBox:hover {\n"
"	color: rgb(255, 255, 255)\n"
"}\n"
"\n"
"QDoubleSpinBox:pressed {\n"
"	border-bottom: 1px solid white;\n"
"}\n"
"")
        self.d_shlifovka_patron.setMaximum(10000.000000000000000)

        self.horizontalLayout_16.addWidget(self.d_shlifovka_patron, 0, Qt.AlignmentFlag.AlignHCenter)

        self.horizontalSpacer_26 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_16.addItem(self.horizontalSpacer_26)


        self.verticalLayout_17.addLayout(self.horizontalLayout_16)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(-1, 0, -1, -1)
        self.horizontalSpacer_27 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_17.addItem(self.horizontalSpacer_27)

        self.label_19 = QLabel(self.widget_9)
        self.label_19.setObjectName(u"label_19")
        sizePolicy2.setHeightForWidth(self.label_19.sizePolicy().hasHeightForWidth())
        self.label_19.setSizePolicy(sizePolicy2)
        self.label_19.setFont(font4)
        self.label_19.setStyleSheet(u"background:none;\n"
"border: none")
        self.label_19.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_17.addWidget(self.label_19)

        self.d_vist_patron = QDoubleSpinBox(self.widget_9)
        self.d_vist_patron.setObjectName(u"d_vist_patron")
        sizePolicy3.setHeightForWidth(self.d_vist_patron.sizePolicy().hasHeightForWidth())
        self.d_vist_patron.setSizePolicy(sizePolicy3)
        self.d_vist_patron.setMinimumSize(QSize(0, 30))
        self.d_vist_patron.setStyleSheet(u"QDoubleSpinBox {\n"
"	padding: 2 5 2 5;	\n"
"	border: none;\n"
"	border-bottom: 1px solid white;\n"
"	border-radius: 1px;\n"
"	background: rgba(255, 255, 255, 0);\n"
"	transition: color 0.3s ease;\n"
"	transition: border-bottom 0.4s ease;\n"
"	color: rgb(204, 204, 204);\n"
"	font-size: 11pt;\n"
"}\n"
"\n"
"QDoubleSpinBox:disabled {\n"
"	color: rgb(120, 106, 107);\n"
"	background: rgba(255, 255, 255, 20);\n"
"}\n"
"\n"
"QDoubleSpinBox:hover {\n"
"	color: rgb(255, 255, 255)\n"
"}\n"
"\n"
"QDoubleSpinBox:pressed {\n"
"	border-bottom: 1px solid white;\n"
"}\n"
"")
        self.d_vist_patron.setMaximum(10000.000000000000000)

        self.horizontalLayout_17.addWidget(self.d_vist_patron, 0, Qt.AlignmentFlag.AlignHCenter)

        self.horizontalSpacer_28 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_17.addItem(self.horizontalSpacer_28)


        self.verticalLayout_17.addLayout(self.horizontalLayout_17)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(-1, 0, -1, -1)
        self.horizontalSpacer_23 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_23)

        self.label_13 = QLabel(self.widget_9)
        self.label_13.setObjectName(u"label_13")
        sizePolicy2.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy2)
        self.label_13.setFont(font4)
        self.label_13.setStyleSheet(u"background:none;\n"
"border: none")
        self.label_13.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_15.addWidget(self.label_13)

        self.bienie_patron = QDoubleSpinBox(self.widget_9)
        self.bienie_patron.setObjectName(u"bienie_patron")
        sizePolicy3.setHeightForWidth(self.bienie_patron.sizePolicy().hasHeightForWidth())
        self.bienie_patron.setSizePolicy(sizePolicy3)
        self.bienie_patron.setMinimumSize(QSize(0, 30))
        self.bienie_patron.setStyleSheet(u"QDoubleSpinBox {\n"
"	padding: 2 5 2 5;	\n"
"	border: none;\n"
"	border-bottom: 1px solid white;\n"
"	border-radius: 1px;\n"
"	background: rgba(255, 255, 255, 0);\n"
"	transition: color 0.3s ease;\n"
"	transition: border-bottom 0.4s ease;\n"
"	color: rgb(204, 204, 204);\n"
"	font-size: 11pt;\n"
"}\n"
"\n"
"QDoubleSpinBox:disabled {\n"
"	color: rgb(120, 106, 107);\n"
"	background: rgba(255, 255, 255, 20);\n"
"}\n"
"\n"
"QDoubleSpinBox:hover {\n"
"	color: rgb(255, 255, 255)\n"
"}\n"
"\n"
"QDoubleSpinBox:pressed {\n"
"	border-bottom: 1px solid white;\n"
"}\n"
"")
        self.bienie_patron.setMaximum(10000.000000000000000)
        self.bienie_patron.setSingleStep(0.010000000000000)

        self.horizontalLayout_15.addWidget(self.bienie_patron, 0, Qt.AlignmentFlag.AlignHCenter)

        self.horizontalSpacer_24 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_24)


        self.verticalLayout_17.addLayout(self.horizontalLayout_15)


        self.verticalLayout_4.addWidget(self.widget_9)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_5)

        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.page_3.setStyleSheet(u"")
        self.verticalLayout_5 = QVBoxLayout(self.page_3)
        self.verticalLayout_5.setSpacing(10)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, -1)
        self.label_4 = QLabel(self.page_3)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font2)
        self.label_4.setStyleSheet(u"QLabel {\n"
"	background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(12, 123, 147, 255), stop:1 rgba(0, 168, 204, 255));\n"
"	padding-left: 2px;	\n"
"	color: rgb(24, 45, 76)\n"
"}\n"
"")

        self.verticalLayout_5.addWidget(self.label_4)

        self.widget_4 = QWidget(self.page_3)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setStyleSheet(u"QWidget {\n"
"	background: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0, stop:0 rgba(39, 72, 109, 129), stop:1 rgba(21, 41, 81, 129))\n"
"}")
        self.verticalLayout_9 = QVBoxLayout(self.widget_4)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.groupBox_2 = QGroupBox(self.widget_4)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setStyleSheet(u"QGroupBox {\n"
"	border: none;\n"
"	background: none;\n"
"}\n"
"QPushButton {\n"
"	background:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(12, 123, 147, 255), stop:1 rgba(0, 168, 204, 255));\n"
"	border: none;\n"
"	font-size: 11px;\n"
"	padding: 5 10 5 10;\n"
"	width: 100px;\n"
"	border: 1px solid qradialgradient(spread:pad, cx:0.506, cy:1, radius:1.147, fx:0.494318, fy:1, stop:0 rgba(12, 123, 147, 255), stop:1 rgba(255, 255, 255, 0));\n"
"}\n"
"QPushButton:hover {\n"
"	color: rgb(0, 168, 204);\n"
"	border-left: 1px solid rgb(10, 169, 255);\n"
"	border-right: 1px solid rgb(10, 169, 255);\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.477, x2:1, y2:0.518, stop:0 rgba(15, 109, 159, 64), stop:0.505682 rgba(15, 111, 149, 0), stop:1 rgba(15, 112, 139, 58));\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: rgb(0, 53, 93)\n"
"}\n"
"QPushButton:checked {\n"
"	background: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(12, 123, 147, 177), stop:"
                        "1 rgba(39, 73, 109, 255));\n"
"	color: rgb(0, 168, 204);\n"
"}")
        self.horizontalLayout_4 = QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(-1, 0, -1, 0)
        self.btn_opravka_ceh = QPushButton(self.groupBox_2)
        self.btn_opravka_ceh.setObjectName(u"btn_opravka_ceh")
        self.btn_opravka_ceh.setFont(font3)
        self.btn_opravka_ceh.setStyleSheet(u"")
        self.btn_opravka_ceh.setCheckable(True)
        self.btn_opravka_ceh.setChecked(True)
        self.btn_opravka_ceh.setAutoExclusive(True)

        self.horizontalLayout_4.addWidget(self.btn_opravka_ceh, 0, Qt.AlignmentFlag.AlignHCenter)

        self.btn_opravka_number = QPushButton(self.groupBox_2)
        self.btn_opravka_number.setObjectName(u"btn_opravka_number")
        self.btn_opravka_number.setFont(font3)
        self.btn_opravka_number.setStyleSheet(u"")
        self.btn_opravka_number.setCheckable(True)
        self.btn_opravka_number.setAutoExclusive(True)

        self.horizontalLayout_4.addWidget(self.btn_opravka_number)


        self.verticalLayout_9.addWidget(self.groupBox_2, 0, Qt.AlignmentFlag.AlignHCenter)

        self.type_opravka = QWidget(self.widget_4)
        self.type_opravka.setObjectName(u"type_opravka")
        self.type_opravka.setStyleSheet(u"QWidget {\n"
"	background: none;\n"
"}\n"
"QSpinBox {\n"
"	padding: 2 5 2 5;	\n"
"	border: none;\n"
"	border-bottom: 1px solid white;\n"
"	border-radius: 1px;\n"
"	background: rgba(255, 255, 255, 0);\n"
"	transition: color 0.3s ease;\n"
"	transition: border-bottom 0.4s ease;\n"
"	color: rgb(204, 204, 204);\n"
"	font-size: 11pt\n"
"}\n"
"\n"
"QSpinBox:disabled {\n"
"	color: rgb(120, 106, 107);\n"
"	background: rgba(255, 255, 255, 20);\n"
"}\n"
"\n"
"QSpinBox:hover {\n"
"	color: rgb(255, 255, 255)\n"
"}\n"
"\n"
"QSpinBox:pressed {\n"
"	border-bottom: 1px solid white;\n"
"}\n"
"")
        self.verticalLayout_8 = QVBoxLayout(self.type_opravka)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(-1, 0, -1, 0)
        self.label_5 = QLabel(self.type_opravka)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout_8.addWidget(self.label_5, 0, Qt.AlignmentFlag.AlignHCenter)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(-1, -1, 0, -1)
        self.number_opravka_1 = QSpinBox(self.type_opravka)
        self.number_opravka_1.setObjectName(u"number_opravka_1")
        self.number_opravka_1.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.number_opravka_1.setStyleSheet(u"")
        self.number_opravka_1.setMinimum(0)
        self.number_opravka_1.setMaximum(10000)
        self.number_opravka_1.setValue(1)

        self.horizontalLayout_5.addWidget(self.number_opravka_1)

        self.label = QLabel(self.type_opravka)
        self.label.setObjectName(u"label")

        self.horizontalLayout_5.addWidget(self.label)

        self.number_opravka_2 = QSpinBox(self.type_opravka)
        self.number_opravka_2.setObjectName(u"number_opravka_2")
        self.number_opravka_2.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.number_opravka_2.setStyleSheet(u"")
        self.number_opravka_2.setMinimum(1)
        self.number_opravka_2.setMaximum(10000)
        self.number_opravka_2.setValue(1)

        self.horizontalLayout_5.addWidget(self.number_opravka_2)


        self.verticalLayout_8.addLayout(self.horizontalLayout_5)


        self.verticalLayout_9.addWidget(self.type_opravka, 0, Qt.AlignmentFlag.AlignHCenter)


        self.verticalLayout_5.addWidget(self.widget_4)

        self.label_6 = QLabel(self.page_3)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font2)
        self.label_6.setStyleSheet(u"QLabel {\n"
"	background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(12, 123, 147, 255), stop:1 rgba(0, 168, 204, 255));\n"
"	padding-left: 2px;	\n"
"	color: rgb(24, 45, 76)\n"
"}\n"
"")

        self.verticalLayout_5.addWidget(self.label_6)

        self.widget_5 = QWidget(self.page_3)
        self.widget_5.setObjectName(u"widget_5")
        self.widget_5.setStyleSheet(u"QWidget {\n"
"	background: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0, stop:0 rgba(39, 72, 109, 129), stop:1 rgba(21, 41, 81, 129))\n"
"}")
        self.verticalLayout_12 = QVBoxLayout(self.widget_5)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(-1, 0, -1, -1)
        self.horizontalSpacer_29 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_18.addItem(self.horizontalSpacer_29)

        self.label_20 = QLabel(self.widget_5)
        self.label_20.setObjectName(u"label_20")
        sizePolicy2.setHeightForWidth(self.label_20.sizePolicy().hasHeightForWidth())
        self.label_20.setSizePolicy(sizePolicy2)
        self.label_20.setFont(font4)
        self.label_20.setStyleSheet(u"background:none;\n"
"border: none")
        self.label_20.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_18.addWidget(self.label_20)

        self.d_ystanovka_opravka = QDoubleSpinBox(self.widget_5)
        self.d_ystanovka_opravka.setObjectName(u"d_ystanovka_opravka")
        sizePolicy3.setHeightForWidth(self.d_ystanovka_opravka.sizePolicy().hasHeightForWidth())
        self.d_ystanovka_opravka.setSizePolicy(sizePolicy3)
        self.d_ystanovka_opravka.setMinimumSize(QSize(0, 30))
        self.d_ystanovka_opravka.setStyleSheet(u"QDoubleSpinBox {\n"
"	padding: 2 5 2 5;	\n"
"	border: none;\n"
"	border-bottom: 1px solid white;\n"
"	border-radius: 1px;\n"
"	background: rgba(255, 255, 255, 0);\n"
"	transition: color 0.3s ease;\n"
"	transition: border-bottom 0.4s ease;\n"
"	color: rgb(204, 204, 204);\n"
"	font-size: 11pt;\n"
"}\n"
"\n"
"QDoubleSpinBox:disabled {\n"
"	color: rgb(120, 106, 107);\n"
"	background: rgba(255, 255, 255, 20);\n"
"}\n"
"\n"
"QDoubleSpinBox:hover {\n"
"	color: rgb(255, 255, 255)\n"
"}\n"
"\n"
"QDoubleSpinBox:pressed {\n"
"	border-bottom: 1px solid white;\n"
"}\n"
"")
        self.d_ystanovka_opravka.setMaximum(10000.000000000000000)

        self.horizontalLayout_18.addWidget(self.d_ystanovka_opravka, 0, Qt.AlignmentFlag.AlignHCenter)

        self.horizontalSpacer_30 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_18.addItem(self.horizontalSpacer_30)


        self.verticalLayout_12.addLayout(self.horizontalLayout_18)


        self.verticalLayout_5.addWidget(self.widget_5)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_3)

        self.stackedWidget.addWidget(self.page_3)

        self.verticalLayout_7.addWidget(self.stackedWidget, 0, Qt.AlignmentFlag.AlignTop)


        self.verticalLayout_2.addWidget(self.widget_3)


        self.verticalLayout_11.addWidget(self.widget)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_11.addItem(self.verticalSpacer_2)

        self.btn_save_result_start = QPushButton(self.group_value_start_2)
        self.btn_save_result_start.setObjectName(u"btn_save_result_start")
        font5 = QFont()
        font5.setBold(True)
        self.btn_save_result_start.setFont(font5)
        self.btn_save_result_start.setStyleSheet(u"QPushButton {\n"
"	height: 30px;\n"
"	border: none;\n"
"	border-radius: 2px;\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(85, 170, 0, 255), stop:1 rgba(63, 126, 0, 255));\n"
"	padding: 2 5 2 5\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(63, 126, 0, 255), stop:1 rgba(85, 170, 0, 255));\n"
"	color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(191, 191, 191, 255), stop:1 rgba(211, 211, 211, 255));\n"
"	border: 1px solid qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(95, 189, 0, 255), stop:1 rgba(108, 217, 0, 255))\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: rgb(62, 124, 0)\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/icons/save.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_save_result_start.setIcon(icon2)
        self.btn_save_result_start.setIconSize(QSize(20, 20))

        self.verticalLayout_11.addWidget(self.btn_save_result_start, 0, Qt.AlignmentFlag.AlignHCenter)

        self.verticalWidget_start_2 = QWidget(self.group_value_start_2)
        self.verticalWidget_start_2.setObjectName(u"verticalWidget_start_2")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.verticalWidget_start_2.sizePolicy().hasHeightForWidth())
        self.verticalWidget_start_2.setSizePolicy(sizePolicy4)
        self.verticalWidget_start_2.setStyleSheet(u"background: none;\n"
"border: none;;\n"
"border-radius: 10px;\n"
"")
        self.verticalLayout_16 = QVBoxLayout(self.verticalWidget_start_2)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setSizeConstraint(QLayout.SizeConstraint.SetNoConstraint)
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_11.addWidget(self.verticalWidget_start_2)


        self.verticalLayout_10.addWidget(self.group_value_start_2)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.table_widget_start = QTableWidget(self.main)
        if (self.table_widget_start.columnCount() < 2):
            self.table_widget_start.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.table_widget_start.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.table_widget_start.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        self.table_widget_start.setObjectName(u"table_widget_start")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.table_widget_start.sizePolicy().hasHeightForWidth())
        self.table_widget_start.setSizePolicy(sizePolicy5)
        self.table_widget_start.setFont(font4)
        self.table_widget_start.setStyleSheet(u"/* \u0421\u0430\u043c \u0432\u0438\u0434\u0436\u0435\u0442 \u2014 \u043f\u0440\u043e\u0437\u0440\u0430\u0447\u043d\u044b\u0439 \u0444\u043e\u043d */\n"
"* {\n"
" background: rgba(255, 255, 255, 0);\n"
"}\n"
"QTableWidget {\n"
"    background: transparent;\n"
"    border: none;\n"
"    color: #ffffff;\n"
"    gridline-color: rgba(255, 255, 255, 0.15);\n"
"    selection-background-color: rgba(255, 255, 255, 0.25);\n"
"    selection-color: #ffffff;\n"
"}\n"
"\n"
"/* \u042f\u0447\u0435\u0439\u043a\u0438 \u2014 \u0431\u0435\u0437 \u0444\u043e\u043d\u0430, \u0431\u0435\u043b\u044b\u0439 \u0442\u0435\u043a\u0441\u0442 */\n"
"QTableWidget::item {\n"
"    background: transparent;\n"
"    color: #ffffff;\n"
"    padding: 4px 6px;\n"
"    border: none;\n"
"	border-left: 1px solid rgba(255, 255, 255, 0.15);\n"
"	border-bottom: 1px solid rgba(255, 255, 255, 0.15);\n"
"	border-right: 1px solid rgba(255, 255, 255, 0.15);\n"
"\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"/* \u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043a\u0438 \u2014"
                        " \u0415\u0414\u0418\u041d\u0421\u0422\u0412\u0415\u041d\u041d\u041e\u0415 \u043c\u0435\u0441\u0442\u043e \u0441 \u0444\u043e\u043d\u043e\u043c */\n"
"QHeaderView::section {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(12, 123, 147, 255), stop:1 rgba(0, 168, 204, 255));\n"
"    color: #ffffff;\n"
"    padding: 6px 8px;\n"
"    border: none;\n"
"    border-right: 1px solid rgba(255, 255, 255, 0.1);\n"
"    border-bottom: 1px solid rgba(255, 255, 255, 0.2);\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"\n"
"\n"
"/* \u0423\u0433\u043b\u043e\u0432\u0430\u044f \u043a\u043d\u043e\u043f\u043a\u0430 (\u043f\u0435\u0440\u0435\u0441\u0435\u0447\u0435\u043d\u0438\u0435 \u0437\u0430\u0433\u043e\u043b\u043e\u0432\u043a\u043e\u0432) */\n"
"QTableCornerButton::section {\n"
"    background-color:  qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(12, 123, 147, 255), stop:1 rgba(0, 168, 204, 255));\n"
"    border: none;\n"
"    border-right: 1px solid rgba(255, 255, 255, 0."
                        "1);\n"
"    border-bottom: 1px solid rgba(255, 255, 255, 0.2);\n"
"}\n"
"\n"
"/* \u0421\u043a\u0440\u043e\u043b\u043b\u0431\u0430\u0440\u044b \u2014 \u043c\u0438\u043d\u0438\u043c\u0430\u043b\u044c\u043d\u043e, \u0447\u0442\u043e\u0431\u044b \u043d\u0435 \u043c\u0435\u0448\u0430\u043b\u0438 */\n"
"QTableWidget QScrollBar:vertical {\n"
"    background: transparent;\n"
"    width: 8px;\n"
"}\n"
"\n"
"QTableWidget QScrollBar::handle:vertical {\n"
"    background: rgba(255, 255, 255, 0.3);\n"
"    border-radius: 4px;\n"
"    min-height: 20px;\n"
"}\n"
"\n"
"QTableWidget QScrollBar::handle:vertical:hover {\n"
"    background: rgba(255, 255, 255, 0.5);\n"
"}\n"
"\n"
"QTableWidget QScrollBar::add-line:vertical,\n"
"QTableWidget QScrollBar::sub-line:vertical,\n"
"QTableWidget QScrollBar::add-page:vertical,\n"
"QTableWidget QScrollBar::sub-page:vertical {\n"
"    background: transparent;\n"
"    height: 0px;\n"
"}\n"
"\n"
"QTableWidget QScrollBar:horizontal {\n"
"    background: transparent;\n"
"    height: 8px;\n"
"}\n"
""
                        "\n"
"QTableWidget QScrollBar::handle:horizontal {\n"
"    background: rgba(255, 255, 255, 0.3);\n"
"    border-radius: 4px;\n"
"    min-width: 20px;\n"
"}\n"
"\n"
"QTableWidget QScrollBar::handle:horizontal:hover {\n"
"    background: rgba(255, 255, 255, 0.5);\n"
"}\n"
"\n"
"QTableWidget QScrollBar::add-line:horizontal,\n"
"QTableWidget QScrollBar::sub-line:horizontal,\n"
"QTableWidget QScrollBar::add-page:horizontal,\n"
"QTableWidget QScrollBar::sub-page:horizontal {\n"
"    background: transparent;\n"
"    width: 0px;\n"
"}\n"
"QPushButton {\n"
"	image: url(:/icons/trash.png);\n"
"	padding: 10;\n"
"	width: 30;\n"
"	height: 30;\n"
"}\n"
"QPushButton:hover {\n"
"	image: url(:/icons/trash_grey.png);\n"
"	cursor: pointer;\n"
"}")
        self.table_widget_start.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.table_widget_start.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.table_widget_start.setAutoScroll(False)
        self.table_widget_start.setRowCount(0)
        self.table_widget_start.setColumnCount(2)
        self.table_widget_start.verticalHeader().setVisible(False)
        self.table_widget_start.verticalHeader().setMinimumSectionSize(90)
        self.table_widget_start.verticalHeader().setDefaultSectionSize(100)

        self.horizontalLayout_6.addWidget(self.table_widget_start)


        self.verticalLayout_10.addLayout(self.horizontalLayout_6)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_10.addItem(self.verticalSpacer)

        self.text_error_start = QLabel(self.main)
        self.text_error_start.setObjectName(u"text_error_start")
        self.text_error_start.setFont(font4)
        self.text_error_start.setStyleSheet(u"background:none")
        self.text_error_start.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_10.addWidget(self.text_error_start)


        self.verticalLayout.addWidget(self.main)


        self.retranslateUi(ShlifovanieStart)

        self.stackedWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(ShlifovanieStart)
    # setupUi

    def retranslateUi(self, ShlifovanieStart):
        ShlifovanieStart.setWindowTitle(QCoreApplication.translate("ShlifovanieStart", u"Form", None))
        self.btn_home.setText(QCoreApplication.translate("ShlifovanieStart", u" \u041d\u0410\u0417\u0410\u0414", None))
        self.pushButton.setText("")
        self.label_7.setText(QCoreApplication.translate("ShlifovanieStart", u"\u0423\u0441\u0442\u0430\u043d\u043e\u0432\u043a\u0430 \u0434\u0435\u0442\u0430\u043b\u0438", None))
        self.label_2.setText(QCoreApplication.translate("ShlifovanieStart", u"\u0412\u044b\u0431\u043e\u0440 \u0443\u0441\u0442\u0430\u043d\u043e\u0432\u043a\u0438 \u0434\u0435\u0442\u0430\u043b\u0438:", None))
        self.btn_centr.setText(QCoreApplication.translate("ShlifovanieStart", u"\u0412 \u0446\u0435\u043d\u0442\u0440\u0430\u0445", None))
        self.btn_patron.setText(QCoreApplication.translate("ShlifovanieStart", u"\u0412 \u043f\u0430\u0442\u0440\u043e\u043d\u0435", None))
        self.btn_opravka.setText(QCoreApplication.translate("ShlifovanieStart", u"\u041d\u0430 \u043e\u043f\u0440\u0430\u0432\u043a\u0435", None))
        self.label_21.setText(QCoreApplication.translate("ShlifovanieStart", u"\u041f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u044b \u0437\u0430\u0436\u0438\u043c\u0430:", None))
        self.label_9.setText(QCoreApplication.translate("ShlifovanieStart", u"\u0414\u0438\u0430\u043c\u0435\u0442\u0440 \u0437\u0430\u0436\u0438\u043c\u0430 \u0437\u0430\u0433\u043e\u0442\u043e\u0432\u043a\u0438 \u043f\u043e\u0432\u043e\u0434\u043a\u043e\u0432\u044b\u043c \u043f\u0430\u0442\u0440\u043e\u043d\u043e\u043c:", None))
        self.d_zazhim_centr.setPrefix(QCoreApplication.translate("ShlifovanieStart", u"\u00d8 ", None))
        self.d_zazhim_centr.setSuffix(QCoreApplication.translate("ShlifovanieStart", u" \u043c\u043c.", None))
        self.label_22.setText(QCoreApplication.translate("ShlifovanieStart", u"\u041f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u044b \u0432\u044b\u0441\u0442\u0430\u0432\u043b\u0435\u043d\u0438\u044f:", None))
        self.label_10.setText(QCoreApplication.translate("ShlifovanieStart", u"\u0414\u0438\u0430\u043c\u0435\u0442\u0440 \u0432\u044b\u0441\u0442\u0430\u0432\u043b\u0435\u043d\u0438\u044f \u0434\u0435\u0442\u0430\u043b\u0438:", None))
        self.d_vist_centr.setPrefix(QCoreApplication.translate("ShlifovanieStart", u"\u00d8 ", None))
        self.d_vist_centr.setSuffix(QCoreApplication.translate("ShlifovanieStart", u" \u043c\u043c.", None))
        self.label_12.setText(QCoreApplication.translate("ShlifovanieStart", u"\u0414\u0438\u0430\u043c\u0435\u0442\u0440 \u0448\u043b\u0438\u0444\u0443\u0435\u043c\u043e\u0439 \u043f\u043e\u0432\u0435\u0440\u0445\u043d\u043e\u0441\u0442\u0438:", None))
        self.d_shlifovka_centr.setPrefix(QCoreApplication.translate("ShlifovanieStart", u"\u00d8 ", None))
        self.d_shlifovka_centr.setSuffix(QCoreApplication.translate("ShlifovanieStart", u" \u043c\u043c.", None))
        self.label_11.setText(QCoreApplication.translate("ShlifovanieStart", u"\u0420\u0430\u0434\u0438\u0430\u043b\u044c\u043d\u043e\u0435 \u0431\u0438\u0435\u043d\u0438\u0435 \u0434\u043b\u044f \u0432\u044b\u0441\u0442\u0430\u0432\u043b\u0435\u043d\u0438\u044f:", None))
        self.bienie_centr.setPrefix(QCoreApplication.translate("ShlifovanieStart", u"\u2197 ", None))
        self.bienie_centr.setSuffix("")
        self.label_8.setText(QCoreApplication.translate("ShlifovanieStart", u"\u041f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u044b \u0437\u0430\u0436\u0438\u043c\u0430:", None))
        self.label_14.setText(QCoreApplication.translate("ShlifovanieStart", u"\u0414\u0438\u0430\u043c\u0435\u0442\u0440 \u0437\u0430\u0436\u0438\u043c\u0430 \u0442\u0440\u0435\u0445\u043a\u0443\u043b\u0430\u0447\u043a\u043e\u0432\u044b\u043c \u043f\u0430\u0442\u0440\u043e\u043d\u043e\u043c:", None))
        self.d_zazhim_patron.setPrefix(QCoreApplication.translate("ShlifovanieStart", u"\u00d8 ", None))
        self.d_zazhim_patron.setSuffix(QCoreApplication.translate("ShlifovanieStart", u" \u043c\u043c.", None))
        self.label_15.setText(QCoreApplication.translate("ShlifovanieStart", u"\u0414\u043b\u0438\u043d\u0430 \u0437\u0430\u0436\u0438\u043c\u0430:", None))
        self.length_zazhim_patron.setPrefix(QCoreApplication.translate("ShlifovanieStart", u"L= ", None))
        self.length_zazhim_patron.setSuffix(QCoreApplication.translate("ShlifovanieStart", u" \u043c\u043c.", None))
        self.label_16.setText(QCoreApplication.translate("ShlifovanieStart", u"\u041f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u044b \u0432\u044b\u0441\u0442\u0430\u0432\u043b\u0435\u043d\u0438\u044f:", None))
        self.label_17.setText(QCoreApplication.translate("ShlifovanieStart", u"\u0414\u0438\u0430\u043c\u0435\u0442\u0440 \u0448\u043b\u0438\u0444\u0443\u0435\u043c\u043e\u0439 \u043f\u043e\u0432\u0435\u0440\u0445\u043d\u043e\u0441\u0442\u0438:", None))
        self.d_shlifovka_patron.setPrefix(QCoreApplication.translate("ShlifovanieStart", u"\u00d8 ", None))
        self.d_shlifovka_patron.setSuffix(QCoreApplication.translate("ShlifovanieStart", u" \u043c\u043c.", None))
        self.label_19.setText(QCoreApplication.translate("ShlifovanieStart", u"\u0414\u0438\u0430\u043c\u0435\u0442\u0440 \u0432\u044b\u0441\u0442\u0430\u0432\u043b\u0435\u043d\u0438\u044f \u0434\u0435\u0442\u0430\u043b\u0438:", None))
        self.d_vist_patron.setPrefix(QCoreApplication.translate("ShlifovanieStart", u"\u00d8 ", None))
        self.d_vist_patron.setSuffix(QCoreApplication.translate("ShlifovanieStart", u" \u043c\u043c.", None))
        self.label_13.setText(QCoreApplication.translate("ShlifovanieStart", u"\u0420\u0430\u0434\u0438\u0430\u043b\u044c\u043d\u043e\u0435 \u0431\u0438\u0435\u043d\u0438\u0435 \u0434\u043b\u044f \u0432\u044b\u0441\u0442\u0430\u0432\u043b\u0435\u043d\u0438\u044f:", None))
        self.bienie_patron.setPrefix(QCoreApplication.translate("ShlifovanieStart", u"\u2197 ", None))
        self.bienie_patron.setSuffix("")
        self.label_4.setText(QCoreApplication.translate("ShlifovanieStart", u"\u0412\u044b\u0431\u043e\u0440 \u043e\u043f\u0440\u0430\u0432\u043a\u0438:", None))
        self.btn_opravka_ceh.setText(QCoreApplication.translate("ShlifovanieStart", u"\u0426\u0435\u0445\u043e\u0432\u0430\u044f", None))
        self.btn_opravka_number.setText(QCoreApplication.translate("ShlifovanieStart", u"\u041d\u043e\u043c\u0435\u0440", None))
        self.label_5.setText(QCoreApplication.translate("ShlifovanieStart", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u043d\u043e\u043c\u0435\u0440 \u043e\u043f\u0440\u0430\u0432\u043a\u0438:", None))
        self.number_opravka_1.setSuffix("")
        self.label.setText(QCoreApplication.translate("ShlifovanieStart", u"\u2014", None))
        self.number_opravka_2.setSuffix("")
        self.label_6.setText(QCoreApplication.translate("ShlifovanieStart", u"\u0423\u0441\u0442\u0430\u043d\u043e\u0432\u043a\u0430 \u0434\u0435\u0442\u0430\u043b\u0438 \u043d\u0430 \u043e\u043f\u0440\u0430\u0432\u043a\u0443:", None))
        self.label_20.setText(QCoreApplication.translate("ShlifovanieStart", u"\u0414\u0438\u0430\u043c\u0435\u0442\u0440 \u0443\u0441\u0442\u0430\u043d\u043e\u0432\u043e\u0447\u043d\u043e\u0433\u043e \u043e\u0442\u0432\u0435\u0440\u0441\u0442\u0438\u044f \u0434\u0435\u0442\u0430\u043b\u0438:", None))
        self.d_ystanovka_opravka.setPrefix(QCoreApplication.translate("ShlifovanieStart", u"\u00d8 ", None))
        self.d_ystanovka_opravka.setSuffix(QCoreApplication.translate("ShlifovanieStart", u" \u043c\u043c.", None))
        self.btn_save_result_start.setText(QCoreApplication.translate("ShlifovanieStart", u" \u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u044f", None))
        ___qtablewidgetitem = self.table_widget_start.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("ShlifovanieStart", u"\u0418\u043d\u0441\u0442\u0440\u0443\u043c\u0435\u043d\u0442", None))
        ___qtablewidgetitem1 = self.table_widget_start.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("ShlifovanieStart", u"\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435", None))
        self.text_error_start.setText("")
    # retranslateUi

