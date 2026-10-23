# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_page_kontrol_otk.ui'
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
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QCheckBox, QComboBox,
    QDoubleSpinBox, QFrame, QGroupBox, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QSpinBox, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_PageKontrolOtk(object):
    def setupUi(self, PageKontrolOtk):
        if not PageKontrolOtk.objectName():
            PageKontrolOtk.setObjectName(u"PageKontrolOtk")
        PageKontrolOtk.resize(913, 1136)
        PageKontrolOtk.setStyleSheet(u"color: white;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(0, 57, 95), stop:1 rgb(0, 83, 122));\n"
"")
        self.verticalLayout = QVBoxLayout(PageKontrolOtk)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.btn_home = QPushButton(PageKontrolOtk)
        self.btn_home.setObjectName(u"btn_home")
        self.btn_home.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_home.setStyleSheet(u"QPushButton {\n"
"	border: 1px solid;\n"
"	border-color: white;\n"
"	border-radius: 10px;\n"
"	height: 20px;\n"
"	width: 100px;\n"
"	background-color: none;\n"
"	padding: 2 5 5 2;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(0, 111, 171)\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: rgb(0, 53, 93)\n"
"}")

        self.verticalLayout.addWidget(self.btn_home, 0, Qt.AlignmentFlag.AlignLeft)

        self.label_9 = QLabel(PageKontrolOtk)
        self.label_9.setObjectName(u"label_9")
        font = QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet(u"background: none;\n"
"")

        self.verticalLayout.addWidget(self.label_9, 0, Qt.AlignmentFlag.AlignHCenter)

        self.label_6 = QLabel(PageKontrolOtk)
        self.label_6.setObjectName(u"label_6")
        font1 = QFont()
        font1.setPointSize(10)
        self.label_6.setFont(font1)
        self.label_6.setStyleSheet(u"background: none;\n"
"")

        self.verticalLayout.addWidget(self.label_6, 0, Qt.AlignmentFlag.AlignHCenter)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, 0, -1, -1)
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self.btn_diameter = QPushButton(PageKontrolOtk)
        self.btn_diameter.setObjectName(u"btn_diameter")
        self.btn_diameter.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_diameter.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background: rgba(154, 154, 154, 60);\n"
"	padding: 5 5 5 5;\n"
"	height: 15px;\n"
"	width: 120px;\n"
"	border-radius:  0;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background: rgba(11, 31, 139,30);\n"
"	border-bottom: 1px solid rgba(255, 255, 255, 20);\n"
"	\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"	background: rgba(11, 31, 139,90);\n"
"	border-bottom: 1px solid white;\n"
"	\n"
"}\n"
"")
        self.btn_diameter.setCheckable(True)
        self.btn_diameter.setChecked(True)
        self.btn_diameter.setAutoExclusive(True)

        self.horizontalLayout_3.addWidget(self.btn_diameter)

        self.btn_length = QPushButton(PageKontrolOtk)
        self.btn_length.setObjectName(u"btn_length")
        self.btn_length.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_length.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background: rgba(154, 154, 154, 60);\n"
"	padding: 5 5 5 5;\n"
"	height: 15px;\n"
"	width: 120px;\n"
"	border-radius:  0;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background: rgba(11, 31, 139,30);\n"
"	border-bottom: 1px solid rgba(255, 255, 255, 20);\n"
"	\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"	background: rgba(11, 31, 139,90);\n"
"	border-bottom: 1px solid white;\n"
"	\n"
"}\n"
"")
        self.btn_length.setCheckable(True)
        self.btn_length.setAutoExclusive(True)

        self.horizontalLayout_3.addWidget(self.btn_length)

        self.btn_hole = QPushButton(PageKontrolOtk)
        self.btn_hole.setObjectName(u"btn_hole")
        self.btn_hole.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_hole.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background: rgba(154, 154, 154, 60);\n"
"	padding: 5 5 5 5;\n"
"	height: 15px;\n"
"	width: 120px;\n"
"	border-radius:  0;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background: rgba(11, 31, 139,30);\n"
"	border-bottom: 1px solid rgba(255, 255, 255, 20);\n"
"	\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"	background: rgba(11, 31, 139,90);\n"
"	border-bottom: 1px solid white;\n"
"	\n"
"}\n"
"")
        self.btn_hole.setCheckable(True)
        self.btn_hole.setAutoExclusive(True)

        self.horizontalLayout_3.addWidget(self.btn_hole)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.pushButton_reset = QPushButton(PageKontrolOtk)
        self.pushButton_reset.setObjectName(u"pushButton_reset")
        self.pushButton_reset.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_reset.setStyleSheet(u"QPushButton {\n"
"	border: 1px solid;\n"
"	border-color: white;\n"
"	border-radius: 2px;\n"
"	height: 20px;\n"
"	width: 100px;\n"
"	background-color: none;\n"
"	padding: 2 5 2 5\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(0, 111, 171)\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: rgb(0, 53, 93)\n"
"}")

        self.verticalLayout.addWidget(self.pushButton_reset, 0, Qt.AlignmentFlag.AlignHCenter)

        self.verticalWidget = QWidget(PageKontrolOtk)
        self.verticalWidget.setObjectName(u"verticalWidget")
        self.verticalWidget.setStyleSheet(u"background: none;")
        self.verticalLayout_3 = QVBoxLayout(self.verticalWidget)
        self.verticalLayout_3.setSpacing(5)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.groupBox = QGroupBox(self.verticalWidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setStyleSheet(u"border: none;\n"
"background: none;")
        self.horizontalLayout_2 = QHBoxLayout(self.groupBox)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.radioButton_otv = QPushButton(self.groupBox)
        self.radioButton_otv.setObjectName(u"radioButton_otv")
        self.radioButton_otv.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.radioButton_otv.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background: rgba(154, 154, 154, 60);\n"
"	padding: 5 5 5 5;\n"
"	height: 15px;\n"
"	width: 120px;\n"
"	border-radius:  0;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background: rgba(11, 31, 139,30);\n"
"	border-bottom: 1px solid rgba(255, 255, 255, 20);\n"
"	\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"	background: rgba(11, 31, 139,90);\n"
"	border-bottom: 1px solid white;\n"
"	\n"
"}\n"
"")
        self.radioButton_otv.setCheckable(True)
        self.radioButton_otv.setChecked(True)
        self.radioButton_otv.setAutoExclusive(True)

        self.horizontalLayout_2.addWidget(self.radioButton_otv)

        self.radioButton_val = QPushButton(self.groupBox)
        self.radioButton_val.setObjectName(u"radioButton_val")
        self.radioButton_val.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.radioButton_val.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background: rgba(154, 154, 154, 60);\n"
"	padding: 5 5 5 5;\n"
"	height: 15px;\n"
"	width: 120px;\n"
"	border-radius:  0;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background: rgba(11, 31, 139,30);\n"
"	border-bottom: 1px solid rgba(255, 255, 255, 20);\n"
"	\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"	background: rgba(11, 31, 139,90);\n"
"	border-bottom: 1px solid white;\n"
"	\n"
"}\n"
"")
        self.radioButton_val.setCheckable(True)
        self.radioButton_val.setChecked(False)
        self.radioButton_val.setAutoExclusive(True)

        self.horizontalLayout_2.addWidget(self.radioButton_val)


        self.verticalLayout_3.addWidget(self.groupBox, 0, Qt.AlignmentFlag.AlignHCenter)

        self.checkBox_rezba = QCheckBox(self.verticalWidget)
        self.checkBox_rezba.setObjectName(u"checkBox_rezba")
        self.checkBox_rezba.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.checkBox_rezba.setStyleSheet(u"QCheckBox::indicator {\n"
"  width: 10px;          \n"
"  height: 10px;         \n"
"  border: 2px solid white;         \n"
"  border-radius: 2px; /* \u0421\u043a\u0440\u0443\u0433\u043b\u0435\u043d\u043d\u044b\u0435 \u0443\u0433\u043b\u044b */          \n"
"  background-color: #FFFFFF;      \n"
"}\n"
"QCheckBox {\n"
"	spacing: 15px; /* \u0420\u0430\u0441\u0441\u0442\u043e\u044f\u043d\u0438\u0435 \u043c\u0435\u0436\u0434\u0443 \u043a\u0432\u0430\u0434\u0440\u0430\u0442\u0438\u043a\u043e\u043c \u0438 \u0442\u0435\u043a\u0441\u0442\u043e\u043c */          \n"
"	border: none;	\n"
"	color: rgb(255, 255, 255) ;	\n"
"	background: none;\n"
"	font-size: 14px;\n"
"	margin-right: 0px\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"  width: 10px;          \n"
"  height: 10px;         \n"
"  border: 2px solid white;         \n"
"  border-radius: 2px; /* \u0421\u043a\u0440\u0443\u0433\u043b\u0435\u043d\u043d\u044b\u0435 \u0443\u0433\u043b\u044b */          \n"
"  background-color: rgb(77, 77, 77);    \n"
"}\n"
"QCheckBox::ind"
                        "icator:hover {\n"
"  width: 10px;          \n"
"  height: 10px;         \n"
"  border: 2px solid rgb(136, 136, 136);         \n"
"  border-radius: 2px; /* \u0421\u043a\u0440\u0443\u0433\u043b\u0435\u043d\u043d\u044b\u0435 \u0443\u0433\u043b\u044b */          \n"
"  background-color: rgb(77, 77, 77);         \n"
"}\n"
"QCheckBox::indicator:disabled {\n"
"  width: 10px;          \n"
"  height: 10px;         \n"
"  border: 2px solid rgb(136, 136, 136);         \n"
"  border-radius: 2px; /* \u0421\u043a\u0440\u0443\u0433\u043b\u0435\u043d\u043d\u044b\u0435 \u0443\u0433\u043b\u044b */          \n"
"  background-color: rgb(86, 86, 86);         \n"
"}")

        self.verticalLayout_3.addWidget(self.checkBox_rezba, 0, Qt.AlignmentFlag.AlignHCenter)

        self.rezba_holes_2 = QWidget(self.verticalWidget)
        self.rezba_holes_2.setObjectName(u"rezba_holes_2")
        self.rezba_holes_2.setStyleSheet(u"background: none;")
        self.horizontalLayout_11 = QHBoxLayout(self.rezba_holes_2)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(1, 1, 1, 1)
        self.horizontalSpacer_15 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_15)

        self.label_23 = QLabel(self.rezba_holes_2)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setFont(font1)
        self.label_23.setStyleSheet(u"background: none;\n"
"")

        self.horizontalLayout_11.addWidget(self.label_23, 0, Qt.AlignmentFlag.AlignHCenter)

        self.comboBox_rezba_d = QComboBox(self.rezba_holes_2)
        self.comboBox_rezba_d.setObjectName(u"comboBox_rezba_d")
        font2 = QFont()
        font2.setPointSize(11)
        self.comboBox_rezba_d.setFont(font2)
        self.comboBox_rezba_d.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.comboBox_rezba_d.setStyleSheet(u"QComboBox {\n"
"	padding: 5, 5, 5, 5;\n"
"	width: 60px;\n"
"	border: none;\n"
"	border-bottom: 1px solid white;\n"
"	background: rgba(255, 255, 255, 0);\n"
"	transition: color 0.3s ease;\n"
"	transition: border-bottom 0.4s ease;\n"
"	color: rgb(204, 204, 204);\n"
"	font-size: 11pt;\n"
"}\n"
"QComboBox:hover {\n"
"   color: rgb(167, 167, 167);\n"
"}\n"
"\n"
"QComboBox::item {\n"
"	background: rgb(67, 67, 67);\n"
"	border-radius: none;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"	border-radius: none;\n"
"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(58, 58, 58), stop:1 rgb(88, 88, 88));\n"
"	selection-border-radius: none;\n"
"	selection-border: none;\n"
"	border: none;\n"
"	border-radius: 0;\n"
"	outline: none;\n"
"}\n"
"QComboBox QAbstractItemView::item {\n"
"    min-height: 15px;\n"
"	width: 15px;\n"
"	border: none;\n"
"	border-radius: none;\n"
"}\n"
"QComboBox QAbstractItemView::item:hover {\n"
"	color:rgb(173, 173, 173);\n"
"	border-bottom: 1px solid white;\n"
"}\n"
"\n"
"")

        self.horizontalLayout_11.addWidget(self.comboBox_rezba_d)

        self.line_13 = QFrame(self.rezba_holes_2)
        self.line_13.setObjectName(u"line_13")
        self.line_13.setStyleSheet(u"background: rgba(124, 124, 124, 40)")
        self.line_13.setFrameShape(QFrame.Shape.VLine)
        self.line_13.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_11.addWidget(self.line_13)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(-1, -1, 0, -1)
        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(-1, -1, 0, -1)
        self.label_24 = QLabel(self.rezba_holes_2)
        self.label_24.setObjectName(u"label_24")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_24.sizePolicy().hasHeightForWidth())
        self.label_24.setSizePolicy(sizePolicy)
        self.label_24.setMinimumSize(QSize(0, 0))
        font3 = QFont()
        font3.setFamilies([u"Onyx"])
        font3.setPointSize(11)
        self.label_24.setFont(font3)
        self.label_24.setStyleSheet(u"background-color: none")
        self.label_24.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_12.addWidget(self.label_24, 0, Qt.AlignmentFlag.AlignHCenter)

        self.comboBox_step_d = QComboBox(self.rezba_holes_2)
        self.comboBox_step_d.setObjectName(u"comboBox_step_d")
        self.comboBox_step_d.setFont(font2)
        self.comboBox_step_d.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.comboBox_step_d.setStyleSheet(u"QComboBox {\n"
"	padding: 5, 5, 5, 5;\n"
"	width: 60px;\n"
"	border: none;\n"
"	border-bottom: 1px solid white;\n"
"	background: rgba(255, 255, 255, 0);\n"
"	transition: color 0.3s ease;\n"
"	transition: border-bottom 0.4s ease;\n"
"	color: rgb(204, 204, 204);\n"
"	font-size: 11pt;\n"
"}\n"
"QComboBox:hover {\n"
"   color: rgb(167, 167, 167);\n"
"}\n"
"\n"
"QComboBox::item {\n"
"	background: rgb(67, 67, 67);\n"
"	border-radius: none;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"	border-radius: none;\n"
"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(58, 58, 58), stop:1 rgb(88, 88, 88));\n"
"	selection-border-radius: none;\n"
"	selection-border: none;\n"
"	border: none;\n"
"	border-radius: 0;\n"
"	outline: none;\n"
"}\n"
"QComboBox QAbstractItemView::item {\n"
"    min-height: 15px;\n"
"	width: 15px;\n"
"	border: none;\n"
"	border-radius: none;\n"
"}\n"
"QComboBox QAbstractItemView::item:hover {\n"
"	color:rgb(173, 173, 173);\n"
"	border-bottom: 1px solid white;\n"
"}\n"
"\n"
"")

        self.horizontalLayout_12.addWidget(self.comboBox_step_d, 0, Qt.AlignmentFlag.AlignHCenter)


        self.verticalLayout_7.addLayout(self.horizontalLayout_12)

        self.label_25 = QLabel(self.rezba_holes_2)
        self.label_25.setObjectName(u"label_25")
        font4 = QFont()
        font4.setWeight(QFont.Light)
        font4.setItalic(False)
        font4.setUnderline(False)
        font4.setKerning(True)
        self.label_25.setFont(font4)
        self.label_25.setStyleSheet(u"background-color: none;\n"
"color: rgb(175, 175, 175)\n"
"")

        self.verticalLayout_7.addWidget(self.label_25, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)


        self.horizontalLayout_11.addLayout(self.verticalLayout_7)

        self.line_16 = QFrame(self.rezba_holes_2)
        self.line_16.setObjectName(u"line_16")
        self.line_16.setStyleSheet(u"background: rgba(124, 124, 124, 40)")
        self.line_16.setFrameShape(QFrame.Shape.VLine)
        self.line_16.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_11.addWidget(self.line_16)

        self.label_26 = QLabel(self.rezba_holes_2)
        self.label_26.setObjectName(u"label_26")
        sizePolicy.setHeightForWidth(self.label_26.sizePolicy().hasHeightForWidth())
        self.label_26.setSizePolicy(sizePolicy)
        self.label_26.setFont(font3)
        self.label_26.setStyleSheet(u"background-color: none")
        self.label_26.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_11.addWidget(self.label_26)

        self.comboBox_dopusk_2 = QComboBox(self.rezba_holes_2)
        self.comboBox_dopusk_2.setObjectName(u"comboBox_dopusk_2")
        self.comboBox_dopusk_2.setFont(font2)
        self.comboBox_dopusk_2.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.comboBox_dopusk_2.setStyleSheet(u"QComboBox {\n"
"	padding: 5, 5, 5, 5;\n"
"	width: 60px;\n"
"	border: none;\n"
"	border-bottom: 1px solid white;\n"
"	background: rgba(255, 255, 255, 0);\n"
"	transition: color 0.3s ease;\n"
"	transition: border-bottom 0.4s ease;\n"
"	color: rgb(204, 204, 204);\n"
"	font-size: 11pt;\n"
"}\n"
"QComboBox:hover {\n"
"   color: rgb(167, 167, 167);\n"
"}\n"
"\n"
"QComboBox::item {\n"
"	background: rgb(67, 67, 67);\n"
"	border-radius: none;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"	border-radius: none;\n"
"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(58, 58, 58), stop:1 rgb(88, 88, 88));\n"
"	selection-border-radius: none;\n"
"	selection-border: none;\n"
"	border: none;\n"
"	border-radius: 0;\n"
"	outline: none;\n"
"}\n"
"QComboBox QAbstractItemView::item {\n"
"    min-height: 15px;\n"
"	width: 15px;\n"
"	border: none;\n"
"	border-radius: none;\n"
"}\n"
"QComboBox QAbstractItemView::item:hover {\n"
"	color:rgb(173, 173, 173);\n"
"	border-bottom: 1px solid white;\n"
"}\n"
"\n"
"")

        self.horizontalLayout_11.addWidget(self.comboBox_dopusk_2)

        self.horizontalSpacer_16 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_16)


        self.verticalLayout_3.addWidget(self.rezba_holes_2)

        self.widget = QWidget(self.verticalWidget)
        self.widget.setObjectName(u"widget")
        self.widget.setStyleSheet(u"background: none;")
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, 1, -1, -1)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setFont(font1)
        self.label.setStyleSheet(u"background: none;\n"
"")

        self.horizontalLayout.addWidget(self.label, 0, Qt.AlignmentFlag.AlignHCenter)

        self.doubleSpinBox_nom_diameter = QDoubleSpinBox(self.widget)
        self.doubleSpinBox_nom_diameter.setObjectName(u"doubleSpinBox_nom_diameter")
        self.doubleSpinBox_nom_diameter.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.doubleSpinBox_nom_diameter.setStyleSheet(u"QDoubleSpinBox {\n"
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
        self.doubleSpinBox_nom_diameter.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.doubleSpinBox_nom_diameter.setDecimals(3)
        self.doubleSpinBox_nom_diameter.setMinimum(0.000000000000000)
        self.doubleSpinBox_nom_diameter.setMaximum(1000.000000000000000)
        self.doubleSpinBox_nom_diameter.setStepType(QAbstractSpinBox.StepType.DefaultStepType)

        self.horizontalLayout.addWidget(self.doubleSpinBox_nom_diameter, 0, Qt.AlignmentFlag.AlignHCenter)

        self.line = QFrame(self.widget)
        self.line.setObjectName(u"line")
        self.line.setStyleSheet(u"background: rgba(124, 124, 124, 40)")
        self.line.setFrameShape(QFrame.Shape.VLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout.addWidget(self.line)

        self.label_5 = QLabel(self.widget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font1)
        self.label_5.setStyleSheet(u"background: none;\n"
"")

        self.horizontalLayout.addWidget(self.label_5)

        self.lineEdit_kvalitet = QLineEdit(self.widget)
        self.lineEdit_kvalitet.setObjectName(u"lineEdit_kvalitet")
        self.lineEdit_kvalitet.setMinimumSize(QSize(0, 0))
        self.lineEdit_kvalitet.setStyleSheet(u"padding: 5, 5, 5, 5;\n"
"border: none;\n"
"border-bottom: 1px solid white;\n"
"background: rgba(255, 255, 255, 0);\n"
"transition: color 0.3s ease;\n"
"transition: border-bottom 0.4s ease;\n"
"color: rgb(204, 204, 204);\n"
"font-size: 10pt;")

        self.horizontalLayout.addWidget(self.lineEdit_kvalitet)

        self.line_2 = QFrame(self.widget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setStyleSheet(u"background: rgba(124, 124, 124, 40)")
        self.line_2.setFrameShape(QFrame.Shape.VLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout.addWidget(self.line_2)

        self.label_7 = QLabel(self.widget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font1)
        self.label_7.setStyleSheet(u"background: none;\n"
"")

        self.horizontalLayout.addWidget(self.label_7)

        self.doubleSpinBox_dopusk_1 = QDoubleSpinBox(self.widget)
        self.doubleSpinBox_dopusk_1.setObjectName(u"doubleSpinBox_dopusk_1")
        self.doubleSpinBox_dopusk_1.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.doubleSpinBox_dopusk_1.setStyleSheet(u"QDoubleSpinBox {\n"
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
        self.doubleSpinBox_dopusk_1.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.doubleSpinBox_dopusk_1.setDecimals(3)
        self.doubleSpinBox_dopusk_1.setMinimum(-10.000000000000000)
        self.doubleSpinBox_dopusk_1.setMaximum(10.000000000000000)
        self.doubleSpinBox_dopusk_1.setSingleStep(0.100000000000000)
        self.doubleSpinBox_dopusk_1.setValue(0.000000000000000)

        self.horizontalLayout.addWidget(self.doubleSpinBox_dopusk_1)

        self.line_4 = QFrame(self.widget)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setStyleSheet(u"background: rgba(124, 124, 124, 40)")
        self.line_4.setFrameShape(QFrame.Shape.VLine)
        self.line_4.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout.addWidget(self.line_4)

        self.label_8 = QLabel(self.widget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font1)
        self.label_8.setStyleSheet(u"background: none;\n"
"")

        self.horizontalLayout.addWidget(self.label_8)

        self.doubleSpinBox_dopusk_2 = QDoubleSpinBox(self.widget)
        self.doubleSpinBox_dopusk_2.setObjectName(u"doubleSpinBox_dopusk_2")
        self.doubleSpinBox_dopusk_2.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.doubleSpinBox_dopusk_2.setStyleSheet(u"QDoubleSpinBox {\n"
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
        self.doubleSpinBox_dopusk_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.doubleSpinBox_dopusk_2.setDecimals(3)
        self.doubleSpinBox_dopusk_2.setMinimum(-10.000000000000000)
        self.doubleSpinBox_dopusk_2.setMaximum(10.000000000000000)
        self.doubleSpinBox_dopusk_2.setSingleStep(0.100000000000000)
        self.doubleSpinBox_dopusk_2.setValue(0.000000000000000)

        self.horizontalLayout.addWidget(self.doubleSpinBox_dopusk_2)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_4)


        self.verticalLayout_3.addWidget(self.widget)


        self.verticalLayout.addWidget(self.verticalWidget)

        self.holes = QWidget(PageKontrolOtk)
        self.holes.setObjectName(u"holes")
        self.holes.setStyleSheet(u"background: none;")
        self.verticalLayout_4 = QVBoxLayout(self.holes)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 20)
        self.groupBox_3 = QGroupBox(self.holes)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setStyleSheet(u"border: none;\n"
"background: none;")
        self.horizontalLayout_7 = QHBoxLayout(self.groupBox_3)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.btn_gladkie = QPushButton(self.groupBox_3)
        self.btn_gladkie.setObjectName(u"btn_gladkie")
        self.btn_gladkie.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_gladkie.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background: rgba(154, 154, 154, 60);\n"
"	padding: 5 5 5 5;\n"
"	height: 15px;\n"
"	width: 120px;\n"
"	border-radius:  0;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background: rgba(11, 31, 139,30);\n"
"	border-bottom: 1px solid rgba(255, 255, 255, 20);\n"
"	\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"	background: rgba(11, 31, 139,90);\n"
"	border-bottom: 1px solid white;\n"
"	\n"
"}\n"
"")
        self.btn_gladkie.setCheckable(True)
        self.btn_gladkie.setChecked(True)
        self.btn_gladkie.setAutoExclusive(True)

        self.horizontalLayout_7.addWidget(self.btn_gladkie)

        self.btn_rezba = QPushButton(self.groupBox_3)
        self.btn_rezba.setObjectName(u"btn_rezba")
        self.btn_rezba.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_rezba.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background: rgba(154, 154, 154, 60);\n"
"	padding: 5 5 5 5;\n"
"	height: 15px;\n"
"	width: 120px;\n"
"	border-radius:  0;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background: rgba(11, 31, 139,30);\n"
"	border-bottom: 1px solid rgba(255, 255, 255, 20);\n"
"	\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"	background: rgba(11, 31, 139,90);\n"
"	border-bottom: 1px solid white;\n"
"	\n"
"}\n"
"")
        self.btn_rezba.setCheckable(True)
        self.btn_rezba.setChecked(False)
        self.btn_rezba.setAutoExclusive(True)

        self.horizontalLayout_7.addWidget(self.btn_rezba)


        self.verticalLayout_4.addWidget(self.groupBox_3, 0, Qt.AlignmentFlag.AlignHCenter)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setSpacing(10)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(-1, -1, -1, 0)
        self.gladkie_holes = QWidget(self.holes)
        self.gladkie_holes.setObjectName(u"gladkie_holes")
        self.gladkie_holes.setStyleSheet(u"background: none;")
        self.horizontalLayout_4 = QHBoxLayout(self.gladkie_holes)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(1, 1, 1, 1)
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_5)

        self.label_3 = QLabel(self.gladkie_holes)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font1)
        self.label_3.setStyleSheet(u"background: none;\n"
"")

        self.horizontalLayout_4.addWidget(self.label_3, 0, Qt.AlignmentFlag.AlignHCenter)

        self.doubleSpinBox_nom_diameter_3 = QDoubleSpinBox(self.gladkie_holes)
        self.doubleSpinBox_nom_diameter_3.setObjectName(u"doubleSpinBox_nom_diameter_3")
        self.doubleSpinBox_nom_diameter_3.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.doubleSpinBox_nom_diameter_3.setStyleSheet(u"QDoubleSpinBox {\n"
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
        self.doubleSpinBox_nom_diameter_3.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.doubleSpinBox_nom_diameter_3.setDecimals(3)
        self.doubleSpinBox_nom_diameter_3.setMinimum(0.000000000000000)
        self.doubleSpinBox_nom_diameter_3.setMaximum(1000.000000000000000)
        self.doubleSpinBox_nom_diameter_3.setStepType(QAbstractSpinBox.StepType.DefaultStepType)

        self.horizontalLayout_4.addWidget(self.doubleSpinBox_nom_diameter_3)

        self.line_5 = QFrame(self.gladkie_holes)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setStyleSheet(u"background: rgba(124, 124, 124, 40)")
        self.line_5.setFrameShape(QFrame.Shape.VLine)
        self.line_5.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_4.addWidget(self.line_5)

        self.label_10 = QLabel(self.gladkie_holes)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font1)
        self.label_10.setStyleSheet(u"background: none;\n"
"")

        self.horizontalLayout_4.addWidget(self.label_10)

        self.lineEdit_kvalitet_2 = QLineEdit(self.gladkie_holes)
        self.lineEdit_kvalitet_2.setObjectName(u"lineEdit_kvalitet_2")
        self.lineEdit_kvalitet_2.setMinimumSize(QSize(0, 0))
        self.lineEdit_kvalitet_2.setStyleSheet(u"padding: 5, 5, 5, 5;\n"
"border: none;\n"
"border-bottom: 1px solid white;\n"
"background: rgba(255, 255, 255, 0);\n"
"transition: color 0.3s ease;\n"
"transition: border-bottom 0.4s ease;\n"
"color: rgb(204, 204, 204);\n"
"font-size: 10pt;")

        self.horizontalLayout_4.addWidget(self.lineEdit_kvalitet_2)

        self.line_6 = QFrame(self.gladkie_holes)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setStyleSheet(u"background: rgba(124, 124, 124, 40)")
        self.line_6.setFrameShape(QFrame.Shape.VLine)
        self.line_6.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_4.addWidget(self.line_6)

        self.label_11 = QLabel(self.gladkie_holes)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font1)
        self.label_11.setStyleSheet(u"background: none;\n"
"")

        self.horizontalLayout_4.addWidget(self.label_11)

        self.doubleSpinBox_dopusk_3 = QDoubleSpinBox(self.gladkie_holes)
        self.doubleSpinBox_dopusk_3.setObjectName(u"doubleSpinBox_dopusk_3")
        self.doubleSpinBox_dopusk_3.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.doubleSpinBox_dopusk_3.setStyleSheet(u"QDoubleSpinBox {\n"
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
        self.doubleSpinBox_dopusk_3.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.doubleSpinBox_dopusk_3.setDecimals(3)
        self.doubleSpinBox_dopusk_3.setMinimum(-10.000000000000000)
        self.doubleSpinBox_dopusk_3.setMaximum(10.000000000000000)
        self.doubleSpinBox_dopusk_3.setSingleStep(0.100000000000000)
        self.doubleSpinBox_dopusk_3.setValue(0.000000000000000)

        self.horizontalLayout_4.addWidget(self.doubleSpinBox_dopusk_3)

        self.line_7 = QFrame(self.gladkie_holes)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setStyleSheet(u"background: rgba(124, 124, 124, 40)")
        self.line_7.setFrameShape(QFrame.Shape.VLine)
        self.line_7.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_4.addWidget(self.line_7)

        self.label_12 = QLabel(self.gladkie_holes)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font1)
        self.label_12.setStyleSheet(u"background: none;\n"
"")

        self.horizontalLayout_4.addWidget(self.label_12)

        self.doubleSpinBox_dopusk_4 = QDoubleSpinBox(self.gladkie_holes)
        self.doubleSpinBox_dopusk_4.setObjectName(u"doubleSpinBox_dopusk_4")
        self.doubleSpinBox_dopusk_4.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.doubleSpinBox_dopusk_4.setStyleSheet(u"QDoubleSpinBox {\n"
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
        self.doubleSpinBox_dopusk_4.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.doubleSpinBox_dopusk_4.setDecimals(3)
        self.doubleSpinBox_dopusk_4.setMinimum(-10.000000000000000)
        self.doubleSpinBox_dopusk_4.setMaximum(10.000000000000000)
        self.doubleSpinBox_dopusk_4.setSingleStep(0.100000000000000)
        self.doubleSpinBox_dopusk_4.setValue(0.000000000000000)

        self.horizontalLayout_4.addWidget(self.doubleSpinBox_dopusk_4)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_6)


        self.verticalLayout_5.addWidget(self.gladkie_holes)

        self.rezba_holes = QWidget(self.holes)
        self.rezba_holes.setObjectName(u"rezba_holes")
        self.rezba_holes.setStyleSheet(u"background: none;")
        self.horizontalLayout_8 = QHBoxLayout(self.rezba_holes)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(1, 1, 1, 1)
        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_11)

        self.label_17 = QLabel(self.rezba_holes)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setFont(font1)
        self.label_17.setStyleSheet(u"background: none;\n"
"")

        self.horizontalLayout_8.addWidget(self.label_17, 0, Qt.AlignmentFlag.AlignHCenter)

        self.comboBox_diameter = QComboBox(self.rezba_holes)
        self.comboBox_diameter.setObjectName(u"comboBox_diameter")
        self.comboBox_diameter.setFont(font2)
        self.comboBox_diameter.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.comboBox_diameter.setStyleSheet(u"QComboBox {\n"
"	padding: 5, 5, 5, 5;\n"
"	width: 60px;\n"
"	border: none;\n"
"	border-bottom: 1px solid white;\n"
"	background: rgba(255, 255, 255, 0);\n"
"	transition: color 0.3s ease;\n"
"	transition: border-bottom 0.4s ease;\n"
"	color: rgb(204, 204, 204);\n"
"	font-size: 11pt;\n"
"}\n"
"QComboBox:hover {\n"
"   color: rgb(167, 167, 167);\n"
"}\n"
"\n"
"QComboBox::item {\n"
"	background: rgb(67, 67, 67);\n"
"	border-radius: none;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"	border-radius: none;\n"
"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(58, 58, 58), stop:1 rgb(88, 88, 88));\n"
"	selection-border-radius: none;\n"
"	selection-border: none;\n"
"	border: none;\n"
"	border-radius: 0;\n"
"	outline: none;\n"
"}\n"
"QComboBox QAbstractItemView::item {\n"
"    min-height: 15px;\n"
"	width: 15px;\n"
"	border: none;\n"
"	border-radius: none;\n"
"}\n"
"QComboBox QAbstractItemView::item:hover {\n"
"	color:rgb(173, 173, 173);\n"
"	border-bottom: 1px solid white;\n"
"}\n"
"\n"
"")

        self.horizontalLayout_8.addWidget(self.comboBox_diameter)

        self.line_11 = QFrame(self.rezba_holes)
        self.line_11.setObjectName(u"line_11")
        self.line_11.setStyleSheet(u"background: rgba(124, 124, 124, 40)")
        self.line_11.setFrameShape(QFrame.Shape.VLine)
        self.line_11.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_8.addWidget(self.line_11)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(-1, -1, 0, -1)
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(-1, -1, 0, -1)
        self.label_18 = QLabel(self.rezba_holes)
        self.label_18.setObjectName(u"label_18")
        sizePolicy.setHeightForWidth(self.label_18.sizePolicy().hasHeightForWidth())
        self.label_18.setSizePolicy(sizePolicy)
        self.label_18.setMinimumSize(QSize(0, 0))
        self.label_18.setFont(font3)
        self.label_18.setStyleSheet(u"background-color: none")
        self.label_18.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_9.addWidget(self.label_18, 0, Qt.AlignmentFlag.AlignHCenter)

        self.comboBox_diameter_2 = QComboBox(self.rezba_holes)
        self.comboBox_diameter_2.setObjectName(u"comboBox_diameter_2")
        self.comboBox_diameter_2.setFont(font2)
        self.comboBox_diameter_2.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.comboBox_diameter_2.setStyleSheet(u"QComboBox {\n"
"	padding: 5, 5, 5, 5;\n"
"	width: 60px;\n"
"	border: none;\n"
"	border-bottom: 1px solid white;\n"
"	background: rgba(255, 255, 255, 0);\n"
"	transition: color 0.3s ease;\n"
"	transition: border-bottom 0.4s ease;\n"
"	color: rgb(204, 204, 204);\n"
"	font-size: 11pt;\n"
"}\n"
"QComboBox:hover {\n"
"   color: rgb(167, 167, 167);\n"
"}\n"
"\n"
"QComboBox::item {\n"
"	background: rgb(67, 67, 67);\n"
"	border-radius: none;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"	border-radius: none;\n"
"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(58, 58, 58), stop:1 rgb(88, 88, 88));\n"
"	selection-border-radius: none;\n"
"	selection-border: none;\n"
"	border: none;\n"
"	border-radius: 0;\n"
"	outline: none;\n"
"}\n"
"QComboBox QAbstractItemView::item {\n"
"    min-height: 15px;\n"
"	width: 15px;\n"
"	border: none;\n"
"	border-radius: none;\n"
"}\n"
"QComboBox QAbstractItemView::item:hover {\n"
"	color:rgb(173, 173, 173);\n"
"	border-bottom: 1px solid white;\n"
"}\n"
"\n"
"")

        self.horizontalLayout_9.addWidget(self.comboBox_diameter_2, 0, Qt.AlignmentFlag.AlignHCenter)


        self.verticalLayout_6.addLayout(self.horizontalLayout_9)

        self.label_2 = QLabel(self.rezba_holes)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font4)
        self.label_2.setStyleSheet(u"background-color: none;\n"
"color: rgb(175, 175, 175)\n"
"")

        self.verticalLayout_6.addWidget(self.label_2, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)


        self.horizontalLayout_8.addLayout(self.verticalLayout_6)

        self.line_12 = QFrame(self.rezba_holes)
        self.line_12.setObjectName(u"line_12")
        self.line_12.setStyleSheet(u"background: rgba(124, 124, 124, 40)")
        self.line_12.setFrameShape(QFrame.Shape.VLine)
        self.line_12.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_8.addWidget(self.line_12)

        self.label_19 = QLabel(self.rezba_holes)
        self.label_19.setObjectName(u"label_19")
        sizePolicy.setHeightForWidth(self.label_19.sizePolicy().hasHeightForWidth())
        self.label_19.setSizePolicy(sizePolicy)
        self.label_19.setFont(font3)
        self.label_19.setStyleSheet(u"background-color: none")
        self.label_19.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_8.addWidget(self.label_19)

        self.comboBox_dopusk = QComboBox(self.rezba_holes)
        self.comboBox_dopusk.setObjectName(u"comboBox_dopusk")
        self.comboBox_dopusk.setFont(font2)
        self.comboBox_dopusk.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.comboBox_dopusk.setStyleSheet(u"QComboBox {\n"
"	padding: 5, 5, 5, 5;\n"
"	width: 60px;\n"
"	border: none;\n"
"	border-bottom: 1px solid white;\n"
"	background: rgba(255, 255, 255, 0);\n"
"	transition: color 0.3s ease;\n"
"	transition: border-bottom 0.4s ease;\n"
"	color: rgb(204, 204, 204);\n"
"	font-size: 11pt;\n"
"}\n"
"QComboBox:hover {\n"
"   color: rgb(167, 167, 167);\n"
"}\n"
"\n"
"QComboBox::item {\n"
"	background: rgb(67, 67, 67);\n"
"	border-radius: none;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"	border-radius: none;\n"
"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(58, 58, 58), stop:1 rgb(88, 88, 88));\n"
"	selection-border-radius: none;\n"
"	selection-border: none;\n"
"	border: none;\n"
"	border-radius: 0;\n"
"	outline: none;\n"
"}\n"
"QComboBox QAbstractItemView::item {\n"
"    min-height: 15px;\n"
"	width: 15px;\n"
"	border: none;\n"
"	border-radius: none;\n"
"}\n"
"QComboBox QAbstractItemView::item:hover {\n"
"	color:rgb(173, 173, 173);\n"
"	border-bottom: 1px solid white;\n"
"}\n"
"\n"
"")

        self.horizontalLayout_8.addWidget(self.comboBox_dopusk)

        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_12)


        self.verticalLayout_5.addWidget(self.rezba_holes)

        self.gladkie_holes_2 = QWidget(self.holes)
        self.gladkie_holes_2.setObjectName(u"gladkie_holes_2")
        self.gladkie_holes_2.setStyleSheet(u"background: none;")
        self.horizontalLayout_6 = QHBoxLayout(self.gladkie_holes_2)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(1, 1, 1, 1)
        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_9)

        self.label_16 = QLabel(self.gladkie_holes_2)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setFont(font1)
        self.label_16.setStyleSheet(u"background: none;\n"
"")

        self.horizontalLayout_6.addWidget(self.label_16, 0, Qt.AlignmentFlag.AlignHCenter)

        self.spinBox_count = QSpinBox(self.gladkie_holes_2)
        self.spinBox_count.setObjectName(u"spinBox_count")
        self.spinBox_count.setStyleSheet(u"QSpinBox {\n"
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
        self.spinBox_count.setMinimum(1)
        self.spinBox_count.setMaximum(100)
        self.spinBox_count.setValue(1)

        self.horizontalLayout_6.addWidget(self.spinBox_count, 0, Qt.AlignmentFlag.AlignHCenter)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_10)


        self.verticalLayout_5.addWidget(self.gladkie_holes_2)

        self.checkBox_add_length = QCheckBox(self.holes)
        self.checkBox_add_length.setObjectName(u"checkBox_add_length")
        self.checkBox_add_length.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.checkBox_add_length.setStyleSheet(u"QCheckBox::indicator {\n"
"  width: 10px;          \n"
"  height: 10px;         \n"
"  border: 2px solid white;         \n"
"  border-radius: 2px; /* \u0421\u043a\u0440\u0443\u0433\u043b\u0435\u043d\u043d\u044b\u0435 \u0443\u0433\u043b\u044b */          \n"
"  background-color: #FFFFFF;      \n"
"}\n"
"QCheckBox {\n"
"	spacing: 15px; /* \u0420\u0430\u0441\u0441\u0442\u043e\u044f\u043d\u0438\u0435 \u043c\u0435\u0436\u0434\u0443 \u043a\u0432\u0430\u0434\u0440\u0430\u0442\u0438\u043a\u043e\u043c \u0438 \u0442\u0435\u043a\u0441\u0442\u043e\u043c */          \n"
"	border: none;	\n"
"	color: rgb(255, 255, 255) ;	\n"
"	background: none;\n"
"	font-size: 14px;\n"
"	margin-right: 0px\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"  width: 10px;          \n"
"  height: 10px;         \n"
"  border: 2px solid white;         \n"
"  border-radius: 2px; /* \u0421\u043a\u0440\u0443\u0433\u043b\u0435\u043d\u043d\u044b\u0435 \u0443\u0433\u043b\u044b */          \n"
"  background-color: rgb(77, 77, 77);    \n"
"}\n"
"QCheckBox::ind"
                        "icator:hover {\n"
"  width: 10px;          \n"
"  height: 10px;         \n"
"  border: 2px solid rgb(136, 136, 136);         \n"
"  border-radius: 2px; /* \u0421\u043a\u0440\u0443\u0433\u043b\u0435\u043d\u043d\u044b\u0435 \u0443\u0433\u043b\u044b */          \n"
"  background-color: rgb(77, 77, 77);         \n"
"}\n"
"QCheckBox::indicator:disabled {\n"
"  width: 10px;          \n"
"  height: 10px;         \n"
"  border: 2px solid rgb(136, 136, 136);         \n"
"  border-radius: 2px; /* \u0421\u043a\u0440\u0443\u0433\u043b\u0435\u043d\u043d\u044b\u0435 \u0443\u0433\u043b\u044b */          \n"
"  background-color: rgb(86, 86, 86);         \n"
"}")

        self.verticalLayout_5.addWidget(self.checkBox_add_length, 0, Qt.AlignmentFlag.AlignHCenter)

        self.length = QWidget(self.holes)
        self.length.setObjectName(u"length")
        self.horizontalLayout_5 = QHBoxLayout(self.length)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(-1, -1, -1, 1)
        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_7)

        self.label_4 = QLabel(self.length)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font1)
        self.label_4.setStyleSheet(u"background: none;\n"
"")

        self.horizontalLayout_5.addWidget(self.label_4, 0, Qt.AlignmentFlag.AlignHCenter)

        self.doubleSpinBox_length = QDoubleSpinBox(self.length)
        self.doubleSpinBox_length.setObjectName(u"doubleSpinBox_length")
        self.doubleSpinBox_length.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.doubleSpinBox_length.setStyleSheet(u"QDoubleSpinBox {\n"
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
        self.doubleSpinBox_length.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.doubleSpinBox_length.setDecimals(3)
        self.doubleSpinBox_length.setMinimum(0.000000000000000)
        self.doubleSpinBox_length.setMaximum(1000.000000000000000)
        self.doubleSpinBox_length.setStepType(QAbstractSpinBox.StepType.DefaultStepType)

        self.horizontalLayout_5.addWidget(self.doubleSpinBox_length, 0, Qt.AlignmentFlag.AlignHCenter)

        self.line_10 = QFrame(self.length)
        self.line_10.setObjectName(u"line_10")
        self.line_10.setStyleSheet(u"background: rgba(124, 124, 124, 40)")
        self.line_10.setFrameShape(QFrame.Shape.VLine)
        self.line_10.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_5.addWidget(self.line_10)

        self.label_14 = QLabel(self.length)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setFont(font1)
        self.label_14.setStyleSheet(u"background: none;\n"
"")

        self.horizontalLayout_5.addWidget(self.label_14)

        self.lineEdit_kvalitet_length = QLineEdit(self.length)
        self.lineEdit_kvalitet_length.setObjectName(u"lineEdit_kvalitet_length")
        self.lineEdit_kvalitet_length.setMinimumSize(QSize(0, 0))
        self.lineEdit_kvalitet_length.setStyleSheet(u"padding: 5, 5, 5, 5;\n"
"border: none;\n"
"border-bottom: 1px solid white;\n"
"background: rgba(255, 255, 255, 0);\n"
"transition: color 0.3s ease;\n"
"transition: border-bottom 0.4s ease;\n"
"color: rgb(204, 204, 204);\n"
"font-size: 10pt;")

        self.horizontalLayout_5.addWidget(self.lineEdit_kvalitet_length)

        self.line_9 = QFrame(self.length)
        self.line_9.setObjectName(u"line_9")
        self.line_9.setStyleSheet(u"background: rgba(124, 124, 124, 40)")
        self.line_9.setFrameShape(QFrame.Shape.VLine)
        self.line_9.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_5.addWidget(self.line_9)

        self.label_15 = QLabel(self.length)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setFont(font1)
        self.label_15.setStyleSheet(u"background: none;\n"
"")

        self.horizontalLayout_5.addWidget(self.label_15)

        self.doubleSpinBox_dopusk_length = QDoubleSpinBox(self.length)
        self.doubleSpinBox_dopusk_length.setObjectName(u"doubleSpinBox_dopusk_length")
        self.doubleSpinBox_dopusk_length.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.doubleSpinBox_dopusk_length.setStyleSheet(u"QDoubleSpinBox {\n"
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
        self.doubleSpinBox_dopusk_length.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.doubleSpinBox_dopusk_length.setDecimals(3)
        self.doubleSpinBox_dopusk_length.setMinimum(-10.000000000000000)
        self.doubleSpinBox_dopusk_length.setMaximum(10.000000000000000)
        self.doubleSpinBox_dopusk_length.setSingleStep(0.100000000000000)
        self.doubleSpinBox_dopusk_length.setValue(0.000000000000000)

        self.horizontalLayout_5.addWidget(self.doubleSpinBox_dopusk_length)

        self.label_13 = QLabel(self.length)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setFont(font1)
        self.label_13.setStyleSheet(u"background: none;\n"
"")

        self.horizontalLayout_5.addWidget(self.label_13)

        self.line_8 = QFrame(self.length)
        self.line_8.setObjectName(u"line_8")
        self.line_8.setStyleSheet(u"background: rgba(124, 124, 124, 40)")
        self.line_8.setFrameShape(QFrame.Shape.VLine)
        self.line_8.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_5.addWidget(self.line_8)

        self.doubleSpinBox_dopusk_length_2 = QDoubleSpinBox(self.length)
        self.doubleSpinBox_dopusk_length_2.setObjectName(u"doubleSpinBox_dopusk_length_2")
        self.doubleSpinBox_dopusk_length_2.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.doubleSpinBox_dopusk_length_2.setStyleSheet(u"QDoubleSpinBox {\n"
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
        self.doubleSpinBox_dopusk_length_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.doubleSpinBox_dopusk_length_2.setDecimals(3)
        self.doubleSpinBox_dopusk_length_2.setMinimum(-10.000000000000000)
        self.doubleSpinBox_dopusk_length_2.setMaximum(10.000000000000000)
        self.doubleSpinBox_dopusk_length_2.setSingleStep(0.100000000000000)
        self.doubleSpinBox_dopusk_length_2.setValue(0.000000000000000)

        self.horizontalLayout_5.addWidget(self.doubleSpinBox_dopusk_length_2)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_8)


        self.verticalLayout_5.addWidget(self.length)

        self.widget_2 = QWidget(self.holes)
        self.widget_2.setObjectName(u"widget_2")
        self.horizontalLayout_10 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_13)

        self.label_20 = QLabel(self.widget_2)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setFont(font1)
        self.label_20.setStyleSheet(u"background: none;\n"
"")

        self.horizontalLayout_10.addWidget(self.label_20)

        self.doubleSpinBox_length_rezba = QDoubleSpinBox(self.widget_2)
        self.doubleSpinBox_length_rezba.setObjectName(u"doubleSpinBox_length_rezba")
        self.doubleSpinBox_length_rezba.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.doubleSpinBox_length_rezba.setStyleSheet(u"QDoubleSpinBox {\n"
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
        self.doubleSpinBox_length_rezba.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.doubleSpinBox_length_rezba.setDecimals(3)
        self.doubleSpinBox_length_rezba.setMinimum(0.000000000000000)
        self.doubleSpinBox_length_rezba.setMaximum(1000.000000000000000)
        self.doubleSpinBox_length_rezba.setStepType(QAbstractSpinBox.StepType.DefaultStepType)

        self.horizontalLayout_10.addWidget(self.doubleSpinBox_length_rezba)

        self.line_14 = QFrame(self.widget_2)
        self.line_14.setObjectName(u"line_14")
        self.line_14.setStyleSheet(u"background: rgba(124, 124, 124, 40)")
        self.line_14.setFrameShape(QFrame.Shape.VLine)
        self.line_14.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_10.addWidget(self.line_14)

        self.label_22 = QLabel(self.widget_2)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setFont(font1)
        self.label_22.setStyleSheet(u"background: none;\n"
"")

        self.horizontalLayout_10.addWidget(self.label_22)

        self.doubleSpinBox_dopusk_length_rezba = QDoubleSpinBox(self.widget_2)
        self.doubleSpinBox_dopusk_length_rezba.setObjectName(u"doubleSpinBox_dopusk_length_rezba")
        self.doubleSpinBox_dopusk_length_rezba.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.doubleSpinBox_dopusk_length_rezba.setStyleSheet(u"QDoubleSpinBox {\n"
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
        self.doubleSpinBox_dopusk_length_rezba.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.doubleSpinBox_dopusk_length_rezba.setDecimals(3)
        self.doubleSpinBox_dopusk_length_rezba.setMinimum(-10.000000000000000)
        self.doubleSpinBox_dopusk_length_rezba.setMaximum(10.000000000000000)
        self.doubleSpinBox_dopusk_length_rezba.setSingleStep(0.100000000000000)
        self.doubleSpinBox_dopusk_length_rezba.setValue(0.000000000000000)

        self.horizontalLayout_10.addWidget(self.doubleSpinBox_dopusk_length_rezba)

        self.line_15 = QFrame(self.widget_2)
        self.line_15.setObjectName(u"line_15")
        self.line_15.setStyleSheet(u"background: rgba(124, 124, 124, 40)")
        self.line_15.setFrameShape(QFrame.Shape.VLine)
        self.line_15.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_10.addWidget(self.line_15)

        self.label_21 = QLabel(self.widget_2)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setFont(font1)
        self.label_21.setStyleSheet(u"background: none;\n"
"")

        self.horizontalLayout_10.addWidget(self.label_21)

        self.doubleSpinBox_dopusk_length_rezba_2 = QDoubleSpinBox(self.widget_2)
        self.doubleSpinBox_dopusk_length_rezba_2.setObjectName(u"doubleSpinBox_dopusk_length_rezba_2")
        self.doubleSpinBox_dopusk_length_rezba_2.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.doubleSpinBox_dopusk_length_rezba_2.setStyleSheet(u"QDoubleSpinBox {\n"
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
        self.doubleSpinBox_dopusk_length_rezba_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.doubleSpinBox_dopusk_length_rezba_2.setDecimals(3)
        self.doubleSpinBox_dopusk_length_rezba_2.setMinimum(-10.000000000000000)
        self.doubleSpinBox_dopusk_length_rezba_2.setMaximum(10.000000000000000)
        self.doubleSpinBox_dopusk_length_rezba_2.setSingleStep(0.100000000000000)
        self.doubleSpinBox_dopusk_length_rezba_2.setValue(0.000000000000000)

        self.horizontalLayout_10.addWidget(self.doubleSpinBox_dopusk_length_rezba_2)

        self.horizontalSpacer_14 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_14)


        self.verticalLayout_5.addWidget(self.widget_2)


        self.verticalLayout_4.addLayout(self.verticalLayout_5)


        self.verticalLayout.addWidget(self.holes)

        self.pushButton_add_table = QPushButton(PageKontrolOtk)
        self.pushButton_add_table.setObjectName(u"pushButton_add_table")
        self.pushButton_add_table.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_add_table.setStyleSheet(u"QPushButton {\n"
"	border: 1px solid;\n"
"	border-color: white;\n"
"	border-radius: 10px;\n"
"	height: 25px;\n"
"	background-color: none;\n"
"	padding: 2 5 5 5\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(0, 111, 171)\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: rgb(0, 53, 93)\n"
"}")

        self.verticalLayout.addWidget(self.pushButton_add_table, 0, Qt.AlignmentFlag.AlignHCenter)

        self.text_info = QLabel(PageKontrolOtk)
        self.text_info.setObjectName(u"text_info")
        self.text_info.setFont(font1)
        self.text_info.setStyleSheet(u"background: none;\n"
"")

        self.verticalLayout.addWidget(self.text_info, 0, Qt.AlignmentFlag.AlignHCenter)

        self.line_3 = QFrame(PageKontrolOtk)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.Shape.HLine)
        self.line_3.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout.addWidget(self.line_3)

        self.btn_clear_table = QPushButton(PageKontrolOtk)
        self.btn_clear_table.setObjectName(u"btn_clear_table")
        self.btn_clear_table.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_clear_table.setStyleSheet(u"QPushButton {\n"
"	border: 1px solid;\n"
"	border-color: white;\n"
"	border-radius: 10px;\n"
"	height: 20px;\n"
"	width: 110px;\n"
"	background-color: none;\n"
"	padding: 2 5 2 5\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(0, 111, 171)\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: rgb(0, 53, 93)\n"
"}")

        self.verticalLayout.addWidget(self.btn_clear_table, 0, Qt.AlignmentFlag.AlignRight)

        self.table_widget_kontrol_otk = QTableWidget(PageKontrolOtk)
        if (self.table_widget_kontrol_otk.columnCount() < 3):
            self.table_widget_kontrol_otk.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.table_widget_kontrol_otk.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.table_widget_kontrol_otk.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.table_widget_kontrol_otk.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.table_widget_kontrol_otk.setObjectName(u"table_widget_kontrol_otk")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.table_widget_kontrol_otk.sizePolicy().hasHeightForWidth())
        self.table_widget_kontrol_otk.setSizePolicy(sizePolicy1)
        self.table_widget_kontrol_otk.setMinimumSize(QSize(0, 100))
        self.table_widget_kontrol_otk.setFont(font1)
        self.table_widget_kontrol_otk.setStyleSheet(u"/* \u0421\u0430\u043c \u0432\u0438\u0434\u0436\u0435\u0442 \u2014 \u043f\u0440\u043e\u0437\u0440\u0430\u0447\u043d\u044b\u0439 \u0444\u043e\u043d */\n"
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
"	border-bottom: 1px solid rgba(255, 255, 255, 0.15)\n"
"\n"
"}\n"
"\n"
"QTableWidget::item:hover {\n"
"    background: rgba(255, 255, 255, 0.08);\n"
"}\n"
"\n"
"QTableWidget::item:selected {\n"
"    background: rgba(255, 255, 255, 0.2);\n"
"    color: #ffffff;\n"
"}\n"
""
                        "\n"
"/* \u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043a\u0438 \u2014 \u0415\u0414\u0418\u041d\u0421\u0422\u0412\u0415\u041d\u041d\u041e\u0415 \u043c\u0435\u0441\u0442\u043e \u0441 \u0444\u043e\u043d\u043e\u043c */\n"
"QHeaderView::section {\n"
"    background-color: rgb(21, 69, 140);\n"
"    color: #ffffff;\n"
"    padding: 6px 8px;\n"
"    border: none;\n"
"    border-right: 1px solid rgba(255, 255, 255, 0.1);\n"
"    border-bottom: 1px solid rgba(255, 255, 255, 0.2);\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QHeaderView::section:hover {\n"
"    background-color: #3a3a3a;\n"
"}\n"
"\n"
"/* \u0423\u0433\u043b\u043e\u0432\u0430\u044f \u043a\u043d\u043e\u043f\u043a\u0430 (\u043f\u0435\u0440\u0435\u0441\u0435\u0447\u0435\u043d\u0438\u0435 \u0437\u0430\u0433\u043e\u043b\u043e\u0432\u043a\u043e\u0432) */\n"
"QTableCornerButton::section {\n"
"    background-color:  rgb(21, 69, 140);\n"
"    border: none;\n"
"    border-right: 1px solid rgba(255, 255, 255, 0.1);\n"
"    border-bottom: 1px solid rgba(255, 255, 255, 0"
                        ".2);\n"
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
"\n"
"QTableWidget QScrollBar::handle:horizontal {\n"
""
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
"	border: 1px solid white;\n"
"	margin-top: 25px;\n"
"	margin-bottom: 25px;\n"
"	margin-left: 20px;\n"
"	margin-right: 20px;\n"
"	border-radius: 8px;\n"
"}\n"
"QPushButton:hover {\n"
"	border: 2px solid white;\n"
"	background: rgb(15, 65, 159)\n"
"}")
        self.table_widget_kontrol_otk.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.table_widget_kontrol_otk.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.table_widget_kontrol_otk.setAutoScroll(False)
        self.table_widget_kontrol_otk.setShowGrid(True)
        self.table_widget_kontrol_otk.setRowCount(0)
        self.table_widget_kontrol_otk.setColumnCount(3)
        self.table_widget_kontrol_otk.horizontalHeader().setStretchLastSection(True)
        self.table_widget_kontrol_otk.verticalHeader().setVisible(False)

        self.verticalLayout.addWidget(self.table_widget_kontrol_otk)

        self.btn_save_and_export = QPushButton(PageKontrolOtk)
        self.btn_save_and_export.setObjectName(u"btn_save_and_export")
        self.btn_save_and_export.setMaximumSize(QSize(16777215, 16777215))
        self.btn_save_and_export.setFont(font2)
        self.btn_save_and_export.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_save_and_export.setStyleSheet(u"QPushButton {\n"
"	border: 1px solid;\n"
"	border-color: white;\n"
"	border-radius: 10px;\n"
"	height: 20px;	\n"
"	background-color: rgb(185, 57, 41);\n"
"	padding: 2 5 5 5;\n"
"	font-size: 11pt;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(0, 111, 171)\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: rgb(0, 53, 93)\n"
"}")

        self.verticalLayout.addWidget(self.btn_save_and_export, 0, Qt.AlignmentFlag.AlignHCenter)


        self.retranslateUi(PageKontrolOtk)

        QMetaObject.connectSlotsByName(PageKontrolOtk)
    # setupUi

    def retranslateUi(self, PageKontrolOtk):
        PageKontrolOtk.setWindowTitle(QCoreApplication.translate("PageKontrolOtk", u"\u041a\u043e\u043d\u0442\u0440\u043e\u043b\u044c \u041e\u0422\u041a", None))
        self.btn_home.setText(QCoreApplication.translate("PageKontrolOtk", u"\u0414\u043e\u043c\u043e\u0439", None))
        self.label_9.setText(QCoreApplication.translate("PageKontrolOtk", u"\u041a\u043e\u043d\u0442\u0440\u043e\u043b\u044c \u041e\u0422\u041a", None))
        self.label_6.setText(QCoreApplication.translate("PageKontrolOtk", u"\u0427\u0442\u043e \u043a\u043e\u043d\u0442\u0440\u043e\u043b\u0438\u0440\u043e\u0432\u0430\u0442\u044c?", None))
        self.btn_diameter.setText(QCoreApplication.translate("PageKontrolOtk", u"\u0414\u0438\u0430\u043c\u0435\u0442\u0440", None))
        self.btn_length.setText(QCoreApplication.translate("PageKontrolOtk", u"\u0414\u043b\u0438\u043d\u0430", None))
        self.btn_hole.setText(QCoreApplication.translate("PageKontrolOtk", u"\u041e\u0442\u0432\u0435\u0440\u0441\u0442\u0438\u044f", None))
        self.pushButton_reset.setText(QCoreApplication.translate("PageKontrolOtk", u"\u0421\u0431\u0440\u043e\u0441\u0438\u0442\u044c", None))
        self.groupBox.setTitle("")
        self.radioButton_otv.setText(QCoreApplication.translate("PageKontrolOtk", u"\u041e\u0442\u0432\u0435\u0440\u0441\u0442\u0438\u0435", None))
        self.radioButton_val.setText(QCoreApplication.translate("PageKontrolOtk", u"\u0412\u0430\u043b", None))
        self.checkBox_rezba.setText(QCoreApplication.translate("PageKontrolOtk", u"\u0423\u043a\u0430\u0437\u0430\u0442\u044c \u0440\u0435\u0437\u044c\u0431\u0443", None))
        self.label_23.setText(QCoreApplication.translate("PageKontrolOtk", u"\u041a\u043e\u043d\u0442\u0440\u043e\u043b\u0438\u0440\u0443\u0435\u043c\u0430\u044f \u0440\u0435\u0437\u044c\u0431\u0430:", None))
        self.comboBox_rezba_d.setPlaceholderText(QCoreApplication.translate("PageKontrolOtk", u"\u0420\u0435\u0437\u044c\u0431\u0430...", None))
        self.label_24.setText(QCoreApplication.translate("PageKontrolOtk", u"\u0428\u0430\u0433  \u0440\u0435\u0437\u044c\u0431\u044b:", None))
#if QT_CONFIG(tooltip)
        self.comboBox_step_d.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.comboBox_step_d.setPlaceholderText(QCoreApplication.translate("PageKontrolOtk", u"\u0428\u0430\u0433...", None))
#if QT_CONFIG(tooltip)
        self.label_25.setToolTip(QCoreApplication.translate("PageKontrolOtk", u"<html><head/><body><p>asdasd</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_25.setText(QCoreApplication.translate("PageKontrolOtk", u"\u041f\u0435\u0440\u0432\u044b\u0439 \u0448\u0430\u0433 \u0432 \u0441\u043f\u0438\u0441\u043a\u0435 - \u043e\u0441\u043d\u043e\u0432\u043d\u043e\u0439", None))
        self.label_26.setText(QCoreApplication.translate("PageKontrolOtk", u"\u0414\u043e\u043f\u0443\u0441\u043a  \u0440\u0435\u0437\u044c\u0431\u044b:", None))
        self.comboBox_dopusk_2.setPlaceholderText(QCoreApplication.translate("PageKontrolOtk", u"\u0414\u043e\u043f\u0443\u0441\u043a...", None))
        self.label.setText(QCoreApplication.translate("PageKontrolOtk", u"\u041a\u043e\u043d\u0442\u0440\u043e\u043b\u0438\u0440\u0443\u0435\u043c\u044b\u0439 \u0440\u0430\u0437\u043c\u0435\u0440:", None))
        self.doubleSpinBox_nom_diameter.setPrefix(QCoreApplication.translate("PageKontrolOtk", u"\u00d8 ", None))
        self.label_5.setText(QCoreApplication.translate("PageKontrolOtk", u"\u041a\u0432\u0430\u043b\u0438\u0442\u0435\u0442:", None))
        self.lineEdit_kvalitet.setPlaceholderText("")
        self.label_7.setText(QCoreApplication.translate("PageKontrolOtk", u"\u0414\u043e\u043f\u0443\u0441\u043a 1:", None))
        self.doubleSpinBox_dopusk_1.setPrefix("")
        self.doubleSpinBox_dopusk_1.setSuffix("")
        self.label_8.setText(QCoreApplication.translate("PageKontrolOtk", u"\u0414\u043e\u043f\u0443\u0441\u043a 2:", None))
        self.doubleSpinBox_dopusk_2.setPrefix("")
        self.doubleSpinBox_dopusk_2.setSuffix("")
        self.groupBox_3.setTitle("")
        self.btn_gladkie.setText(QCoreApplication.translate("PageKontrolOtk", u"\u0413\u043b\u0430\u0434\u043a\u0438\u0435", None))
        self.btn_rezba.setText(QCoreApplication.translate("PageKontrolOtk", u"\u0420\u0435\u0437\u044c\u0431\u043e\u0432\u044b\u0435", None))
        self.label_3.setText(QCoreApplication.translate("PageKontrolOtk", u"\u041a\u043e\u043d\u0442\u0440\u043e\u043b\u0438\u0440\u0443\u0435\u043c\u044b\u0439 \u0440\u0430\u0437\u043c\u0435\u0440:", None))
        self.doubleSpinBox_nom_diameter_3.setPrefix(QCoreApplication.translate("PageKontrolOtk", u"\u00d8 ", None))
        self.label_10.setText(QCoreApplication.translate("PageKontrolOtk", u"\u041a\u0432\u0430\u043b\u0438\u0442\u0435\u0442:", None))
        self.lineEdit_kvalitet_2.setPlaceholderText("")
        self.label_11.setText(QCoreApplication.translate("PageKontrolOtk", u"\u0414\u043e\u043f\u0443\u0441\u043a 1:", None))
        self.doubleSpinBox_dopusk_3.setPrefix("")
        self.doubleSpinBox_dopusk_3.setSuffix("")
        self.label_12.setText(QCoreApplication.translate("PageKontrolOtk", u"\u0414\u043e\u043f\u0443\u0441\u043a 2:", None))
        self.doubleSpinBox_dopusk_4.setPrefix("")
        self.doubleSpinBox_dopusk_4.setSuffix("")
        self.label_17.setText(QCoreApplication.translate("PageKontrolOtk", u"\u041a\u043e\u043d\u0442\u0440\u043e\u043b\u0438\u0440\u0443\u0435\u043c\u0430\u044f \u0440\u0435\u0437\u044c\u0431\u0430:", None))
        self.comboBox_diameter.setPlaceholderText(QCoreApplication.translate("PageKontrolOtk", u"\u0420\u0435\u0437\u044c\u0431\u0430...", None))
        self.label_18.setText(QCoreApplication.translate("PageKontrolOtk", u"\u0428\u0430\u0433  \u0440\u0435\u0437\u044c\u0431\u044b:", None))
#if QT_CONFIG(tooltip)
        self.comboBox_diameter_2.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.comboBox_diameter_2.setPlaceholderText(QCoreApplication.translate("PageKontrolOtk", u"\u0428\u0430\u0433...", None))
#if QT_CONFIG(tooltip)
        self.label_2.setToolTip(QCoreApplication.translate("PageKontrolOtk", u"<html><head/><body><p>asdasd</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_2.setText(QCoreApplication.translate("PageKontrolOtk", u"\u041f\u0435\u0440\u0432\u044b\u0439 \u0448\u0430\u0433 \u0432 \u0441\u043f\u0438\u0441\u043a\u0435 - \u043e\u0441\u043d\u043e\u0432\u043d\u043e\u0439", None))
        self.label_19.setText(QCoreApplication.translate("PageKontrolOtk", u"\u0414\u043e\u043f\u0443\u0441\u043a  \u0440\u0435\u0437\u044c\u0431\u044b:", None))
        self.comboBox_dopusk.setPlaceholderText(QCoreApplication.translate("PageKontrolOtk", u"\u0414\u043e\u043f\u0443\u0441\u043a...", None))
        self.label_16.setText(QCoreApplication.translate("PageKontrolOtk", u"\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u043e\u0442\u0432\u0435\u0440\u0441\u0442\u0438\u0439: ", None))
        self.spinBox_count.setSuffix(QCoreApplication.translate("PageKontrolOtk", u" \u0448\u0442.", None))
        self.checkBox_add_length.setText(QCoreApplication.translate("PageKontrolOtk", u"\u0423\u043a\u0430\u0437\u0430\u0442\u044c \u0433\u043b\u0443\u0431\u0438\u043d\u0443 \u043e\u0442\u0432\u0435\u0440\u0441\u0442\u0438\u0439", None))
        self.label_4.setText(QCoreApplication.translate("PageKontrolOtk", u"\u0413\u043b\u0443\u0431\u0438\u043d\u0430 \u0438\u0437 \u043f\u043e\u0434 \u0441\u0432\u0435\u0440\u043b\u0430:", None))
        self.doubleSpinBox_length.setPrefix(QCoreApplication.translate("PageKontrolOtk", u"L= ", None))
        self.label_14.setText(QCoreApplication.translate("PageKontrolOtk", u"\u041a\u0432\u0430\u043b\u0438\u0442\u0435\u0442:", None))
        self.lineEdit_kvalitet_length.setPlaceholderText("")
        self.label_15.setText(QCoreApplication.translate("PageKontrolOtk", u"\u0414\u043e\u043f\u0443\u0441\u043a 1:", None))
        self.doubleSpinBox_dopusk_length.setPrefix("")
        self.doubleSpinBox_dopusk_length.setSuffix("")
        self.label_13.setText(QCoreApplication.translate("PageKontrolOtk", u"\u0414\u043e\u043f\u0443\u0441\u043a 2:", None))
        self.doubleSpinBox_dopusk_length_2.setPrefix("")
        self.doubleSpinBox_dopusk_length_2.setSuffix("")
        self.label_20.setText(QCoreApplication.translate("PageKontrolOtk", u"\u0413\u043b\u0443\u0431\u0438\u043d\u0430 \u0440\u0435\u0437\u044c\u0431\u044b:", None))
        self.doubleSpinBox_length_rezba.setPrefix(QCoreApplication.translate("PageKontrolOtk", u"L= ", None))
        self.label_22.setText(QCoreApplication.translate("PageKontrolOtk", u"\u0414\u043e\u043f\u0443\u0441\u043a 1:", None))
        self.doubleSpinBox_dopusk_length_rezba.setPrefix("")
        self.doubleSpinBox_dopusk_length_rezba.setSuffix("")
        self.label_21.setText(QCoreApplication.translate("PageKontrolOtk", u"\u0414\u043e\u043f\u0443\u0441\u043a 2:", None))
        self.doubleSpinBox_dopusk_length_rezba_2.setPrefix("")
        self.doubleSpinBox_dopusk_length_rezba_2.setSuffix("")
        self.pushButton_add_table.setText(QCoreApplication.translate("PageKontrolOtk", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0432 \u0442\u0430\u0431\u043b\u0438\u0446\u0443", None))
        self.text_info.setText("")
        self.btn_clear_table.setText(QCoreApplication.translate("PageKontrolOtk", u"\u041e\u0447\u0438\u0441\u0442\u0438\u0442\u044c \u0442\u0430\u0431\u043b\u0438\u0446\u0443", None))
        ___qtablewidgetitem = self.table_widget_kontrol_otk.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("PageKontrolOtk", u"\u0418\u043d\u0441\u0442\u0440\u0443\u043c\u0435\u043d\u0442", None))
        ___qtablewidgetitem1 = self.table_widget_kontrol_otk.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("PageKontrolOtk", u"\u0420\u0430\u0437\u043c\u0435\u0440\u044b", None))
        self.btn_save_and_export.setText(QCoreApplication.translate("PageKontrolOtk", u"\u041f\u0435\u0440\u0435\u043d\u0435\u0441\u0442\u0438 \u043f\u0435\u0440\u0435\u0445\u043e\u0434\u044b \u0432 \u0422\u0435\u0445\u043d\u043e\u041f\u0440\u043e", None))
    # retranslateUi

