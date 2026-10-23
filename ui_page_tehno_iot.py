# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_page_tehno_iot.ui'
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
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QCheckBox, QDoubleSpinBox,
    QFrame, QHBoxLayout, QHeaderView, QLabel,
    QPushButton, QSizePolicy, QSpacerItem, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_PageTehnoIot(object):
    def setupUi(self, PageTehnoIot):
        if not PageTehnoIot.objectName():
            PageTehnoIot.setObjectName(u"PageTehnoIot")
        PageTehnoIot.resize(1000, 700)
        PageTehnoIot.setMinimumSize(QSize(1000, 700))
        PageTehnoIot.setStyleSheet(u"color: white;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(0, 57, 95), stop:1 rgb(0, 83, 122))")
        self.verticalLayout = QVBoxLayout(PageTehnoIot)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(5, 0, 5, -1)
        self.btn_home_1 = QPushButton(PageTehnoIot)
        self.btn_home_1.setObjectName(u"btn_home_1")
        self.btn_home_1.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_home_1.setStyleSheet(u"QPushButton {\n"
"	border: 1px solid;\n"
"	border-color: white;\n"
"	border-radius: 10px;\n"
"	height: 20px;\n"
"	width: 100px;\n"
"	background-color: none;\n"
"	padding: 2 5 5 2;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(0, 111, 171)\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: rgb(0, 53, 93)\n"
"}")

        self.horizontalLayout_6.addWidget(self.btn_home_1, 0, Qt.AlignmentFlag.AlignLeft)

        self.btn_update_page = QPushButton(PageTehnoIot)
        self.btn_update_page.setObjectName(u"btn_update_page")
        self.btn_update_page.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_update_page.setStyleSheet(u"QPushButton {\n"
"	border: 1px solid;\n"
"	border-color: white;\n"
"	border-radius: 10px;\n"
"	height: 20px;\n"
"	background-color: none;\n"
"	padding: 2 10 5 10;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(0, 111, 171)\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: rgb(0, 53, 93)\n"
"}")

        self.horizontalLayout_6.addWidget(self.btn_update_page, 0, Qt.AlignmentFlag.AlignRight)


        self.verticalLayout.addLayout(self.horizontalLayout_6)

        self.verticalWidget = QWidget(PageTehnoIot)
        self.verticalWidget.setObjectName(u"verticalWidget")
        self.verticalWidget.setStyleSheet(u"height: 100px;\n"
"background: none;")
        self.verticalLayout_3 = QVBoxLayout(self.verticalWidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(-1, -1, -1, 1)
        self.show_text = QLabel(self.verticalWidget)
        self.show_text.setObjectName(u"show_text")
        font = QFont()
        font.setPointSize(11)
        self.show_text.setFont(font)
        self.show_text.setStyleSheet(u"background: none;")

        self.verticalLayout_3.addWidget(self.show_text, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignBottom)

        self.show_text_2str = QLabel(self.verticalWidget)
        self.show_text_2str.setObjectName(u"show_text_2str")
        self.show_text_2str.setFont(font)
        self.show_text_2str.setStyleSheet(u"background: none;")

        self.verticalLayout_3.addWidget(self.show_text_2str, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)


        self.verticalLayout.addWidget(self.verticalWidget)

        self.main = QWidget(PageTehnoIot)
        self.main.setObjectName(u"main")
        self.main.setStyleSheet(u"background: none;")
        self.verticalLayout_2 = QVBoxLayout(self.main)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_2 = QLabel(self.main)
        self.label_2.setObjectName(u"label_2")
        font1 = QFont()
        font1.setPointSize(11)
        font1.setBold(True)
        self.label_2.setFont(font1)
        self.label_2.setStyleSheet(u"background-color: none")

        self.verticalLayout_2.addWidget(self.label_2, 0, Qt.AlignmentFlag.AlignHCenter)

        self.label_5 = QLabel(self.main)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setStyleSheet(u"background-color: none")

        self.verticalLayout_2.addWidget(self.label_5, 0, Qt.AlignmentFlag.AlignHCenter)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(20)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, 0, -1, -1)
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)

        self.doubleSpinBox_nom_diameter = QDoubleSpinBox(self.main)
        self.doubleSpinBox_nom_diameter.setObjectName(u"doubleSpinBox_nom_diameter")
        self.doubleSpinBox_nom_diameter.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.doubleSpinBox_nom_diameter.setStyleSheet(u"QDoubleSpinBox {\n"
"	padding: 2 5 2 5;	\n"
"	border: none;\n"
"	border-bottom: 1px solid rgb(255, 147, 14);\n"
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
        self.doubleSpinBox_nom_diameter.setDecimals(3)
        self.doubleSpinBox_nom_diameter.setMinimum(0.000000000000000)
        self.doubleSpinBox_nom_diameter.setMaximum(10000.000000000000000)
        self.doubleSpinBox_nom_diameter.setStepType(QAbstractSpinBox.StepType.DefaultStepType)

        self.horizontalLayout_3.addWidget(self.doubleSpinBox_nom_diameter)

        self.doubleSpinBox_nom_diameter_2 = QDoubleSpinBox(self.main)
        self.doubleSpinBox_nom_diameter_2.setObjectName(u"doubleSpinBox_nom_diameter_2")
        self.doubleSpinBox_nom_diameter_2.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.doubleSpinBox_nom_diameter_2.setStyleSheet(u"QDoubleSpinBox {\n"
"	padding: 2 5 2 5;	\n"
"	border: none;\n"
"	border-bottom: 1px solid rgb(255, 147, 14);\n"
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
        self.doubleSpinBox_nom_diameter_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.doubleSpinBox_nom_diameter_2.setDecimals(3)
        self.doubleSpinBox_nom_diameter_2.setMinimum(0.000000000000000)
        self.doubleSpinBox_nom_diameter_2.setMaximum(10000.000000000000000)
        self.doubleSpinBox_nom_diameter_2.setStepType(QAbstractSpinBox.StepType.DefaultStepType)

        self.horizontalLayout_3.addWidget(self.doubleSpinBox_nom_diameter_2)

        self.button_podbor = QPushButton(self.main)
        self.button_podbor.setObjectName(u"button_podbor")
        self.button_podbor.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.button_podbor.setStyleSheet(u"QPushButton {\n"
"	border: 1px solid;\n"
"	border-color: white;\n"
"	border-radius: 10px;\n"
"	height: 20px;\n"
"	width: 100px;\n"
"	background-color: none;\n"
"	padding: 2 5 2 5\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(0, 111, 171)\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: rgb(0, 53, 93)\n"
"}")

        self.horizontalLayout_3.addWidget(self.button_podbor)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_4)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.line = QFrame(self.main)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_2.addWidget(self.line)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, -1, 0)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.btn_select_all = QPushButton(self.main)
        self.btn_select_all.setObjectName(u"btn_select_all")
        self.btn_select_all.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_select_all.setStyleSheet(u"QPushButton {\n"
"	border: 1px solid;\n"
"	border-color: white;\n"
"	border-radius: 10px;\n"
"	height: 12px;\n"
"	background-color: none;\n"
"	padding: 2 10 5 10;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(0, 111, 171)\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: rgb(0, 53, 93)\n"
"}")

        self.horizontalLayout_2.addWidget(self.btn_select_all, 0, Qt.AlignmentFlag.AlignHCenter)

        self.btn_unsellect_all = QPushButton(self.main)
        self.btn_unsellect_all.setObjectName(u"btn_unsellect_all")
        self.btn_unsellect_all.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_unsellect_all.setStyleSheet(u"QPushButton {\n"
"	border: 1px solid;\n"
"	border-color: white;\n"
"	border-radius: 10px;\n"
"	height: 12px;\n"
"	background-color: none;\n"
"	padding: 2 10 5 10;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(0, 111, 171)\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: rgb(0, 53, 93)\n"
"}")

        self.horizontalLayout_2.addWidget(self.btn_unsellect_all, 0, Qt.AlignmentFlag.AlignHCenter)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, 0, -1, -1)
        self.label = QLabel(self.main)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setFont(font)
        self.label.setStyleSheet(u"background-color: none")

        self.horizontalLayout.addWidget(self.label, 0, Qt.AlignmentFlag.AlignHCenter)

        self.label_3 = QLabel(self.main)
        self.label_3.setObjectName(u"label_3")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(3)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy1)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(u"background-color: none")

        self.horizontalLayout.addWidget(self.label_3, 0, Qt.AlignmentFlag.AlignHCenter)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.tableWidget = QTableWidget(self.main)
        if (self.tableWidget.columnCount() < 3):
            self.tableWidget.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.tableWidget.setObjectName(u"tableWidget")
        font2 = QFont()
        font2.setPointSize(10)
        self.tableWidget.setFont(font2)
        self.tableWidget.viewport().setProperty(u"cursor", QCursor(Qt.CursorShape.ArrowCursor))
        self.tableWidget.setStyleSheet(u"/* \u0421\u0430\u043c \u0432\u0438\u0434\u0436\u0435\u0442 \u2014 \u043f\u0440\u043e\u0437\u0440\u0430\u0447\u043d\u044b\u0439 \u0444\u043e\u043d */\n"
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
"	border-bottom: 1px solid rgba(255, 255, 255, 0.15)\n"
"\n"
"}\n"
"\n"
"QTableWidget::item:hover {\n"
"    background: rgba(255, 255, 255, 0.08);\n"
"}\n"
"\n"
"QTableWidget::item:selected {\n"
"    background: rgba(255, 255, 255, 0.2);\n"
"    color: #ffffff;\n"
"}\n"
""
                        "\n"
"/* \u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043a\u0438 \u2014 \u0415\u0414\u0418\u041d\u0421\u0422\u0412\u0415\u041d\u041d\u041e\u0415 \u043c\u0435\u0441\u0442\u043e \u0441 \u0444\u043e\u043d\u043e\u043c */\n"
"QHeaderView::section {\n"
"    background-color: rgb(21, 69, 140);\n"
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
"    background-color:  rgb(21, 69, 140);\n"
"    border: none;\n"
"    border-right: 1px solid rgba(255, 255, 255, 0.1);\n"
"    border-bottom: 1px solid rgba(255, 255, 255, 0"
                        ".2);\n"
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
"\n"
"QTableWidget QScrollBar::handle:horizontal {\n"
""
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
        self.tableWidget.horizontalHeader().setMinimumSectionSize(250)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(250)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(False)

        self.verticalLayout_2.addWidget(self.tableWidget)

        self.checkBox_del_instrument = QCheckBox(self.main)
        self.checkBox_del_instrument.setObjectName(u"checkBox_del_instrument")
        self.checkBox_del_instrument.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.checkBox_del_instrument.setStyleSheet(u"QCheckBox::indicator {\n"
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

        self.verticalLayout_2.addWidget(self.checkBox_del_instrument, 0, Qt.AlignmentFlag.AlignHCenter)

        self.label_4 = QLabel(self.main)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_2.addWidget(self.label_4, 0, Qt.AlignmentFlag.AlignHCenter)

        self.button_start = QPushButton(self.main)
        self.button_start.setObjectName(u"button_start")
        self.button_start.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.button_start.setStyleSheet(u"QPushButton {\n"
"	border: 1px solid;\n"
"	border-color: white;\n"
"	border-radius: 10px;\n"
"	height: 30px;\n"
"	width: 150px;\n"
"	background-color: none;\n"
"	padding: 2 5 2 5\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(0, 111, 171)\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: rgb(0, 53, 93)\n"
"}")

        self.verticalLayout_2.addWidget(self.button_start, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)


        self.verticalLayout.addWidget(self.main)


        self.retranslateUi(PageTehnoIot)

        QMetaObject.connectSlotsByName(PageTehnoIot)
    # setupUi

    def retranslateUi(self, PageTehnoIot):
        PageTehnoIot.setWindowTitle(QCoreApplication.translate("PageTehnoIot", u"Form", None))
        self.btn_home_1.setText(QCoreApplication.translate("PageTehnoIot", u"\u0414\u043e\u043c\u043e\u0439", None))
        self.btn_update_page.setText(QCoreApplication.translate("PageTehnoIot", u"\u041e\u0431\u043d\u043e\u0432\u0438\u0442\u044c \u0441\u0442\u0440\u0430\u043d\u0438\u0446\u0443", None))
        self.show_text.setText("")
        self.show_text_2str.setText("")
        self.label_2.setText(QCoreApplication.translate("PageTehnoIot", u"\u0417\u0430\u043f\u043e\u043b\u043d\u0435\u043d\u0438\u0435 \u0418\u041e\u0422 \u0438 \u043e\u0431\u043e\u0440\u0443\u0434\u043e\u0432\u0430\u043d\u0438\u044f \u0432 \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0435 \u0422\u0435\u0445\u043d\u043e\u041f\u0440\u043e", None))
        self.label_5.setText(QCoreApplication.translate("PageTehnoIot", u"\u041f\u043e\u0434\u043e\u0431\u0440\u0430\u0442\u044c \u0441\u0442\u0430\u043d\u043a\u0438 \u043f\u043e \u0433\u0430\u0431\u0430\u0440\u0438\u0442\u0430\u043c \u0437\u0430\u0433\u043e\u0442\u043e\u0432\u043a\u0438 \u0443 \u0432\u044b\u0431\u0440\u0430\u043d\u043d\u044b\u0445 \u043e\u043f\u0435\u0440\u0430\u0446\u0438\u0439:", None))
        self.doubleSpinBox_nom_diameter.setPrefix(QCoreApplication.translate("PageTehnoIot", u"\u00d8 ", None))
        self.doubleSpinBox_nom_diameter_2.setPrefix(QCoreApplication.translate("PageTehnoIot", u"L=", None))
        self.button_podbor.setText(QCoreApplication.translate("PageTehnoIot", u"\u041f\u043e\u0434\u043e\u0431\u0440\u0430\u0442\u044c", None))
        self.btn_select_all.setText(QCoreApplication.translate("PageTehnoIot", u"\u0412\u044b\u0434\u0435\u043b\u0438\u0442\u044c \u0432\u0441\u0451", None))
        self.btn_unsellect_all.setText(QCoreApplication.translate("PageTehnoIot", u"\u0423\u0431\u0440\u0430\u0442\u044c \u0432\u0441\u0435 \u0432\u044b\u0434\u0435\u043b\u0435\u043d\u0438\u044f", None))
        self.label.setText(QCoreApplication.translate("PageTehnoIot", u"\u041d\u0430\u0439\u0434\u0435\u043d\u043d\u044b\u0435 \u043e\u043f\u0435\u0440\u0430\u0446\u0438\u0438", None))
        self.label_3.setText(QCoreApplication.translate("PageTehnoIot", u"\u0417\u043d\u0430\u0447\u0435\u043d\u0438\u044f, \u043a\u043e\u0442\u043e\u0440\u044b\u0435 \u0431\u0443\u0434\u0443\u0442 \u0434\u043e\u0431\u0430\u0432\u043b\u0435\u043d\u044b \u043a \u043a\u0430\u0436\u0434\u043e\u0439 \u043e\u043f\u0435\u0440\u0430\u0446\u0438\u0438", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("PageTehnoIot", u"\u041e\u043f\u0435\u0440\u0430\u0446\u0438\u044f", None))
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("PageTehnoIot", u"\u0418\u041e\u0422", None))
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("PageTehnoIot", u"\u041e\u0431\u043e\u0440\u0443\u0434\u043e\u0432\u0430\u043d\u0438\u0435", None))
        self.checkBox_del_instrument.setText(QCoreApplication.translate("PageTehnoIot", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c \u043e\u0431\u043e\u0440\u0443\u0434\u043e\u0432\u0430\u043d\u0438\u0435, \u043a\u043e\u0442\u043e\u0440\u043e\u0435 \u0443\u0436\u0435 \u0434\u043e\u0431\u0430\u0432\u043b\u0435\u043d\u043e \u0432 \u0422\u0435\u0445\u043d\u043e\u041f\u0440\u043e", None))
        self.label_4.setText("")
        self.button_start.setText(QCoreApplication.translate("PageTehnoIot", u"\u0417\u0430\u043f\u0443\u0441\u0442\u0438\u0442\u044c \u0437\u0430\u043f\u043e\u043b\u043d\u0435\u043d\u0438\u0435", None))
    # retranslateUi

