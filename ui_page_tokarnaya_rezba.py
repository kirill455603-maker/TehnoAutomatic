# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_page_tokarnaya_rezba.ui'
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
    QHBoxLayout, QHeaderView, QLabel, QPushButton,
    QRadioButton, QSizePolicy, QSpacerItem, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)
import res_rc

class Ui_PageTokarnayaRezba(object):
    def setupUi(self, PageTokarnayaRezba):
        if not PageTokarnayaRezba.objectName():
            PageTokarnayaRezba.setObjectName(u"PageTokarnayaRezba")
        PageTokarnayaRezba.resize(1000, 729)
        PageTokarnayaRezba.setStyleSheet(u"color: white;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0, stop:0 rgba(20, 40, 80, 255), stop:1 rgba(39, 73, 109, 255));\n"
"")
        self.verticalLayout_2 = QVBoxLayout(PageTokarnayaRezba)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, 0, -1, -1)
        self.btn_home = QPushButton(PageTokarnayaRezba)
        self.btn_home.setObjectName(u"btn_home")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_home.sizePolicy().hasHeightForWidth())
        self.btn_home.setSizePolicy(sizePolicy)
        self.btn_home.setMinimumSize(QSize(70, 0))
        self.btn_home.setMaximumSize(QSize(150, 30))
        font = QFont()
        font.setPointSize(11)
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

        self.horizontalLayout_3.addWidget(self.btn_home, 0, Qt.AlignmentFlag.AlignLeft)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.label_7 = QLabel(PageTokarnayaRezba)
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

        self.verticalLayout_2.addWidget(self.label_7)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(-1, 10, -1, -1)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer)

        self.main = QWidget(PageTokarnayaRezba)
        self.main.setObjectName(u"main")
        self.main.setMouseTracking(True)
        self.main.setTabletTracking(False)
        self.main.setAutoFillBackground(False)
        self.main.setStyleSheet(u"QWidget {\n"
"	border: none;\n"
"	background: none;\n"
"}\n"
"")
        self.verticalLayout_11 = QVBoxLayout(self.main)
        self.verticalLayout_11.setSpacing(12)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(10, 10, 10, 20)
        self.label_12 = QLabel(self.main)
        self.label_12.setObjectName(u"label_12")
        font2 = QFont()
        font2.setFamilies([u"Segoe UI Light"])
        font2.setPointSize(10)
        font2.setBold(False)
        self.label_12.setFont(font2)
        self.label_12.setStyleSheet(u"QLabel {\n"
"	background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(12, 123, 147, 255), stop:1 rgba(0, 168, 204, 255));\n"
"	padding-left: 2px;	\n"
"	color: rgb(24, 45, 76)\n"
"}\n"
"")

        self.verticalLayout_11.addWidget(self.label_12)

        self.widget = QWidget(self.main)
        self.widget.setObjectName(u"widget")
        self.widget.setStyleSheet(u"QWidget {\n"
"	background: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0, stop:0 rgba(39, 72, 109, 129), stop:1 rgba(21, 41, 81, 129))\n"
"}")
        self.verticalLayout_3 = QVBoxLayout(self.widget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalWidget_2 = QWidget(self.widget)
        self.horizontalWidget_2.setObjectName(u"horizontalWidget_2")
        self.horizontalWidget_2.setStyleSheet(u"border-radius: none;\n"
"border: none;\n"
"background: none;")
        self.horizontalLayout_7 = QHBoxLayout(self.horizontalWidget_2)
        self.horizontalLayout_7.setSpacing(10)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_3)

        self.label_5 = QLabel(self.horizontalWidget_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font)
        self.label_5.setStyleSheet(u"background: none;\n"
"border: none;\n"
"border-radius: none;")

        self.horizontalLayout_7.addWidget(self.label_5, 0, Qt.AlignmentFlag.AlignHCenter)

        self.spinBox_diameter = QComboBox(self.horizontalWidget_2)
        self.spinBox_diameter.setObjectName(u"spinBox_diameter")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(2)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.spinBox_diameter.sizePolicy().hasHeightForWidth())
        self.spinBox_diameter.setSizePolicy(sizePolicy2)
        self.spinBox_diameter.setMaximumSize(QSize(70, 16777215))
        self.spinBox_diameter.setFont(font)
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


        self.verticalLayout_3.addWidget(self.horizontalWidget_2)

        self.horizontalWidget_3 = QWidget(self.widget)
        self.horizontalWidget_3.setObjectName(u"horizontalWidget_3")
        self.horizontalWidget_3.setStyleSheet(u"border-radius: none;\n"
"border: none;\n"
"background: none;")
        self.horizontalLayout_8 = QHBoxLayout(self.horizontalWidget_3)
        self.horizontalLayout_8.setSpacing(10)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_5)

        self.label_6 = QLabel(self.horizontalWidget_3)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font)
        self.label_6.setStyleSheet(u"background: none;\n"
"border: none;\n"
"border-radius: none;")

        self.horizontalLayout_8.addWidget(self.label_6, 0, Qt.AlignmentFlag.AlignHCenter)

        self.comboBox_step = QComboBox(self.horizontalWidget_3)
        self.comboBox_step.setObjectName(u"comboBox_step")
        sizePolicy2.setHeightForWidth(self.comboBox_step.sizePolicy().hasHeightForWidth())
        self.comboBox_step.setSizePolicy(sizePolicy2)
        self.comboBox_step.setMaximumSize(QSize(70, 16777215))
        self.comboBox_step.setFont(font)
        self.comboBox_step.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.comboBox_step.setStyleSheet(u"QComboBox {\n"
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

        self.horizontalLayout_8.addWidget(self.comboBox_step)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_6)


        self.verticalLayout_3.addWidget(self.horizontalWidget_3)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_7)

        self.label_9 = QLabel(self.widget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font)
        self.label_9.setStyleSheet(u"background: none;\n"
"border: none;\n"
"border-radius: none;")

        self.horizontalLayout.addWidget(self.label_9, 0, Qt.AlignmentFlag.AlignHCenter)

        self.double_spin_length = QDoubleSpinBox(self.widget)
        self.double_spin_length.setObjectName(u"double_spin_length")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.double_spin_length.sizePolicy().hasHeightForWidth())
        self.double_spin_length.setSizePolicy(sizePolicy3)
        self.double_spin_length.setMinimumSize(QSize(100, 30))
        self.double_spin_length.setMaximumSize(QSize(100, 16777215))
        self.double_spin_length.setStyleSheet(u"QDoubleSpinBox {\n"
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
        self.double_spin_length.setMaximum(200.000000000000000)

        self.horizontalLayout.addWidget(self.double_spin_length, 0, Qt.AlignmentFlag.AlignHCenter)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_8)


        self.verticalLayout_3.addLayout(self.horizontalLayout)


        self.verticalLayout_11.addWidget(self.widget)

        self.label_13 = QLabel(self.main)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setFont(font2)
        self.label_13.setStyleSheet(u"QLabel {\n"
"	background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(12, 123, 147, 255), stop:1 rgba(0, 168, 204, 255));\n"
"	padding-left: 2px;	\n"
"	color: rgb(24, 45, 76)\n"
"}\n"
"")

        self.verticalLayout_11.addWidget(self.label_13)

        self.widget_2 = QWidget(self.main)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setStyleSheet(u"QWidget {\n"
"	background: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0, stop:0 rgba(39, 72, 109, 129), stop:1 rgba(21, 41, 81, 129))\n"
"}")
        self.verticalLayout_4 = QVBoxLayout(self.widget_2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_10 = QLabel(self.widget_2)
        self.label_10.setObjectName(u"label_10")
        font3 = QFont()
        font3.setPointSize(11)
        font3.setUnderline(False)
        self.label_10.setFont(font3)
        self.label_10.setStyleSheet(u"background: none;\n"
"border: none;\n"
"border-radius: none;\n"
"color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(12, 123, 147, 255), stop:1 rgba(0, 168, 204, 255))")

        self.verticalLayout_4.addWidget(self.label_10, 0, Qt.AlignmentFlag.AlignHCenter)

        self.groupBox = QGroupBox(self.widget_2)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setFont(font)
        self.groupBox.setStyleSheet(u"border: none;\n"
"border-radius: 0;\n"
"background: none;")
        self.groupBox.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.horizontalLayout_2 = QHBoxLayout(self.groupBox)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.radioButton_in = QRadioButton(self.groupBox)
        self.radioButton_in.setObjectName(u"radioButton_in")
        self.radioButton_in.setFont(font)
        self.radioButton_in.setChecked(False)

        self.horizontalLayout_2.addWidget(self.radioButton_in, 0, Qt.AlignmentFlag.AlignHCenter)

        self.radioButton_out = QRadioButton(self.groupBox)
        self.radioButton_out.setObjectName(u"radioButton_out")
        self.radioButton_out.setFont(font)
        self.radioButton_out.setChecked(True)

        self.horizontalLayout_2.addWidget(self.radioButton_out, 0, Qt.AlignmentFlag.AlignHCenter)


        self.verticalLayout_4.addWidget(self.groupBox)

        self.label_11 = QLabel(self.widget_2)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font3)
        self.label_11.setStyleSheet(u"background: none;\n"
"border: none;\n"
"border-radius: none;\n"
"color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(12, 123, 147, 255), stop:1 rgba(0, 168, 204, 255))")

        self.verticalLayout_4.addWidget(self.label_11, 0, Qt.AlignmentFlag.AlignHCenter)

        self.groupBox_2 = QGroupBox(self.widget_2)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setFont(font)
        self.groupBox_2.setStyleSheet(u"border: none;\n"
"border-radius: 0;\n"
"background: none;")
        self.groupBox_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.horizontalLayout_4 = QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.radioButton_left = QRadioButton(self.groupBox_2)
        self.radioButton_left.setObjectName(u"radioButton_left")
        self.radioButton_left.setFont(font)
        self.radioButton_left.setChecked(False)

        self.horizontalLayout_4.addWidget(self.radioButton_left, 0, Qt.AlignmentFlag.AlignHCenter)

        self.radioButton_right = QRadioButton(self.groupBox_2)
        self.radioButton_right.setObjectName(u"radioButton_right")
        self.radioButton_right.setFont(font)
        self.radioButton_right.setChecked(True)

        self.horizontalLayout_4.addWidget(self.radioButton_right, 0, Qt.AlignmentFlag.AlignHCenter)


        self.verticalLayout_4.addWidget(self.groupBox_2)

        self.horizontalWidget_4 = QWidget(self.widget_2)
        self.horizontalWidget_4.setObjectName(u"horizontalWidget_4")
        self.horizontalWidget_4.setStyleSheet(u"border-radius: none;\n"
"border: none;\n"
"background: none;")
        self.horizontalLayout_9 = QHBoxLayout(self.horizontalWidget_4)
        self.horizontalLayout_9.setSpacing(10)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_9)

        self.label_8 = QLabel(self.horizontalWidget_4)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font)
        self.label_8.setStyleSheet(u"background: none;\n"
"border: none;\n"
"border-radius: none;")

        self.horizontalLayout_9.addWidget(self.label_8)

        self.comboBox_dopusk = QComboBox(self.horizontalWidget_4)
        self.comboBox_dopusk.setObjectName(u"comboBox_dopusk")
        sizePolicy2.setHeightForWidth(self.comboBox_dopusk.sizePolicy().hasHeightForWidth())
        self.comboBox_dopusk.setSizePolicy(sizePolicy2)
        self.comboBox_dopusk.setMaximumSize(QSize(40, 16777215))
        self.comboBox_dopusk.setFont(font)
        self.comboBox_dopusk.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.comboBox_dopusk.setStyleSheet(u"QComboBox {\n"
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

        self.horizontalLayout_9.addWidget(self.comboBox_dopusk)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_10)


        self.verticalLayout_4.addWidget(self.horizontalWidget_4)


        self.verticalLayout_11.addWidget(self.widget_2)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_11.addItem(self.verticalSpacer_2)

        self.btn_save_result_rezba = QPushButton(self.main)
        self.btn_save_result_rezba.setObjectName(u"btn_save_result_rezba")
        font4 = QFont()
        font4.setBold(True)
        self.btn_save_result_rezba.setFont(font4)
        self.btn_save_result_rezba.setStyleSheet(u"QPushButton {\n"
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
        self.btn_save_result_rezba.setIcon(icon1)
        self.btn_save_result_rezba.setIconSize(QSize(20, 20))

        self.verticalLayout_11.addWidget(self.btn_save_result_rezba, 0, Qt.AlignmentFlag.AlignHCenter)


        self.horizontalLayout_6.addWidget(self.main)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.horizontalLayout_6)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.table_widget_rezba = QTableWidget(PageTokarnayaRezba)
        if (self.table_widget_rezba.columnCount() < 2):
            self.table_widget_rezba.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.table_widget_rezba.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.table_widget_rezba.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        self.table_widget_rezba.setObjectName(u"table_widget_rezba")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.table_widget_rezba.sizePolicy().hasHeightForWidth())
        self.table_widget_rezba.setSizePolicy(sizePolicy4)
        font5 = QFont()
        font5.setPointSize(10)
        self.table_widget_rezba.setFont(font5)
        self.table_widget_rezba.setStyleSheet(u"/* \u0421\u0430\u043c \u0432\u0438\u0434\u0436\u0435\u0442 \u2014 \u043f\u0440\u043e\u0437\u0440\u0430\u0447\u043d\u044b\u0439 \u0444\u043e\u043d */\n"
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
        self.table_widget_rezba.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.table_widget_rezba.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.table_widget_rezba.setAutoScroll(False)
        self.table_widget_rezba.setRowCount(0)
        self.table_widget_rezba.setColumnCount(2)
        self.table_widget_rezba.verticalHeader().setVisible(False)
        self.table_widget_rezba.verticalHeader().setMinimumSectionSize(90)
        self.table_widget_rezba.verticalHeader().setDefaultSectionSize(100)

        self.horizontalLayout_5.addWidget(self.table_widget_rezba)


        self.verticalLayout.addLayout(self.horizontalLayout_5)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_3)

        self.text_error_start = QLabel(PageTokarnayaRezba)
        self.text_error_start.setObjectName(u"text_error_start")
        self.text_error_start.setFont(font5)
        self.text_error_start.setStyleSheet(u"background:none")
        self.text_error_start.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.text_error_start)


        self.retranslateUi(PageTokarnayaRezba)

        QMetaObject.connectSlotsByName(PageTokarnayaRezba)
    # setupUi

    def retranslateUi(self, PageTokarnayaRezba):
        PageTokarnayaRezba.setWindowTitle(QCoreApplication.translate("PageTokarnayaRezba", u"Form", None))
        self.btn_home.setText(QCoreApplication.translate("PageTokarnayaRezba", u" \u041d\u0410\u0417\u0410\u0414", None))
        self.label_7.setText(QCoreApplication.translate("PageTokarnayaRezba", u"\u041d\u0410\u0420\u0415\u0417\u0410\u041d\u0418\u0415 \u0420\u0415\u0417\u042c\u0411\u042b", None))
        self.label_12.setText(QCoreApplication.translate("PageTokarnayaRezba", u"\u0413\u0435\u043e\u043c\u0435\u0442\u0440\u0438\u0447\u0435\u0441\u043a\u0438\u0435 \u0440\u0430\u0437\u043c\u0435\u0440\u044b \u0440\u0435\u0437\u044c\u0431\u044b:", None))
        self.label_5.setText(QCoreApplication.translate("PageTokarnayaRezba", u"\u0414\u0438\u0430\u043c\u0435\u0442\u0440 \u0440\u0435\u0437\u044c\u0431\u044b: ", None))
        self.label_6.setText(QCoreApplication.translate("PageTokarnayaRezba", u"\u0428\u0430\u0433 \u0440\u0435\u0437\u044c\u0431\u044b: ", None))
        self.label_9.setText(QCoreApplication.translate("PageTokarnayaRezba", u"\u0414\u043b\u0438\u043d\u0430 \u0440\u0435\u0437\u044c\u0431\u044b:", None))
        self.double_spin_length.setPrefix("")
        self.double_spin_length.setSuffix(QCoreApplication.translate("PageTokarnayaRezba", u" \u043c\u043c.", None))
        self.label_13.setText(QCoreApplication.translate("PageTokarnayaRezba", u"\u041f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u044b \u0442\u0438\u043f\u0430 \u0440\u0435\u0437\u044c\u0431\u044b:", None))
        self.label_10.setText(QCoreApplication.translate("PageTokarnayaRezba", u"\u0420\u0430\u0441\u043f\u043e\u043b\u043e\u0436\u0435\u043d\u0438\u0435 \u0440\u0435\u0437\u044c\u0431\u044b:", None))
        self.groupBox.setTitle("")
        self.radioButton_in.setText(QCoreApplication.translate("PageTokarnayaRezba", u"\u0412\u043d\u0443\u0442\u0440\u0435\u043d\u043d\u044f\u044f", None))
        self.radioButton_out.setText(QCoreApplication.translate("PageTokarnayaRezba", u"\u0412\u043d\u0435\u0448\u043d\u044f\u044f", None))
        self.label_11.setText(QCoreApplication.translate("PageTokarnayaRezba", u"\u041d\u0430\u043f\u0440\u0430\u0432\u043b\u0435\u043d\u0438\u0435 \u0440\u0435\u0437\u044c\u0431\u044b:", None))
        self.groupBox_2.setTitle("")
        self.radioButton_left.setText(QCoreApplication.translate("PageTokarnayaRezba", u"\u041b\u0435\u0432\u043e\u0435", None))
        self.radioButton_right.setText(QCoreApplication.translate("PageTokarnayaRezba", u"\u041f\u0440\u0430\u0432\u043e\u0435", None))
        self.label_8.setText(QCoreApplication.translate("PageTokarnayaRezba", u"\u0414\u043e\u043f\u0443\u0441\u043a \u0440\u0435\u0437\u044c\u0431\u044b:", None))
        self.comboBox_dopusk.setPlaceholderText("")
        self.btn_save_result_rezba.setText(QCoreApplication.translate("PageTokarnayaRezba", u" \u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u044f", None))
        ___qtablewidgetitem = self.table_widget_rezba.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("PageTokarnayaRezba", u"\u0418\u043d\u0441\u0442\u0440\u0443\u043c\u0435\u043d\u0442", None))
        ___qtablewidgetitem1 = self.table_widget_rezba.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("PageTokarnayaRezba", u"\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435", None))
        self.text_error_start.setText("")
    # retranslateUi

