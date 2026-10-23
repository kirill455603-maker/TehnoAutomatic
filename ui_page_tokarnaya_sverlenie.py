# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_page_tokarnaya_sverlenie.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDoubleSpinBox,
    QHBoxLayout, QHeaderView, QLabel, QPushButton,
    QSizePolicy, QSpacerItem, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)
import res_rc

class Ui_PageTokarnayaSverlenie(object):
    def setupUi(self, PageTokarnayaSverlenie):
        if not PageTokarnayaSverlenie.objectName():
            PageTokarnayaSverlenie.setObjectName(u"PageTokarnayaSverlenie")
        PageTokarnayaSverlenie.resize(1026, 700)
        PageTokarnayaSverlenie.setMinimumSize(QSize(1000, 0))
        PageTokarnayaSverlenie.setStyleSheet(u"color: white;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0, stop:0 rgba(20, 40, 80, 255), stop:1 rgba(39, 73, 109, 255));\n"
"")
        self.verticalLayout = QVBoxLayout(PageTokarnayaSverlenie)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.btn_home_tokarnaya_sverlenie = QPushButton(PageTokarnayaSverlenie)
        self.btn_home_tokarnaya_sverlenie.setObjectName(u"btn_home_tokarnaya_sverlenie")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_home_tokarnaya_sverlenie.sizePolicy().hasHeightForWidth())
        self.btn_home_tokarnaya_sverlenie.setSizePolicy(sizePolicy)
        self.btn_home_tokarnaya_sverlenie.setMinimumSize(QSize(70, 0))
        self.btn_home_tokarnaya_sverlenie.setMaximumSize(QSize(150, 30))
        font = QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.btn_home_tokarnaya_sverlenie.setFont(font)
        self.btn_home_tokarnaya_sverlenie.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_home_tokarnaya_sverlenie.setStyleSheet(u"QPushButton {\n"
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
        self.btn_home_tokarnaya_sverlenie.setIcon(icon)
        self.btn_home_tokarnaya_sverlenie.setIconSize(QSize(20, 20))

        self.verticalLayout.addWidget(self.btn_home_tokarnaya_sverlenie, 0, Qt.AlignmentFlag.AlignLeft)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.label_7 = QLabel(PageTokarnayaSverlenie)
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
        self.horizontalLayout.setContentsMargins(-1, 0, -1, -1)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.main = QWidget(PageTokarnayaSverlenie)
        self.main.setObjectName(u"main")
        self.main.setMouseTracking(True)
        self.main.setTabletTracking(False)
        self.main.setAutoFillBackground(False)
        self.main.setStyleSheet(u"QWidget { \n"
"	border: none;\n"
"	background: none;\n"
"}")
        self.verticalLayout_11 = QVBoxLayout(self.main)
        self.verticalLayout_11.setSpacing(10)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(10, 20, 10, 20)
        self.label_3 = QLabel(self.main)
        self.label_3.setObjectName(u"label_3")
        font2 = QFont()
        font2.setFamilies([u"Segoe UI Light"])
        font2.setPointSize(10)
        font2.setBold(False)
        self.label_3.setFont(font2)
        self.label_3.setStyleSheet(u"QLabel {\n"
"	background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(12, 123, 147, 255), stop:1 rgba(0, 168, 204, 255));\n"
"	padding-left: 2px;	\n"
"	color: rgb(24, 45, 76)\n"
"}\n"
"")

        self.verticalLayout_11.addWidget(self.label_3)

        self.widget = QWidget(self.main)
        self.widget.setObjectName(u"widget")
        self.widget.setStyleSheet(u"#widget {\n"
"	background: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0, stop:0 rgba(39, 72, 109, 129), stop:1 rgba(21, 41, 81, 129))\n"
"}")
        self.verticalLayout_2 = QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(9, -1, -1, -1)
        self.horizontalWidget_2 = QWidget(self.widget)
        self.horizontalWidget_2.setObjectName(u"horizontalWidget_2")
        self.horizontalWidget_2.setStyleSheet(u"border-radius: none;\n"
"border: none;")
        self.horizontalLayout_2 = QHBoxLayout(self.horizontalWidget_2)
        self.horizontalLayout_2.setSpacing(0)
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
"")

        self.horizontalLayout_2.addWidget(self.label, 0, Qt.AlignmentFlag.AlignHCenter)

        self.comboBox_sverlenie = QComboBox(self.horizontalWidget_2)
        self.comboBox_sverlenie.setObjectName(u"comboBox_sverlenie")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(2)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.comboBox_sverlenie.sizePolicy().hasHeightForWidth())
        self.comboBox_sverlenie.setSizePolicy(sizePolicy2)
        self.comboBox_sverlenie.setFont(font3)
        self.comboBox_sverlenie.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.comboBox_sverlenie.setStyleSheet(u"QComboBox {\n"
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

        self.horizontalLayout_2.addWidget(self.comboBox_sverlenie)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_4)


        self.verticalLayout_2.addWidget(self.horizontalWidget_2)

        self.checkbox_length = QCheckBox(self.widget)
        self.checkbox_length.setObjectName(u"checkbox_length")
        font4 = QFont()
        font4.setBold(True)
        self.checkbox_length.setFont(font4)
        self.checkbox_length.setStyleSheet(u"QCheckBox::indicator {\n"
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

        self.verticalLayout_2.addWidget(self.checkbox_length, 0, Qt.AlignmentFlag.AlignHCenter)


        self.verticalLayout_11.addWidget(self.widget)

        self.widget_length = QWidget(self.main)
        self.widget_length.setObjectName(u"widget_length")
        self.verticalLayout_4 = QVBoxLayout(self.widget_length)
        self.verticalLayout_4.setSpacing(10)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.widget_length)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font2)
        self.label_4.setStyleSheet(u"QLabel {\n"
"	background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(12, 123, 147, 255), stop:1 rgba(0, 168, 204, 255));\n"
"	padding-left: 2px;	\n"
"	color: rgb(24, 45, 76)\n"
"}\n"
"")

        self.verticalLayout_4.addWidget(self.label_4)

        self.widget_2 = QWidget(self.widget_length)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setStyleSheet(u"QWidget {\n"
"	background: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0, stop:0 rgba(39, 72, 109, 129), stop:1 rgba(21, 41, 81, 129))\n"
"}")
        self.verticalLayout_3 = QVBoxLayout(self.widget_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(-1, -1, -1, 0)
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_5)

        self.label_2 = QLabel(self.widget_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font3)
        self.label_2.setStyleSheet(u"background: none;\n"
"")

        self.horizontalLayout_4.addWidget(self.label_2)

        self.double_spin_length = QDoubleSpinBox(self.widget_2)
        self.double_spin_length.setObjectName(u"double_spin_length")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.double_spin_length.sizePolicy().hasHeightForWidth())
        self.double_spin_length.setSizePolicy(sizePolicy3)
        self.double_spin_length.setMinimumSize(QSize(150, 30))
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
        self.double_spin_length.setMaximum(2000.000000000000000)

        self.horizontalLayout_4.addWidget(self.double_spin_length)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_6)


        self.verticalLayout_3.addLayout(self.horizontalLayout_4)


        self.verticalLayout_4.addWidget(self.widget_2)


        self.verticalLayout_11.addWidget(self.widget_length)

        self.btn_save_result_sverlenie = QPushButton(self.main)
        self.btn_save_result_sverlenie.setObjectName(u"btn_save_result_sverlenie")
        self.btn_save_result_sverlenie.setFont(font4)
        self.btn_save_result_sverlenie.setStyleSheet(u"QPushButton {\n"
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
        self.btn_save_result_sverlenie.setIcon(icon1)
        self.btn_save_result_sverlenie.setIconSize(QSize(20, 20))

        self.verticalLayout_11.addWidget(self.btn_save_result_sverlenie, 0, Qt.AlignmentFlag.AlignHCenter)


        self.horizontalLayout.addWidget(self.main)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.verticalLayout_10.addLayout(self.horizontalLayout)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.table_widget_sverlenie = QTableWidget(PageTokarnayaSverlenie)
        if (self.table_widget_sverlenie.columnCount() < 2):
            self.table_widget_sverlenie.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.table_widget_sverlenie.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.table_widget_sverlenie.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        self.table_widget_sverlenie.setObjectName(u"table_widget_sverlenie")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.table_widget_sverlenie.sizePolicy().hasHeightForWidth())
        self.table_widget_sverlenie.setSizePolicy(sizePolicy4)
        font5 = QFont()
        font5.setPointSize(10)
        self.table_widget_sverlenie.setFont(font5)
        self.table_widget_sverlenie.setStyleSheet(u"/* \u0421\u0430\u043c \u0432\u0438\u0434\u0436\u0435\u0442 \u2014 \u043f\u0440\u043e\u0437\u0440\u0430\u0447\u043d\u044b\u0439 \u0444\u043e\u043d */\n"
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
        self.table_widget_sverlenie.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.table_widget_sverlenie.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.table_widget_sverlenie.setAutoScroll(False)
        self.table_widget_sverlenie.setRowCount(0)
        self.table_widget_sverlenie.setColumnCount(2)
        self.table_widget_sverlenie.verticalHeader().setVisible(False)
        self.table_widget_sverlenie.verticalHeader().setMinimumSectionSize(90)
        self.table_widget_sverlenie.verticalHeader().setDefaultSectionSize(100)

        self.horizontalLayout_3.addWidget(self.table_widget_sverlenie)


        self.verticalLayout_10.addLayout(self.horizontalLayout_3)


        self.verticalLayout.addLayout(self.verticalLayout_10)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_3)

        self.text_error_start = QLabel(PageTokarnayaSverlenie)
        self.text_error_start.setObjectName(u"text_error_start")
        self.text_error_start.setFont(font5)
        self.text_error_start.setStyleSheet(u"background:none")
        self.text_error_start.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.text_error_start)


        self.retranslateUi(PageTokarnayaSverlenie)

        QMetaObject.connectSlotsByName(PageTokarnayaSverlenie)
    # setupUi

    def retranslateUi(self, PageTokarnayaSverlenie):
        PageTokarnayaSverlenie.setWindowTitle(QCoreApplication.translate("PageTokarnayaSverlenie", u"Form", None))
        self.btn_home_tokarnaya_sverlenie.setText(QCoreApplication.translate("PageTokarnayaSverlenie", u" \u041d\u0410\u0417\u0410\u0414", None))
        self.label_7.setText(QCoreApplication.translate("PageTokarnayaSverlenie", u"\u0421\u0412\u0415\u0420\u041b\u0415\u041d\u0418\u0415 \u0426\u0415\u041d\u0422\u0420\u0410\u041b\u042c\u041d\u041e\u0413\u041e \u041e\u0422\u0412\u0415\u0420\u0421\u0422\u0418\u042f", None))
        self.label_3.setText(QCoreApplication.translate("PageTokarnayaSverlenie", u"\u041f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u044b \u0434\u0438\u0430\u043c\u0435\u0442\u0440\u0430:", None))
        self.label.setText(QCoreApplication.translate("PageTokarnayaSverlenie", u"\u0421\u0432\u0435\u0440\u043b\u043e \u00d8: ", None))
        self.comboBox_sverlenie.setPlaceholderText("")
        self.checkbox_length.setText(QCoreApplication.translate("PageTokarnayaSverlenie", u"\u0423\u043a\u0430\u0437\u0430\u0442\u044c \u0434\u043b\u0438\u043d\u0443 \u0441\u0432\u0435\u0440\u043b\u0435\u043d\u0438\u044f?", None))
        self.label_4.setText(QCoreApplication.translate("PageTokarnayaSverlenie", u"\u041f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u044b \u0434\u043b\u0438\u043d\u044b:", None))
        self.label_2.setText(QCoreApplication.translate("PageTokarnayaSverlenie", u"\u0414\u043b\u0438\u043d\u0430", None))
        self.double_spin_length.setPrefix(QCoreApplication.translate("PageTokarnayaSverlenie", u"L= ", None))
        self.double_spin_length.setSuffix("")
        self.btn_save_result_sverlenie.setText(QCoreApplication.translate("PageTokarnayaSverlenie", u" \u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u044f", None))
        ___qtablewidgetitem = self.table_widget_sverlenie.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("PageTokarnayaSverlenie", u"\u0418\u043d\u0441\u0442\u0440\u0443\u043c\u0435\u043d\u0442", None))
        ___qtablewidgetitem1 = self.table_widget_sverlenie.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("PageTokarnayaSverlenie", u"\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435", None))
        self.text_error_start.setText("")
    # retranslateUi

