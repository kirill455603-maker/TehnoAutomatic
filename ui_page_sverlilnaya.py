# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_page_sverlilnaya.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGroupBox, QHBoxLayout,
    QHeaderView, QLabel, QPushButton, QSizePolicy,
    QStackedWidget, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)

from views.pages.page_sverlilnaya_chistovaya import PageSverlilnayaChistovaya
from views.pages.page_sverlilnaya_expanding_hole import PageSverlilnayaExpandingHole
from views.pages.page_sverlilnaya_faska import PageSverlilnayaFaska
from views.pages.page_sverlilnaya_rezba import PageSverlilnayaRezba
from views.pages.page_sverlilnaya_start import PageSverlilnayaStart
import res_rc

class Ui_PageSverlilnaya(object):
    def setupUi(self, PageSverlilnaya):
        if not PageSverlilnaya.objectName():
            PageSverlilnaya.setObjectName(u"PageSverlilnaya")
        PageSverlilnaya.resize(1000, 683)
        PageSverlilnaya.setMinimumSize(QSize(1000, 0))
        PageSverlilnaya.setStyleSheet(u"color: white;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0, stop:0 rgba(20, 40, 80, 255), stop:1 rgba(39, 73, 109, 255));\n"
"")
        self.verticalLayout_4 = QVBoxLayout(PageSverlilnaya)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 5, 0, -1)
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(5, 0, -1, -1)
        self.btn_home_1 = QPushButton(PageSverlilnaya)
        self.btn_home_1.setObjectName(u"btn_home_1")
        font = QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.btn_home_1.setFont(font)
        self.btn_home_1.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_home_1.setStyleSheet(u"QPushButton {\n"
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
        self.btn_home_1.setIcon(icon)
        self.btn_home_1.setIconSize(QSize(20, 20))

        self.horizontalLayout_6.addWidget(self.btn_home_1, 0, Qt.AlignmentFlag.AlignLeft)


        self.verticalLayout_4.addLayout(self.horizontalLayout_6)

        self.label_title_2 = QLabel(PageSverlilnaya)
        self.label_title_2.setObjectName(u"label_title_2")
        self.label_title_2.setMaximumSize(QSize(16777215, 30))
        font1 = QFont()
        font1.setFamilies([u"Onyx"])
        font1.setWeight(QFont.DemiBold)
        self.label_title_2.setFont(font1)
        self.label_title_2.setStyleSheet(u"background-color: none;\n"
"color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(12, 123, 147, 255), stop:1 rgba(0, 168, 204, 255));\n"
"font-size: 28px;\n"
"font-weight: 600;\n"
"border: none;\n"
"width: 300px;\n"
"\n"
"")
        self.label_title_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_title_2)

        self.label = QLabel(PageSverlilnaya)
        self.label.setObjectName(u"label")
        font2 = QFont()
        font2.setBold(False)
        self.label.setFont(font2)
        self.label.setStyleSheet(u"background-color: none;\n"
"color: rgb(203, 203, 203);\n"
"font-size: 15px;\n"
"font-weight: 400;\n"
"border: none")
        self.label.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignHCenter)

        self.verticalLayout_4.addWidget(self.label)

        self.groupBox = QGroupBox(PageSverlilnaya)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setStyleSheet(u"QWidget {\n"
"	background: none;\n"
"	border: none;\n"
"}\n"
"QPushButton {\n"
"	background:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(12, 123, 147, 255), stop:1 rgba(0, 168, 204, 255));\n"
"	border: none;\n"
"	height: 20px;	\n"
"	width: 400px;\n"
"	font-size: 17px;\n"
"	padding: 5 0 5 40;\n"
"	border-bottom-right-radius: 5px;\n"
"	border-top-left-radius: 5px;\n"
"	border: 1px solid qradialgradient(spread:pad, cx:0.506, cy:1, radius:1.147, fx:0.494318, fy:1, stop:0 rgba(12, 123, 147, 255), stop:1 rgba(255, 255, 255, 0));\n"
"	text-align: left;\n"
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
"	backgroun"
                        "d: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(12, 123, 147, 177), stop:1 rgba(39, 73, 109, 255));\n"
"	color: rgb(0, 168, 204);\n"
"}")
        self.verticalLayout_3 = QVBoxLayout(self.groupBox)
        self.verticalLayout_3.setSpacing(6)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(10, 0, 10, 0)
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(5)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.btn_page1 = QPushButton(self.groupBox)
        self.btn_page1.setObjectName(u"btn_page1")
        font3 = QFont()
        self.btn_page1.setFont(font3)
        self.btn_page1.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_page1.setStyleSheet(u"")
        icon1 = QIcon()
        icon1.addFile(u":/icons/sverlovka/sverlenie-no-back.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_page1.setIcon(icon1)
        self.btn_page1.setIconSize(QSize(40, 40))
        self.btn_page1.setCheckable(True)
        self.btn_page1.setChecked(True)
        self.btn_page1.setAutoExclusive(True)

        self.horizontalLayout_4.addWidget(self.btn_page1)

        self.btn_page2 = QPushButton(self.groupBox)
        self.btn_page2.setObjectName(u"btn_page2")
        self.btn_page2.setFont(font3)
        self.btn_page2.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_page2.setStyleSheet(u"")
        icon2 = QIcon()
        icon2.addFile(u":/icons/sverlovka/rashirenie-no-back.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_page2.setIcon(icon2)
        self.btn_page2.setIconSize(QSize(40, 40))
        self.btn_page2.setCheckable(True)
        self.btn_page2.setChecked(False)
        self.btn_page2.setAutoRepeat(False)
        self.btn_page2.setAutoExclusive(True)

        self.horizontalLayout_4.addWidget(self.btn_page2)

        self.btn_page3 = QPushButton(self.groupBox)
        self.btn_page3.setObjectName(u"btn_page3")
        self.btn_page3.setFont(font3)
        self.btn_page3.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_page3.setStyleSheet(u"")
        icon3 = QIcon()
        icon3.addFile(u":/icons/sverlovka/razvertivanie-no-back.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_page3.setIcon(icon3)
        self.btn_page3.setIconSize(QSize(40, 40))
        self.btn_page3.setCheckable(True)
        self.btn_page3.setChecked(False)
        self.btn_page3.setAutoRepeat(False)
        self.btn_page3.setAutoExclusive(True)

        self.horizontalLayout_4.addWidget(self.btn_page3)


        self.verticalLayout_3.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(5)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.btn_page5 = QPushButton(self.groupBox)
        self.btn_page5.setObjectName(u"btn_page5")
        self.btn_page5.setFont(font3)
        self.btn_page5.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_page5.setStyleSheet(u"")
        icon4 = QIcon()
        icon4.addFile(u":/icons/sverlovka/faska-no-back.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_page5.setIcon(icon4)
        self.btn_page5.setIconSize(QSize(40, 40))
        self.btn_page5.setCheckable(True)
        self.btn_page5.setChecked(False)
        self.btn_page5.setAutoRepeat(False)
        self.btn_page5.setAutoExclusive(True)

        self.horizontalLayout_3.addWidget(self.btn_page5)

        self.btn_page4 = QPushButton(self.groupBox)
        self.btn_page4.setObjectName(u"btn_page4")
        self.btn_page4.setFont(font3)
        self.btn_page4.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_page4.setStyleSheet(u"")
        icon5 = QIcon()
        icon5.addFile(u":/icons/sverlovka/rezba-no-back.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_page4.setIcon(icon5)
        self.btn_page4.setIconSize(QSize(40, 40))
        self.btn_page4.setCheckable(True)
        self.btn_page4.setChecked(False)
        self.btn_page4.setAutoRepeat(False)
        self.btn_page4.setAutoExclusive(True)

        self.horizontalLayout_3.addWidget(self.btn_page4)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)


        self.verticalLayout_4.addWidget(self.groupBox)

        self.line = QFrame(PageSverlilnaya)
        self.line.setObjectName(u"line")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line.sizePolicy().hasHeightForWidth())
        self.line.setSizePolicy(sizePolicy)
        self.line.setMaximumSize(QSize(16777215, 1))
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_4.addWidget(self.line)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, 20, 0, -1)
        self.stackedWidget_pages = QStackedWidget(PageSverlilnaya)
        self.stackedWidget_pages.setObjectName(u"stackedWidget_pages")
        self.stackedWidget_pages.setStyleSheet(u"color: white;\n"
"background-color: rgba(0, 0, 0, 0)\n"
"")
        self.page_sverlilnaya_start = PageSverlilnayaStart()
        self.page_sverlilnaya_start.setObjectName(u"page_sverlilnaya_start")
        self.page_sverlilnaya_start.setStyleSheet(u"")
        self.stackedWidget_pages.addWidget(self.page_sverlilnaya_start)
        self.page_sverlilnaya_expanding_hole = PageSverlilnayaExpandingHole()
        self.page_sverlilnaya_expanding_hole.setObjectName(u"page_sverlilnaya_expanding_hole")
        self.stackedWidget_pages.addWidget(self.page_sverlilnaya_expanding_hole)
        self.page_sverlilnaya_chistovaya = PageSverlilnayaChistovaya()
        self.page_sverlilnaya_chistovaya.setObjectName(u"page_sverlilnaya_chistovaya")
        self.page_sverlilnaya_chistovaya.setStyleSheet(u"color: white;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0, stop:0 rgba(20, 40, 80, 255), stop:1 rgba(39, 73, 109, 255));\n"
"")
        self.stackedWidget_pages.addWidget(self.page_sverlilnaya_chistovaya)
        self.page_sverlilnaya_rezba = PageSverlilnayaRezba()
        self.page_sverlilnaya_rezba.setObjectName(u"page_sverlilnaya_rezba")
        self.stackedWidget_pages.addWidget(self.page_sverlilnaya_rezba)
        self.page_sverlilnaya_faska = PageSverlilnayaFaska()
        self.page_sverlilnaya_faska.setObjectName(u"page_sverlilnaya_faska")
        self.stackedWidget_pages.addWidget(self.page_sverlilnaya_faska)

        self.horizontalLayout.addWidget(self.stackedWidget_pages)


        self.verticalLayout_4.addLayout(self.horizontalLayout)

        self.btn_save_result = QPushButton(PageSverlilnaya)
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
        icon6 = QIcon()
        icon6.addFile(u":/icons/save.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_save_result.setIcon(icon6)
        self.btn_save_result.setIconSize(QSize(20, 20))

        self.verticalLayout_4.addWidget(self.btn_save_result, 0, Qt.AlignmentFlag.AlignHCenter)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(10)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(10, 0, 10, -1)
        self.text_info = QLabel(PageSverlilnaya)
        self.text_info.setObjectName(u"text_info")
        font5 = QFont()
        font5.setPointSize(10)
        self.text_info.setFont(font5)
        self.text_info.setStyleSheet(u"background:none;\n"
"color: rgb(255, 85, 85);")
        self.text_info.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.text_info)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, 0, -1, -1)
        self.btn_clear_table = QPushButton(PageSverlilnaya)
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
        icon7 = QIcon()
        icon7.addFile(u":/icons/clear.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_clear_table.setIcon(icon7)

        self.horizontalLayout_2.addWidget(self.btn_clear_table, 0, Qt.AlignmentFlag.AlignRight)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.table_widget_sverlilnaya = QTableWidget(PageSverlilnaya)
        if (self.table_widget_sverlilnaya.columnCount() < 3):
            self.table_widget_sverlilnaya.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.table_widget_sverlilnaya.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.table_widget_sverlilnaya.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.table_widget_sverlilnaya.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.table_widget_sverlilnaya.setObjectName(u"table_widget_sverlilnaya")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.table_widget_sverlilnaya.sizePolicy().hasHeightForWidth())
        self.table_widget_sverlilnaya.setSizePolicy(sizePolicy1)
        self.table_widget_sverlilnaya.setMinimumSize(QSize(0, 100))
        self.table_widget_sverlilnaya.setFont(font5)
        self.table_widget_sverlilnaya.setStyleSheet(u"/* \u0421\u0430\u043c \u0432\u0438\u0434\u0436\u0435\u0442 \u2014 \u043f\u0440\u043e\u0437\u0440\u0430\u0447\u043d\u044b\u0439 \u0444\u043e\u043d */\n"
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
        self.table_widget_sverlilnaya.setRowCount(0)
        self.table_widget_sverlilnaya.setColumnCount(3)
        self.table_widget_sverlilnaya.horizontalHeader().setVisible(True)
        self.table_widget_sverlilnaya.verticalHeader().setVisible(False)
        self.table_widget_sverlilnaya.verticalHeader().setMinimumSectionSize(90)
        self.table_widget_sverlilnaya.verticalHeader().setDefaultSectionSize(100)
        self.table_widget_sverlilnaya.verticalHeader().setProperty(u"showSortIndicator", False)
        self.table_widget_sverlilnaya.verticalHeader().setStretchLastSection(False)

        self.verticalLayout_2.addWidget(self.table_widget_sverlilnaya)


        self.verticalLayout_4.addLayout(self.verticalLayout_2)

        self.btn_save_and_export = QPushButton(PageSverlilnaya)
        self.btn_save_and_export.setObjectName(u"btn_save_and_export")
        self.btn_save_and_export.setMaximumSize(QSize(16777215, 16777215))
        font6 = QFont()
        font6.setPointSize(15)
        self.btn_save_and_export.setFont(font6)
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
        icon8 = QIcon()
        icon8.addFile(u":/icons/export.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_save_and_export.setIcon(icon8)
        self.btn_save_and_export.setIconSize(QSize(20, 20))

        self.verticalLayout_4.addWidget(self.btn_save_and_export, 0, Qt.AlignmentFlag.AlignHCenter)


        self.retranslateUi(PageSverlilnaya)

        self.btn_page1.setDefault(False)
        self.btn_page3.setDefault(False)
        self.btn_page4.setDefault(False)
        self.stackedWidget_pages.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(PageSverlilnaya)
    # setupUi

    def retranslateUi(self, PageSverlilnaya):
        PageSverlilnaya.setWindowTitle(QCoreApplication.translate("PageSverlilnaya", u"\u0421\u0432\u0435\u0440\u043b\u0438\u043b\u044c\u043d\u0430\u044f \u043e\u043f\u0435\u0440\u0430\u0446\u0438\u044f", None))
        self.btn_home_1.setText(QCoreApplication.translate("PageSverlilnaya", u"  \u0414\u041e\u041c\u041e\u0419", None))
        self.label_title_2.setText(QCoreApplication.translate("PageSverlilnaya", u"\u0421\u0432\u0435\u0440\u043b\u0438\u043b\u044c\u043d\u0430\u044f \u043e\u043f\u0435\u0440\u0430\u0446\u0438\u044f", None))
        self.label.setText(QCoreApplication.translate("PageSverlilnaya", u"\u041e\u043f\u0435\u0440\u0430\u0446\u0438\u0438 \u043e\u0431\u0440\u0430\u0431\u043e\u0442\u043a\u0438:", None))
        self.groupBox.setTitle("")
        self.btn_page1.setText(QCoreApplication.translate("PageSverlilnaya", u" \u0421\u0432\u0435\u0440\u043b\u0435\u043d\u0438\u0435 \u043e\u0442\u0432\u0435\u0440\u0441\u0442\u0438\u0439", None))
        self.btn_page2.setText(QCoreApplication.translate("PageSverlilnaya", u" \u0420\u0430\u0441\u0448\u0438\u0440\u0435\u043d\u0438\u0435 \u043e\u0442\u0432\u0435\u0440\u0441\u0442\u0438\u0439", None))
        self.btn_page3.setText(QCoreApplication.translate("PageSverlilnaya", u" \u0420\u0430\u0437\u0432\u0435\u0440\u0442\u044b\u0432\u0430\u043d\u0438\u0435 \u043e\u0442\u0432\u0435\u0440\u0441\u0442\u0438\u0439", None))
        self.btn_page5.setText(QCoreApplication.translate("PageSverlilnaya", u" \u0421\u043e\u0437\u0434\u0430\u043d\u0438\u0435 \u0444\u0430\u0441\u043a\u0438", None))
        self.btn_page4.setText(QCoreApplication.translate("PageSverlilnaya", u" \u041d\u0430\u0440\u0435\u0437\u0430\u043d\u0438\u0435 \u0440\u0435\u0437\u044c\u0431\u044b", None))
        self.btn_save_result.setText(QCoreApplication.translate("PageSverlilnaya", u" \u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u044f", None))
        self.text_info.setText("")
        self.btn_clear_table.setText(QCoreApplication.translate("PageSverlilnaya", u"\u041e\u0447\u0438\u0441\u0442\u0438\u0442\u044c \u0442\u0430\u0431\u043b\u0438\u0446\u0443", None))
        ___qtablewidgetitem = self.table_widget_sverlilnaya.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("PageSverlilnaya", u"\u0418\u043d\u0441\u0442\u0440\u0443\u043c\u0435\u043d\u0442", None))
        ___qtablewidgetitem1 = self.table_widget_sverlilnaya.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("PageSverlilnaya", u"\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 [\u041c\u043e\u0436\u043d\u043e \u0438\u0437\u043c\u0435\u043d\u044f\u0442\u044c]", None))
        self.btn_save_and_export.setText(QCoreApplication.translate("PageSverlilnaya", u" \u041f\u0435\u0440\u0435\u043d\u0435\u0441\u0442\u0438 \u043f\u0435\u0440\u0435\u0445\u043e\u0434\u044b \u0432 \u0422\u0435\u0445\u043d\u043e\u041f\u0440\u043e", None))
    # retranslateUi

