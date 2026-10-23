# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_page_tokarnaya_podrezka.ui'
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
from PySide6.QtWidgets import (QApplication, QDoubleSpinBox, QFrame, QGroupBox,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QPushButton, QRadioButton, QSizePolicy, QSpacerItem,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)
import res_rc

class Ui_PageTokarnayaPodrezka(object):
    def setupUi(self, PageTokarnayaPodrezka):
        if not PageTokarnayaPodrezka.objectName():
            PageTokarnayaPodrezka.setObjectName(u"PageTokarnayaPodrezka")
        PageTokarnayaPodrezka.setEnabled(True)
        PageTokarnayaPodrezka.resize(1000, 750)
        PageTokarnayaPodrezka.setMinimumSize(QSize(1000, 750))
        PageTokarnayaPodrezka.setMaximumSize(QSize(1000, 750))
        PageTokarnayaPodrezka.setStyleSheet(u"color: white;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0, stop:0 rgba(20, 40, 80, 255), stop:1 rgba(39, 73, 109, 255));\n"
"")
        self.verticalLayout_2 = QVBoxLayout(PageTokarnayaPodrezka)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(9, -1, -1, -1)
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(-1, 0, -1, 0)
        self.btn_home_tokarnaya_podrezka = QPushButton(PageTokarnayaPodrezka)
        self.btn_home_tokarnaya_podrezka.setObjectName(u"btn_home_tokarnaya_podrezka")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_home_tokarnaya_podrezka.sizePolicy().hasHeightForWidth())
        self.btn_home_tokarnaya_podrezka.setSizePolicy(sizePolicy)
        self.btn_home_tokarnaya_podrezka.setMinimumSize(QSize(70, 0))
        self.btn_home_tokarnaya_podrezka.setMaximumSize(QSize(150, 30))
        font = QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.btn_home_tokarnaya_podrezka.setFont(font)
        self.btn_home_tokarnaya_podrezka.setStyleSheet(u"QPushButton {\n"
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
        self.btn_home_tokarnaya_podrezka.setIcon(icon)
        self.btn_home_tokarnaya_podrezka.setIconSize(QSize(20, 20))

        self.horizontalLayout_5.addWidget(self.btn_home_tokarnaya_podrezka, 0, Qt.AlignmentFlag.AlignLeft)


        self.verticalLayout_2.addLayout(self.horizontalLayout_5)

        self.widget = QWidget(PageTokarnayaPodrezka)
        self.widget.setObjectName(u"widget")
        self.widget.setStyleSheet(u"border: none;\n"
"background: none;")
        self.verticalLayout_6 = QVBoxLayout(self.widget)
        self.verticalLayout_6.setSpacing(5)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(15, 20, 15, 15)
        self.label_4 = QLabel(self.widget)
        self.label_4.setObjectName(u"label_4")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)
        sizePolicy1.setHorizontalStretch(3)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy1)
        font1 = QFont()
        font1.setWeight(QFont.DemiBold)
        self.label_4.setFont(font1)
        self.label_4.setStyleSheet(u"background-color: none;\n"
"color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(12, 123, 147, 255), stop:1 rgba(0, 168, 204, 255));\n"
"font-size: 28px;\n"
"font-weight: 600;\n"
"border: none;\n"
"width: 300px;\n"
"\n"
"")
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_6.addWidget(self.label_4)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, -1)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.group_value_podrezka = QWidget(self.widget)
        self.group_value_podrezka.setObjectName(u"group_value_podrezka")
        self.group_value_podrezka.setMouseTracking(True)
        self.group_value_podrezka.setTabletTracking(False)
        self.group_value_podrezka.setAutoFillBackground(False)
        self.group_value_podrezka.setStyleSheet(u"QWidget { \n"
"	border: none;\n"
"	background: none;\n"
"}")
        self.verticalLayout = QVBoxLayout(self.group_value_podrezka)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 20, 10, 20)
        self.label_6 = QLabel(self.group_value_podrezka)
        self.label_6.setObjectName(u"label_6")
        font2 = QFont()
        font2.setFamilies([u"Segoe UI Light"])
        font2.setPointSize(10)
        font2.setBold(False)
        self.label_6.setFont(font2)
        self.label_6.setStyleSheet(u"QLabel {\n"
"	background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(12, 123, 147, 255), stop:1 rgba(0, 168, 204, 255));\n"
"	padding-left: 2px;	\n"
"	color: rgb(24, 45, 76)\n"
"}\n"
"")

        self.verticalLayout.addWidget(self.label_6)

        self.widget_2 = QWidget(self.group_value_podrezka)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setStyleSheet(u"QWidget {\n"
"	background: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0, stop:0 rgba(39, 72, 109, 129), stop:1 rgba(21, 41, 81, 129))\n"
"}")
        self.verticalLayout_5 = QVBoxLayout(self.widget_2)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_7 = QLabel(self.widget_2)
        self.label_7.setObjectName(u"label_7")
        font3 = QFont()
        font3.setFamilies([u"Segoe UI Light"])
        font3.setPointSize(10)
        self.label_7.setFont(font3)
        self.label_7.setStyleSheet(u"color: rgb(6, 171, 204);\n"
"background: none;")

        self.verticalLayout_5.addWidget(self.label_7, 0, Qt.AlignmentFlag.AlignHCenter)


        self.verticalLayout.addWidget(self.widget_2)

        self.label_5 = QLabel(self.group_value_podrezka)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font2)
        self.label_5.setStyleSheet(u"QLabel {\n"
"	background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(12, 123, 147, 255), stop:1 rgba(0, 168, 204, 255));\n"
"	padding-left: 2px;	\n"
"	color: rgb(24, 45, 76)\n"
"}\n"
"")

        self.verticalLayout.addWidget(self.label_5)

        self.widget_3 = QWidget(self.group_value_podrezka)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setStyleSheet(u"QWidget {\n"
"	background: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0, stop:0 rgba(39, 72, 109, 129), stop:1 rgba(21, 41, 81, 129));\n"
"\n"
"}\n"
"Line {\n"
"	background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(8, 81, 97, 128), stop:1 rgba(0, 117, 142, 106))\n"
"}")
        self.verticalLayout_7 = QVBoxLayout(self.widget_3)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(10)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.widget_3)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"background: none;")

        self.horizontalLayout_2.addWidget(self.label)

        self.value_length = QDoubleSpinBox(self.widget_3)
        self.value_length.setObjectName(u"value_length")
        self.value_length.setEnabled(True)
        self.value_length.setMinimumSize(QSize(80, 0))
        self.value_length.setStyleSheet(u"QDoubleSpinBox {\n"
"	padding: 2 5 2 5;	\n"
"	border: none;\n"
"	border-bottom: 1px solid white;\n"
"	border-radius: 1px;\n"
"	background: rgba(255, 255, 255, 0);\n"
"	transition: color 0.3s ease;\n"
"	transition: border-bottom 0.4s ease;\n"
"	color: rgb(204, 204, 204);\n"
"	font-size: 15px\n"
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
        self.value_length.setDecimals(3)
        self.value_length.setMaximum(2000.000000000000000)

        self.horizontalLayout_2.addWidget(self.value_length, 0, Qt.AlignmentFlag.AlignLeft)

        self.line = QFrame(self.widget_3)
        self.line.setObjectName(u"line")
        self.line.setStyleSheet(u"")
        self.line.setFrameShape(QFrame.Shape.VLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_2.addWidget(self.line)

        self.label_2 = QLabel(self.widget_3)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"background: none;")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.kavalitet_length = QLineEdit(self.widget_3)
        self.kavalitet_length.setObjectName(u"kavalitet_length")
        self.kavalitet_length.setEnabled(True)
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.kavalitet_length.sizePolicy().hasHeightForWidth())
        self.kavalitet_length.setSizePolicy(sizePolicy2)
        self.kavalitet_length.setMaximumSize(QSize(70, 16777215))
        font4 = QFont()
        font4.setBold(False)
        self.kavalitet_length.setFont(font4)
        self.kavalitet_length.setStyleSheet(u"QLineEdit {\n"
"	padding: 2;	\n"
"	border: none;\n"
"	border-bottom: 1px solid white;\n"
"	border-radius: 1px;\n"
"	background: rgba(255, 255, 255, 0);\n"
"	transition: color 0.3s ease;\n"
"	transition: border-bottom 0.4s ease;\n"
"	color: rgb(204, 204, 204);\n"
"	font-size: 12px\n"
"}\n"
"QLineEdit:disabled {\n"
"	color: rgb(120, 106, 107);\n"
"	background: rgba(255, 255, 255, 20);\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"	color: rgb(255, 255, 255)\n"
"}\n"
"\n"
"QLineEdit:pressed {\n"
"	border-bottom: 1px solid white;\n"
"}")

        self.horizontalLayout_2.addWidget(self.kavalitet_length)

        self.line_2 = QFrame(self.widget_3)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setStyleSheet(u"")
        self.line_2.setFrameShape(QFrame.Shape.VLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_2.addWidget(self.line_2)

        self.label_8 = QLabel(self.widget_3)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setStyleSheet(u"background: none;")

        self.horizontalLayout_2.addWidget(self.label_8)

        self.dopusk_length = QDoubleSpinBox(self.widget_3)
        self.dopusk_length.setObjectName(u"dopusk_length")
        self.dopusk_length.setEnabled(True)
        sizePolicy2.setHeightForWidth(self.dopusk_length.sizePolicy().hasHeightForWidth())
        self.dopusk_length.setSizePolicy(sizePolicy2)
        self.dopusk_length.setMaximumSize(QSize(80, 16777215))
        self.dopusk_length.setStyleSheet(u"QDoubleSpinBox {\n"
"	padding: 2 5 2 5;	\n"
"	border: none;\n"
"	border-bottom: 1px solid white;\n"
"	border-radius: 1px;\n"
"	background: rgba(255, 255, 255, 0);\n"
"	transition: color 0.3s ease;\n"
"	transition: border-bottom 0.4s ease;\n"
"	color: rgb(204, 204, 204);\n"
"	font-size: 15px\n"
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
        self.dopusk_length.setDecimals(3)
        self.dopusk_length.setMinimum(-5.000000000000000)
        self.dopusk_length.setMaximum(5.000000000000000)
        self.dopusk_length.setSingleStep(0.010000000000000)

        self.horizontalLayout_2.addWidget(self.dopusk_length)

        self.label_9 = QLabel(self.widget_3)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setStyleSheet(u"background: none;")

        self.horizontalLayout_2.addWidget(self.label_9)

        self.dopusk_length_2 = QDoubleSpinBox(self.widget_3)
        self.dopusk_length_2.setObjectName(u"dopusk_length_2")
        self.dopusk_length_2.setEnabled(True)
        sizePolicy2.setHeightForWidth(self.dopusk_length_2.sizePolicy().hasHeightForWidth())
        self.dopusk_length_2.setSizePolicy(sizePolicy2)
        self.dopusk_length_2.setMaximumSize(QSize(80, 16777215))
        self.dopusk_length_2.setStyleSheet(u"QDoubleSpinBox {\n"
"	padding: 2 5 2 5;	\n"
"	border: none;\n"
"	border-bottom: 1px solid white;\n"
"	border-radius: 1px;\n"
"	background: rgba(255, 255, 255, 0);\n"
"	transition: color 0.3s ease;\n"
"	transition: border-bottom 0.4s ease;\n"
"	color: rgb(204, 204, 204);\n"
"	font-size: 15px\n"
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
        self.dopusk_length_2.setDecimals(3)
        self.dopusk_length_2.setMinimum(-5.000000000000000)
        self.dopusk_length_2.setMaximum(5.000000000000000)
        self.dopusk_length_2.setSingleStep(0.010000000000000)

        self.horizontalLayout_2.addWidget(self.dopusk_length_2)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_9)


        self.verticalLayout_7.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(10)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(-1, 0, -1, -1)
        self.label_3 = QLabel(self.widget_3)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"background: none;")

        self.horizontalLayout_4.addWidget(self.label_3)

        self.groupBox = QGroupBox(self.widget_3)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setStyleSheet(u"QGroupBox {\n"
"	border: none;\n"
"	background: none;\n"
"}\n"
"\n"
"QRadioButton {\n"
"	background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(89, 89, 89, 255), stop:1 rgba(111, 111, 111, 255));\n"
"	padding: 2 10 2 5;\n"
"	font-size: 15px;\n"
"	border-top-left-radius: 10px;\n"
"	border-bottom-right-radius: 10px;\n"
"}\n"
"\n"
"QRadioButton:hover {\n"
"	color: rgb(216, 216, 216);\n"
"	background: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.851, fx:0.5, fy:0.5, stop:0 rgba(60, 60, 60, 255), stop:1 rgba(89, 89, 89, 255))\n"
"}\n"
"\n"
"QRadioButton:checked {\n"
"	background: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0, stop:0 rgba(12, 123, 147, 255), stop:1 rgba(0, 168, 204, 255));\n"
"}\n"
"\n"
"QRadioButton:disabled {\n"
"	background: \n"
"}\n"
"QRadioButton::indicator:enabled {\n"
"	background: rgb(156, 156, 156);\n"
"}\n"
"QRadioButton::indicator:disabled {\n"
"	background: none;\n"
"	border: 1px solid rgb(200, 200, 200);\n"
"	border-radius: 6px;\n"
"}\n"
"QRadioButton::"
                        "indicator {\n"
"	width: 12px;\n"
"	height: 12px;\n"
"	background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(135, 135, 135, 255), stop:1 rgba(184, 184, 184, 255));\n"
"	border-radius: 6px;\n"
"}\n"
"QRadioButton::indicator:checked {\n"
"	background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(8, 81, 97, 255), stop:1 rgba(0, 117, 142, 255))\n"
"}\n"
"\n"
"QRadioButton:disabled {\n"
"	background: none;\n"
"	color: rgb(200, 200, 200);\n"
"}")
        self.horizontalLayout_6 = QHBoxLayout(self.groupBox)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.radioButton_ra1 = QRadioButton(self.groupBox)
        self.radioButton_ra1.setObjectName(u"radioButton_ra1")
        self.radioButton_ra1.setEnabled(True)
        self.radioButton_ra1.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.radioButton_ra1.setAutoFillBackground(False)
        self.radioButton_ra1.setStyleSheet(u"")
        self.radioButton_ra1.setCheckable(True)
        self.radioButton_ra1.setChecked(False)
        self.radioButton_ra1.setAutoExclusive(True)

        self.horizontalLayout_6.addWidget(self.radioButton_ra1)

        self.radioButton_ra2 = QRadioButton(self.groupBox)
        self.radioButton_ra2.setObjectName(u"radioButton_ra2")
        self.radioButton_ra2.setEnabled(True)
        self.radioButton_ra2.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.radioButton_ra2.setStyleSheet(u"")
        self.radioButton_ra2.setCheckable(True)
        self.radioButton_ra2.setChecked(False)
        self.radioButton_ra2.setAutoExclusive(True)

        self.horizontalLayout_6.addWidget(self.radioButton_ra2)

        self.radioButton_ra3 = QRadioButton(self.groupBox)
        self.radioButton_ra3.setObjectName(u"radioButton_ra3")
        self.radioButton_ra3.setEnabled(True)
        self.radioButton_ra3.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.radioButton_ra3.setStyleSheet(u"")

        self.horizontalLayout_6.addWidget(self.radioButton_ra3)

        self.radioButton_ra4 = QRadioButton(self.groupBox)
        self.radioButton_ra4.setObjectName(u"radioButton_ra4")
        self.radioButton_ra4.setEnabled(True)
        self.radioButton_ra4.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.radioButton_ra4.setStyleSheet(u"")
        self.radioButton_ra4.setCheckable(True)
        self.radioButton_ra4.setChecked(False)
        self.radioButton_ra4.setAutoExclusive(True)

        self.horizontalLayout_6.addWidget(self.radioButton_ra4)

        self.radioButton_ra5 = QRadioButton(self.groupBox)
        self.radioButton_ra5.setObjectName(u"radioButton_ra5")
        self.radioButton_ra5.setEnabled(True)
        self.radioButton_ra5.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.radioButton_ra5.setStyleSheet(u"")
        self.radioButton_ra5.setCheckable(True)
        self.radioButton_ra5.setChecked(False)
        self.radioButton_ra5.setAutoExclusive(True)

        self.horizontalLayout_6.addWidget(self.radioButton_ra5)


        self.horizontalLayout_4.addWidget(self.groupBox)

        self.cancel_surf_rad = QPushButton(self.widget_3)
        self.cancel_surf_rad.setObjectName(u"cancel_surf_rad")
        self.cancel_surf_rad.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.cancel_surf_rad.setStyleSheet(u"QPushButton {\n"
"	image: url(:/icons/return_white.png);\n"
"	background: none;\n"
"	padding: 5;\n"
"	widgth: 25;\n"
"	height: 25;\n"
"}\n"
"QPushButton:hover {\n"
"	image: url(:/icons/return_grey.png);\n"
"}")

        self.horizontalLayout_4.addWidget(self.cancel_surf_rad)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_3)


        self.verticalLayout_7.addLayout(self.horizontalLayout_4)


        self.verticalLayout.addWidget(self.widget_3)

        self.btn_save = QPushButton(self.group_value_podrezka)
        self.btn_save.setObjectName(u"btn_save")
        font5 = QFont()
        font5.setBold(True)
        self.btn_save.setFont(font5)
        self.btn_save.setStyleSheet(u"QPushButton {\n"
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
        icon1 = QIcon()
        icon1.addFile(u":/icons/save.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_save.setIcon(icon1)
        self.btn_save.setIconSize(QSize(20, 20))

        self.verticalLayout.addWidget(self.btn_save, 0, Qt.AlignmentFlag.AlignHCenter)


        self.horizontalLayout.addWidget(self.group_value_podrezka)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.verticalLayout_6.addLayout(self.horizontalLayout)


        self.verticalLayout_2.addWidget(self.widget)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.table_widget = QTableWidget(PageTokarnayaPodrezka)
        if (self.table_widget.columnCount() < 2):
            self.table_widget.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.table_widget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.table_widget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        self.table_widget.setObjectName(u"table_widget")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.table_widget.sizePolicy().hasHeightForWidth())
        self.table_widget.setSizePolicy(sizePolicy3)
        font6 = QFont()
        font6.setPointSize(10)
        self.table_widget.setFont(font6)
        self.table_widget.setStyleSheet(u"/* \u0421\u0430\u043c \u0432\u0438\u0434\u0436\u0435\u0442 \u2014 \u043f\u0440\u043e\u0437\u0440\u0430\u0447\u043d\u044b\u0439 \u0444\u043e\u043d */\n"
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
        self.table_widget.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.table_widget.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.table_widget.setAutoScroll(False)
        self.table_widget.setRowCount(0)
        self.table_widget.setColumnCount(2)
        self.table_widget.verticalHeader().setVisible(False)
        self.table_widget.verticalHeader().setMinimumSectionSize(90)
        self.table_widget.verticalHeader().setDefaultSectionSize(100)

        self.horizontalLayout_3.addWidget(self.table_widget)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.text_error_podrezka = QLabel(PageTokarnayaPodrezka)
        self.text_error_podrezka.setObjectName(u"text_error_podrezka")
        self.text_error_podrezka.setFont(font6)
        self.text_error_podrezka.setStyleSheet(u"background:none;\n"
"border: none;")
        self.text_error_podrezka.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.text_error_podrezka)


        self.retranslateUi(PageTokarnayaPodrezka)

        QMetaObject.connectSlotsByName(PageTokarnayaPodrezka)
    # setupUi

    def retranslateUi(self, PageTokarnayaPodrezka):
        PageTokarnayaPodrezka.setWindowTitle(QCoreApplication.translate("PageTokarnayaPodrezka", u"\u041f\u043e\u0434\u0440\u0435\u0437\u043a\u0430", None))
        self.btn_home_tokarnaya_podrezka.setText(QCoreApplication.translate("PageTokarnayaPodrezka", u" \u041d\u0410\u0417\u0410\u0414", None))
        self.label_4.setText(QCoreApplication.translate("PageTokarnayaPodrezka", u"\u041f\u041e\u0414\u0420\u0415\u0417\u041a\u0410 \u0422\u041e\u0420\u0426\u0410", None))
        self.label_6.setText(QCoreApplication.translate("PageTokarnayaPodrezka", u"\u041e\u0441\u043d\u043e\u0432\u043d\u044b\u0435 \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u044b:", None))
        self.label_7.setText(QCoreApplication.translate("PageTokarnayaPodrezka", u"\u041e\u0441\u043d\u043e\u0432\u043d\u044b\u0445 \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u043e\u0432 \u043d\u0435\u0442. \u0422\u0435\u043a\u0441\u0442 \u0432\u044b\u0432\u043e\u0434\u0430: \"\u041f\u043e\u0434\u0440\u0435\u0437\u0430\u0442\u044c \u043a\u0430\u043a \u0447\u0438\u0441\u0442\u043e\"", None))
        self.label_5.setText(QCoreApplication.translate("PageTokarnayaPodrezka", u"\u0414\u043e\u043f\u043e\u043b\u043d\u0438\u0442\u0435\u043b\u044c\u043d\u044b\u0435 \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u044b:", None))
        self.label.setText(QCoreApplication.translate("PageTokarnayaPodrezka", u"\u041a\u043e\u043d\u0442\u0440\u043e\u043b\u0438\u0440\u0443\u0435\u043c\u0430\u044f \u0434\u043b\u0438\u043d\u0430:", None))
        self.value_length.setPrefix(QCoreApplication.translate("PageTokarnayaPodrezka", u"L= ", None))
        self.label_2.setText(QCoreApplication.translate("PageTokarnayaPodrezka", u"\u041a\u0432\u0430\u043b\u0438\u0442\u0435\u0442:", None))
        self.kavalitet_length.setText("")
        self.kavalitet_length.setPlaceholderText("")
        self.label_8.setText(QCoreApplication.translate("PageTokarnayaPodrezka", u"\u0414\u043e\u043f\u0443\u0441\u043a 1:", None))
        self.dopusk_length.setPrefix("")
        self.label_9.setText(QCoreApplication.translate("PageTokarnayaPodrezka", u"\u0414\u043e\u043f\u0443\u0441\u043a 2:", None))
        self.dopusk_length_2.setPrefix("")
        self.label_3.setText(QCoreApplication.translate("PageTokarnayaPodrezka", u"\u0428\u0435\u0440\u043e\u0445\u043e\u0432\u0430\u0442\u043e\u0441\u0442\u044c \u0442\u043e\u0440\u0446\u0435\u0432\u043e\u0439 \u043f\u043e\u0432\u0435\u0440\u0445\u043d\u043e\u0441\u0442\u0438:", None))
        self.groupBox.setTitle("")
        self.radioButton_ra1.setText(QCoreApplication.translate("PageTokarnayaPodrezka", u"Ra 0,8", None))
        self.radioButton_ra2.setText(QCoreApplication.translate("PageTokarnayaPodrezka", u"Ra 1,6", None))
        self.radioButton_ra3.setText(QCoreApplication.translate("PageTokarnayaPodrezka", u"Ra 3,2", None))
        self.radioButton_ra4.setText(QCoreApplication.translate("PageTokarnayaPodrezka", u"Ra 6,3", None))
        self.radioButton_ra5.setText(QCoreApplication.translate("PageTokarnayaPodrezka", u"Ra 12,5", None))
        self.cancel_surf_rad.setText("")
        self.btn_save.setText(QCoreApplication.translate("PageTokarnayaPodrezka", u" \u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u044f", None))
        ___qtablewidgetitem = self.table_widget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("PageTokarnayaPodrezka", u"\u0418\u043d\u0441\u0442\u0440\u0443\u043c\u0435\u043d\u0442", None))
        ___qtablewidgetitem1 = self.table_widget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("PageTokarnayaPodrezka", u"\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 [\u041c\u043e\u0436\u043d\u043e \u0438\u0437\u043c\u0435\u043d\u044f\u0442\u044c]", None))
        self.text_error_podrezka.setText("")
    # retranslateUi

