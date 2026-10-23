# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_page_razmetka.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDoubleSpinBox, QGroupBox,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QSpacerItem, QSpinBox,
    QStackedWidget, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)
import res_rc

class Ui_PageRazmetka(object):
    def setupUi(self, PageRazmetka):
        if not PageRazmetka.objectName():
            PageRazmetka.setObjectName(u"PageRazmetka")
        PageRazmetka.resize(1000, 870)
        PageRazmetka.setMinimumSize(QSize(1000, 0))
        PageRazmetka.setStyleSheet(u"color: white;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0, stop:0 rgba(20, 40, 80, 255), stop:1 rgba(39, 73, 109, 255));\n"
"")
        self.verticalLayout = QVBoxLayout(PageRazmetka)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(-1, 0, -1, -1)
        self.btn_home_2 = QPushButton(PageRazmetka)
        self.btn_home_2.setObjectName(u"btn_home_2")
        font = QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.btn_home_2.setFont(font)
        self.btn_home_2.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_home_2.setStyleSheet(u"QPushButton {\n"
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
        self.btn_home_2.setIcon(icon)
        self.btn_home_2.setIconSize(QSize(20, 20))

        self.horizontalLayout_11.addWidget(self.btn_home_2, 0, Qt.AlignmentFlag.AlignLeft)


        self.verticalLayout.addLayout(self.horizontalLayout_11)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setSpacing(10)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(-1, -1, -1, 0)
        self.widget = QWidget(PageRazmetka)
        self.widget.setObjectName(u"widget")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(3)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setStyleSheet(u"background: none;")
        self.verticalLayout_9 = QVBoxLayout(self.widget)
        self.verticalLayout_9.setSpacing(6)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(1, 1, 1, 20)
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setWeight(QFont.DemiBold)
        self.label.setFont(font1)
        self.label.setStyleSheet(u"background-color: none;\n"
"color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(12, 123, 147, 255), stop:1 rgba(0, 168, 204, 255));\n"
"font-size: 28px;\n"
"font-weight: 600;\n"
"border: none;\n"
"width: 300px;\n"
"\n"
"")

        self.verticalLayout_9.addWidget(self.label, 0, Qt.AlignmentFlag.AlignHCenter)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, 0, -1, 10)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.main = QWidget(self.widget)
        self.main.setObjectName(u"main")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.main.sizePolicy().hasHeightForWidth())
        self.main.setSizePolicy(sizePolicy1)
        self.main.setMinimumSize(QSize(300, 0))
        self.main.setMouseTracking(True)
        self.main.setTabletTracking(False)
        self.main.setAutoFillBackground(False)
        self.main.setStyleSheet(u"QWidget {\n"
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
"\n"
"#widget_3, #widget_4 {\n"
"	background: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0, stop:0 rgba(39, 72, 109, 129), stop:1 rgba(21, 41, 81, 129));\n"
"}\n"
"")
        self.verticalLayout_2 = QVBoxLayout(self.main)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_2 = QLabel(self.main)
        self.label_2.setObjectName(u"label_2")
        font2 = QFont()
        font2.setFamilies([u"Segoe UI Light"])
        font2.setPointSize(10)
        font2.setBold(False)
        self.label_2.setFont(font2)
        self.label_2.setStyleSheet(u"")

        self.verticalLayout_2.addWidget(self.label_2)

        self.widget_2 = QWidget(self.main)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setStyleSheet(u"QWidget {\n"
"	background: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0, stop:0 rgba(39, 72, 109, 129), stop:1 rgba(21, 41, 81, 129));\n"
"\n"
"}\n"
"Line {\n"
"	background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(8, 81, 97, 128), stop:1 rgba(0, 117, 142, 106))\n"
"}")
        self.verticalLayout_6 = QVBoxLayout(self.widget_2)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.horizontalGroupBox = QGroupBox(self.widget_2)
        self.horizontalGroupBox.setObjectName(u"horizontalGroupBox")
        self.horizontalGroupBox.setStyleSheet(u"QGroupBox {\n"
"	border: none;\n"
"	background: none;\n"
"}\n"
"QPushButton {\n"
"	background:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(12, 123, 147, 255), stop:1 rgba(0, 168, 204, 255));\n"
"	border: none;\n"
"	font-size: 11px;\n"
"	padding: 5 10 5 10;\n"
"	width: 150px;\n"
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
        self.horizontalGroupBox.setCheckable(False)
        self.horizontalLayout_4 = QHBoxLayout(self.horizontalGroupBox)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(-1, 5, -1, 5)
        self.pushButton_rezba = QPushButton(self.horizontalGroupBox)
        self.pushButton_rezba.setObjectName(u"pushButton_rezba")
        font3 = QFont()
        self.pushButton_rezba.setFont(font3)
        self.pushButton_rezba.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_rezba.setStyleSheet(u"")
        self.pushButton_rezba.setCheckable(True)
        self.pushButton_rezba.setChecked(True)
        self.pushButton_rezba.setAutoRepeat(False)
        self.pushButton_rezba.setAutoExclusive(True)

        self.horizontalLayout_4.addWidget(self.pushButton_rezba, 0, Qt.AlignmentFlag.AlignHCenter)

        self.pushButton_no_rezba = QPushButton(self.horizontalGroupBox)
        self.pushButton_no_rezba.setObjectName(u"pushButton_no_rezba")
        self.pushButton_no_rezba.setFont(font3)
        self.pushButton_no_rezba.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_no_rezba.setStyleSheet(u"")
        self.pushButton_no_rezba.setCheckable(True)
        self.pushButton_no_rezba.setChecked(False)
        self.pushButton_no_rezba.setAutoExclusive(True)

        self.horizontalLayout_4.addWidget(self.pushButton_no_rezba, 0, Qt.AlignmentFlag.AlignHCenter)


        self.verticalLayout_6.addWidget(self.horizontalGroupBox, 0, Qt.AlignmentFlag.AlignHCenter)

        self.stackedWidget = QStackedWidget(self.widget_2)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"border: none;\n"
"background: none;\n"
"color: white;")
        self.page_6 = QWidget()
        self.page_6.setObjectName(u"page_6")
        self.page_6.setStyleSheet(u"background: rgba(90, 255, 61, 0);\n"
"border: none;")
        self.verticalLayout_3 = QVBoxLayout(self.page_6)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalWidget_7 = QWidget(self.page_6)
        self.horizontalWidget_7.setObjectName(u"horizontalWidget_7")
        self.horizontalWidget_7.setStyleSheet(u"background: rgba(0, 0, 0, 0);")
        self.horizontalLayout_9 = QHBoxLayout(self.horizontalWidget_7)
        self.horizontalLayout_9.setSpacing(10)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_13)

        self.label_8 = QLabel(self.horizontalWidget_7)
        self.label_8.setObjectName(u"label_8")
        font4 = QFont()
        font4.setPointSize(11)
        self.label_8.setFont(font4)
        self.label_8.setStyleSheet(u"background: none;\n"
"border: none;\n"
"border-radius: none;")

        self.horizontalLayout_9.addWidget(self.label_8)

        self.doubleSpinBox_diameter = QDoubleSpinBox(self.horizontalWidget_7)
        self.doubleSpinBox_diameter.setObjectName(u"doubleSpinBox_diameter")
        self.doubleSpinBox_diameter.setStyleSheet(u"QDoubleSpinBox {\n"
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
        self.doubleSpinBox_diameter.setMaximum(1000.000000000000000)

        self.horizontalLayout_9.addWidget(self.doubleSpinBox_diameter)

        self.horizontalSpacer_14 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_14)


        self.verticalLayout_3.addWidget(self.horizontalWidget_7)

        self.stackedWidget.addWidget(self.page_6)
        self.page_7 = QWidget()
        self.page_7.setObjectName(u"page_7")
        self.page_7.setStyleSheet(u"background: rgba(90, 255, 61, 0);\n"
"border: none;")
        self.verticalLayout_5 = QVBoxLayout(self.page_7)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalWidget_2 = QWidget(self.page_7)
        self.horizontalWidget_2.setObjectName(u"horizontalWidget_2")
        self.horizontalWidget_2.setStyleSheet(u"border-radius: none;\n"
"border: none;")
        self.horizontalLayout_7 = QHBoxLayout(self.horizontalWidget_2)
        self.horizontalLayout_7.setSpacing(10)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_3)

        self.label_5 = QLabel(self.horizontalWidget_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font4)
        self.label_5.setStyleSheet(u"")

        self.horizontalLayout_7.addWidget(self.label_5)

        self.spinBox_diameter = QComboBox(self.horizontalWidget_2)
        self.spinBox_diameter.setObjectName(u"spinBox_diameter")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(2)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.spinBox_diameter.sizePolicy().hasHeightForWidth())
        self.spinBox_diameter.setSizePolicy(sizePolicy2)
        self.spinBox_diameter.setMaximumSize(QSize(70, 16777215))
        self.spinBox_diameter.setFont(font4)
        self.spinBox_diameter.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.spinBox_diameter.setStyleSheet(u"QComboBox {\n"
"	border: none;\n"
"	border-bottom: 1px solid white;\n"
"	background: rgba(255, 255, 255, 0);\n"
"	border-radius: none;\n"
"	transition: color 0.3s ease;\n"
"	transition: border-bottom 0.4s ease;\n"
"	color: rgb(204, 204, 204);\n"
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

        self.horizontalLayout_7.addWidget(self.spinBox_diameter)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_4)


        self.verticalLayout_5.addWidget(self.horizontalWidget_2)

        self.stackedWidget.addWidget(self.page_7)

        self.verticalLayout_6.addWidget(self.stackedWidget)


        self.verticalLayout_2.addWidget(self.widget_2)

        self.label_3 = QLabel(self.main)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font2)
        self.label_3.setStyleSheet(u"")

        self.verticalLayout_2.addWidget(self.label_3)

        self.widget_3 = QWidget(self.main)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setStyleSheet(u"color: white;")
        self.verticalLayout_7 = QVBoxLayout(self.widget_3)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.horizontalWidget_3 = QWidget(self.widget_3)
        self.horizontalWidget_3.setObjectName(u"horizontalWidget_3")
        self.horizontalWidget_3.setStyleSheet(u"border-radius: none;\n"
"border: none;\n"
"backround: none;")
        self.horizontalLayout_12 = QHBoxLayout(self.horizontalWidget_3)
        self.horizontalLayout_12.setSpacing(10)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_7)

        self.label_9 = QLabel(self.horizontalWidget_3)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font4)
        self.label_9.setStyleSheet(u"background: none;\n"
"border: none;\n"
"border-radius: none;")

        self.horizontalLayout_12.addWidget(self.label_9, 0, Qt.AlignmentFlag.AlignHCenter)

        self.doubleSpinBox_diameter_position = QDoubleSpinBox(self.horizontalWidget_3)
        self.doubleSpinBox_diameter_position.setObjectName(u"doubleSpinBox_diameter_position")
        self.doubleSpinBox_diameter_position.setStyleSheet(u"QDoubleSpinBox {\n"
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
        self.doubleSpinBox_diameter_position.setMaximum(1000.000000000000000)

        self.horizontalLayout_12.addWidget(self.doubleSpinBox_diameter_position)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_8)


        self.verticalLayout_7.addWidget(self.horizontalWidget_3)

        self.horizontalWidget_4 = QWidget(self.widget_3)
        self.horizontalWidget_4.setObjectName(u"horizontalWidget_4")
        self.horizontalWidget_4.setStyleSheet(u"border-radius: none;\n"
"border: none;")
        self.horizontalLayout_13 = QHBoxLayout(self.horizontalWidget_4)
        self.horizontalLayout_13.setSpacing(10)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_9)

        self.label_11 = QLabel(self.horizontalWidget_4)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font4)
        self.label_11.setStyleSheet(u"background: none;\n"
"border: none;\n"
"border-radius: none;")

        self.horizontalLayout_13.addWidget(self.label_11, 0, Qt.AlignmentFlag.AlignHCenter)

        self.spinBox_count = QSpinBox(self.horizontalWidget_4)
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

        self.horizontalLayout_13.addWidget(self.spinBox_count)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_10)


        self.verticalLayout_7.addWidget(self.horizontalWidget_4)

        self.horizontalWidget_5 = QWidget(self.widget_3)
        self.horizontalWidget_5.setObjectName(u"horizontalWidget_5")
        self.horizontalWidget_5.setStyleSheet(u"border-radius: none;\n"
"border: none;")
        self.horizontalLayout_14 = QHBoxLayout(self.horizontalWidget_5)
        self.horizontalLayout_14.setSpacing(10)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_15 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_15)

        self.label_13 = QLabel(self.horizontalWidget_5)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setFont(font4)
        self.label_13.setStyleSheet(u"background: none;\n"
"border: none;\n"
"border-radius: none;")

        self.horizontalLayout_14.addWidget(self.label_13, 0, Qt.AlignmentFlag.AlignHCenter)

        self.spinBox_angle = QSpinBox(self.horizontalWidget_5)
        self.spinBox_angle.setObjectName(u"spinBox_angle")
        self.spinBox_angle.setStyleSheet(u"QSpinBox {\n"
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
        self.spinBox_angle.setMinimum(0)
        self.spinBox_angle.setMaximum(360)
        self.spinBox_angle.setValue(0)

        self.horizontalLayout_14.addWidget(self.spinBox_angle)

        self.horizontalSpacer_16 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_16)


        self.verticalLayout_7.addWidget(self.horizontalWidget_5)


        self.verticalLayout_2.addWidget(self.widget_3)

        self.label_4 = QLabel(self.main)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font2)
        self.label_4.setStyleSheet(u"")

        self.verticalLayout_2.addWidget(self.label_4)

        self.widget_4 = QWidget(self.main)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setStyleSheet(u"color: white;")
        self.verticalLayout_8 = QVBoxLayout(self.widget_4)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.horizontalWidget_6 = QWidget(self.widget_4)
        self.horizontalWidget_6.setObjectName(u"horizontalWidget_6")
        self.horizontalWidget_6.setStyleSheet(u"border-radius: none;\n"
"border: none;")
        self.horizontalLayout_15 = QHBoxLayout(self.horizontalWidget_6)
        self.horizontalLayout_15.setSpacing(10)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_17 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_17)

        self.label_14 = QLabel(self.horizontalWidget_6)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setFont(font4)
        self.label_14.setStyleSheet(u"background: none;\n"
"border: none;\n"
"border-radius: none;")

        self.horizontalLayout_15.addWidget(self.label_14, 0, Qt.AlignmentFlag.AlignHCenter)

        self.doubleSpinBox_dopusk = QDoubleSpinBox(self.horizontalWidget_6)
        self.doubleSpinBox_dopusk.setObjectName(u"doubleSpinBox_dopusk")
        self.doubleSpinBox_dopusk.setStyleSheet(u"QDoubleSpinBox {\n"
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
        self.doubleSpinBox_dopusk.setDecimals(3)
        self.doubleSpinBox_dopusk.setMinimum(-1.000000000000000)
        self.doubleSpinBox_dopusk.setMaximum(1.000000000000000)
        self.doubleSpinBox_dopusk.setSingleStep(0.010000000000000)

        self.horizontalLayout_15.addWidget(self.doubleSpinBox_dopusk)

        self.label_15 = QLabel(self.horizontalWidget_6)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setFont(font4)
        self.label_15.setStyleSheet(u"background: none;\n"
"border: none;\n"
"border-radius: none;")

        self.horizontalLayout_15.addWidget(self.label_15)

        self.lineEdit_baza = QLineEdit(self.horizontalWidget_6)
        self.lineEdit_baza.setObjectName(u"lineEdit_baza")
        self.lineEdit_baza.setStyleSheet(u"QLineEdit {\n"
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

        self.horizontalLayout_15.addWidget(self.lineEdit_baza)

        self.horizontalSpacer_18 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_18)


        self.verticalLayout_8.addWidget(self.horizontalWidget_6)


        self.verticalLayout_2.addWidget(self.widget_4)

        self.btn_save_result = QPushButton(self.main)
        self.btn_save_result.setObjectName(u"btn_save_result")
        font5 = QFont()
        font5.setBold(True)
        self.btn_save_result.setFont(font5)
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

        self.verticalLayout_2.addWidget(self.btn_save_result, 0, Qt.AlignmentFlag.AlignHCenter)


        self.horizontalLayout.addWidget(self.main)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.verticalLayout_9.addLayout(self.horizontalLayout)

        self.text_info = QLabel(self.widget)
        self.text_info.setObjectName(u"text_info")
        font6 = QFont()
        font6.setPointSize(10)
        self.text_info.setFont(font6)
        self.text_info.setStyleSheet(u"background:none")
        self.text_info.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_9.addWidget(self.text_info)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, 0, -1, -1)
        self.btn_clear_table = QPushButton(self.widget)
        self.btn_clear_table.setObjectName(u"btn_clear_table")
        self.btn_clear_table.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_clear_table.setStyleSheet(u"QPushButton {\n"
"	border-bottom: 1px solid white;\n"
"	height: 30px;\n"
"	background-color: rgba(0,0,0,0);\n"
"	padding: 5 20 5 5\n"
"\n"
"}\n"
"QPushButton:hover {\n"
"	border-radius: 10px;\n"
"	border: none;\n"
"	background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(12, 123, 147, 177), stop:1 rgba(39, 73, 109, 255))\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: rgb(0, 53, 93)\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/icons/clear.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_clear_table.setIcon(icon2)

        self.horizontalLayout_2.addWidget(self.btn_clear_table, 0, Qt.AlignmentFlag.AlignRight)


        self.verticalLayout_9.addLayout(self.horizontalLayout_2)

        self.table_widget_razmetka = QTableWidget(self.widget)
        if (self.table_widget_razmetka.columnCount() < 3):
            self.table_widget_razmetka.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.table_widget_razmetka.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.table_widget_razmetka.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.table_widget_razmetka.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.table_widget_razmetka.setObjectName(u"table_widget_razmetka")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.table_widget_razmetka.sizePolicy().hasHeightForWidth())
        self.table_widget_razmetka.setSizePolicy(sizePolicy3)
        self.table_widget_razmetka.setFont(font6)
        self.table_widget_razmetka.setStyleSheet(u"/* \u0421\u0430\u043c \u0432\u0438\u0434\u0436\u0435\u0442 \u2014 \u043f\u0440\u043e\u0437\u0440\u0430\u0447\u043d\u044b\u0439 \u0444\u043e\u043d */\n"
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
        self.table_widget_razmetka.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.table_widget_razmetka.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.table_widget_razmetka.setAutoScroll(False)
        self.table_widget_razmetka.setRowCount(0)
        self.table_widget_razmetka.setColumnCount(3)
        self.table_widget_razmetka.verticalHeader().setMinimumSectionSize(90)
        self.table_widget_razmetka.verticalHeader().setDefaultSectionSize(100)

        self.verticalLayout_9.addWidget(self.table_widget_razmetka)


        self.verticalLayout_4.addWidget(self.widget)


        self.verticalLayout.addLayout(self.verticalLayout_4)

        self.btn_save_and_export = QPushButton(PageRazmetka)
        self.btn_save_and_export.setObjectName(u"btn_save_and_export")
        self.btn_save_and_export.setMaximumSize(QSize(16777215, 16777215))
        font7 = QFont()
        font7.setPointSize(15)
        self.btn_save_and_export.setFont(font7)
        self.btn_save_and_export.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_save_and_export.setStyleSheet(u"QPushButton {\n"
"	border: 1px solid;\n"
"	border-color: rgb(125, 50, 50);\n"
"	border-radius: 2px;\n"
"	height: 30px;	\n"
"	width: 350px;\n"
"	background-color: rgb(185, 57, 41);\n"
"	padding: 2 5 5 5;\n"
"	font-size: 15pt;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(175, 41, 41)\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: rgb(115, 28, 28)\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u":/icons/export.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_save_and_export.setIcon(icon3)
        self.btn_save_and_export.setIconSize(QSize(20, 20))

        self.verticalLayout.addWidget(self.btn_save_and_export, 0, Qt.AlignmentFlag.AlignHCenter)


        self.retranslateUi(PageRazmetka)
        self.pushButton_rezba.clicked["bool"].connect(self.horizontalWidget_2.show)
        self.pushButton_no_rezba.clicked["bool"].connect(self.horizontalWidget_2.hide)

        self.pushButton_rezba.setDefault(False)
        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(PageRazmetka)
    # setupUi

    def retranslateUi(self, PageRazmetka):
        PageRazmetka.setWindowTitle(QCoreApplication.translate("PageRazmetka", u"Form", None))
        self.btn_home_2.setText(QCoreApplication.translate("PageRazmetka", u" \u041d\u0410\u0417\u0410\u0414", None))
        self.label.setText(QCoreApplication.translate("PageRazmetka", u"\u0420\u0430\u0437\u043c\u0435\u0442\u043a\u0430 \u043e\u0442\u0432\u0435\u0440\u0441\u0442\u0438\u0439", None))
        self.label_2.setText(QCoreApplication.translate("PageRazmetka", u"\u041e\u043f\u0435\u0440\u0435\u0434\u0435\u043b\u0435\u043d\u0438\u044f \u043e\u0442\u0432\u0435\u0440\u0441\u0442\u0438\u0439:", None))
        self.pushButton_rezba.setText(QCoreApplication.translate("PageRazmetka", u"\u041e\u0442\u0432\u0435\u0440\u0441\u0442\u0438\u0435 \u0441 \u0440\u0435\u0437\u044c\u0431\u043e\u0439", None))
        self.pushButton_no_rezba.setText(QCoreApplication.translate("PageRazmetka", u"\u041e\u0442\u0432\u0435\u0440\u0441\u0442\u0438\u0435 \u0431\u0435\u0437 \u0440\u0435\u0437\u044c\u0431\u044b", None))
        self.label_8.setText(QCoreApplication.translate("PageRazmetka", u"\u041e\u0431\u043e\u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0435 \u043e\u0442\u0432\u0435\u0440\u0441\u0442\u0438\u044f(-\u0438\u0439): ", None))
        self.doubleSpinBox_diameter.setPrefix(QCoreApplication.translate("PageRazmetka", u"\u00d8 ", None))
        self.doubleSpinBox_diameter.setSuffix("")
        self.label_5.setText(QCoreApplication.translate("PageRazmetka", u"\u041e\u0431\u043e\u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0435 \u043e\u0442\u0432\u0435\u0440\u0441\u0442\u0438\u044f(-\u0438\u0439): ", None))
        self.spinBox_diameter.setPlaceholderText(QCoreApplication.translate("PageRazmetka", u"\u0420\u0435\u0437\u044c\u0431\u0430...", None))
        self.label_3.setText(QCoreApplication.translate("PageRazmetka", u"\u0420\u0430\u0441\u043f\u043e\u043b\u043e\u0436\u0435\u043d\u0438\u0435 \u043e\u0442\u0432\u0435\u0440\u0441\u0442\u0438\u0439:", None))
        self.label_9.setText(QCoreApplication.translate("PageRazmetka", u"\u041d\u043e\u043c\u0438\u043d\u0430\u043b\u044c\u043d\u044b\u0439 \u0434\u0438\u0430\u043c\u0435\u0442\u0440 \u0440\u0430\u0437\u043c\u0435\u0442\u043a\u0438: ", None))
        self.doubleSpinBox_diameter_position.setPrefix(QCoreApplication.translate("PageRazmetka", u"\u00d8 ", None))
        self.doubleSpinBox_diameter_position.setSuffix("")
        self.label_11.setText(QCoreApplication.translate("PageRazmetka", u"\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u043e\u0442\u0432\u0435\u0440\u0441\u0442\u0438\u0439:", None))
        self.spinBox_count.setSuffix(QCoreApplication.translate("PageRazmetka", u" \u0448\u0442.", None))
        self.label_13.setText(QCoreApplication.translate("PageRazmetka", u"\u041e\u0441\u0435\u0432\u043e\u0439 \u0443\u0433\u043e\u043b \u0441\u043c\u0435\u0449\u0435\u043d\u0438\u044f:", None))
        self.spinBox_angle.setSuffix(QCoreApplication.translate("PageRazmetka", u" \u00b0", None))
        self.label_4.setText(QCoreApplication.translate("PageRazmetka", u"\u041f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u044b \u043e\u0442\u0432\u0435\u0440\u0441\u0442\u0438\u0439:", None))
        self.label_14.setText(QCoreApplication.translate("PageRazmetka", u"\u041f\u043e\u0437\u0438\u0446\u0438\u043e\u043d\u044b\u0439 \u0434\u043e\u043f\u0443\u0441\u043a:", None))
        self.doubleSpinBox_dopusk.setSuffix(QCoreApplication.translate("PageRazmetka", u" \u043c\u043c.", None))
        self.label_15.setText(QCoreApplication.translate("PageRazmetka", u"\u0411\u0430\u0437\u0430:", None))
        self.lineEdit_baza.setPlaceholderText(QCoreApplication.translate("PageRazmetka", u"\u041e\u0431\u043e\u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0435..", None))
        self.btn_save_result.setText(QCoreApplication.translate("PageRazmetka", u" \u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u044f", None))
        self.text_info.setText("")
        self.btn_clear_table.setText(QCoreApplication.translate("PageRazmetka", u"\u041e\u0447\u0438\u0441\u0442\u0438\u0442\u044c \u0442\u0430\u0431\u043b\u0438\u0446\u0443", None))
        ___qtablewidgetitem = self.table_widget_razmetka.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("PageRazmetka", u"\u0418\u043d\u0441\u0442\u0440\u0443\u043c\u0435\u043d\u0442", None))
        ___qtablewidgetitem1 = self.table_widget_razmetka.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("PageRazmetka", u"\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 [\u041c\u043e\u0436\u043d\u043e \u0438\u0437\u043c\u0435\u043d\u044f\u0442\u044c]", None))
        self.btn_save_and_export.setText(QCoreApplication.translate("PageRazmetka", u"\u041f\u0435\u0440\u0435\u043d\u0435\u0441\u0442\u0438 \u043f\u0435\u0440\u0435\u0445\u043e\u0434\u044b \u0432 \u0422\u0435\u0445\u043d\u043e\u041f\u0440\u043e", None))
    # retranslateUi

