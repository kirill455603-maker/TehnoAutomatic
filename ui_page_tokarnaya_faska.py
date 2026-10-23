# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_page_tokarnaya_faska.ui'
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
    QHeaderView, QLabel, QPushButton, QRadioButton,
    QSizePolicy, QSpacerItem, QSpinBox, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)
import res_rc

class Ui_PageTokarnayaFaska(object):
    def setupUi(self, PageTokarnayaFaska):
        if not PageTokarnayaFaska.objectName():
            PageTokarnayaFaska.setObjectName(u"PageTokarnayaFaska")
        PageTokarnayaFaska.resize(1000, 587)
        PageTokarnayaFaska.setMinimumSize(QSize(1000, 0))
        PageTokarnayaFaska.setStyleSheet(u"color: white;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0, stop:0 rgba(20, 40, 80, 255), stop:1 rgba(39, 73, 109, 255));\n"
"")
        self.verticalLayout = QVBoxLayout(PageTokarnayaFaska)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.btn_home_tokarnaya_faska = QPushButton(PageTokarnayaFaska)
        self.btn_home_tokarnaya_faska.setObjectName(u"btn_home_tokarnaya_faska")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_home_tokarnaya_faska.sizePolicy().hasHeightForWidth())
        self.btn_home_tokarnaya_faska.setSizePolicy(sizePolicy)
        self.btn_home_tokarnaya_faska.setMinimumSize(QSize(70, 0))
        self.btn_home_tokarnaya_faska.setMaximumSize(QSize(150, 30))
        font = QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.btn_home_tokarnaya_faska.setFont(font)
        self.btn_home_tokarnaya_faska.setStyleSheet(u"QPushButton {\n"
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
        self.btn_home_tokarnaya_faska.setIcon(icon)
        self.btn_home_tokarnaya_faska.setIconSize(QSize(20, 20))

        self.verticalLayout.addWidget(self.btn_home_tokarnaya_faska, 0, Qt.AlignmentFlag.AlignLeft)

        self.verticalSpacer = QSpacerItem(979, 78, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.label_7 = QLabel(PageTokarnayaFaska)
        self.label_7.setObjectName(u"label_7")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy1)
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

        self.verticalLayout.addWidget(self.label_7)

        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setSpacing(10)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, 10, -1, -1)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.main = QWidget(PageTokarnayaFaska)
        self.main.setObjectName(u"main")
        self.main.setMouseTracking(True)
        self.main.setTabletTracking(False)
        self.main.setAutoFillBackground(False)
        self.main.setStyleSheet(u"QWidget {\n"
"	background: none;\n"
"	\n"
"}\n"
"")
        self.verticalLayout_11 = QVBoxLayout(self.main)
        self.verticalLayout_11.setSpacing(10)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(10, 20, 10, 20)
        self.label_6 = QLabel(self.main)
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

        self.verticalLayout_11.addWidget(self.label_6)

        self.widget = QWidget(self.main)
        self.widget.setObjectName(u"widget")
        self.widget.setStyleSheet(u"QWidget {\n"
"	background: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0, stop:0 rgba(39, 72, 109, 129), stop:1 rgba(21, 41, 81, 129));\n"
"\n"
"}\n"
"Line {\n"
"	background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(8, 81, 97, 128), stop:1 rgba(0, 117, 142, 106))\n"
"}")
        self.verticalLayout_2 = QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalWidget_2 = QWidget(self.widget)
        self.horizontalWidget_2.setObjectName(u"horizontalWidget_2")
        self.horizontalWidget_2.setStyleSheet(u"border-radius: none;\n"
"border: none;\n"
"background: none;")
        self.horizontalLayout_2 = QHBoxLayout(self.horizontalWidget_2)
        self.horizontalLayout_2.setSpacing(10)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)

        self.label = QLabel(self.horizontalWidget_2)
        self.label.setObjectName(u"label")
        font3 = QFont()
        font3.setPointSize(11)
        self.label.setFont(font3)
        self.label.setStyleSheet(u"background: none;\n"
"border: none;\n"
"\n"
"border-radius: none;")

        self.horizontalLayout_2.addWidget(self.label, 0, Qt.AlignmentFlag.AlignHCenter)

        self.doubleSpinBox_len = QDoubleSpinBox(self.horizontalWidget_2)
        self.doubleSpinBox_len.setObjectName(u"doubleSpinBox_len")
        self.doubleSpinBox_len.setStyleSheet(u"QDoubleSpinBox {\n"
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
        self.doubleSpinBox_len.setMinimum(0.000000000000000)
        self.doubleSpinBox_len.setMaximum(50.000000000000000)
        self.doubleSpinBox_len.setValue(1.000000000000000)

        self.horizontalLayout_2.addWidget(self.doubleSpinBox_len, 0, Qt.AlignmentFlag.AlignRight)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_4)


        self.verticalLayout_2.addWidget(self.horizontalWidget_2)

        self.horizontalWidget_3 = QWidget(self.widget)
        self.horizontalWidget_3.setObjectName(u"horizontalWidget_3")
        self.horizontalWidget_3.setStyleSheet(u"border-radius: none;\n"
"border: none;\n"
"background: none;")
        self.horizontalLayout_4 = QHBoxLayout(self.horizontalWidget_3)
        self.horizontalLayout_4.setSpacing(10)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_5)

        self.label_2 = QLabel(self.horizontalWidget_3)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font3)
        self.label_2.setStyleSheet(u"background: none;\n"
"border: none;\n"
"\n"
"border-radius: none;")

        self.horizontalLayout_4.addWidget(self.label_2, 0, Qt.AlignmentFlag.AlignHCenter)

        self.spinBox_angle = QSpinBox(self.horizontalWidget_3)
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
        self.spinBox_angle.setValue(45)

        self.horizontalLayout_4.addWidget(self.spinBox_angle)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_6)


        self.verticalLayout_2.addWidget(self.horizontalWidget_3)


        self.verticalLayout_11.addWidget(self.widget)

        self.label_8 = QLabel(self.main)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font2)
        self.label_8.setStyleSheet(u"QLabel {\n"
"	background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(12, 123, 147, 255), stop:1 rgba(0, 168, 204, 255));\n"
"	padding-left: 2px;	\n"
"	color: rgb(24, 45, 76)\n"
"}\n"
"")

        self.verticalLayout_11.addWidget(self.label_8)

        self.widget_2 = QWidget(self.main)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setStyleSheet(u"QWidget {\n"
"	background: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0, stop:0 rgba(39, 72, 109, 129), stop:1 rgba(21, 41, 81, 129));\n"
"\n"
"}\n"
"Line {\n"
"	background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(8, 81, 97, 128), stop:1 rgba(0, 117, 142, 106))\n"
"}")
        self.verticalLayout_3 = QVBoxLayout(self.widget_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalWidget_4 = QWidget(self.widget_2)
        self.horizontalWidget_4.setObjectName(u"horizontalWidget_4")
        self.horizontalWidget_4.setStyleSheet(u"border-radius: none;\n"
"border: none;\n"
"background: none;")
        self.horizontalLayout_5 = QHBoxLayout(self.horizontalWidget_4)
        self.horizontalLayout_5.setSpacing(10)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_7)

        self.label_3 = QLabel(self.horizontalWidget_4)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font3)
        self.label_3.setStyleSheet(u"background: none;\n"
"border: none;\n"
"\n"
"border-radius: none;")

        self.horizontalLayout_5.addWidget(self.label_3, 0, Qt.AlignmentFlag.AlignHCenter)

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
        self.spinBox_count.setMaximum(10)

        self.horizontalLayout_5.addWidget(self.spinBox_count)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_8)


        self.verticalLayout_3.addWidget(self.horizontalWidget_4)

        self.horizontalWidget_5 = QWidget(self.widget_2)
        self.horizontalWidget_5.setObjectName(u"horizontalWidget_5")
        self.horizontalWidget_5.setStyleSheet(u"border-radius: none;\n"
"border: none;\n"
"background: none;")
        self.horizontalLayout_6 = QHBoxLayout(self.horizontalWidget_5)
        self.horizontalLayout_6.setSpacing(10)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_9)

        self.label_11 = QLabel(self.horizontalWidget_5)
        self.label_11.setObjectName(u"label_11")
        font4 = QFont()
        font4.setPointSize(11)
        font4.setUnderline(False)
        self.label_11.setFont(font4)
        self.label_11.setStyleSheet(u"background: none;\n"
"border: none;\n"
"border-radius: none;\n"
"color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(12, 123, 147, 255), stop:1 rgba(0, 168, 204, 255))")

        self.horizontalLayout_6.addWidget(self.label_11)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_10)


        self.verticalLayout_3.addWidget(self.horizontalWidget_5)

        self.groupBox = QGroupBox(self.widget_2)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setFont(font3)
        self.groupBox.setStyleSheet(u"border: none;\n"
"border-radius: 0;\n"
"background: none;")
        self.groupBox.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.horizontalLayout_8 = QHBoxLayout(self.groupBox)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.radioButton_in_2 = QRadioButton(self.groupBox)
        self.radioButton_in_2.setObjectName(u"radioButton_in_2")
        self.radioButton_in_2.setFont(font3)
        self.radioButton_in_2.setChecked(False)

        self.horizontalLayout_8.addWidget(self.radioButton_in_2, 0, Qt.AlignmentFlag.AlignHCenter)

        self.radioButton_out_2 = QRadioButton(self.groupBox)
        self.radioButton_out_2.setObjectName(u"radioButton_out_2")
        self.radioButton_out_2.setFont(font3)
        self.radioButton_out_2.setChecked(True)

        self.horizontalLayout_8.addWidget(self.radioButton_out_2, 0, Qt.AlignmentFlag.AlignHCenter)


        self.verticalLayout_3.addWidget(self.groupBox)


        self.verticalLayout_11.addWidget(self.widget_2)

        self.btn_save_result_faska = QPushButton(self.main)
        self.btn_save_result_faska.setObjectName(u"btn_save_result_faska")
        font5 = QFont()
        font5.setBold(True)
        self.btn_save_result_faska.setFont(font5)
        self.btn_save_result_faska.setStyleSheet(u"QPushButton {\n"
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
        self.btn_save_result_faska.setIcon(icon1)
        self.btn_save_result_faska.setIconSize(QSize(20, 20))

        self.verticalLayout_11.addWidget(self.btn_save_result_faska, 0, Qt.AlignmentFlag.AlignHCenter)


        self.horizontalLayout.addWidget(self.main)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.verticalLayout_10.addLayout(self.horizontalLayout)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_10.addItem(self.verticalSpacer_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.table_widget_faska = QTableWidget(PageTokarnayaFaska)
        if (self.table_widget_faska.columnCount() < 2):
            self.table_widget_faska.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.table_widget_faska.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.table_widget_faska.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        self.table_widget_faska.setObjectName(u"table_widget_faska")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.table_widget_faska.sizePolicy().hasHeightForWidth())
        self.table_widget_faska.setSizePolicy(sizePolicy2)
        font6 = QFont()
        font6.setPointSize(10)
        self.table_widget_faska.setFont(font6)
        self.table_widget_faska.setStyleSheet(u"/* \u0421\u0430\u043c \u0432\u0438\u0434\u0436\u0435\u0442 \u2014 \u043f\u0440\u043e\u0437\u0440\u0430\u0447\u043d\u044b\u0439 \u0444\u043e\u043d */\n"
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
        self.table_widget_faska.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.table_widget_faska.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.table_widget_faska.setAutoScroll(False)
        self.table_widget_faska.setRowCount(0)
        self.table_widget_faska.setColumnCount(2)
        self.table_widget_faska.verticalHeader().setVisible(False)
        self.table_widget_faska.verticalHeader().setMinimumSectionSize(90)
        self.table_widget_faska.verticalHeader().setDefaultSectionSize(100)

        self.horizontalLayout_3.addWidget(self.table_widget_faska)


        self.verticalLayout_10.addLayout(self.horizontalLayout_3)


        self.verticalLayout.addLayout(self.verticalLayout_10)

        self.text_error_faska = QLabel(PageTokarnayaFaska)
        self.text_error_faska.setObjectName(u"text_error_faska")
        self.text_error_faska.setFont(font6)
        self.text_error_faska.setStyleSheet(u"background:none")
        self.text_error_faska.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.text_error_faska)


        self.retranslateUi(PageTokarnayaFaska)

        QMetaObject.connectSlotsByName(PageTokarnayaFaska)
    # setupUi

    def retranslateUi(self, PageTokarnayaFaska):
        PageTokarnayaFaska.setWindowTitle(QCoreApplication.translate("PageTokarnayaFaska", u"Form", None))
        self.btn_home_tokarnaya_faska.setText(QCoreApplication.translate("PageTokarnayaFaska", u" \u041d\u0410\u0417\u0410\u0414", None))
        self.label_7.setText(QCoreApplication.translate("PageTokarnayaFaska", u"\u0424\u0410\u0421\u041a\u0410", None))
        self.label_6.setText(QCoreApplication.translate("PageTokarnayaFaska", u"\u041f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u044b \u0444\u043e\u0440\u043c\u044b \u0444\u0430\u0441\u043a\u0438:", None))
        self.label.setText(QCoreApplication.translate("PageTokarnayaFaska", u"\u0414\u043b\u0438\u043d\u0430:", None))
        self.doubleSpinBox_len.setSuffix(QCoreApplication.translate("PageTokarnayaFaska", u" \u043c\u043c", None))
        self.label_2.setText(QCoreApplication.translate("PageTokarnayaFaska", u"\u0423\u0433\u043e\u043b:", None))
        self.spinBox_angle.setSuffix(QCoreApplication.translate("PageTokarnayaFaska", u" \u00b0", None))
        self.label_8.setText(QCoreApplication.translate("PageTokarnayaFaska", u"\u041f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u044b \u0440\u0430\u0437\u043c\u0435\u0449\u0435\u043d\u0438\u044f \u0444\u0430\u0441\u043a\u0438:", None))
        self.label_3.setText(QCoreApplication.translate("PageTokarnayaFaska", u"\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e:", None))
        self.spinBox_count.setSuffix("")
        self.label_11.setText(QCoreApplication.translate("PageTokarnayaFaska", u"\u0420\u0430\u0441\u043f\u043e\u043b\u043e\u0436\u0435\u043d\u0438\u0435 \u0444\u0430\u0441\u043a\u0438:", None))
        self.groupBox.setTitle("")
        self.radioButton_in_2.setText(QCoreApplication.translate("PageTokarnayaFaska", u"\u0412\u043d\u0443\u0442\u0440\u0435\u043d\u043d\u044f\u044f", None))
        self.radioButton_out_2.setText(QCoreApplication.translate("PageTokarnayaFaska", u"\u0412\u043d\u0435\u0448\u043d\u044f\u044f", None))
        self.btn_save_result_faska.setText(QCoreApplication.translate("PageTokarnayaFaska", u" \u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u044f", None))
#if QT_CONFIG(shortcut)
        self.btn_save_result_faska.setShortcut(QCoreApplication.translate("PageTokarnayaFaska", u"Ctrl+R", None))
#endif // QT_CONFIG(shortcut)
        ___qtablewidgetitem = self.table_widget_faska.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("PageTokarnayaFaska", u"\u0418\u043d\u0441\u0442\u0440\u0443\u043c\u0435\u043d\u0442", None))
        ___qtablewidgetitem1 = self.table_widget_faska.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("PageTokarnayaFaska", u"\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435", None))
        self.text_error_faska.setText("")
    # retranslateUi

