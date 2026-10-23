# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_page_tokarnaya.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QHeaderView, QLabel, QPushButton, QSizePolicy,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)
import res_rc

class Ui_PageTokarnaya(object):
    def setupUi(self, PageTokarnaya):
        if not PageTokarnaya.objectName():
            PageTokarnaya.setObjectName(u"PageTokarnaya")
        PageTokarnaya.resize(1000, 774)
        PageTokarnaya.setMinimumSize(QSize(1000, 0))
        PageTokarnaya.setStyleSheet(u"color: white;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0, stop:0 rgba(20, 40, 80, 255), stop:1 rgba(39, 73, 109, 255));\n"
"")
        self.verticalLayout = QVBoxLayout(PageTokarnaya)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, 0, -1, -1)
        self.btn_home = QPushButton(PageTokarnaya)
        self.btn_home.setObjectName(u"btn_home")
        font = QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.btn_home.setFont(font)
        self.btn_home.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
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

        self.horizontalLayout.addWidget(self.btn_home, 0, Qt.AlignmentFlag.AlignLeft)

        self.pushButton = QPushButton(PageTokarnaya)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setStyleSheet(u"background: rgba(0, 0, 0, 0);")
        icon1 = QIcon()
        icon1.addFile(u":/icons/logo_cut.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton.setIcon(icon1)
        self.pushButton.setIconSize(QSize(50, 50))

        self.horizontalLayout.addWidget(self.pushButton, 0, Qt.AlignmentFlag.AlignRight)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.label_title_2 = QLabel(PageTokarnaya)
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

        self.verticalLayout.addWidget(self.label_title_2)

        self.label = QLabel(PageTokarnaya)
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

        self.verticalLayout.addWidget(self.label)

        self.widget = QWidget(PageTokarnaya)
        self.widget.setObjectName(u"widget")
        self.widget.setStyleSheet(u"QWidget {\n"
"	background: none;\n"
"}\n"
"QPushButton {\n"
"	background:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(12, 123, 147, 255), stop:1 rgba(0, 168, 204, 255));\n"
"	border: none;\n"
"	height: 30px;	\n"
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
"}")
        self.verticalLayout_3 = QVBoxLayout(self.widget)
        self.verticalLayout_3.setSpacing(2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 10, 0, 0)
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(-1, -1, -1, 10)
        self.btn_rezba = QPushButton(self.widget)
        self.btn_rezba.setObjectName(u"btn_rezba")
        self.btn_rezba.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_rezba.setStyleSheet(u"")
        icon2 = QIcon()
        icon2.addFile(u":/tokar/rezba-no-back.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_rezba.setIcon(icon2)
        self.btn_rezba.setIconSize(QSize(90, 40))

        self.gridLayout.addWidget(self.btn_rezba, 1, 2, 1, 1)

        self.btn_tochenie = QPushButton(self.widget)
        self.btn_tochenie.setObjectName(u"btn_tochenie")
        self.btn_tochenie.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_tochenie.setStyleSheet(u"")
        icon3 = QIcon()
        icon3.addFile(u":/tokar/tochenie_no_back.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_tochenie.setIcon(icon3)
        self.btn_tochenie.setIconSize(QSize(90, 40))

        self.gridLayout.addWidget(self.btn_tochenie, 1, 1, 1, 1)

        self.btn_angle = QPushButton(self.widget)
        self.btn_angle.setObjectName(u"btn_angle")
        self.btn_angle.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_angle.setStyleSheet(u"")
        icon4 = QIcon()
        icon4.addFile(u":/tokar/angle-no-back.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_angle.setIcon(icon4)
        self.btn_angle.setIconSize(QSize(90, 40))

        self.gridLayout.addWidget(self.btn_angle, 2, 1, 1, 1)

        self.btn_start_obrabotki = QPushButton(self.widget)
        self.btn_start_obrabotki.setObjectName(u"btn_start_obrabotki")
        self.btn_start_obrabotki.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_start_obrabotki.setStyleSheet(u"")
        icon5 = QIcon()
        icon5.addFile(u":/tokar/tok_start_no_back.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_start_obrabotki.setIcon(icon5)
        self.btn_start_obrabotki.setIconSize(QSize(90, 40))

        self.gridLayout.addWidget(self.btn_start_obrabotki, 0, 0, 1, 1, Qt.AlignmentFlag.AlignLeft)

        self.btn_tochenie_4 = QPushButton(self.widget)
        self.btn_tochenie_4.setObjectName(u"btn_tochenie_4")
        self.btn_tochenie_4.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_tochenie_4.setStyleSheet(u"")
        icon6 = QIcon()
        icon6.addFile(u":/tokar/kanavka-no-back.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_tochenie_4.setIcon(icon6)
        self.btn_tochenie_4.setIconSize(QSize(90, 40))

        self.gridLayout.addWidget(self.btn_tochenie_4, 2, 2, 1, 1)

        self.btn_faska = QPushButton(self.widget)
        self.btn_faska.setObjectName(u"btn_faska")
        self.btn_faska.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_faska.setStyleSheet(u"")
        icon7 = QIcon()
        icon7.addFile(u":/tokar/faska-no-back.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_faska.setIcon(icon7)
        self.btn_faska.setIconSize(QSize(90, 40))

        self.gridLayout.addWidget(self.btn_faska, 2, 0, 1, 1)

        self.btn_sverlenie = QPushButton(self.widget)
        self.btn_sverlenie.setObjectName(u"btn_sverlenie")
        self.btn_sverlenie.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_sverlenie.setStyleSheet(u"")
        icon8 = QIcon()
        icon8.addFile(u":/tokar/sverlenie_no_back.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_sverlenie.setIcon(icon8)
        self.btn_sverlenie.setIconSize(QSize(90, 40))

        self.gridLayout.addWidget(self.btn_sverlenie, 1, 0, 1, 1)

        self.btn_podrezka = QPushButton(self.widget)
        self.btn_podrezka.setObjectName(u"btn_podrezka")
        self.btn_podrezka.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_podrezka.setStyleSheet(u"")
        icon9 = QIcon()
        icon9.addFile(u":/tokar/podrezka_no_back.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_podrezka.setIcon(icon9)
        self.btn_podrezka.setIconSize(QSize(90, 40))

        self.gridLayout.addWidget(self.btn_podrezka, 0, 1, 1, 1)

        self.btn_rastochka = QPushButton(self.widget)
        self.btn_rastochka.setObjectName(u"btn_rastochka")
        self.btn_rastochka.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_rastochka.setStyleSheet(u"")
        icon10 = QIcon()
        icon10.addFile(u":/tokar/rastach-no-back.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_rastochka.setIcon(icon10)
        self.btn_rastochka.setIconSize(QSize(90, 40))

        self.gridLayout.addWidget(self.btn_rastochka, 0, 2, 1, 1)


        self.verticalLayout_3.addLayout(self.gridLayout)


        self.verticalLayout.addWidget(self.widget)

        self.line = QFrame(PageTokarnaya)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout.addWidget(self.line)

        self.btn_clear_table = QPushButton(PageTokarnaya)
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
        icon11 = QIcon()
        icon11.addFile(u":/icons/clear.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_clear_table.setIcon(icon11)

        self.verticalLayout.addWidget(self.btn_clear_table, 0, Qt.AlignmentFlag.AlignRight)

        self.table_widget_tokarnaya = QTableWidget(PageTokarnaya)
        if (self.table_widget_tokarnaya.columnCount() < 3):
            self.table_widget_tokarnaya.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.table_widget_tokarnaya.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.table_widget_tokarnaya.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.table_widget_tokarnaya.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.table_widget_tokarnaya.setObjectName(u"table_widget_tokarnaya")
        font3 = QFont()
        font3.setPointSize(10)
        self.table_widget_tokarnaya.setFont(font3)
        self.table_widget_tokarnaya.setStyleSheet(u"/* \u0421\u0430\u043c \u0432\u0438\u0434\u0436\u0435\u0442 \u2014 \u043f\u0440\u043e\u0437\u0440\u0430\u0447\u043d\u044b\u0439 \u0444\u043e\u043d */\n"
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
"\n"
"}\n"
"QPushButton:hover {\n"
"	image: url(:/icons/trash_grey.png);\n"
"	cursor: pointer;\n"
"}")
        self.table_widget_tokarnaya.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.table_widget_tokarnaya.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.table_widget_tokarnaya.setAutoScroll(False)
        self.table_widget_tokarnaya.setShowGrid(True)
        self.table_widget_tokarnaya.setColumnCount(3)
        self.table_widget_tokarnaya.verticalHeader().setMinimumSectionSize(50)
        self.table_widget_tokarnaya.verticalHeader().setDefaultSectionSize(80)
        self.table_widget_tokarnaya.verticalHeader().setStretchLastSection(False)

        self.verticalLayout.addWidget(self.table_widget_tokarnaya)

        self.btn_save_and_export = QPushButton(PageTokarnaya)
        self.btn_save_and_export.setObjectName(u"btn_save_and_export")
        self.btn_save_and_export.setMaximumSize(QSize(16777215, 16777215))
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
        icon12 = QIcon()
        icon12.addFile(u":/icons/export.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_save_and_export.setIcon(icon12)
        self.btn_save_and_export.setIconSize(QSize(20, 20))

        self.verticalLayout.addWidget(self.btn_save_and_export, 0, Qt.AlignmentFlag.AlignHCenter)


        self.retranslateUi(PageTokarnaya)

        QMetaObject.connectSlotsByName(PageTokarnaya)
    # setupUi

    def retranslateUi(self, PageTokarnaya):
        PageTokarnaya.setWindowTitle(QCoreApplication.translate("PageTokarnaya", u"\u0422\u043e\u043a\u0430\u0440\u043d\u0430\u044f \u043e\u0431\u0440\u0430\u0431\u043e\u0442\u043a\u0430", None))
        self.btn_home.setText(QCoreApplication.translate("PageTokarnaya", u"  \u0414\u041e\u041c\u041e\u0419", None))
#if QT_CONFIG(shortcut)
        self.btn_home.setShortcut(QCoreApplication.translate("PageTokarnaya", u"Ctrl+Shift+S", None))
#endif // QT_CONFIG(shortcut)
        self.pushButton.setText("")
        self.label_title_2.setText(QCoreApplication.translate("PageTokarnaya", u"\u0422\u043e\u043a\u0430\u0440\u043d\u0430\u044f \u043e\u043f\u0435\u0440\u0430\u0446\u0438\u044f", None))
        self.label.setText(QCoreApplication.translate("PageTokarnaya", u"\u041e\u043f\u0435\u0440\u0430\u0446\u0438\u0438 \u043e\u0431\u0440\u0430\u0431\u043e\u0442\u043a\u0438:", None))
        self.btn_rezba.setText(QCoreApplication.translate("PageTokarnaya", u"  \u041d\u0430\u0440\u0435\u0437\u0430\u043d\u0438\u0435 \u0440\u0435\u0437\u044c\u0431\u044b", None))
        self.btn_tochenie.setText(QCoreApplication.translate("PageTokarnaya", u"\u0422\u043e\u0447\u0435\u043d\u0438\u0435", None))
        self.btn_angle.setText(QCoreApplication.translate("PageTokarnaya", u" \u041e\u0431\u0440\u0430\u0431\u043e\u0442\u043a\u0430 \u0443\u0433\u043b\u0430", None))
        self.btn_start_obrabotki.setText(QCoreApplication.translate("PageTokarnaya", u"    \u0423\u0441\u0442\u0430\u043d\u043e\u0432\u043a\u0430 \u0434\u0435\u0442\u0430\u043b\u0438", None))
        self.btn_tochenie_4.setText(QCoreApplication.translate("PageTokarnaya", u"  \u041a\u0430\u043d\u0430\u0432\u043a\u0430", None))
        self.btn_faska.setText(QCoreApplication.translate("PageTokarnaya", u"    \u041e\u0431\u0440\u0430\u0431\u043e\u0442\u043a\u0430 \u0444\u0430\u0441\u043a\u0438", None))
        self.btn_sverlenie.setText(QCoreApplication.translate("PageTokarnaya", u"\u0421\u0432\u0435\u0440\u043b\u0435\u043d\u0438\u0435", None))
        self.btn_podrezka.setText(QCoreApplication.translate("PageTokarnaya", u"\u041f\u043e\u0434\u0440\u0435\u0437\u043a\u0430 \u0442\u043e\u0440\u0446\u0430", None))
        self.btn_rastochka.setText(QCoreApplication.translate("PageTokarnaya", u"\u0420\u0430\u0441\u0442\u0430\u0447\u0438\u0432\u0430\u043d\u0438\u0435", None))
        self.btn_clear_table.setText(QCoreApplication.translate("PageTokarnaya", u"\u041e\u0447\u0438\u0441\u0442\u0438\u0442\u044c \u0442\u0430\u0431\u043b\u0438\u0446\u0443", None))
        ___qtablewidgetitem = self.table_widget_tokarnaya.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("PageTokarnaya", u"\u0418\u043d\u0441\u0442\u0440\u0443\u043c\u0435\u043d\u0442", None))
        ___qtablewidgetitem1 = self.table_widget_tokarnaya.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("PageTokarnaya", u"\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 [\u041c\u043e\u0436\u043d\u043e \u0438\u0437\u043c\u0435\u043d\u044f\u0442\u044c]", None))
        self.btn_save_and_export.setText(QCoreApplication.translate("PageTokarnaya", u"  \u041f\u0435\u0440\u0435\u043d\u0435\u0441\u0442\u0438 \u043f\u0435\u0440\u0435\u0445\u043e\u0434\u044b \u0432 \u0422\u0435\u0445\u043d\u043e\u041f\u0440\u043e", None))
    # retranslateUi

