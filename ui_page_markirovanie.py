# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_page_markirovanie.ui'
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
    QHeaderView, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)
import res_rc

class Ui_PageMarkirovanie(object):
    def setupUi(self, PageMarkirovanie):
        if not PageMarkirovanie.objectName():
            PageMarkirovanie.setObjectName(u"PageMarkirovanie")
        PageMarkirovanie.resize(1000, 679)
        PageMarkirovanie.setStyleSheet(u"color: white;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0, stop:0 rgba(20, 40, 80, 255), stop:1 rgba(39, 73, 109, 255));\n"
"")
        self.verticalLayout = QVBoxLayout(PageMarkirovanie)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.btn_home = QPushButton(PageMarkirovanie)
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

        self.verticalLayout.addWidget(self.btn_home, 0, Qt.AlignmentFlag.AlignLeft)

        self.label_5 = QLabel(PageMarkirovanie)
        self.label_5.setObjectName(u"label_5")
        font1 = QFont()
        font1.setWeight(QFont.DemiBold)
        self.label_5.setFont(font1)
        self.label_5.setStyleSheet(u"background-color: none;\n"
"color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(12, 123, 147, 255), stop:1 rgba(0, 168, 204, 255));\n"
"font-size: 28px;\n"
"font-weight: 600;\n"
"border: none;\n"
"width: 300px;\n"
"\n"
"")

        self.verticalLayout.addWidget(self.label_5, 0, Qt.AlignmentFlag.AlignHCenter)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, -1, -1, 20)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.widget = QWidget(PageMarkirovanie)
        self.widget.setObjectName(u"widget")
        self.widget.setStyleSheet(u"background: none;")
        self.verticalLayout_3 = QVBoxLayout(self.widget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        font2 = QFont()
        font2.setFamilies([u"Segoe UI Light"])
        font2.setPointSize(10)
        self.label.setFont(font2)
        self.label.setStyleSheet(u"QLabel {\n"
"	background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(12, 123, 147, 255), stop:1 rgba(0, 168, 204, 255));\n"
"	padding-left: 2px;	\n"
"	color: rgb(24, 45, 76)\n"
"}\n"
"")

        self.verticalLayout_3.addWidget(self.label)

        self.groupBox = QGroupBox(self.widget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setStyleSheet(u"QGroupBox {\n"
"	border: none;\n"
"	background: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0, stop:0 rgba(39, 72, 109, 129), stop:1 rgba(21, 41, 81, 129));\n"
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
"	background: q"
                        "radialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(12, 123, 147, 177), stop:1 rgba(39, 73, 109, 255));\n"
"	color: rgb(0, 168, 204);\n"
"}")
        self.horizontalLayout = QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, 9, -1, -1)
        self.btn_panch = QPushButton(self.groupBox)
        self.btn_panch.setObjectName(u"btn_panch")
        self.btn_panch.setStyleSheet(u"")
        self.btn_panch.setCheckable(True)
        self.btn_panch.setChecked(True)
        self.btn_panch.setAutoExclusive(True)

        self.horizontalLayout.addWidget(self.btn_panch)

        self.btn_marker = QPushButton(self.groupBox)
        self.btn_marker.setObjectName(u"btn_marker")
        self.btn_marker.setStyleSheet(u"")
        self.btn_marker.setCheckable(True)
        self.btn_marker.setAutoExclusive(True)

        self.horizontalLayout.addWidget(self.btn_marker)


        self.verticalLayout_3.addWidget(self.groupBox)

        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font2)
        self.label_2.setStyleSheet(u"QLabel {\n"
"	background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(12, 123, 147, 255), stop:1 rgba(0, 168, 204, 255));\n"
"	padding-left: 2px;	\n"
"	color: rgb(24, 45, 76)\n"
"}\n"
"")

        self.verticalLayout_3.addWidget(self.label_2)

        self.groupBox_2 = QGroupBox(self.widget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setStyleSheet(u"QGroupBox {\n"
"	border: none;\n"
"	background: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0, stop:0 rgba(39, 72, 109, 129), stop:1 rgba(21, 41, 81, 129));\n"
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
"	background: q"
                        "radialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(12, 123, 147, 177), stop:1 rgba(39, 73, 109, 255));\n"
"	color: rgb(0, 168, 204);\n"
"}")
        self.horizontalLayout_2 = QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, 9, -1, -1)
        self.btn_sborka = QPushButton(self.groupBox_2)
        self.btn_sborka.setObjectName(u"btn_sborka")
        self.btn_sborka.setStyleSheet(u"")
        self.btn_sborka.setCheckable(True)
        self.btn_sborka.setChecked(True)
        self.btn_sborka.setAutoExclusive(True)

        self.horizontalLayout_2.addWidget(self.btn_sborka)

        self.btn_detail = QPushButton(self.groupBox_2)
        self.btn_detail.setObjectName(u"btn_detail")
        self.btn_detail.setStyleSheet(u"")
        self.btn_detail.setCheckable(True)
        self.btn_detail.setAutoExclusive(True)

        self.horizontalLayout_2.addWidget(self.btn_detail)


        self.verticalLayout_3.addWidget(self.groupBox_2)

        self.label_6 = QLabel(self.widget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font2)
        self.label_6.setStyleSheet(u"QLabel {\n"
"	background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(12, 123, 147, 255), stop:1 rgba(0, 168, 204, 255));\n"
"	padding-left: 2px;	\n"
"	color: rgb(24, 45, 76)\n"
"}\n"
"")

        self.verticalLayout_3.addWidget(self.label_6)

        self.widget_2 = QWidget(self.widget)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setStyleSheet(u"QWidget {\n"
"	background: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0, stop:0 rgba(39, 72, 109, 129), stop:1 rgba(21, 41, 81, 129));\n"
"}")
        self.verticalLayout_2 = QVBoxLayout(self.widget_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(-1, -1, -1, 0)
        self.label_4 = QLabel(self.widget_2)
        self.label_4.setObjectName(u"label_4")
        font3 = QFont()
        font3.setPointSize(10)
        self.label_4.setFont(font3)
        self.label_4.setStyleSheet(u"background: none;\n"
"\n"
"")

        self.horizontalLayout_4.addWidget(self.label_4)

        self.doubleSpinBox_nom_diameter = QDoubleSpinBox(self.widget_2)
        self.doubleSpinBox_nom_diameter.setObjectName(u"doubleSpinBox_nom_diameter")
        self.doubleSpinBox_nom_diameter.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.doubleSpinBox_nom_diameter.setStyleSheet(u"QDoubleSpinBox {\n"
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
        self.doubleSpinBox_nom_diameter.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.doubleSpinBox_nom_diameter.setDecimals(0)
        self.doubleSpinBox_nom_diameter.setMinimum(1.000000000000000)
        self.doubleSpinBox_nom_diameter.setMaximum(1000.000000000000000)

        self.horizontalLayout_4.addWidget(self.doubleSpinBox_nom_diameter)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.label_3 = QLabel(self.widget_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font3)
        self.label_3.setStyleSheet(u"background: none;\n"
"")

        self.verticalLayout_2.addWidget(self.label_3, 0, Qt.AlignmentFlag.AlignLeft)

        self.lineEdit = QLineEdit(self.widget_2)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(200, 0))
        self.lineEdit.setStyleSheet(u"padding: 5, 5, 5, 5;\n"
"border: none;\n"
"border-bottom: 1px solid white;\n"
"background: rgba(255, 255, 255, 0);\n"
"transition: color 0.3s ease;\n"
"transition: border-bottom 0.4s ease;\n"
"color: rgb(204, 204, 204);\n"
"font-size: 10pt;")

        self.verticalLayout_2.addWidget(self.lineEdit)


        self.verticalLayout_3.addWidget(self.widget_2)

        self.btn_save_result = QPushButton(self.widget)
        self.btn_save_result.setObjectName(u"btn_save_result")
        font4 = QFont()
        font4.setBold(True)
        self.btn_save_result.setFont(font4)
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

        self.verticalLayout_3.addWidget(self.btn_save_result, 0, Qt.AlignmentFlag.AlignHCenter)


        self.horizontalLayout_3.addWidget(self.widget)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.table_widget = QTableWidget(PageMarkirovanie)
        if (self.table_widget.columnCount() < 2):
            self.table_widget.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.table_widget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.table_widget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        self.table_widget.setObjectName(u"table_widget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.table_widget.sizePolicy().hasHeightForWidth())
        self.table_widget.setSizePolicy(sizePolicy1)
        self.table_widget.setFont(font3)
        self.table_widget.setStyleSheet(u"/* \u0421\u0430\u043c \u0432\u0438\u0434\u0436\u0435\u0442 \u2014 \u043f\u0440\u043e\u0437\u0440\u0430\u0447\u043d\u044b\u0439 \u0444\u043e\u043d */\n"
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
"QTableWidget::item:hover {\n"
"    background: rgba(255, 255, 255, 0.08);\n"
"}\n"
"\n"
"QTableWidget::item:selected {\n"
"    background: r"
                        "gba(255, 255, 255, 0.2);\n"
"    color: #ffffff;\n"
"}\n"
"\n"
"/* \u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043a\u0438 \u2014 \u0415\u0414\u0418\u041d\u0421\u0422\u0412\u0415\u041d\u041d\u041e\u0415 \u043c\u0435\u0441\u0442\u043e \u0441 \u0444\u043e\u043d\u043e\u043c */\n"
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
"QHeaderView::section:hover {\n"
"    background-color: #3a3a3a;\n"
"}\n"
"\n"
"/* \u0423\u0433\u043b\u043e\u0432\u0430\u044f \u043a\u043d\u043e\u043f\u043a\u0430 (\u043f\u0435\u0440\u0435\u0441\u0435\u0447\u0435\u043d\u0438\u0435 \u0437\u0430\u0433\u043e\u043b\u043e\u0432\u043a\u043e\u0432) */\n"
"QTableCornerButton::section {\n"
"    background-col"
                        "or:  rgb(21, 69, 140);\n"
"    border: none;\n"
"    border-right: 1px solid rgba(255, 255, 255, 0.1);\n"
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
""
                        "QTableWidget QScrollBar:horizontal {\n"
"    background: transparent;\n"
"    height: 8px;\n"
"}\n"
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
"	border: 1px solid white;\n"
"	margin-top: 25px;\n"
"	margin-bottom: 25px;\n"
"	margin-left: 20px;\n"
"	margin-right: 20px;\n"
"	border-radius: 8px;\n"
"}\n"
"QPushButton:hover {\n"
"	border: 2px solid white;\n"
"	background: rgb(15, 65, 159)\n"
"}")
        self.table_widget.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.table_widget.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.table_widget.setAutoScroll(False)
        self.table_widget.setRowCount(0)
        self.table_widget.setColumnCount(2)
        self.table_widget.verticalHeader().setVisible(False)
        self.table_widget.verticalHeader().setMinimumSectionSize(90)
        self.table_widget.verticalHeader().setDefaultSectionSize(100)

        self.verticalLayout.addWidget(self.table_widget)

        self.pushButton_save = QPushButton(PageMarkirovanie)
        self.pushButton_save.setObjectName(u"pushButton_save")
        self.pushButton_save.setMinimumSize(QSize(0, 0))
        self.pushButton_save.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_save.setStyleSheet(u"QPushButton {\n"
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
        icon2 = QIcon()
        icon2.addFile(u":/icons/export.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_save.setIcon(icon2)
        self.pushButton_save.setIconSize(QSize(20, 20))

        self.verticalLayout.addWidget(self.pushButton_save, 0, Qt.AlignmentFlag.AlignHCenter)

        self.label_error = QLabel(PageMarkirovanie)
        self.label_error.setObjectName(u"label_error")
        self.label_error.setStyleSheet(u"background: none;\n"
"color: rgb(254, 95, 32)")

        self.verticalLayout.addWidget(self.label_error)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.retranslateUi(PageMarkirovanie)

        QMetaObject.connectSlotsByName(PageMarkirovanie)
    # setupUi

    def retranslateUi(self, PageMarkirovanie):
        PageMarkirovanie.setWindowTitle(QCoreApplication.translate("PageMarkirovanie", u"Form", None))
        self.btn_home.setText(QCoreApplication.translate("PageMarkirovanie", u" \u041d\u0410\u0417\u0410\u0414", None))
        self.label_5.setText(QCoreApplication.translate("PageMarkirovanie", u"\u041c\u0430\u0440\u043a\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u0435", None))
        self.label.setText(QCoreApplication.translate("PageMarkirovanie", u"\u041c\u0435\u0442\u043e\u0434 \u043d\u0430\u043d\u0435\u0441\u0435\u043d\u0438\u044f \u043c\u0430\u0440\u043a\u0438\u0440\u043e\u0432\u043a\u0438:", None))
        self.groupBox.setTitle("")
        self.btn_panch.setText(QCoreApplication.translate("PageMarkirovanie", u"\u0423\u0434\u0430\u0440\u043d\u044b\u043c \u0441\u043f\u043e\u0441\u043e\u0431\u043e\u043c", None))
        self.btn_marker.setText(QCoreApplication.translate("PageMarkirovanie", u"\u041c\u0430\u0440\u043a\u0435\u0440\u043e\u043c", None))
        self.label_2.setText(QCoreApplication.translate("PageMarkirovanie", u"\u041e\u0431\u044a\u0435\u043a\u0442 \u043c\u0430\u0440\u043a\u0438\u0440\u043e\u0432\u043a\u0438:", None))
        self.groupBox_2.setTitle("")
        self.btn_sborka.setText(QCoreApplication.translate("PageMarkirovanie", u"\u0421\u0431\u043e\u0440\u043e\u0447\u043d\u0430\u044f \u0435\u0434\u0438\u043d\u0438\u0446\u0430", None))
        self.btn_detail.setText(QCoreApplication.translate("PageMarkirovanie", u"\u0414\u0435\u0442\u0430\u043b\u044c", None))
        self.label_6.setText(QCoreApplication.translate("PageMarkirovanie", u"\u041f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u044b \u043c\u0430\u0440\u043a\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u044f:", None))
        self.label_4.setText(QCoreApplication.translate("PageMarkirovanie", u"\u041f\u0443\u043d\u043a\u0442 \u0422\u0422 \u043c\u0430\u0440\u043a\u0438\u0440\u043e\u0432\u043a\u0438 \u0432 \u0447\u0435\u0440\u0442\u0435\u0436\u0435:", None))
        self.doubleSpinBox_nom_diameter.setPrefix(QCoreApplication.translate("PageMarkirovanie", u"\u2116 ", None))
        self.doubleSpinBox_nom_diameter.setSuffix("")
        self.label_3.setText(QCoreApplication.translate("PageMarkirovanie", u"\u041e\u0431\u043e\u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0435 \u0447\u0435\u0440\u0442\u0435\u0436\u0430:", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("PageMarkirovanie", u"\u041d\u043e\u043c\u0435\u0440 \u0447\u0435\u0440\u0442\u0435\u0436\u0430...", None))
        self.btn_save_result.setText(QCoreApplication.translate("PageMarkirovanie", u" \u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u044f", None))
#if QT_CONFIG(shortcut)
        self.btn_save_result.setShortcut(QCoreApplication.translate("PageMarkirovanie", u"Ctrl+R", None))
#endif // QT_CONFIG(shortcut)
        ___qtablewidgetitem = self.table_widget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("PageMarkirovanie", u"\u0418\u043d\u0441\u0442\u0440\u0443\u043c\u0435\u043d\u0442", None))
        ___qtablewidgetitem1 = self.table_widget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("PageMarkirovanie", u"\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 [\u041c\u043e\u0436\u043d\u043e \u0438\u0437\u043c\u0435\u043d\u044f\u0442\u044c]", None))
        self.pushButton_save.setText(QCoreApplication.translate("PageMarkirovanie", u" \u041f\u0435\u0440\u0435\u043d\u0435\u0441\u0442\u0438 \u0432 \u0422\u0435\u0445\u043d\u043e\u041f\u0440\u043e", None))
#if QT_CONFIG(shortcut)
        self.pushButton_save.setShortcut(QCoreApplication.translate("PageMarkirovanie", u"Ctrl+R", None))
#endif // QT_CONFIG(shortcut)
        self.label_error.setText("")
    # retranslateUi

