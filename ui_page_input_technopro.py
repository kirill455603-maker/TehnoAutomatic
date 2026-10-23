# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_page_input_technopro.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QGroupBox,
    QHBoxLayout, QHeaderView, QLabel, QPushButton,
    QSizePolicy, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)
import res_rc

class Ui_PageInputTechnopro(object):
    def setupUi(self, PageInputTechnopro):
        if not PageInputTechnopro.objectName():
            PageInputTechnopro.setObjectName(u"PageInputTechnopro")
        PageInputTechnopro.resize(1000, 750)
        PageInputTechnopro.setMinimumSize(QSize(1000, 750))
        PageInputTechnopro.setMaximumSize(QSize(1000, 750))
        PageInputTechnopro.setStyleSheet(u"color: white;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0, stop:0 rgba(20, 40, 80, 255), stop:1 rgba(39, 73, 109, 255));\n"
"")
        self.verticalLayout_3 = QVBoxLayout(PageInputTechnopro)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, 0, -1, -1)
        self.btn_home_tokarnaya = QPushButton(PageInputTechnopro)
        self.btn_home_tokarnaya.setObjectName(u"btn_home_tokarnaya")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_home_tokarnaya.sizePolicy().hasHeightForWidth())
        self.btn_home_tokarnaya.setSizePolicy(sizePolicy)
        self.btn_home_tokarnaya.setMinimumSize(QSize(70, 0))
        self.btn_home_tokarnaya.setMaximumSize(QSize(150, 30))
        font = QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.btn_home_tokarnaya.setFont(font)
        self.btn_home_tokarnaya.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
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

        self.horizontalLayout_2.addWidget(self.btn_home_tokarnaya, 0, Qt.AlignmentFlag.AlignLeft)

        self.btn_update = QPushButton(PageInputTechnopro)
        self.btn_update.setObjectName(u"btn_update")
        sizePolicy.setHeightForWidth(self.btn_update.sizePolicy().hasHeightForWidth())
        self.btn_update.setSizePolicy(sizePolicy)
        self.btn_update.setMinimumSize(QSize(70, 0))
        self.btn_update.setFont(font)
        self.btn_update.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_update.setStyleSheet(u"QPushButton {\n"
"	padding: 2 5 2 5;\n"
"	background: rgba(0, 0, 0, 0);\n"
"}\n"
"QPushButton:hover {\n"
"	color: rgb(218, 218, 218)\n"
"}\n"
"")
        icon1 = QIcon()
        icon1.addFile(u":/icons/update.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_update.setIcon(icon1)
        self.btn_update.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.btn_update, 0, Qt.AlignmentFlag.AlignRight)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.error_label = QLabel(PageInputTechnopro)
        self.error_label.setObjectName(u"error_label")
        self.error_label.setStyleSheet(u"background: none;")
        self.error_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_3.addWidget(self.error_label)

        self.menu = QWidget(PageInputTechnopro)
        self.menu.setObjectName(u"menu")
        self.menu.setStyleSheet(u"background: rgba(0,0,0,0);")
        self.menu23 = QVBoxLayout(self.menu)
        self.menu23.setObjectName(u"menu23")
        self.menu23.setContentsMargins(10, 15, 10, 20)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, -1, -1, 0)
        self.label_3 = QLabel(self.menu)
        self.label_3.setObjectName(u"label_3")
        font1 = QFont()
        font1.setWeight(QFont.DemiBold)
        self.label_3.setFont(font1)
        self.label_3.setStyleSheet(u"background-color: none;\n"
"color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(12, 123, 147, 255), stop:1 rgba(0, 168, 204, 255));\n"
"font-size: 28px;\n"
"font-weight: 600;\n"
"border: none;\n"
"width: 300px;\n"
"\n"
"")

        self.verticalLayout.addWidget(self.label_3, 0, Qt.AlignmentFlag.AlignHCenter)

        self.label = QLabel(self.menu)
        self.label.setObjectName(u"label")
        font2 = QFont()
        font2.setFamilies([u"Segoe UI Light"])
        font2.setPointSize(12)
        font2.setBold(False)
        self.label.setFont(font2)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.label, 0, Qt.AlignmentFlag.AlignHCenter)

        self.tableWidget = QTableWidget(self.menu)
        if (self.tableWidget.columnCount() < 1):
            self.tableWidget.setColumnCount(1)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        if (self.tableWidget.rowCount() < 1):
            self.tableWidget.setRowCount(1)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setCheckState(Qt.Unchecked)
        self.tableWidget.setItem(0, 0, __qtablewidgetitem1)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.viewport().setProperty(u"cursor", QCursor(Qt.CursorShape.ArrowCursor))
        self.tableWidget.setStyleSheet(u"/* === \u0421\u0430\u043c\u0430 \u0442\u0430\u0431\u043b\u0438\u0446\u0430 === */\n"
"QTableWidget {\n"
"	border: none;\n"
"    gridline-color: rgba(0, 0, 0, 0);             /* \u0426\u0432\u0435\u0442 \u043b\u0438\u043d\u0438\u0439 \u0441\u0435\u0442\u043a\u0438 */\n"
"    selection-background-color: #0078d7; /* \u0426\u0432\u0435\u0442 \u0444\u043e\u043d\u0430 \u0432\u044b\u0434\u0435\u043b\u0435\u043d\u043d\u043e\u0439 \u044f\u0447\u0435\u0439\u043a\u0438 */\n"
"    selection-color: rgb(42, 82, 127);            /* \u0426\u0432\u0435\u0442 \u0442\u0435\u043a\u0441\u0442\u0430 \u0432\u044b\u0434\u0435\u043b\u0435\u043d\u043d\u043e\u0439 \u044f\u0447\u0435\u0439\u043a\u0438 */                  /* \u0423\u0431\u0438\u0440\u0430\u0435\u043c \u0440\u0430\u043c\u043a\u0443 \u0444\u043e\u043a\u0443\u0441\u0430 */\n"
"}\n"
"\n"
"/* === \u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043a\u0438 \u0441\u0442\u043e\u043b\u0431\u0446\u043e\u0432 \u0438 \u0441\u0442\u0440\u043e\u043a === */\n"
"QHeaderView::section {\n"
"   "
                        " background-color: rgba(74, 74, 74, 0);\n"
"    color: rgb(255, 255, 255);\n"
"    padding: 6px;\n"
"    border: none;   /* \u0420\u0430\u0437\u0434\u0435\u043b\u0438\u0442\u0435\u043b\u044c \u043c\u0435\u0436\u0434\u0443 \u0437\u0430\u0433\u043e\u043b\u043e\u0432\u043a\u0430\u043c\u0438 */\n"
"    font-weight: 600;\n"
"    font-size: 13px;\n"
"}\n"
"\n"
"QHeaderView::section:last {\n"
"	border: none;\n"
"}\n"
"\n"
"/* \u0423\u0433\u043b\u043e\u0432\u0430\u044f \u043a\u043d\u043e\u043f\u043a\u0430 (\u043f\u0435\u0440\u0435\u0441\u0435\u0447\u0435\u043d\u0438\u0435 \u0437\u0430\u0433\u043e\u043b\u043e\u0432\u043a\u043e\u0432 \u0441\u0442\u0440\u043e\u043a \u0438 \u0441\u0442\u043e\u043b\u0431\u0446\u043e\u0432) */\n"
"QTableCornerButton::section {\n"
"    background-color: rgba(74, 74, 74, 0);\n"
"    border: none;\n"
"}\n"
"\n"
"/* === \u042f\u0447\u0435\u0439\u043a\u0438 \u0442\u0430\u0431\u043b\u0438\u0446\u044b === */\n"
"QTableWidget::item {\n"
"    padding: 5px;\n"
"	border-bottom: 1px solid white;\n"
"  "
                        "  color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"/* \u0421\u043e\u0441\u0442\u043e\u044f\u043d\u0438\u0435 \u043f\u0440\u0438 \u043d\u0430\u0432\u0435\u0434\u0435\u043d\u0438\u0438 \u043c\u044b\u0448\u0438 */\n"
"QTableWidget::item:hover {\n"
"    color: rgb(202, 202, 202);\n"
"}\n"
"\n"
"/* \u0421\u043e\u0441\u0442\u043e\u044f\u043d\u0438\u0435 \u0432\u044b\u0434\u0435\u043b\u0435\u043d\u043d\u043e\u0439 \u044f\u0447\u0435\u0439\u043a\u0438 (\u043f\u0435\u0440\u0435\u043e\u043f\u0440\u0435\u0434\u0435\u043b\u044f\u0435\u043c hover, \u0435\u0441\u043b\u0438 \u043e\u043d\u0430 \u0432\u044b\u0434\u0435\u043b\u0435\u043d\u0430) */\n"
"QTableWidget::item:selected {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0, stop:0 rgba(39, 72, 109, 129), stop:1 rgba(21, 41, 81, 129));\n"
"    color: rgb(152, 152, 152);\n"
"}\n"
"\n"
"/* === \u041f\u043e\u043b\u043e\u0441\u044b \u043f\u0440\u043e\u043a\u0440\u0443\u0442\u043a\u0438 === */\n"
"QScrollBar:vertical {\n"
"    background: #f4f6f8;\n"
"    w"
                        "idth: 10px;\n"
"    margin: 0px;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"    background: #c0c0c0;\n"
"    min-height: 20px;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical:hover {\n"
"    background: #a0a0a0;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {\n"
"    height: 0px; /* \u0421\u043a\u0440\u044b\u0432\u0430\u0435\u043c \u0441\u0442\u0440\u0435\u043b\u043a\u0438 \u043f\u0440\u043e\u043a\u0440\u0443\u0442\u043a\u0438 */\n"
"}\n"
"\n"
"QScrollBar:horizontal {\n"
"    background: #f4f6f8;\n"
"    height: 10px;\n"
"    margin: 0px;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal {\n"
"    background: #c0c0c0;\n"
"    min-width: 20px;\n"
"    border-radius: 5px;\n"
"}")
        self.tableWidget.horizontalHeader().setStretchLastSection(True)

        self.verticalLayout.addWidget(self.tableWidget, 0, Qt.AlignmentFlag.AlignHCenter)


        self.menu23.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(20)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 20, 0, 100)
        self.groupBox_2 = QGroupBox(self.menu)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setStyleSheet(u"border: none;\n"
"background: none;")
        self.verticalLayout_4 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")

        self.verticalLayout_2.addWidget(self.groupBox_2, 0, Qt.AlignmentFlag.AlignHCenter)

        self.error_label_start = QLabel(self.menu)
        self.error_label_start.setObjectName(u"error_label_start")
        font3 = QFont()
        font3.setPointSize(12)
        font3.setBold(False)
        self.error_label_start.setFont(font3)
        self.error_label_start.setStyleSheet(u"background: none;")

        self.verticalLayout_2.addWidget(self.error_label_start, 0, Qt.AlignmentFlag.AlignHCenter)

        self.line = QFrame(self.menu)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_2.addWidget(self.line)

        self.checkBox_clear_table = QCheckBox(self.menu)
        self.checkBox_clear_table.setObjectName(u"checkBox_clear_table")
        self.checkBox_clear_table.setStyleSheet(u"QCheckBox::indicator {\n"
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

        self.verticalLayout_2.addWidget(self.checkBox_clear_table, 0, Qt.AlignmentFlag.AlignHCenter)

        self.button_start = QPushButton(self.menu)
        self.button_start.setObjectName(u"button_start")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.button_start.sizePolicy().hasHeightForWidth())
        self.button_start.setSizePolicy(sizePolicy1)
        self.button_start.setMaximumSize(QSize(16777215, 50))
        font4 = QFont()
        font4.setPointSize(15)
        font4.setWeight(QFont.DemiBold)
        self.button_start.setFont(font4)
        self.button_start.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.button_start.setStyleSheet(u"QPushButton {\n"
"	background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(11, 98, 0, 255), stop:1 rgba(5, 179, 0, 255));\n"
"	border: 1px solid qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(8, 144, 0, 255), stop:1 rgba(11, 104, 0, 255));\n"
"	border-radius: 7px;\n"
"	height: 30px;	\n"
"	padding: 5 10 5 10;\n"
"	font-size: 15pt;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(5, 179, 0, 255), stop:1 rgba(11, 98, 0, 255));\n"
"	border: 1px solid qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(11, 104, 0, 255), stop:1 rgba(8, 144, 0, 255))\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(1, 13, 0, 255), stop:1 rgba(2, 62, 0, 255))\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/icons/start.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.button_start.setIcon(icon2)
        self.button_start.setIconSize(QSize(30, 30))

        self.verticalLayout_2.addWidget(self.button_start, 0, Qt.AlignmentFlag.AlignHCenter)


        self.menu23.addLayout(self.verticalLayout_2)


        self.verticalLayout_3.addWidget(self.menu)


        self.retranslateUi(PageInputTechnopro)

        QMetaObject.connectSlotsByName(PageInputTechnopro)
    # setupUi

    def retranslateUi(self, PageInputTechnopro):
        PageInputTechnopro.setWindowTitle(QCoreApplication.translate("PageInputTechnopro", u"Form", None))
        self.btn_home_tokarnaya.setText(QCoreApplication.translate("PageInputTechnopro", u" \u041d\u0410\u0417\u0410\u0414", None))
        self.btn_update.setText(QCoreApplication.translate("PageInputTechnopro", u" \u041e\u0431\u043d\u043e\u0432\u0438\u0442\u044c \u0441\u0442\u0440\u0430\u043d\u0438\u0446\u0443", None))
        self.error_label.setText("")
        self.label_3.setText(QCoreApplication.translate("PageInputTechnopro", u"\u041f\u0435\u0440\u0435\u043d\u043e\u0441 \u043f\u0435\u0440\u0435\u0445\u043e\u0434\u043e\u0432 \u0432 \u0422\u0435\u0445\u043d\u043e\u041f\u0440\u043e", None))
        self.label.setText(QCoreApplication.translate("PageInputTechnopro", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u043f\u043e\u0440\u044f\u0434\u043a\u043e\u0432\u044b\u0439 \u043d\u043e\u043c\u0435\u0440 \u0434\u043b\u044f \u0437\u0430\u043f\u043e\u043b\u043d\u0435\u043d\u0438\u044f", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("PageInputTechnopro", u"\u041d\u0430\u0439\u0434\u0435\u043d\u043d\u044b\u0435 \u043e\u043f\u0435\u0440\u0430\u0446\u0438\u0438:", None))

        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        ___qtablewidgetitem1 = self.tableWidget.item(0, 0)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("PageInputTechnopro", u"asdasd", None))
        self.tableWidget.setSortingEnabled(__sortingEnabled)

        self.groupBox_2.setTitle("")
        self.error_label_start.setText("")
        self.checkBox_clear_table.setText(QCoreApplication.translate("PageInputTechnopro", u"\u0421\u0442\u0435\u0440\u0435\u0442\u044c \u043f\u0435\u0440\u0435\u0445\u043e\u0434\u044b \u043f\u043e\u0441\u043b\u0435 \u0437\u0430\u043f\u043e\u043b\u043d\u0435\u043d\u0438\u044f \u0438\u0445 \u0432 \u0422\u0435\u0445\u043d\u043e\u041f\u0440\u043e?", None))
        self.button_start.setText(QCoreApplication.translate("PageInputTechnopro", u"\u0417\u0410\u041f\u0423\u0421\u0422\u0418\u0422\u042c", None))
    # retranslateUi

