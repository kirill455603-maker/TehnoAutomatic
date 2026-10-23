# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_page_tokarnaya_start.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QDoubleSpinBox, QGroupBox,
    QHBoxLayout, QHeaderView, QLabel, QLayout,
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)
import res_rc

class Ui_PageTokarnayaStart(object):
    def setupUi(self, PageTokarnayaStart):
        if not PageTokarnayaStart.objectName():
            PageTokarnayaStart.setObjectName(u"PageTokarnayaStart")
        PageTokarnayaStart.resize(798, 793)
        PageTokarnayaStart.setStyleSheet(u"color: white;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0, stop:0 rgba(20, 40, 80, 255), stop:1 rgba(39, 73, 109, 255));\n"
"")
        self.verticalLayout = QVBoxLayout(PageTokarnayaStart)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, 0, -1, -1)
        self.btn_home_tokarnaya = QPushButton(PageTokarnayaStart)
        self.btn_home_tokarnaya.setObjectName(u"btn_home_tokarnaya")
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
        self.btn_home_tokarnaya.setIconSize(QSize(20, 20))

        self.horizontalLayout.addWidget(self.btn_home_tokarnaya, 0, Qt.AlignmentFlag.AlignLeft)

        self.pushButton = QPushButton(PageTokarnayaStart)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setStyleSheet(u"background: rgba(0, 0, 0, 0);")
        icon1 = QIcon()
        icon1.addFile(u":/icons/logo_cut.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton.setIcon(icon1)
        self.pushButton.setIconSize(QSize(50, 50))

        self.horizontalLayout.addWidget(self.pushButton, 0, Qt.AlignmentFlag.AlignRight)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.main = QWidget(PageTokarnayaStart)
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
        self.verticalLayout_11.setContentsMargins(100, 10, 100, 10)
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
        self.verticalLayout_6.setContentsMargins(0, 5, 0, 5)
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(-1, 0, -1, -1)
        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_7)

        self.label_9 = QLabel(self.widget_2)
        self.label_9.setObjectName(u"label_9")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy1)
        font3 = QFont()
        font3.setPointSize(10)
        self.label_9.setFont(font3)
        self.label_9.setStyleSheet(u"background:none;\n"
"border: none")
        self.label_9.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_7.addWidget(self.label_9)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_8)


        self.verticalLayout_3.addLayout(self.horizontalLayout_7)

        self.label_14 = QLabel(self.widget_2)
        self.label_14.setObjectName(u"label_14")
        sizePolicy1.setHeightForWidth(self.label_14.sizePolicy().hasHeightForWidth())
        self.label_14.setSizePolicy(sizePolicy1)
        self.label_14.setFont(font3)
        self.label_14.setStyleSheet(u"background:none;\n"
"border: none;\n"
"color: rgba(255, 255, 255, 70)\n"
"")
        self.label_14.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_14)


        self.verticalLayout_6.addLayout(self.verticalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(-1, 0, -1, -1)
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_5)

        self.label_8 = QLabel(self.widget_2)
        self.label_8.setObjectName(u"label_8")
        sizePolicy1.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy1)
        self.label_8.setFont(font3)
        self.label_8.setStyleSheet(u"background:none;\n"
"border: none")
        self.label_8.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_4.addWidget(self.label_8)

        self.double_spin_start_diameter = QDoubleSpinBox(self.widget_2)
        self.double_spin_start_diameter.setObjectName(u"double_spin_start_diameter")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.double_spin_start_diameter.sizePolicy().hasHeightForWidth())
        self.double_spin_start_diameter.setSizePolicy(sizePolicy2)
        self.double_spin_start_diameter.setMinimumSize(QSize(0, 30))
        self.double_spin_start_diameter.setStyleSheet(u"QDoubleSpinBox {\n"
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
        self.double_spin_start_diameter.setMaximum(10000.000000000000000)

        self.horizontalLayout_4.addWidget(self.double_spin_start_diameter, 0, Qt.AlignmentFlag.AlignHCenter)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_6)


        self.verticalLayout_6.addLayout(self.horizontalLayout_4)

        self.checkBox = QCheckBox(self.widget_2)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setFont(font3)
        self.checkBox.setStyleSheet(u"QCheckBox::indicator {      \n"
" width: 10px;          \n"
"  height: 10px;    \n"
"  border: 2px solid white;         \n"
"  border-radius: 2px; /* \u0421\u043a\u0440\u0443\u0433\u043b\u0435\u043d\u043d\u044b\u0435 \u0443\u0433\u043b\u044b */          \n"
"  background-color: #FFFFFF;      \n"
"}\n"
"QCheckBox {\n"
"	spacing: 15px; /* \u0420\u0430\u0441\u0441\u0442\u043e\u044f\u043d\u0438\u0435 \u043c\u0435\u0436\u0434\u0443 \u043a\u0432\u0430\u0434\u0440\u0430\u0442\u0438\u043a\u043e\u043c \u0438 \u0442\u0435\u043a\u0441\u0442\u043e\u043c */          \n"
"	border: none;	\n"
"	color: rgb(255, 255, 255) ;	\n"
"	background: none;\n"
"	font-size: 10pt;\n"
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

        self.verticalLayout_6.addWidget(self.checkBox, 0, Qt.AlignmentFlag.AlignHCenter)


        self.verticalLayout_11.addWidget(self.widget_2)

        self.widget = QWidget(self.group_value_start_2)
        self.widget.setObjectName(u"widget")
        self.widget.setStyleSheet(u"border: none;\n"
"background: none")
        self.verticalLayout_2 = QVBoxLayout(self.widget)
        self.verticalLayout_2.setSpacing(10)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font2)
        self.label_3.setStyleSheet(u"QLabel {\n"
"	background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(12, 123, 147, 255), stop:1 rgba(0, 168, 204, 255));\n"
"	padding-left: 2px;	\n"
"	color: rgb(24, 45, 76)\n"
"}\n"
"")

        self.verticalLayout_2.addWidget(self.label_3)

        self.widget_3 = QWidget(self.widget)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setStyleSheet(u"#widget_3 {\n"
"	background: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0, stop:0 rgba(39, 72, 109, 129), stop:1 rgba(21, 41, 81, 129))\n"
"}")
        self.verticalLayout_7 = QVBoxLayout(self.widget_3)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 5, 0, 5)
        self.groupBox = QGroupBox(self.widget_3)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setStyleSheet(u"QGroupBox {\n"
"	border: none;\n"
"\u0419\n"
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
"	background: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(12, 123, 147, 177), stop:1 rgba(39, 7"
                        "3, 109, 255));\n"
"	color: rgb(0, 168, 204);\n"
"}")
        self.horizontalLayout_3 = QHBoxLayout(self.groupBox)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, 1, -1, -1)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.btn_diameter = QPushButton(self.groupBox)
        self.btn_diameter.setObjectName(u"btn_diameter")
        font4 = QFont()
        self.btn_diameter.setFont(font4)
        self.btn_diameter.setStyleSheet(u"")
        self.btn_diameter.setCheckable(True)
        self.btn_diameter.setChecked(True)
        self.btn_diameter.setAutoExclusive(True)

        self.horizontalLayout_3.addWidget(self.btn_diameter, 0, Qt.AlignmentFlag.AlignHCenter)

        self.btn_baza = QPushButton(self.groupBox)
        self.btn_baza.setObjectName(u"btn_baza")
        self.btn_baza.setFont(font4)
        self.btn_baza.setStyleSheet(u"")
        self.btn_baza.setCheckable(True)
        self.btn_baza.setAutoExclusive(True)

        self.horizontalLayout_3.addWidget(self.btn_baza, 0, Qt.AlignmentFlag.AlignHCenter)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)


        self.verticalLayout_7.addWidget(self.groupBox)

        self.layout_baza = QWidget(self.widget_3)
        self.layout_baza.setObjectName(u"layout_baza")
        self.horizontalLayout_9 = QHBoxLayout(self.layout_baza)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_13)

        self.label_13 = QLabel(self.layout_baza)
        self.label_13.setObjectName(u"label_13")
        sizePolicy2.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy2)
        self.label_13.setMinimumSize(QSize(0, 20))
        font5 = QFont()
        font5.setPointSize(10)
        font5.setUnderline(False)
        font5.setStrikeOut(False)
        self.label_13.setFont(font5)
        self.label_13.setStyleSheet(u"background:none;\n"
"border:none;\n"
"")
        self.label_13.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_13.setMargin(0)

        self.horizontalLayout_9.addWidget(self.label_13)

        self.line_edit_baza = QLineEdit(self.layout_baza)
        self.line_edit_baza.setObjectName(u"line_edit_baza")
        self.line_edit_baza.setEnabled(True)
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.line_edit_baza.sizePolicy().hasHeightForWidth())
        self.line_edit_baza.setSizePolicy(sizePolicy3)
        self.line_edit_baza.setMaximumSize(QSize(16777215, 16777215))
        font6 = QFont()
        font6.setPointSize(10)
        font6.setBold(False)
        self.line_edit_baza.setFont(font6)
        self.line_edit_baza.setStyleSheet(u"QLineEdit {\n"
"	padding: 2;	\n"
"	border: none;\n"
"	border-bottom: 1px solid white;\n"
"	border-radius: 1px;\n"
"	background: rgba(255, 255, 255, 0);\n"
"	transition: color 0.3s ease;\n"
"	transition: border-bottom 0.4s ease;\n"
"	color: rgb(204, 204, 204);\n"
"	font-size: 10pt\n"
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

        self.horizontalLayout_9.addWidget(self.line_edit_baza)

        self.horizontalSpacer_14 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_14)


        self.verticalLayout_7.addWidget(self.layout_baza)

        self.layout_diameter = QWidget(self.widget_3)
        self.layout_diameter.setObjectName(u"layout_diameter")
        self.horizontalLayout_5 = QHBoxLayout(self.layout_diameter)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_9)

        self.label_11 = QLabel(self.layout_diameter)
        self.label_11.setObjectName(u"label_11")
        sizePolicy2.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy2)
        self.label_11.setMinimumSize(QSize(0, 20))
        self.label_11.setFont(font5)
        self.label_11.setStyleSheet(u"background:none;\n"
"border:none;\n"
"")
        self.label_11.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_11.setMargin(0)

        self.horizontalLayout_5.addWidget(self.label_11)

        self.double_spin_start_diameter_2 = QDoubleSpinBox(self.layout_diameter)
        self.double_spin_start_diameter_2.setObjectName(u"double_spin_start_diameter_2")
        sizePolicy2.setHeightForWidth(self.double_spin_start_diameter_2.sizePolicy().hasHeightForWidth())
        self.double_spin_start_diameter_2.setSizePolicy(sizePolicy2)
        self.double_spin_start_diameter_2.setMinimumSize(QSize(0, 30))
        self.double_spin_start_diameter_2.setStyleSheet(u"QDoubleSpinBox {\n"
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
        self.double_spin_start_diameter_2.setMaximum(10000.000000000000000)

        self.horizontalLayout_5.addWidget(self.double_spin_start_diameter_2)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_10)


        self.verticalLayout_7.addWidget(self.layout_diameter)

        self.horizontalWidget_3 = QWidget(self.widget_3)
        self.horizontalWidget_3.setObjectName(u"horizontalWidget_3")
        self.horizontalWidget_3.setFont(font3)
        self.horizontalLayout_8 = QHBoxLayout(self.horizontalWidget_3)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(5, 0, 5, 0)
        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_11)

        self.label_12 = QLabel(self.horizontalWidget_3)
        self.label_12.setObjectName(u"label_12")
        sizePolicy2.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy2)
        self.label_12.setMinimumSize(QSize(0, 20))
        font7 = QFont()
        font7.setPointSize(9)
        font7.setUnderline(False)
        font7.setStrikeOut(False)
        self.label_12.setFont(font7)
        self.label_12.setStyleSheet(u"background:none;\n"
"border:none;\n"
"")
        self.label_12.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_12.setMargin(0)

        self.horizontalLayout_8.addWidget(self.label_12)

        self.double_spin_start_diameter_3 = QDoubleSpinBox(self.horizontalWidget_3)
        self.double_spin_start_diameter_3.setObjectName(u"double_spin_start_diameter_3")
        sizePolicy2.setHeightForWidth(self.double_spin_start_diameter_3.sizePolicy().hasHeightForWidth())
        self.double_spin_start_diameter_3.setSizePolicy(sizePolicy2)
        self.double_spin_start_diameter_3.setMinimumSize(QSize(0, 30))
        self.double_spin_start_diameter_3.setStyleSheet(u"QDoubleSpinBox {\n"
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
        self.double_spin_start_diameter_3.setDecimals(3)
        self.double_spin_start_diameter_3.setMaximum(10000.000000000000000)
        self.double_spin_start_diameter_3.setSingleStep(0.010000000000000)

        self.horizontalLayout_8.addWidget(self.double_spin_start_diameter_3)

        self.label_15 = QLabel(self.horizontalWidget_3)
        self.label_15.setObjectName(u"label_15")
        sizePolicy2.setHeightForWidth(self.label_15.sizePolicy().hasHeightForWidth())
        self.label_15.setSizePolicy(sizePolicy2)
        self.label_15.setMinimumSize(QSize(0, 20))
        self.label_15.setFont(font7)
        self.label_15.setStyleSheet(u"background:none;\n"
"border:none;\n"
"")
        self.label_15.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_15.setMargin(0)

        self.horizontalLayout_8.addWidget(self.label_15)

        self.double_spin_start_diameter_4 = QDoubleSpinBox(self.horizontalWidget_3)
        self.double_spin_start_diameter_4.setObjectName(u"double_spin_start_diameter_4")
        sizePolicy2.setHeightForWidth(self.double_spin_start_diameter_4.sizePolicy().hasHeightForWidth())
        self.double_spin_start_diameter_4.setSizePolicy(sizePolicy2)
        self.double_spin_start_diameter_4.setMinimumSize(QSize(0, 30))
        self.double_spin_start_diameter_4.setStyleSheet(u"QDoubleSpinBox {\n"
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
        self.double_spin_start_diameter_4.setDecimals(3)
        self.double_spin_start_diameter_4.setMaximum(10000.000000000000000)
        self.double_spin_start_diameter_4.setSingleStep(0.010000000000000)

        self.horizontalLayout_8.addWidget(self.double_spin_start_diameter_4)

        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_12)


        self.verticalLayout_7.addWidget(self.horizontalWidget_3)

        self.label_16 = QLabel(self.widget_3)
        self.label_16.setObjectName(u"label_16")
        sizePolicy1.setHeightForWidth(self.label_16.sizePolicy().hasHeightForWidth())
        self.label_16.setSizePolicy(sizePolicy1)
        self.label_16.setFont(font3)
        self.label_16.setStyleSheet(u"background:none;\n"
"border: none;\n"
"color: rgba(255, 255, 255, 70)\n"
"")
        self.label_16.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_7.addWidget(self.label_16)


        self.verticalLayout_2.addWidget(self.widget_3)


        self.verticalLayout_11.addWidget(self.widget)

        self.btn_save_result_start = QPushButton(self.group_value_start_2)
        self.btn_save_result_start.setObjectName(u"btn_save_result_start")
        font8 = QFont()
        font8.setBold(True)
        self.btn_save_result_start.setFont(font8)
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
        self.table_widget_start.setFont(font3)
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
        self.text_error_start.setFont(font3)
        self.text_error_start.setStyleSheet(u"background:none")
        self.text_error_start.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_10.addWidget(self.text_error_start)


        self.verticalLayout.addWidget(self.main)


        self.retranslateUi(PageTokarnayaStart)

        QMetaObject.connectSlotsByName(PageTokarnayaStart)
    # setupUi

    def retranslateUi(self, PageTokarnayaStart):
        PageTokarnayaStart.setWindowTitle(QCoreApplication.translate("PageTokarnayaStart", u"\u0423\u0441\u0442\u0430\u043d\u043e\u0432\u043a\u0430", None))
        self.btn_home_tokarnaya.setText(QCoreApplication.translate("PageTokarnayaStart", u" \u041d\u0410\u0417\u0410\u0414", None))
        self.pushButton.setText("")
        self.label_7.setText(QCoreApplication.translate("PageTokarnayaStart", u"\u0423\u0441\u0442\u0430\u043d\u043e\u0432\u043a\u0430 \u0434\u0435\u0442\u0430\u043b\u0438", None))
        self.label_2.setText(QCoreApplication.translate("PageTokarnayaStart", u"\u041e\u0441\u043d\u043e\u0432\u043d\u044b\u0435 \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u044b:", None))
        self.label_9.setText(QCoreApplication.translate("PageTokarnayaStart", u"\u0414\u0438\u0430\u043c\u0435\u0442\u0440 \u0437\u0430\u0433\u043e\u0442\u043e\u0432\u043a\u0438:", None))
        self.label_14.setText(QCoreApplication.translate("PageTokarnayaStart", u"\u0414\u043b\u044f \u043f\u043e\u0434\u0431\u043e\u0440\u0430 \u043f\u0430\u0442\u0440\u043e\u043d\u0430", None))
        self.label_8.setText(QCoreApplication.translate("PageTokarnayaStart", u"\u0414\u0438\u0430\u043c\u0435\u0442\u0440 \u0443\u0441\u0442\u0430\u043d\u043e\u0432\u043a\u0438:", None))
        self.double_spin_start_diameter.setPrefix(QCoreApplication.translate("PageTokarnayaStart", u"\u00d8 ", None))
        self.double_spin_start_diameter.setSuffix(QCoreApplication.translate("PageTokarnayaStart", u" \u043c\u043c.", None))
        self.checkBox.setText(QCoreApplication.translate("PageTokarnayaStart", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u044b \u043e\u0442\u043d\u043e\u0441\u0438\u0442\u0435\u043b\u044c\u043d\u043e\u0433\u043e \u0440\u0430\u0441\u043f\u043e\u043b\u043e\u0436\u0435\u043d\u0438\u044f ", None))
        self.label_3.setText(QCoreApplication.translate("PageTokarnayaStart", u"\u0414\u043e\u043f\u043e\u043b\u043d\u0438\u0442\u0435\u043b\u044c\u043d\u044b\u0435 \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u044b:", None))
        self.btn_diameter.setText(QCoreApplication.translate("PageTokarnayaStart", u"\u041f\u043e \u0434\u0438\u0430\u043c\u0435\u0442\u0440\u0443", None))
        self.btn_baza.setText(QCoreApplication.translate("PageTokarnayaStart", u"\u041f\u043e \u0431\u0430\u0437\u0435", None))
        self.label_13.setText(QCoreApplication.translate("PageTokarnayaStart", u"\u0411\u0430\u0437\u044b \u043e\u0442\u043d\u043e\u0441\u0438\u0442\u0435\u043b\u044c\u043d\u043e\u0433\u043e \u043f\u043e\u0437\u0438\u0446\u0438\u043e\u043d\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u044f:", None))
#if QT_CONFIG(tooltip)
        self.line_edit_baza.setToolTip(QCoreApplication.translate("PageTokarnayaStart", u"<html><head/><body><p><span style=\" color:#000000;\">\u041c\u043e\u0436\u043d\u043e \u0443\u043a\u0430\u0437\u0430\u0442\u044c \u043d\u0435\u0441\u043a\u043e\u043b\u044c\u043a\u043e</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.line_edit_baza.setText("")
        self.line_edit_baza.setPlaceholderText(QCoreApplication.translate("PageTokarnayaStart", u"\u0411\u0430\u0437\u044b...", None))
        self.label_11.setText(QCoreApplication.translate("PageTokarnayaStart", u"\u0414\u0438\u0430\u043c\u0435\u0442\u0440 \u043e\u0442\u043d\u043e\u0441\u0438\u0442\u0435\u043b\u044c\u043d\u043e\u0433\u043e \u043f\u043e\u0437\u0438\u0446\u0438\u043e\u043d\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u044f:", None))
        self.double_spin_start_diameter_2.setPrefix(QCoreApplication.translate("PageTokarnayaStart", u"\u00d8 ", None))
        self.double_spin_start_diameter_2.setSuffix(QCoreApplication.translate("PageTokarnayaStart", u" \u043c\u043c.", None))
        self.label_12.setText(QCoreApplication.translate("PageTokarnayaStart", u"\u0423\u043a\u0430\u0436\u0438\u0442\u0435 \u0431\u0438\u0435\u043d\u0438\u0435 \u0440\u0430\u0434\u0438\u0430\u043b\u044c\u043d\u043e\u0435:", None))
        self.double_spin_start_diameter_3.setPrefix("")
        self.double_spin_start_diameter_3.setSuffix("")
        self.label_15.setText(QCoreApplication.translate("PageTokarnayaStart", u"\u0423\u043a\u0430\u0436\u0438\u0442\u0435 \u0431\u0438\u0435\u043d\u0438\u0435 \u0442\u043e\u0440\u0446\u0435\u0432\u043e\u0435:", None))
        self.double_spin_start_diameter_4.setPrefix("")
        self.double_spin_start_diameter_4.setSuffix("")
        self.label_16.setText(QCoreApplication.translate("PageTokarnayaStart", u"\u041c\u043e\u0436\u043d\u043e \u0443\u043a\u0430\u0437\u0430\u0442\u044c \u043a\u0430\u043a \u043e\u0434\u043d\u043e \u0438\u0437\u0432\u0435\u0441\u0442\u043d\u043e\u0435 \u0431\u0438\u0435\u043d\u0438\u0435, \u0442\u0430\u043a \u0438 \u0441\u0440\u0430\u0437\u0443 \u0434\u0432\u0430", None))
        self.btn_save_result_start.setText(QCoreApplication.translate("PageTokarnayaStart", u" \u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u044f", None))
        ___qtablewidgetitem = self.table_widget_start.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("PageTokarnayaStart", u"\u0418\u043d\u0441\u0442\u0440\u0443\u043c\u0435\u043d\u0442", None))
        ___qtablewidgetitem1 = self.table_widget_start.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("PageTokarnayaStart", u"\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435", None))
        self.text_error_start.setText("")
    # retranslateUi

