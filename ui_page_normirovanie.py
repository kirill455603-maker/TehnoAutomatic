# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_page_normirovanie.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QHBoxLayout,
    QLabel, QPlainTextEdit, QPushButton, QScrollArea,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)
import res_rc

class Ui_PageNormirovanie(object):
    def setupUi(self, PageNormirovanie):
        if not PageNormirovanie.objectName():
            PageNormirovanie.setObjectName(u"PageNormirovanie")
        PageNormirovanie.resize(875, 952)
        PageNormirovanie.setStyleSheet(u"color: white;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0, stop:0 rgba(20, 40, 80, 255), stop:1 rgba(39, 73, 109, 255));\n"
"")
        self.verticalLayout = QVBoxLayout(PageNormirovanie)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(-1, -1, -1, 0)
        self.btn_home = QPushButton(PageNormirovanie)
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

        self.horizontalLayout_5.addWidget(self.btn_home, 0, Qt.AlignmentFlag.AlignLeft)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.label = QLabel(PageNormirovanie)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"background: none;")

        self.verticalLayout.addWidget(self.label, 0, Qt.AlignmentFlag.AlignHCenter)

        self.btn_open_file = QPushButton(PageNormirovanie)
        self.btn_open_file.setObjectName(u"btn_open_file")
        font1 = QFont()
        self.btn_open_file.setFont(font1)
        self.btn_open_file.setStyleSheet(u"QPushButton {\n"
"	background:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(12, 123, 147, 255), stop:1 rgba(0, 168, 204, 255));\n"
"	border: none;\n"
"	font-size: 11px;\n"
"	padding: 5 10 5 10;\n"
"	border-radius: 5px;\n"
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
"	background: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(12, 123, 147, 177), stop:1 rgba(39, 73, 109, 255));\n"
"	color: rgb(0, 168, 204);\n"
""
                        "}")
        icon1 = QIcon()
        icon1.addFile(u":/icons/read_excel.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_open_file.setIcon(icon1)

        self.verticalLayout.addWidget(self.btn_open_file)

        self.error_path = QLabel(PageNormirovanie)
        self.error_path.setObjectName(u"error_path")
        self.error_path.setStyleSheet(u"background: none;")

        self.verticalLayout.addWidget(self.error_path, 0, Qt.AlignmentFlag.AlignHCenter)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, -1, 0, 20)
        self.verticalWidget_3 = QWidget(PageNormirovanie)
        self.verticalWidget_3.setObjectName(u"verticalWidget_3")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.verticalWidget_3.sizePolicy().hasHeightForWidth())
        self.verticalWidget_3.setSizePolicy(sizePolicy)
        self.verticalWidget_3.setSizeIncrement(QSize(0, 0))
        self.verticalWidget_3.setStyleSheet(u"background: none;")
        self.verticalLayout_2 = QVBoxLayout(self.verticalWidget_3)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, -1, -1, 1)
        self.widget_with_buttons = QWidget(self.verticalWidget_3)
        self.widget_with_buttons.setObjectName(u"widget_with_buttons")
        self.verticalLayout_4 = QVBoxLayout(self.widget_with_buttons)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.widget_with_buttons)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_4.addWidget(self.label_4, 0, Qt.AlignmentFlag.AlignHCenter)

        self.layout_with_buttons = QHBoxLayout()
        self.layout_with_buttons.setObjectName(u"layout_with_buttons")

        self.verticalLayout_4.addLayout(self.layout_with_buttons)


        self.verticalLayout_2.addWidget(self.widget_with_buttons)

        self.widget_with_details = QWidget(self.verticalWidget_3)
        self.widget_with_details.setObjectName(u"widget_with_details")
        self.widget_with_details.setStyleSheet(u"background: none;")
        self.layout_with_details = QVBoxLayout(self.widget_with_details)
        self.layout_with_details.setSpacing(3)
        self.layout_with_details.setObjectName(u"layout_with_details")
        self.layout_with_details.setContentsMargins(-1, -1, -1, 0)
        self.label_2 = QLabel(self.widget_with_details)
        self.label_2.setObjectName(u"label_2")
        font2 = QFont()
        font2.setPointSize(10)
        self.label_2.setFont(font2)

        self.layout_with_details.addWidget(self.label_2, 0, Qt.AlignmentFlag.AlignHCenter)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, -1, -1, 0)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.comboBox_details = QComboBox(self.widget_with_details)
        self.comboBox_details.setObjectName(u"comboBox_details")
        self.comboBox_details.setMinimumSize(QSize(370, 0))
        self.comboBox_details.setStyleSheet(u"QComboBox {\n"
"	padding: 3, 3, 3, 3;\n"
"	width: 60px;\n"
"	border: none;\n"
"	border-bottom: 1px solid white;\n"
"	background: rgba(255, 255, 255, 0);\n"
"	transition: color 0.3s ease;\n"
"	transition: border-bottom 0.4s ease;\n"
"	color: rgb(204, 204, 204);\n"
"	font-size: 10pt;\n"
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
        self.comboBox_details.setEditable(True)
        self.comboBox_details.setInsertPolicy(QComboBox.InsertPolicy.NoInsert)

        self.horizontalLayout_3.addWidget(self.comboBox_details, 0, Qt.AlignmentFlag.AlignHCenter)

        self.btn_clear_details = QPushButton(self.widget_with_details)
        self.btn_clear_details.setObjectName(u"btn_clear_details")
        self.btn_clear_details.setStyleSheet(u"QPushButton {\n"
"	background:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(12, 123, 147, 255), stop:1 rgba(0, 168, 204, 255));\n"
"	border: none;\n"
"	font-size: 11px;\n"
"	padding: 5 10 5 10;\n"
"	border: 1px solid qradialgradient(spread:pad, cx:0.506, cy:1, radius:1.147, fx:0.494318, fy:1, stop:0 rgba(12, 123, 147, 255), stop:1 rgba(255, 255, 255, 0));\n"
"	border-radius: 5px;\n"
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
"	background: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(12, 123, 147, 177), stop:1 rgba(39, 73, 109, 255));\n"
"	color: rgb(0, 168, 204);\n"
""
                        "}")
        icon2 = QIcon()
        icon2.addFile(u":/icons/clear_string.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_clear_details.setIcon(icon2)

        self.horizontalLayout_3.addWidget(self.btn_clear_details)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)


        self.layout_with_details.addLayout(self.horizontalLayout_3)

        self.label_3 = QLabel(self.widget_with_details)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font2)

        self.layout_with_details.addWidget(self.label_3, 0, Qt.AlignmentFlag.AlignHCenter)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(-1, -1, -1, 5)
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_3)

        self.comboBox_operations = QComboBox(self.widget_with_details)
        self.comboBox_operations.setObjectName(u"comboBox_operations")
        self.comboBox_operations.setMinimumSize(QSize(370, 0))
        self.comboBox_operations.setSizeIncrement(QSize(0, 0))
        self.comboBox_operations.setStyleSheet(u"QComboBox {\n"
"	padding: 3, 3, 3, 3;\n"
"	width: 60px;\n"
"	border: none;\n"
"	border-bottom: 1px solid white;\n"
"	background: rgba(255, 255, 255, 0);\n"
"	transition: color 0.3s ease;\n"
"	transition: border-bottom 0.4s ease;\n"
"	color: rgb(204, 204, 204);\n"
"	font-size: 10pt;\n"
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
        self.comboBox_operations.setEditable(True)

        self.horizontalLayout_4.addWidget(self.comboBox_operations, 0, Qt.AlignmentFlag.AlignHCenter)

        self.btn_clear_operations = QPushButton(self.widget_with_details)
        self.btn_clear_operations.setObjectName(u"btn_clear_operations")
        self.btn_clear_operations.setStyleSheet(u"QPushButton {\n"
"	background:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(12, 123, 147, 255), stop:1 rgba(0, 168, 204, 255));\n"
"	border: none;\n"
"	font-size: 11px;\n"
"	padding: 5 10 5 10;\n"
"	border: 1px solid qradialgradient(spread:pad, cx:0.506, cy:1, radius:1.147, fx:0.494318, fy:1, stop:0 rgba(12, 123, 147, 255), stop:1 rgba(255, 255, 255, 0));\n"
"	border-radius: 5px;\n"
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
"	background: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(12, 123, 147, 177), stop:1 rgba(39, 73, 109, 255));\n"
"	color: rgb(0, 168, 204);\n"
""
                        "}")
        self.btn_clear_operations.setIcon(icon2)

        self.horizontalLayout_4.addWidget(self.btn_clear_operations)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_4)


        self.layout_with_details.addLayout(self.horizontalLayout_4)

        self.scrollArea = QScrollArea(self.widget_with_details)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setMinimumSize(QSize(0, 500))
        self.scrollArea.setStyleSheet(u"/* \u0421\u0430\u043c \u043a\u043e\u043d\u0442\u0435\u0439\u043d\u0435\u0440 \u2014 \u043f\u0440\u043e\u0437\u0440\u0430\u0447\u043d\u044b\u0439 */\n"
"QScrollArea {\n"
"    background: transparent;\n"
"    border: none;\n"
"}\n"
"\n"
"/* Viewport (\u043e\u0431\u043b\u0430\u0441\u0442\u044c \u0441\u043e\u0434\u0435\u0440\u0436\u0438\u043c\u043e\u0433\u043e) \u2014 \u0442\u043e\u0436\u0435 \u043f\u0440\u043e\u0437\u0440\u0430\u0447\u043d\u044b\u0439 */\n"
"QAbstractScrollArea::viewport {\n"
"    background: transparent;\n"
"}\n"
"\n"
"/* \u0421\u043a\u0440\u043e\u043b\u043b\u0431\u0430\u0440\u044b (\u043e\u043f\u0446\u0438\u043e\u043d\u0430\u043b\u044c\u043d\u043e, \u0435\u0441\u043b\u0438 \u043d\u0443\u0436\u043d\u044b) */\n"
"QScrollBar:vertical {\n"
"    background: transparent;\n"
"    width: 10px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"    background: rgba(0, 0, 0, 0.3);\n"
"    border-radius: 5px;\n"
"    min-height: 30px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical:hover {\n"
"    background: rg"
                        "ba(0, 0, 0, 0.5);\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {\n"
"    height: 0;\n"
"}\n"
"\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"    background: none;\n"
"}")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 524, 500))
        self.scrollAreaWidgetContents.setStyleSheet(u"background: rgba(255, 29, 29, 0);")
        self.layout_234 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.layout_234.setObjectName(u"layout_234")
        self.layout_widgets = QVBoxLayout()
        self.layout_widgets.setObjectName(u"layout_widgets")

        self.layout_234.addLayout(self.layout_widgets)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.layout_with_details.addWidget(self.scrollArea)

        self.pushButton_calc_result = QPushButton(self.widget_with_details)
        self.pushButton_calc_result.setObjectName(u"pushButton_calc_result")
        font3 = QFont()
        font3.setBold(True)
        self.pushButton_calc_result.setFont(font3)
        self.pushButton_calc_result.setStyleSheet(u"QWidget {\n"
"	background: none;\n"
"}\n"
"QPushButton {\n"
"	background:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(12, 123, 147, 255), stop:1 rgba(0, 168, 204, 255));\n"
"	border: none;\n"
"	height: 30px;	\n"
"	width: 400px;\n"
"	font-size: 17px;\n"
"	padding: 5 0 5 0;\n"
"	border-bottom-right-radius: 30px;\n"
"	border-top-left-radius: 30px;\n"
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
"}")
        icon3 = QIcon()
        icon3.addFile(u":/icons/time.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_calc_result.setIcon(icon3)
        self.pushButton_calc_result.setIconSize(QSize(30, 30))

        self.layout_with_details.addWidget(self.pushButton_calc_result, 0, Qt.AlignmentFlag.AlignHCenter)


        self.verticalLayout_2.addWidget(self.widget_with_details)


        self.horizontalLayout_2.addWidget(self.verticalWidget_3)

        self.line = QFrame(PageNormirovanie)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.VLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_2.addWidget(self.line)

        self.find_operations = QWidget(PageNormirovanie)
        self.find_operations.setObjectName(u"find_operations")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(1)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.find_operations.sizePolicy().hasHeightForWidth())
        self.find_operations.setSizePolicy(sizePolicy1)
        self.find_operations.setStyleSheet(u"background: none;")
        self.verticalLayout_3 = QVBoxLayout(self.find_operations)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.pushButton_show_btn_operations = QPushButton(self.find_operations)
        self.pushButton_show_btn_operations.setObjectName(u"pushButton_show_btn_operations")
        self.pushButton_show_btn_operations.setStyleSheet(u"QPushButton {\n"
"	background:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(12, 123, 147, 255), stop:1 rgba(0, 168, 204, 255));\n"
"	border: none;\n"
"	font-size: 11px;\n"
"	padding: 5 10 5 10;\n"
"	border-radius: 5px;\n"
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
"	background: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(12, 123, 147, 177), stop:1 rgba(39, 73, 109, 255));\n"
"	color: rgb(0, 168, 204);\n"
""
                        "}")
        icon4 = QIcon()
        icon4.addFile(u":/icons/operations_tehno.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_show_btn_operations.setIcon(icon4)

        self.verticalLayout_3.addWidget(self.pushButton_show_btn_operations, 0, Qt.AlignmentFlag.AlignHCenter)

        self.layout_buttons_tehno_pro = QVBoxLayout()
        self.layout_buttons_tehno_pro.setSpacing(2)
        self.layout_buttons_tehno_pro.setObjectName(u"layout_buttons_tehno_pro")

        self.verticalLayout_3.addLayout(self.layout_buttons_tehno_pro)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_2)


        self.horizontalLayout_2.addWidget(self.find_operations)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_3)

        self.plainTextEdit_log = QPlainTextEdit(PageNormirovanie)
        self.plainTextEdit_log.setObjectName(u"plainTextEdit_log")
        self.plainTextEdit_log.setMaximumSize(QSize(16777215, 200))
        font4 = QFont()
        font4.setFamilies([u"Segoe UI Light"])
        self.plainTextEdit_log.setFont(font4)
        self.plainTextEdit_log.setStyleSheet(u"background: rgba(255, 255, 255,0);\n"
"border: none;")
        self.plainTextEdit_log.setFrameShape(QFrame.Shape.StyledPanel)
        self.plainTextEdit_log.setFrameShadow(QFrame.Shadow.Sunken)
        self.plainTextEdit_log.setReadOnly(True)
        self.plainTextEdit_log.setTabStopDistance(80.000000000000000)
        self.plainTextEdit_log.setBackgroundVisible(False)

        self.verticalLayout.addWidget(self.plainTextEdit_log)


        self.retranslateUi(PageNormirovanie)

        QMetaObject.connectSlotsByName(PageNormirovanie)
    # setupUi

    def retranslateUi(self, PageNormirovanie):
        PageNormirovanie.setWindowTitle(QCoreApplication.translate("PageNormirovanie", u"\u041d\u043e\u0440\u043c\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u0435", None))
        self.btn_home.setText(QCoreApplication.translate("PageNormirovanie", u"\u041d\u0410\u0417\u0410\u0414", None))
        self.label.setText("")
        self.btn_open_file.setText(QCoreApplication.translate("PageNormirovanie", u" \u041e\u0442\u043a\u0440\u044b\u0442\u044c \u0444\u0430\u0439\u043b", None))
        self.error_path.setText("")
        self.label_4.setText(QCoreApplication.translate("PageNormirovanie", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u043b\u0438\u0441\u0442, \u0432 \u043a\u043e\u0442\u043e\u0440\u043e\u043c \u043d\u0430\u0445\u043e\u0434\u044f\u0442\u0441\u044f \u0434\u0435\u0442\u0430\u043b\u0438 \u0438 \u043e\u043f\u0435\u0440\u0430\u0446\u0438\u0438:", None))
        self.label_2.setText(QCoreApplication.translate("PageNormirovanie", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u0414\u0415\u0422\u0410\u041b\u042c \u0438\u0437 \u0441\u043f\u0438\u0441\u043a\u0430:", None))
        self.comboBox_details.setCurrentText("")
        self.comboBox_details.setPlaceholderText(QCoreApplication.translate("PageNormirovanie", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u0438\u043b\u0438 \u0432\u0432\u0435\u0434\u0438\u0442\u0435...", None))
        self.btn_clear_details.setText(QCoreApplication.translate("PageNormirovanie", u"\u041e\u0447\u0438\u0441\u0442\u0438\u0442\u044c \u0441\u0442\u0440\u043e\u043a\u0443", None))
        self.label_3.setText(QCoreApplication.translate("PageNormirovanie", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u041e\u041f\u0415\u0420\u0410\u0426\u0418\u042e \u0438\u0437 \u0441\u043f\u0438\u0441\u043a\u0430:", None))
        self.comboBox_operations.setPlaceholderText(QCoreApplication.translate("PageNormirovanie", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u0438\u043b\u0438 \u0432\u0432\u0435\u0434\u0438\u0442\u0435...", None))
        self.btn_clear_operations.setText(QCoreApplication.translate("PageNormirovanie", u"\u041e\u0447\u0438\u0441\u0442\u0438\u0442\u044c \u0441\u0442\u0440\u043e\u043a\u0443", None))
        self.pushButton_calc_result.setText(QCoreApplication.translate("PageNormirovanie", u" \u0420\u0430\u0441\u0441\u0447\u0438\u0442\u0430\u0442\u044c \u0432\u0440\u0435\u043c\u044f", None))
#if QT_CONFIG(shortcut)
        self.pushButton_calc_result.setShortcut(QCoreApplication.translate("PageNormirovanie", u"Ctrl+R", None))
#endif // QT_CONFIG(shortcut)
        self.pushButton_show_btn_operations.setText(QCoreApplication.translate("PageNormirovanie", u"\u041e\u043f\u0435\u0440\u0430\u0446\u0438\u0438 \u0438\u0437 \u0422\u0435\u0445\u043d\u043e\u041f\u0440\u043e", None))
        self.plainTextEdit_log.setPlainText("")
    # retranslateUi

