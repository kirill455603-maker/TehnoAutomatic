# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_page_shlifovanie.ui'
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

class Ui_Shlifovanie(object):
    def setupUi(self, Shlifovanie):
        if not Shlifovanie.objectName():
            Shlifovanie.setObjectName(u"Shlifovanie")
        Shlifovanie.resize(1000, 631)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Shlifovanie.sizePolicy().hasHeightForWidth())
        Shlifovanie.setSizePolicy(sizePolicy)
        Shlifovanie.setMinimumSize(QSize(1000, 0))
        Shlifovanie.setStyleSheet(u"color: white;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0, stop:0 rgba(20, 40, 80, 255), stop:1 rgba(39, 73, 109, 255));\n"
"")
        self.verticalLayout = QVBoxLayout(Shlifovanie)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, 0, -1, -1)
        self.btn_home = QPushButton(Shlifovanie)
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

        self.pushButton = QPushButton(Shlifovanie)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setStyleSheet(u"background: rgba(0, 0, 0, 0);")
        icon1 = QIcon()
        icon1.addFile(u":/icons/logo_cut.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton.setIcon(icon1)
        self.pushButton.setIconSize(QSize(50, 50))

        self.horizontalLayout.addWidget(self.pushButton, 0, Qt.AlignmentFlag.AlignRight)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.label_title_2 = QLabel(Shlifovanie)
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

        self.label = QLabel(Shlifovanie)
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

        self.widget = QWidget(Shlifovanie)
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
        self.btn_start_obrabotki = QPushButton(self.widget)
        self.btn_start_obrabotki.setObjectName(u"btn_start_obrabotki")
        self.btn_start_obrabotki.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_start_obrabotki.setStyleSheet(u"")
        icon2 = QIcon()
        icon2.addFile(u":/tokar/tok_start_no_back.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_start_obrabotki.setIcon(icon2)
        self.btn_start_obrabotki.setIconSize(QSize(90, 40))

        self.gridLayout.addWidget(self.btn_start_obrabotki, 0, 0, 1, 1, Qt.AlignmentFlag.AlignLeft)

        self.btn_shlifovka_poverh = QPushButton(self.widget)
        self.btn_shlifovka_poverh.setObjectName(u"btn_shlifovka_poverh")
        self.btn_shlifovka_poverh.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_shlifovka_poverh.setStyleSheet(u"")
        icon3 = QIcon()
        icon3.addFile(u":/shlifovka/shlifovanie.PNG", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_shlifovka_poverh.setIcon(icon3)
        self.btn_shlifovka_poverh.setIconSize(QSize(90, 40))

        self.gridLayout.addWidget(self.btn_shlifovka_poverh, 0, 1, 1, 1)


        self.verticalLayout_3.addLayout(self.gridLayout)


        self.verticalLayout.addWidget(self.widget, 0, Qt.AlignmentFlag.AlignHCenter)

        self.line = QFrame(Shlifovanie)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout.addWidget(self.line)

        self.btn_clear_table = QPushButton(Shlifovanie)
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
        icon4 = QIcon()
        icon4.addFile(u":/icons/clear.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_clear_table.setIcon(icon4)

        self.verticalLayout.addWidget(self.btn_clear_table, 0, Qt.AlignmentFlag.AlignRight)

        self.table_widget = QTableWidget(Shlifovanie)
        if (self.table_widget.columnCount() < 3):
            self.table_widget.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.table_widget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.table_widget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.table_widget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.table_widget.setObjectName(u"table_widget")
        font3 = QFont()
        font3.setPointSize(10)
        self.table_widget.setFont(font3)
        self.table_widget.setStyleSheet(u"/* \u0421\u0430\u043c \u0432\u0438\u0434\u0436\u0435\u0442 \u2014 \u043f\u0440\u043e\u0437\u0440\u0430\u0447\u043d\u044b\u0439 \u0444\u043e\u043d */\n"
"* {\n"
" background: rgba(255, 255, 255, 0);\n"
"}\n"
"QTableWidget {\n"
"    background: transparent;\n"
"    border: none;\n"
"    color: #ffffff;\n"
"    gridline-color: rgba(255, 255, 255, 0.15);  /* \u2190 \u044d\u0442\u043e \u0440\u0438\u0441\u0443\u0435\u0442 \u0441\u0435\u0442\u043a\u0443 */\n"
"    selection-background-color: rgba(255, 255, 255, 0.25);\n"
"    selection-color: #ffffff;\n"
"}\n"
"\n"
"QTableWidget::item {\n"
"    background: transparent;\n"
"    color: #ffffff;\n"
"    border: none;\n"
"	padding: 4 6\n"
"    /* padding \u0438 border \u0423\u0411\u0420\u0410\u041b\u0418 \u2014 \u043e\u043d\u0438 \u043b\u043e\u043c\u0430\u044e\u0442 resizeRowsToContents */\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"/* \u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043a\u0438 \u2014 \u0415\u0414\u0418\u041d\u0421\u0422\u0412\u0415\u041d\u041d\u041e\u0415 \u043c\u0435"
                        "\u0441\u0442\u043e \u0441 \u0444\u043e\u043d\u043e\u043c */\n"
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
"    border-right: 1px solid rgba(255, 255, 255, 0.1);\n"
"    border-bottom: 1px solid rgba(255, 255, 255, 0.2);\n"
"}\n"
"\n"
"/* \u0421"
                        "\u043a\u0440\u043e\u043b\u043b\u0431\u0430\u0440\u044b \u2014 \u043c\u0438\u043d\u0438\u043c\u0430\u043b\u044c\u043d\u043e, \u0447\u0442\u043e\u0431\u044b \u043d\u0435 \u043c\u0435\u0448\u0430\u043b\u0438 */\n"
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
"    background: rgba(255, 255"
                        ", 255, 0.3);\n"
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
"	min-height: 30px;\n"
"	min-width: 30px;\n"
"\n"
"}\n"
"QPushButton:hover {\n"
"	image: url(:/icons/trash_grey.png);\n"
"	cursor: pointer;\n"
"}")
        self.table_widget.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.table_widget.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.table_widget.setAutoScroll(False)
        self.table_widget.setShowGrid(True)
        self.table_widget.setColumnCount(3)
        self.table_widget.horizontalHeader().setVisible(True)
        self.table_widget.verticalHeader().setMinimumSectionSize(0)
        self.table_widget.verticalHeader().setDefaultSectionSize(0)

        self.verticalLayout.addWidget(self.table_widget)

        self.btn_save_and_export = QPushButton(Shlifovanie)
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
        icon5 = QIcon()
        icon5.addFile(u":/icons/export.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_save_and_export.setIcon(icon5)
        self.btn_save_and_export.setIconSize(QSize(20, 20))

        self.verticalLayout.addWidget(self.btn_save_and_export, 0, Qt.AlignmentFlag.AlignHCenter)


        self.retranslateUi(Shlifovanie)

        QMetaObject.connectSlotsByName(Shlifovanie)
    # setupUi

    def retranslateUi(self, Shlifovanie):
        Shlifovanie.setWindowTitle(QCoreApplication.translate("Shlifovanie", u"Form", None))
        self.btn_home.setText(QCoreApplication.translate("Shlifovanie", u"  \u0414\u041e\u041c\u041e\u0419", None))
#if QT_CONFIG(shortcut)
        self.btn_home.setShortcut(QCoreApplication.translate("Shlifovanie", u"Esc", None))
#endif // QT_CONFIG(shortcut)
        self.pushButton.setText("")
        self.label_title_2.setText(QCoreApplication.translate("Shlifovanie", u"\u0428\u043b\u0438\u0444\u043e\u0432\u0430\u043b\u044c\u043d\u0430\u044f \u043e\u043f\u0435\u0440\u0430\u0446\u0438\u044f", None))
        self.label.setText(QCoreApplication.translate("Shlifovanie", u"\u041e\u043f\u0435\u0440\u0430\u0446\u0438\u0438 \u043e\u0431\u0440\u0430\u0431\u043e\u0442\u043a\u0438:", None))
        self.btn_start_obrabotki.setText(QCoreApplication.translate("Shlifovanie", u"    \u0423\u0441\u0442\u0430\u043d\u043e\u0432\u043a\u0430 \u0434\u0435\u0442\u0430\u043b\u0438", None))
        self.btn_shlifovka_poverh.setText(QCoreApplication.translate("Shlifovanie", u"\u0428\u043b\u0438\u0444\u043e\u0432\u0430\u043d\u0438\u0435 \u043f\u043e\u0432\u0435\u0440\u0445\u043d\u043e\u0441\u0442\u0438", None))
        self.btn_clear_table.setText(QCoreApplication.translate("Shlifovanie", u"\u041e\u0447\u0438\u0441\u0442\u0438\u0442\u044c \u0442\u0430\u0431\u043b\u0438\u0446\u0443", None))
        ___qtablewidgetitem = self.table_widget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Shlifovanie", u"\u0418\u043d\u0441\u0442\u0440\u0443\u043c\u0435\u043d\u0442", None))
        ___qtablewidgetitem1 = self.table_widget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Shlifovanie", u"\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 [\u041c\u043e\u0436\u043d\u043e \u0438\u0437\u043c\u0435\u043d\u044f\u0442\u044c]", None))
        self.btn_save_and_export.setText(QCoreApplication.translate("Shlifovanie", u"  \u041f\u0435\u0440\u0435\u043d\u0435\u0441\u0442\u0438 \u043f\u0435\u0440\u0435\u0445\u043e\u0434\u044b \u0432 \u0422\u0435\u0445\u043d\u043e\u041f\u0440\u043e", None))
    # retranslateUi

