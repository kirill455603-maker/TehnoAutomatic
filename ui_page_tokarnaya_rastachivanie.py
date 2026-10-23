# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_page_tokarnaya_rastachivanie.ui'
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

class Ui_PageTokarnayaRastachivanie(object):
    def setupUi(self, PageTokarnayaRastachivanie):
        if not PageTokarnayaRastachivanie.objectName():
            PageTokarnayaRastachivanie.setObjectName(u"PageTokarnayaRastachivanie")
        PageTokarnayaRastachivanie.resize(1006, 886)
        PageTokarnayaRastachivanie.setMinimumSize(QSize(1000, 0))
        PageTokarnayaRastachivanie.setStyleSheet(u"color: white;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0, stop:0 rgba(20, 40, 80, 255), stop:1 rgba(39, 73, 109, 255));\n"
"")
        self.verticalLayout_2 = QVBoxLayout(PageTokarnayaRastachivanie)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(-1, 0, -1, 0)
        self.btn_home_tokarnaya = QPushButton(PageTokarnayaRastachivanie)
        self.btn_home_tokarnaya.setObjectName(u"btn_home_tokarnaya")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_home_tokarnaya.sizePolicy().hasHeightForWidth())
        self.btn_home_tokarnaya.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.btn_home_tokarnaya.setFont(font)
        self.btn_home_tokarnaya.setStyleSheet(u"QPushButton {\n"
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
        self.btn_home_tokarnaya.setIcon(icon)

        self.horizontalLayout_6.addWidget(self.btn_home_tokarnaya, 0, Qt.AlignmentFlag.AlignLeft)


        self.verticalLayout_2.addLayout(self.horizontalLayout_6)

        self.widget = QWidget(PageTokarnayaRastachivanie)
        self.widget.setObjectName(u"widget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(2)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy1)
        self.widget.setStyleSheet(u"border: none;\n"
"border-radius: 15px;\n"
"background: none;")
        self.verticalLayout_6 = QVBoxLayout(self.widget)
        self.verticalLayout_6.setSpacing(2)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(15, 20, 15, 0)
        self.label_4 = QLabel(self.widget)
        self.label_4.setObjectName(u"label_4")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(10)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy2)
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

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(-1, 10, -1, -1)
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_3)

        self.group_value_tochenie = QWidget(self.widget)
        self.group_value_tochenie.setObjectName(u"group_value_tochenie")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.group_value_tochenie.sizePolicy().hasHeightForWidth())
        self.group_value_tochenie.setSizePolicy(sizePolicy3)
        self.group_value_tochenie.setMouseTracking(True)
        self.group_value_tochenie.setTabletTracking(False)
        self.group_value_tochenie.setAutoFillBackground(False)
        self.group_value_tochenie.setStyleSheet(u"QWidget {\n"
"	background: none;\n"
"	border-radius: 0;\n"
"}\n"
"\n"
"\n"
"QLabel {\n"
"	background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(12, 123, 147, 255), stop:1 rgba(0, 168, 204, 255));\n"
"	padding-left: 2px;	\n"
"	color: rgb(24, 45, 76)\n"
"}\n"
"")
        self.verticalLayout = QVBoxLayout(self.group_value_tochenie)
        self.verticalLayout.setSpacing(7)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 20, 0, 20)
        self.label_2 = QLabel(self.group_value_tochenie)
        self.label_2.setObjectName(u"label_2")
        font2 = QFont()
        font2.setFamilies([u"Segoe UI Light"])
        font2.setPointSize(10)
        font2.setBold(False)
        self.label_2.setFont(font2)
        self.label_2.setStyleSheet(u"")

        self.verticalLayout.addWidget(self.label_2)

        self.widget_2 = QWidget(self.group_value_tochenie)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setStyleSheet(u"QWidget {\n"
"	background: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0, stop:0 rgba(39, 72, 109, 129), stop:1 rgba(21, 41, 81, 129));\n"
"\n"
"}\n"
"Line {\n"
"	background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(8, 81, 97, 128), stop:1 rgba(0, 117, 142, 106))\n"
"}")
        self.verticalLayout_9 = QVBoxLayout(self.widget_2)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setSpacing(10)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, -1)
        self.label = QLabel(self.widget_2)
        self.label.setObjectName(u"label")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy4)
        self.label.setMaximumSize(QSize(16777215, 300))
        self.label.setStyleSheet(u"	margin-right: 0px; /* \u0420\u0430\u0441\u0441\u0442\u043e\u044f\u043d\u0438\u0435 \u043c\u0435\u0436\u0434\u0443 \u043a\u0432\u0430\u0434\u0440\u0430\u0442\u0438\u043a\u043e\u043c \u0438 \u0442\u0435\u043a\u0441\u0442\u043e\u043c */          \n"
"	border: none;	\n"
"	color: rgb(255, 255, 255) ;	\n"
"	background: none;\n"
"	font-size: 14px;")

        self.horizontalLayout_15.addWidget(self.label)

        self.value_diameter = QDoubleSpinBox(self.widget_2)
        self.value_diameter.setObjectName(u"value_diameter")
        self.value_diameter.setEnabled(True)
        sizePolicy4.setHeightForWidth(self.value_diameter.sizePolicy().hasHeightForWidth())
        self.value_diameter.setSizePolicy(sizePolicy4)
        self.value_diameter.setMaximumSize(QSize(16777215, 16777215))
        self.value_diameter.setStyleSheet(u"QDoubleSpinBox {\n"
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
        self.value_diameter.setDecimals(2)
        self.value_diameter.setMaximum(630.000000000000000)

        self.horizontalLayout_15.addWidget(self.value_diameter)

        self.line = QFrame(self.widget_2)
        self.line.setObjectName(u"line")
        self.line.setStyleSheet(u"")
        self.line.setFrameShape(QFrame.Shape.VLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_15.addWidget(self.line)

        self.label_8 = QLabel(self.widget_2)
        self.label_8.setObjectName(u"label_8")
        sizePolicy4.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy4)
        self.label_8.setMaximumSize(QSize(16777215, 300))
        self.label_8.setStyleSheet(u"	margin-right: 0px; /* \u0420\u0430\u0441\u0441\u0442\u043e\u044f\u043d\u0438\u0435 \u043c\u0435\u0436\u0434\u0443 \u043a\u0432\u0430\u0434\u0440\u0430\u0442\u0438\u043a\u043e\u043c \u0438 \u0442\u0435\u043a\u0441\u0442\u043e\u043c */          \n"
"	border: none;	\n"
"	color: rgb(255, 255, 255) ;	\n"
"	background: none;\n"
"	font-size: 14px;")

        self.horizontalLayout_15.addWidget(self.label_8)

        self.kvalitet_diameter = QLineEdit(self.widget_2)
        self.kvalitet_diameter.setObjectName(u"kvalitet_diameter")
        self.kvalitet_diameter.setEnabled(True)
        sizePolicy4.setHeightForWidth(self.kvalitet_diameter.sizePolicy().hasHeightForWidth())
        self.kvalitet_diameter.setSizePolicy(sizePolicy4)
        self.kvalitet_diameter.setMaximumSize(QSize(16777215, 16777215))
        font3 = QFont()
        font3.setBold(False)
        self.kvalitet_diameter.setFont(font3)
        self.kvalitet_diameter.setStyleSheet(u"QLineEdit {\n"
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

        self.horizontalLayout_15.addWidget(self.kvalitet_diameter)

        self.line_2 = QFrame(self.widget_2)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setStyleSheet(u"")
        self.line_2.setFrameShape(QFrame.Shape.VLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_15.addWidget(self.line_2)

        self.label_9 = QLabel(self.widget_2)
        self.label_9.setObjectName(u"label_9")
        sizePolicy4.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy4)
        self.label_9.setMaximumSize(QSize(16777215, 300))
        self.label_9.setStyleSheet(u"	margin-right: 0px; /* \u0420\u0430\u0441\u0441\u0442\u043e\u044f\u043d\u0438\u0435 \u043c\u0435\u0436\u0434\u0443 \u043a\u0432\u0430\u0434\u0440\u0430\u0442\u0438\u043a\u043e\u043c \u0438 \u0442\u0435\u043a\u0441\u0442\u043e\u043c */          \n"
"	border: none;	\n"
"	color: rgb(255, 255, 255) ;	\n"
"	background: none;\n"
"	font-size: 14px;")

        self.horizontalLayout_15.addWidget(self.label_9)

        self.dopusk_diameter_1 = QDoubleSpinBox(self.widget_2)
        self.dopusk_diameter_1.setObjectName(u"dopusk_diameter_1")
        self.dopusk_diameter_1.setEnabled(True)
        sizePolicy4.setHeightForWidth(self.dopusk_diameter_1.sizePolicy().hasHeightForWidth())
        self.dopusk_diameter_1.setSizePolicy(sizePolicy4)
        self.dopusk_diameter_1.setMaximumSize(QSize(16777215, 16777215))
        self.dopusk_diameter_1.setStyleSheet(u"QDoubleSpinBox {\n"
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
        self.dopusk_diameter_1.setDecimals(3)
        self.dopusk_diameter_1.setMinimum(-5.000000000000000)
        self.dopusk_diameter_1.setMaximum(5.000000000000000)
        self.dopusk_diameter_1.setSingleStep(0.010000000000000)

        self.horizontalLayout_15.addWidget(self.dopusk_diameter_1)

        self.line_3 = QFrame(self.widget_2)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setStyleSheet(u"")
        self.line_3.setFrameShape(QFrame.Shape.VLine)
        self.line_3.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_15.addWidget(self.line_3)

        self.label_10 = QLabel(self.widget_2)
        self.label_10.setObjectName(u"label_10")
        sizePolicy4.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy4)
        self.label_10.setMaximumSize(QSize(16777215, 300))
        self.label_10.setStyleSheet(u"	margin-right: 0px; /* \u0420\u0430\u0441\u0441\u0442\u043e\u044f\u043d\u0438\u0435 \u043c\u0435\u0436\u0434\u0443 \u043a\u0432\u0430\u0434\u0440\u0430\u0442\u0438\u043a\u043e\u043c \u0438 \u0442\u0435\u043a\u0441\u0442\u043e\u043c */          \n"
"	border: none;	\n"
"	color: rgb(255, 255, 255) ;	\n"
"	background: none;\n"
"	font-size: 14px;")

        self.horizontalLayout_15.addWidget(self.label_10)

        self.dopusk_diameter_2 = QDoubleSpinBox(self.widget_2)
        self.dopusk_diameter_2.setObjectName(u"dopusk_diameter_2")
        self.dopusk_diameter_2.setEnabled(True)
        sizePolicy4.setHeightForWidth(self.dopusk_diameter_2.sizePolicy().hasHeightForWidth())
        self.dopusk_diameter_2.setSizePolicy(sizePolicy4)
        self.dopusk_diameter_2.setMaximumSize(QSize(16777215, 16777215))
        self.dopusk_diameter_2.setStyleSheet(u"QDoubleSpinBox {\n"
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
        self.dopusk_diameter_2.setDecimals(3)
        self.dopusk_diameter_2.setMinimum(-5.000000000000000)
        self.dopusk_diameter_2.setMaximum(5.000000000000000)
        self.dopusk_diameter_2.setSingleStep(0.010000000000000)

        self.horizontalLayout_15.addWidget(self.dopusk_diameter_2)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_5)


        self.verticalLayout_9.addLayout(self.horizontalLayout_15)


        self.verticalLayout.addWidget(self.widget_2)

        self.label_3 = QLabel(self.group_value_tochenie)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font2)

        self.verticalLayout.addWidget(self.label_3)

        self.widget_3 = QWidget(self.group_value_tochenie)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setStyleSheet(u"QWidget {\n"
"	background: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0, stop:0 rgba(39, 72, 109, 129), stop:1 rgba(21, 41, 81, 129));\n"
"\n"
"}\n"
"Line {\n"
"	background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(8, 81, 97, 128), stop:1 rgba(0, 117, 142, 106))\n"
"}")
        self.verticalLayout_10 = QVBoxLayout(self.widget_3)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setSpacing(10)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, -1)
        self.label_11 = QLabel(self.widget_3)
        self.label_11.setObjectName(u"label_11")
        sizePolicy4.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy4)
        self.label_11.setMaximumSize(QSize(16777215, 300))
        self.label_11.setStyleSheet(u"	margin-right: 0px; /* \u0420\u0430\u0441\u0441\u0442\u043e\u044f\u043d\u0438\u0435 \u043c\u0435\u0436\u0434\u0443 \u043a\u0432\u0430\u0434\u0440\u0430\u0442\u0438\u043a\u043e\u043c \u0438 \u0442\u0435\u043a\u0441\u0442\u043e\u043c */          \n"
"	border: none;	\n"
"	color: rgb(255, 255, 255) ;	\n"
"	background: none;\n"
"	font-size: 14px;")

        self.horizontalLayout_16.addWidget(self.label_11)

        self.value_length = QDoubleSpinBox(self.widget_3)
        self.value_length.setObjectName(u"value_length")
        self.value_length.setEnabled(True)
        sizePolicy4.setHeightForWidth(self.value_length.sizePolicy().hasHeightForWidth())
        self.value_length.setSizePolicy(sizePolicy4)
        self.value_length.setMaximumSize(QSize(16777215, 16777215))
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
        self.value_length.setDecimals(2)
        self.value_length.setMaximum(2000.000000000000000)

        self.horizontalLayout_16.addWidget(self.value_length)

        self.line_4 = QFrame(self.widget_3)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setStyleSheet(u"")
        self.line_4.setFrameShape(QFrame.Shape.VLine)
        self.line_4.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_16.addWidget(self.line_4)

        self.label_12 = QLabel(self.widget_3)
        self.label_12.setObjectName(u"label_12")
        sizePolicy4.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy4)
        self.label_12.setMaximumSize(QSize(16777215, 300))
        self.label_12.setStyleSheet(u"	margin-right: 0px; /* \u0420\u0430\u0441\u0441\u0442\u043e\u044f\u043d\u0438\u0435 \u043c\u0435\u0436\u0434\u0443 \u043a\u0432\u0430\u0434\u0440\u0430\u0442\u0438\u043a\u043e\u043c \u0438 \u0442\u0435\u043a\u0441\u0442\u043e\u043c */          \n"
"	border: none;	\n"
"	color: rgb(255, 255, 255) ;	\n"
"	background: none;\n"
"	font-size: 14px;")

        self.horizontalLayout_16.addWidget(self.label_12)

        self.kvalitet_length = QLineEdit(self.widget_3)
        self.kvalitet_length.setObjectName(u"kvalitet_length")
        self.kvalitet_length.setEnabled(True)
        sizePolicy4.setHeightForWidth(self.kvalitet_length.sizePolicy().hasHeightForWidth())
        self.kvalitet_length.setSizePolicy(sizePolicy4)
        self.kvalitet_length.setMaximumSize(QSize(16777215, 16777215))
        self.kvalitet_length.setFont(font3)
        self.kvalitet_length.setStyleSheet(u"QLineEdit {\n"
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

        self.horizontalLayout_16.addWidget(self.kvalitet_length)

        self.line_5 = QFrame(self.widget_3)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setStyleSheet(u"")
        self.line_5.setFrameShape(QFrame.Shape.VLine)
        self.line_5.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_16.addWidget(self.line_5)

        self.label_13 = QLabel(self.widget_3)
        self.label_13.setObjectName(u"label_13")
        sizePolicy4.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy4)
        self.label_13.setMaximumSize(QSize(16777215, 300))
        self.label_13.setStyleSheet(u"	margin-right: 0px; /* \u0420\u0430\u0441\u0441\u0442\u043e\u044f\u043d\u0438\u0435 \u043c\u0435\u0436\u0434\u0443 \u043a\u0432\u0430\u0434\u0440\u0430\u0442\u0438\u043a\u043e\u043c \u0438 \u0442\u0435\u043a\u0441\u0442\u043e\u043c */          \n"
"	border: none;	\n"
"	color: rgb(255, 255, 255) ;	\n"
"	background: none;\n"
"	font-size: 14px;")

        self.horizontalLayout_16.addWidget(self.label_13)

        self.dopusk_length_1 = QDoubleSpinBox(self.widget_3)
        self.dopusk_length_1.setObjectName(u"dopusk_length_1")
        self.dopusk_length_1.setEnabled(True)
        sizePolicy4.setHeightForWidth(self.dopusk_length_1.sizePolicy().hasHeightForWidth())
        self.dopusk_length_1.setSizePolicy(sizePolicy4)
        self.dopusk_length_1.setMaximumSize(QSize(16777215, 16777215))
        self.dopusk_length_1.setStyleSheet(u"QDoubleSpinBox {\n"
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
        self.dopusk_length_1.setDecimals(3)
        self.dopusk_length_1.setMinimum(-5.000000000000000)
        self.dopusk_length_1.setMaximum(5.000000000000000)
        self.dopusk_length_1.setSingleStep(0.010000000000000)
        self.dopusk_length_1.setValue(0.000000000000000)

        self.horizontalLayout_16.addWidget(self.dopusk_length_1)

        self.line_6 = QFrame(self.widget_3)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setStyleSheet(u"")
        self.line_6.setFrameShape(QFrame.Shape.VLine)
        self.line_6.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_16.addWidget(self.line_6)

        self.label_14 = QLabel(self.widget_3)
        self.label_14.setObjectName(u"label_14")
        sizePolicy4.setHeightForWidth(self.label_14.sizePolicy().hasHeightForWidth())
        self.label_14.setSizePolicy(sizePolicy4)
        self.label_14.setMaximumSize(QSize(16777215, 300))
        self.label_14.setStyleSheet(u"	margin-right: 0px; /* \u0420\u0430\u0441\u0441\u0442\u043e\u044f\u043d\u0438\u0435 \u043c\u0435\u0436\u0434\u0443 \u043a\u0432\u0430\u0434\u0440\u0430\u0442\u0438\u043a\u043e\u043c \u0438 \u0442\u0435\u043a\u0441\u0442\u043e\u043c */          \n"
"	border: none;	\n"
"	color: rgb(255, 255, 255) ;	\n"
"	background: none;\n"
"	font-size: 14px;")

        self.horizontalLayout_16.addWidget(self.label_14)

        self.dopusk_length_2 = QDoubleSpinBox(self.widget_3)
        self.dopusk_length_2.setObjectName(u"dopusk_length_2")
        self.dopusk_length_2.setEnabled(True)
        sizePolicy4.setHeightForWidth(self.dopusk_length_2.sizePolicy().hasHeightForWidth())
        self.dopusk_length_2.setSizePolicy(sizePolicy4)
        self.dopusk_length_2.setMaximumSize(QSize(16777215, 16777215))
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
        self.dopusk_length_2.setValue(0.000000000000000)

        self.horizontalLayout_16.addWidget(self.dopusk_length_2)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_16.addItem(self.horizontalSpacer_4)


        self.verticalLayout_10.addLayout(self.horizontalLayout_16)


        self.verticalLayout.addWidget(self.widget_3)

        self.label_6 = QLabel(self.group_value_tochenie)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font2)

        self.verticalLayout.addWidget(self.label_6)

        self.widget_4 = QWidget(self.group_value_tochenie)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setStyleSheet(u"QWidget {\n"
"	background: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0, stop:0 rgba(39, 72, 109, 129), stop:1 rgba(21, 41, 81, 129))\n"
"}\n"
"QGroupBox {\n"
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
""
                        "QRadioButton::indicator:disabled {\n"
"	background: none;\n"
"	border: 1px solid rgb(200, 200, 200);\n"
"	border-radius: 6px;\n"
"}\n"
"QRadioButton::indicator {\n"
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
"}\n"
"\n"
"")
        self.verticalLayout_4 = QVBoxLayout(self.widget_4)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, -1, 0, -1)
        self.label_15 = QLabel(self.widget_4)
        self.label_15.setObjectName(u"label_15")
        sizePolicy4.setHeightForWidth(self.label_15.sizePolicy().hasHeightForWidth())
        self.label_15.setSizePolicy(sizePolicy4)
        self.label_15.setMinimumSize(QSize(300, 0))
        self.label_15.setMaximumSize(QSize(16777215, 350))
        self.label_15.setStyleSheet(u"	margin-right: 0px; /* \u0420\u0430\u0441\u0441\u0442\u043e\u044f\u043d\u0438\u0435 \u043c\u0435\u0436\u0434\u0443 \u043a\u0432\u0430\u0434\u0440\u0430\u0442\u0438\u043a\u043e\u043c \u0438 \u0442\u0435\u043a\u0441\u0442\u043e\u043c */          \n"
"	border: none;	\n"
"	color: rgb(255, 255, 255) ;	\n"
"	background: none;\n"
"	font-size: 14px;\n"
"	wigth: 370px;")

        self.horizontalLayout_7.addWidget(self.label_15)

        self.groupBox_rad = QGroupBox(self.widget_4)
        self.groupBox_rad.setObjectName(u"groupBox_rad")
        self.groupBox_rad.setEnabled(True)
        self.groupBox_rad.setStyleSheet(u"")
        self.groupBox_rad.setAlignment(Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)
        self.l_surfs_rad = QHBoxLayout(self.groupBox_rad)
        self.l_surfs_rad.setSpacing(15)
        self.l_surfs_rad.setObjectName(u"l_surfs_rad")
        self.l_surfs_rad.setContentsMargins(0, 0, 0, 0)
        self.radioButton_ra1 = QRadioButton(self.groupBox_rad)
        self.radioButton_ra1.setObjectName(u"radioButton_ra1")
        self.radioButton_ra1.setEnabled(True)
        self.radioButton_ra1.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.radioButton_ra1.setAutoFillBackground(False)
        self.radioButton_ra1.setStyleSheet(u"")
        self.radioButton_ra1.setCheckable(True)
        self.radioButton_ra1.setChecked(False)
        self.radioButton_ra1.setAutoExclusive(True)

        self.l_surfs_rad.addWidget(self.radioButton_ra1)

        self.radioButton_ra2 = QRadioButton(self.groupBox_rad)
        self.radioButton_ra2.setObjectName(u"radioButton_ra2")
        self.radioButton_ra2.setEnabled(True)
        self.radioButton_ra2.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.radioButton_ra2.setStyleSheet(u"")
        self.radioButton_ra2.setCheckable(True)
        self.radioButton_ra2.setChecked(False)
        self.radioButton_ra2.setAutoExclusive(True)

        self.l_surfs_rad.addWidget(self.radioButton_ra2)

        self.radioButton_ra3 = QRadioButton(self.groupBox_rad)
        self.radioButton_ra3.setObjectName(u"radioButton_ra3")
        self.radioButton_ra3.setEnabled(True)
        self.radioButton_ra3.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.radioButton_ra3.setStyleSheet(u"")

        self.l_surfs_rad.addWidget(self.radioButton_ra3)

        self.radioButton_ra4 = QRadioButton(self.groupBox_rad)
        self.radioButton_ra4.setObjectName(u"radioButton_ra4")
        self.radioButton_ra4.setEnabled(True)
        self.radioButton_ra4.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.radioButton_ra4.setStyleSheet(u"")
        self.radioButton_ra4.setCheckable(True)
        self.radioButton_ra4.setChecked(False)
        self.radioButton_ra4.setAutoExclusive(True)

        self.l_surfs_rad.addWidget(self.radioButton_ra4)

        self.radioButton_ra5 = QRadioButton(self.groupBox_rad)
        self.radioButton_ra5.setObjectName(u"radioButton_ra5")
        self.radioButton_ra5.setEnabled(True)
        self.radioButton_ra5.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.radioButton_ra5.setStyleSheet(u"")
        self.radioButton_ra5.setCheckable(True)
        self.radioButton_ra5.setChecked(False)
        self.radioButton_ra5.setAutoExclusive(True)

        self.l_surfs_rad.addWidget(self.radioButton_ra5)


        self.horizontalLayout_7.addWidget(self.groupBox_rad)

        self.cancel_surf_rad = QPushButton(self.widget_4)
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

        self.horizontalLayout_7.addWidget(self.cancel_surf_rad)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_6)


        self.verticalLayout_4.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, -1, 0, -1)
        self.label_16 = QLabel(self.widget_4)
        self.label_16.setObjectName(u"label_16")
        sizePolicy4.setHeightForWidth(self.label_16.sizePolicy().hasHeightForWidth())
        self.label_16.setSizePolicy(sizePolicy4)
        self.label_16.setMinimumSize(QSize(300, 0))
        self.label_16.setMaximumSize(QSize(16777215, 350))
        self.label_16.setStyleSheet(u"	margin-right: 0px; /* \u0420\u0430\u0441\u0441\u0442\u043e\u044f\u043d\u0438\u0435 \u043c\u0435\u0436\u0434\u0443 \u043a\u0432\u0430\u0434\u0440\u0430\u0442\u0438\u043a\u043e\u043c \u0438 \u0442\u0435\u043a\u0441\u0442\u043e\u043c */          \n"
"	border: none;	\n"
"	color: rgb(255, 255, 255) ;	\n"
"	background: none;\n"
"	font-size: 14px;\n"
"	width: 370px;")

        self.horizontalLayout_10.addWidget(self.label_16)

        self.groupBox_tor = QGroupBox(self.widget_4)
        self.groupBox_tor.setObjectName(u"groupBox_tor")
        self.groupBox_tor.setEnabled(True)
        self.groupBox_tor.setStyleSheet(u"")
        self.groupBox_tor.setAlignment(Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)
        self.l_surfs_tor = QHBoxLayout(self.groupBox_tor)
        self.l_surfs_tor.setSpacing(15)
        self.l_surfs_tor.setObjectName(u"l_surfs_tor")
        self.l_surfs_tor.setContentsMargins(0, 0, 0, 0)
        self.radioButton_ra1_2 = QRadioButton(self.groupBox_tor)
        self.radioButton_ra1_2.setObjectName(u"radioButton_ra1_2")
        self.radioButton_ra1_2.setEnabled(True)
        self.radioButton_ra1_2.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.radioButton_ra1_2.setAutoFillBackground(False)
        self.radioButton_ra1_2.setStyleSheet(u"")
        self.radioButton_ra1_2.setCheckable(True)
        self.radioButton_ra1_2.setChecked(False)
        self.radioButton_ra1_2.setAutoExclusive(True)

        self.l_surfs_tor.addWidget(self.radioButton_ra1_2)

        self.radioButton_ra2_2 = QRadioButton(self.groupBox_tor)
        self.radioButton_ra2_2.setObjectName(u"radioButton_ra2_2")
        self.radioButton_ra2_2.setEnabled(True)
        self.radioButton_ra2_2.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.radioButton_ra2_2.setStyleSheet(u"")
        self.radioButton_ra2_2.setCheckable(True)
        self.radioButton_ra2_2.setChecked(False)
        self.radioButton_ra2_2.setAutoExclusive(True)

        self.l_surfs_tor.addWidget(self.radioButton_ra2_2)

        self.radioButton_ra3_2 = QRadioButton(self.groupBox_tor)
        self.radioButton_ra3_2.setObjectName(u"radioButton_ra3_2")
        self.radioButton_ra3_2.setEnabled(True)
        self.radioButton_ra3_2.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.radioButton_ra3_2.setStyleSheet(u"")

        self.l_surfs_tor.addWidget(self.radioButton_ra3_2)

        self.radioButton_ra4_2 = QRadioButton(self.groupBox_tor)
        self.radioButton_ra4_2.setObjectName(u"radioButton_ra4_2")
        self.radioButton_ra4_2.setEnabled(True)
        self.radioButton_ra4_2.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.radioButton_ra4_2.setStyleSheet(u"")
        self.radioButton_ra4_2.setCheckable(True)
        self.radioButton_ra4_2.setChecked(False)
        self.radioButton_ra4_2.setAutoExclusive(True)

        self.l_surfs_tor.addWidget(self.radioButton_ra4_2)

        self.radioButton_ra5_2 = QRadioButton(self.groupBox_tor)
        self.radioButton_ra5_2.setObjectName(u"radioButton_ra5_2")
        self.radioButton_ra5_2.setEnabled(True)
        self.radioButton_ra5_2.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.radioButton_ra5_2.setStyleSheet(u"")
        self.radioButton_ra5_2.setCheckable(True)
        self.radioButton_ra5_2.setChecked(False)
        self.radioButton_ra5_2.setAutoExclusive(True)

        self.l_surfs_tor.addWidget(self.radioButton_ra5_2)


        self.horizontalLayout_10.addWidget(self.groupBox_tor)

        self.cancel_surf_tor = QPushButton(self.widget_4)
        self.cancel_surf_tor.setObjectName(u"cancel_surf_tor")
        self.cancel_surf_tor.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.cancel_surf_tor.setStyleSheet(u"QPushButton {\n"
"	image: url(:/icons/return_white.png);\n"
"	background: none;\n"
"	padding: 5;\n"
"	widgth: 25;\n"
"	height: 25;\n"
"}\n"
"QPushButton:hover {\n"
"	image: url(:/icons/return_grey.png);\n"
"}")

        self.horizontalLayout_10.addWidget(self.cancel_surf_tor)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_8)


        self.verticalLayout_4.addLayout(self.horizontalLayout_10)


        self.verticalLayout.addWidget(self.widget_4)

        self.label_7 = QLabel(self.group_value_tochenie)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font2)

        self.verticalLayout.addWidget(self.label_7)

        self.widget_5 = QWidget(self.group_value_tochenie)
        self.widget_5.setObjectName(u"widget_5")
        self.widget_5.setStyleSheet(u"QWidget {\n"
"	background: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0, stop:0 rgba(39, 72, 109, 129), stop:1 rgba(21, 41, 81, 129));\n"
"\n"
"}\n"
"Line {\n"
"	background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(8, 81, 97, 128), stop:1 rgba(0, 117, 142, 106))\n"
"}")
        self.verticalLayout_5 = QVBoxLayout(self.widget_5)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setSpacing(15)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, -1, 0, -1)
        self.label_17 = QLabel(self.widget_5)
        self.label_17.setObjectName(u"label_17")
        sizePolicy4.setHeightForWidth(self.label_17.sizePolicy().hasHeightForWidth())
        self.label_17.setSizePolicy(sizePolicy4)
        self.label_17.setMaximumSize(QSize(16777215, 300))
        self.label_17.setStyleSheet(u"	margin-right: 0px; /* \u0420\u0430\u0441\u0441\u0442\u043e\u044f\u043d\u0438\u0435 \u043c\u0435\u0436\u0434\u0443 \u043a\u0432\u0430\u0434\u0440\u0430\u0442\u0438\u043a\u043e\u043c \u0438 \u0442\u0435\u043a\u0441\u0442\u043e\u043c */          \n"
"	border: none;	\n"
"	color: rgb(255, 255, 255) ;	\n"
"	background: none;\n"
"	font-size: 14px;")

        self.horizontalLayout_9.addWidget(self.label_17)

        self.bienie_rad = QDoubleSpinBox(self.widget_5)
        self.bienie_rad.setObjectName(u"bienie_rad")
        self.bienie_rad.setEnabled(True)
        sizePolicy4.setHeightForWidth(self.bienie_rad.sizePolicy().hasHeightForWidth())
        self.bienie_rad.setSizePolicy(sizePolicy4)
        self.bienie_rad.setMaximumSize(QSize(16777215, 16777215))
        self.bienie_rad.setStyleSheet(u"QDoubleSpinBox {\n"
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
        self.bienie_rad.setDecimals(3)
        self.bienie_rad.setMaximum(3.000000000000000)
        self.bienie_rad.setSingleStep(0.010000000000000)

        self.horizontalLayout_9.addWidget(self.bienie_rad)

        self.line_7 = QFrame(self.widget_5)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setStyleSheet(u"")
        self.line_7.setFrameShape(QFrame.Shape.VLine)
        self.line_7.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_9.addWidget(self.line_7)

        self.label_19 = QLabel(self.widget_5)
        self.label_19.setObjectName(u"label_19")
        sizePolicy4.setHeightForWidth(self.label_19.sizePolicy().hasHeightForWidth())
        self.label_19.setSizePolicy(sizePolicy4)
        self.label_19.setMaximumSize(QSize(16777215, 300))
        self.label_19.setStyleSheet(u"	margin-right: 0px; /* \u0420\u0430\u0441\u0441\u0442\u043e\u044f\u043d\u0438\u0435 \u043c\u0435\u0436\u0434\u0443 \u043a\u0432\u0430\u0434\u0440\u0430\u0442\u0438\u043a\u043e\u043c \u0438 \u0442\u0435\u043a\u0441\u0442\u043e\u043c */          \n"
"	border: none;	\n"
"	color: rgb(255, 255, 255) ;	\n"
"	background: none;\n"
"	font-size: 14px;")

        self.horizontalLayout_9.addWidget(self.label_19)

        self.baza_rad = QLineEdit(self.widget_5)
        self.baza_rad.setObjectName(u"baza_rad")
        self.baza_rad.setEnabled(True)
        sizePolicy4.setHeightForWidth(self.baza_rad.sizePolicy().hasHeightForWidth())
        self.baza_rad.setSizePolicy(sizePolicy4)
        self.baza_rad.setMaximumSize(QSize(16777215, 16777215))
        self.baza_rad.setFont(font3)
        self.baza_rad.setStyleSheet(u"QLineEdit {\n"
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

        self.horizontalLayout_9.addWidget(self.baza_rad)

        self.groupBox_2 = QGroupBox(self.widget_5)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setEnabled(True)
        self.groupBox_2.setStyleSheet(u"border: none;\n"
"background: none;")
        self.groupBox_2.setAlignment(Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)
        self.verticalLayout_7 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_7.setSpacing(5)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_9.addWidget(self.groupBox_2)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer)


        self.verticalLayout_5.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setSpacing(15)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, -1, 0, -1)
        self.label_18 = QLabel(self.widget_5)
        self.label_18.setObjectName(u"label_18")
        sizePolicy4.setHeightForWidth(self.label_18.sizePolicy().hasHeightForWidth())
        self.label_18.setSizePolicy(sizePolicy4)
        self.label_18.setMaximumSize(QSize(16777215, 300))
        self.label_18.setStyleSheet(u"	margin-right: 0px; /* \u0420\u0430\u0441\u0441\u0442\u043e\u044f\u043d\u0438\u0435 \u043c\u0435\u0436\u0434\u0443 \u043a\u0432\u0430\u0434\u0440\u0430\u0442\u0438\u043a\u043e\u043c \u0438 \u0442\u0435\u043a\u0441\u0442\u043e\u043c */          \n"
"	border: none;	\n"
"	color: rgb(255, 255, 255) ;	\n"
"	background: none;\n"
"	font-size: 14px;")

        self.horizontalLayout_11.addWidget(self.label_18)

        self.bienie_tor = QDoubleSpinBox(self.widget_5)
        self.bienie_tor.setObjectName(u"bienie_tor")
        self.bienie_tor.setEnabled(True)
        sizePolicy4.setHeightForWidth(self.bienie_tor.sizePolicy().hasHeightForWidth())
        self.bienie_tor.setSizePolicy(sizePolicy4)
        self.bienie_tor.setMaximumSize(QSize(16777215, 16777215))
        self.bienie_tor.setStyleSheet(u"QDoubleSpinBox {\n"
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
        self.bienie_tor.setDecimals(3)
        self.bienie_tor.setMaximum(3.000000000000000)
        self.bienie_tor.setSingleStep(0.010000000000000)

        self.horizontalLayout_11.addWidget(self.bienie_tor)

        self.line_8 = QFrame(self.widget_5)
        self.line_8.setObjectName(u"line_8")
        self.line_8.setStyleSheet(u"")
        self.line_8.setFrameShape(QFrame.Shape.VLine)
        self.line_8.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_11.addWidget(self.line_8)

        self.label_20 = QLabel(self.widget_5)
        self.label_20.setObjectName(u"label_20")
        sizePolicy4.setHeightForWidth(self.label_20.sizePolicy().hasHeightForWidth())
        self.label_20.setSizePolicy(sizePolicy4)
        self.label_20.setMaximumSize(QSize(16777215, 300))
        self.label_20.setStyleSheet(u"	margin-right: 0px; /* \u0420\u0430\u0441\u0441\u0442\u043e\u044f\u043d\u0438\u0435 \u043c\u0435\u0436\u0434\u0443 \u043a\u0432\u0430\u0434\u0440\u0430\u0442\u0438\u043a\u043e\u043c \u0438 \u0442\u0435\u043a\u0441\u0442\u043e\u043c */          \n"
"	border: none;	\n"
"	color: rgb(255, 255, 255) ;	\n"
"	background: none;\n"
"	font-size: 14px;")

        self.horizontalLayout_11.addWidget(self.label_20)

        self.baza_tor = QLineEdit(self.widget_5)
        self.baza_tor.setObjectName(u"baza_tor")
        self.baza_tor.setEnabled(True)
        sizePolicy4.setHeightForWidth(self.baza_tor.sizePolicy().hasHeightForWidth())
        self.baza_tor.setSizePolicy(sizePolicy4)
        self.baza_tor.setMaximumSize(QSize(16777215, 16777215))
        self.baza_tor.setFont(font3)
        self.baza_tor.setStyleSheet(u"QLineEdit {\n"
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

        self.horizontalLayout_11.addWidget(self.baza_tor)

        self.groupBox_4 = QGroupBox(self.widget_5)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setEnabled(True)
        self.groupBox_4.setStyleSheet(u"border: none;\n"
"background: none;")
        self.groupBox_4.setAlignment(Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)
        self.verticalLayout_11 = QVBoxLayout(self.groupBox_4)
        self.verticalLayout_11.setSpacing(5)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_11.addWidget(self.groupBox_4)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_2)


        self.verticalLayout_5.addLayout(self.horizontalLayout_11)


        self.verticalLayout.addWidget(self.widget_5)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(-1, -1, -1, 0)
        self.btn_save_result = QPushButton(self.group_value_tochenie)
        self.btn_save_result.setObjectName(u"btn_save_result")
        font4 = QFont()
        font4.setBold(True)
        self.btn_save_result.setFont(font4)
        self.btn_save_result.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_save_result.setStyleSheet(u"QPushButton {\n"
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
        self.btn_save_result.setIcon(icon1)
        self.btn_save_result.setIconSize(QSize(20, 20))

        self.horizontalLayout_8.addWidget(self.btn_save_result, 0, Qt.AlignmentFlag.AlignHCenter)


        self.verticalLayout.addLayout(self.horizontalLayout_8)


        self.horizontalLayout_5.addWidget(self.group_value_tochenie)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_7)


        self.verticalLayout_6.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.table_widget_rastachivanie = QTableWidget(self.widget)
        if (self.table_widget_rastachivanie.columnCount() < 2):
            self.table_widget_rastachivanie.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.table_widget_rastachivanie.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.table_widget_rastachivanie.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        self.table_widget_rastachivanie.setObjectName(u"table_widget_rastachivanie")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.table_widget_rastachivanie.sizePolicy().hasHeightForWidth())
        self.table_widget_rastachivanie.setSizePolicy(sizePolicy5)
        font5 = QFont()
        font5.setPointSize(10)
        self.table_widget_rastachivanie.setFont(font5)
        self.table_widget_rastachivanie.setStyleSheet(u"/* \u0421\u0430\u043c \u0432\u0438\u0434\u0436\u0435\u0442 \u2014 \u043f\u0440\u043e\u0437\u0440\u0430\u0447\u043d\u044b\u0439 \u0444\u043e\u043d */\n"
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
        self.table_widget_rastachivanie.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.table_widget_rastachivanie.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.table_widget_rastachivanie.setAutoScroll(False)
        self.table_widget_rastachivanie.setRowCount(0)
        self.table_widget_rastachivanie.setColumnCount(2)
        self.table_widget_rastachivanie.verticalHeader().setVisible(False)
        self.table_widget_rastachivanie.verticalHeader().setMinimumSectionSize(90)
        self.table_widget_rastachivanie.verticalHeader().setDefaultSectionSize(100)

        self.horizontalLayout_3.addWidget(self.table_widget_rastachivanie)


        self.verticalLayout_6.addLayout(self.horizontalLayout_3)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer)

        self.text_error_tochenie = QLabel(self.widget)
        self.text_error_tochenie.setObjectName(u"text_error_tochenie")
        self.text_error_tochenie.setMinimumSize(QSize(0, 30))
        self.text_error_tochenie.setFont(font5)
        self.text_error_tochenie.setStyleSheet(u"background:none;\n"
"border: none;\n"
"")
        self.text_error_tochenie.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_6.addWidget(self.text_error_tochenie)


        self.verticalLayout_2.addWidget(self.widget)


        self.retranslateUi(PageTokarnayaRastachivanie)

        QMetaObject.connectSlotsByName(PageTokarnayaRastachivanie)
    # setupUi

    def retranslateUi(self, PageTokarnayaRastachivanie):
        PageTokarnayaRastachivanie.setWindowTitle(QCoreApplication.translate("PageTokarnayaRastachivanie", u"\u0420\u0430\u0441\u0442\u0430\u0447\u0438\u0432\u0430\u043d\u0438\u0435", None))
        self.btn_home_tokarnaya.setText(QCoreApplication.translate("PageTokarnayaRastachivanie", u" \u041d\u0410\u0417\u0410\u0414", None))
        self.label_4.setText(QCoreApplication.translate("PageTokarnayaRastachivanie", u"\u0420\u0430\u0441\u0441\u0442\u0430\u0447\u0438\u0432\u0430\u043d\u0438\u0435 \u0437\u0430\u0433\u043e\u0442\u043e\u0432\u043a\u0438", None))
        self.label_2.setText(QCoreApplication.translate("PageTokarnayaRastachivanie", u"\u041f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u044b \u0434\u0438\u0430\u043c\u0435\u0442\u0440\u0430:", None))
        self.label.setText(QCoreApplication.translate("PageTokarnayaRastachivanie", u"\u0414\u0438\u0430\u043c\u0435\u0442\u0440 \u043e\u0431\u0440\u0430\u0431\u043e\u0442\u043a\u0438:", None))
        self.value_diameter.setPrefix(QCoreApplication.translate("PageTokarnayaRastachivanie", u"\u00d8 ", None))
        self.label_8.setText(QCoreApplication.translate("PageTokarnayaRastachivanie", u"\u041a\u0432\u0430\u043b\u0438\u0442\u0435\u0442:", None))
        self.kvalitet_diameter.setText("")
        self.kvalitet_diameter.setPlaceholderText(QCoreApplication.translate("PageTokarnayaRastachivanie", u"...", None))
        self.label_9.setText(QCoreApplication.translate("PageTokarnayaRastachivanie", u"\u0414\u043e\u043f\u0443\u0441\u043a 1:", None))
        self.dopusk_diameter_1.setPrefix("")
        self.label_10.setText(QCoreApplication.translate("PageTokarnayaRastachivanie", u"\u0414\u043e\u043f\u0443\u0441\u043a 2:", None))
        self.dopusk_diameter_2.setPrefix("")
        self.label_3.setText(QCoreApplication.translate("PageTokarnayaRastachivanie", u"\u041f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u044b \u0434\u043b\u0438\u043d\u044b:", None))
        self.label_11.setText(QCoreApplication.translate("PageTokarnayaRastachivanie", u"\u0414\u043b\u0438\u043d\u0430 \u043e\u0431\u0440\u0430\u0431\u043e\u0442\u043a\u0438:", None))
        self.value_length.setPrefix(QCoreApplication.translate("PageTokarnayaRastachivanie", u"L= ", None))
        self.value_length.setSuffix("")
        self.label_12.setText(QCoreApplication.translate("PageTokarnayaRastachivanie", u"\u041a\u0432\u0430\u043b\u0438\u0442\u0435\u0442:", None))
        self.kvalitet_length.setText("")
        self.kvalitet_length.setPlaceholderText(QCoreApplication.translate("PageTokarnayaRastachivanie", u"...", None))
        self.label_13.setText(QCoreApplication.translate("PageTokarnayaRastachivanie", u"\u0414\u043e\u043f\u0443\u0441\u043a 1:", None))
        self.dopusk_length_1.setPrefix("")
        self.label_14.setText(QCoreApplication.translate("PageTokarnayaRastachivanie", u"\u0414\u043e\u043f\u0443\u0441\u043a 2:", None))
        self.dopusk_length_2.setPrefix("")
        self.label_6.setText(QCoreApplication.translate("PageTokarnayaRastachivanie", u"\u041f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u044b \u0448\u0435\u0440\u043e\u0445\u043e\u0432\u0430\u0442\u043e\u0441\u0442\u0438:", None))
        self.label_15.setText(QCoreApplication.translate("PageTokarnayaRastachivanie", u"\u0428\u0435\u0440\u043e\u0445\u043e\u0432\u0430\u0442\u043e\u0441\u0442\u044c \u0440\u0430\u0434\u0438\u0430\u043b\u044c\u043d\u043e\u0439 \u043f\u043e\u0432\u0435\u0440\u0445\u043d\u043e\u0441\u0442\u0438:", None))
        self.groupBox_rad.setTitle("")
        self.radioButton_ra1.setText(QCoreApplication.translate("PageTokarnayaRastachivanie", u"Ra 0,8", None))
        self.radioButton_ra2.setText(QCoreApplication.translate("PageTokarnayaRastachivanie", u"Ra 1,6", None))
        self.radioButton_ra3.setText(QCoreApplication.translate("PageTokarnayaRastachivanie", u"Ra 3,2", None))
        self.radioButton_ra4.setText(QCoreApplication.translate("PageTokarnayaRastachivanie", u"Ra 6,3", None))
        self.radioButton_ra5.setText(QCoreApplication.translate("PageTokarnayaRastachivanie", u"Ra 12,5", None))
        self.cancel_surf_rad.setText("")
        self.label_16.setText(QCoreApplication.translate("PageTokarnayaRastachivanie", u"\u0428\u0435\u0440\u043e\u0445\u043e\u0432\u0430\u0442\u043e\u0441\u0442\u044c \u0442\u043e\u0440\u0446\u0435\u0432\u043e\u0439 \u043f\u043e\u0432\u0435\u0440\u0445\u043d\u043e\u0441\u0442\u0438:", None))
        self.groupBox_tor.setTitle("")
        self.radioButton_ra1_2.setText(QCoreApplication.translate("PageTokarnayaRastachivanie", u"Ra 0,8", None))
        self.radioButton_ra2_2.setText(QCoreApplication.translate("PageTokarnayaRastachivanie", u"Ra 1,6", None))
        self.radioButton_ra3_2.setText(QCoreApplication.translate("PageTokarnayaRastachivanie", u"Ra 3,2", None))
        self.radioButton_ra4_2.setText(QCoreApplication.translate("PageTokarnayaRastachivanie", u"Ra 6,3", None))
        self.radioButton_ra5_2.setText(QCoreApplication.translate("PageTokarnayaRastachivanie", u"Ra 12,5", None))
        self.cancel_surf_tor.setText("")
        self.label_7.setText(QCoreApplication.translate("PageTokarnayaRastachivanie", u"\u041f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u044b \u0431\u0438\u0435\u043d\u0438\u044f:", None))
        self.label_17.setText(QCoreApplication.translate("PageTokarnayaRastachivanie", u"\u0411\u0438\u0435\u043d\u0438\u0435 \u0440\u0430\u0434\u0438\u0430\u043b\u044c\u043d\u043e\u0439 \u043f\u043e\u0432\u0435\u0440\u0445\u043d\u043e\u0441\u0442\u0438:", None))
        self.bienie_rad.setPrefix("")
        self.label_19.setText(QCoreApplication.translate("PageTokarnayaRastachivanie", u"\u0411\u0430\u0437\u0430:", None))
        self.baza_rad.setText("")
        self.baza_rad.setPlaceholderText(QCoreApplication.translate("PageTokarnayaRastachivanie", u"\u0411\u0430\u0437\u0430(-\u044b)", None))
        self.groupBox_2.setTitle("")
        self.label_18.setText(QCoreApplication.translate("PageTokarnayaRastachivanie", u"\u0411\u0438\u0435\u043d\u0438\u0435 \u0442\u043e\u0440\u0446\u0435\u0432\u043e\u0439 \u043f\u043e\u0432\u0435\u0440\u0445\u043d\u043e\u0441\u0442\u0438:", None))
        self.bienie_tor.setPrefix("")
        self.label_20.setText(QCoreApplication.translate("PageTokarnayaRastachivanie", u"\u0411\u0430\u0437\u0430:", None))
        self.baza_tor.setText("")
        self.baza_tor.setPlaceholderText(QCoreApplication.translate("PageTokarnayaRastachivanie", u"\u0411\u0430\u0437\u0430(-\u044b)", None))
        self.groupBox_4.setTitle("")
        self.btn_save_result.setText(QCoreApplication.translate("PageTokarnayaRastachivanie", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u044f", None))
        ___qtablewidgetitem = self.table_widget_rastachivanie.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("PageTokarnayaRastachivanie", u"\u0418\u043d\u0441\u0442\u0440\u0443\u043c\u0435\u043d\u0442", None))
        ___qtablewidgetitem1 = self.table_widget_rastachivanie.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("PageTokarnayaRastachivanie", u"\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435", None))
        self.text_error_tochenie.setText("")
    # retranslateUi

