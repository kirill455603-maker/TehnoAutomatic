# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_dialog_slesarnaya.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QDoubleSpinBox,
    QFrame, QGridLayout, QGroupBox, QHBoxLayout,
    QLabel, QListWidget, QListWidgetItem, QPushButton,
    QSizePolicy, QSpacerItem, QSpinBox, QStackedWidget,
    QVBoxLayout, QWidget)

class Ui_DialogSlesarnaya(object):
    def setupUi(self, DialogSlesarnaya):
        if not DialogSlesarnaya.objectName():
            DialogSlesarnaya.setObjectName(u"DialogSlesarnaya")
        DialogSlesarnaya.resize(713, 630)
        DialogSlesarnaya.setMaximumSize(QSize(16777215, 630))
        DialogSlesarnaya.setWindowOpacity(0.950000000000000)
        DialogSlesarnaya.setStyleSheet(u"color: white;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(0, 57, 95), stop:1 rgb(0, 83, 122))")
        self.verticalLayout = QVBoxLayout(DialogSlesarnaya)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_8 = QLabel(DialogSlesarnaya)
        self.label_8.setObjectName(u"label_8")
        font = QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet(u"background: none;\n"
"")

        self.verticalLayout.addWidget(self.label_8, 0, Qt.AlignmentFlag.AlignHCenter)

        self.groupBox = QGroupBox(DialogSlesarnaya)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setStyleSheet(u"border: none;\n"
"background: transparent;")
        self.groupBox.setCheckable(False)
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.btn_meh = QPushButton(self.groupBox)
        self.btn_meh.setObjectName(u"btn_meh")
        self.btn_meh.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background: rgba(154, 154, 154, 60);\n"
"	padding: 5 5 5 5;\n"
"	height: 20px;\n"
"	border-radius:  0;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background: rgba(11, 31, 139,30);\n"
"	border-bottom: 1px solid rgba(255, 255, 255, 20);\n"
"	\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"	background: rgba(11, 31, 139,90);\n"
"	border-bottom: 1px solid white;\n"
"	\n"
"}\n"
"")
        self.btn_meh.setCheckable(True)
        self.btn_meh.setAutoExclusive(True)

        self.gridLayout.addWidget(self.btn_meh, 0, 3, 1, 1)

        self.btn_svarka = QPushButton(self.groupBox)
        self.btn_svarka.setObjectName(u"btn_svarka")
        self.btn_svarka.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background: rgba(154, 154, 154, 60);\n"
"	padding: 5 5 5 5;\n"
"	height: 20px;\n"
"	border-radius:  0;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background: rgba(11, 31, 139,30);\n"
"	border-bottom: 1px solid rgba(255, 255, 255, 20);\n"
"	\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"	background: rgba(11, 31, 139,90);\n"
"	border-bottom: 1px solid white;\n"
"	\n"
"}\n"
"")
        self.btn_svarka.setCheckable(True)
        self.btn_svarka.setAutoExclusive(True)

        self.gridLayout.addWidget(self.btn_svarka, 0, 1, 1, 1)

        self.btn_sborka = QPushButton(self.groupBox)
        self.btn_sborka.setObjectName(u"btn_sborka")
        self.btn_sborka.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background: rgba(154, 154, 154, 60);\n"
"	padding: 5 5 5 5;\n"
"	height: 20px;\n"
"	border-radius:  0;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background: rgba(11, 31, 139,30);\n"
"	border-bottom: 1px solid rgba(255, 255, 255, 20);\n"
"	\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"	background: rgba(11, 31, 139,90);\n"
"	border-bottom: 1px solid white;\n"
"	\n"
"}\n"
"")
        self.btn_sborka.setCheckable(True)
        self.btn_sborka.setChecked(True)
        self.btn_sborka.setAutoExclusive(True)

        self.gridLayout.addWidget(self.btn_sborka, 0, 0, 1, 1)


        self.verticalLayout.addWidget(self.groupBox)

        self.stackedWidget = QStackedWidget(DialogSlesarnaya)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page_sborka = QWidget()
        self.page_sborka.setObjectName(u"page_sborka")
        self.verticalLayout_2 = QVBoxLayout(self.page_sborka)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.listWidget_sborka = QListWidget(self.page_sborka)
        QListWidgetItem(self.listWidget_sborka)
        self.listWidget_sborka.setObjectName(u"listWidget_sborka")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listWidget_sborka.sizePolicy().hasHeightForWidth())
        self.listWidget_sborka.setSizePolicy(sizePolicy)
        self.listWidget_sborka.setMinimumSize(QSize(200, 0))
        font1 = QFont()
        font1.setPointSize(10)
        font1.setBold(True)
        self.listWidget_sborka.setFont(font1)
        self.listWidget_sborka.setStyleSheet(u"\n"
"/* \u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500 \u0421\u0430\u043c \u0441\u043f\u0438\u0441\u043e\u043a \u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500 */\n"
"QListWidget {\n"
"    background: transparent;\n"
"    font-size: 10pt;\n"
"	border: none;\n"
"    color: #E8EAF0;\n"
"}\n"
"\n"
"/* \u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500 \u042d\u043b\u0435\u043c\u0435\u043d\u0442\u044b \u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500 */\n"
"QListWidget::item {\n"
"    background: transparent;\n"
"    border: none;\n"
"    border-radius: 12px;\n"
"    margin: 2px 6px;\n"
"    color: rgba(255, 255, 255, 0.72);\n"
"}\n"
"\n"
"QListWidget::item:hover {\n"
"    background: rgba(255, 255, 255, 0.07);\n"
"    color: #FFFFFF;\n"
"}\n"
"\n"
"QListWidget::item:selected {\n"
"    background: qlineargradient(x1:0, y1:0, x2:1, y2:0,\n"
"        stop:0 rgba(94, 129, 255, 0.32),\n"
"        stop:"
                        "1 rgba(94, 129, 255, 0.08));\n"
"    color: #FFFFFF;\n"
"}\n"
"\n"
"QListWidget::item:selected:hover {\n"
"    background: qlineargradient(x1:0, y1:0, x2:1, y2:0,\n"
"        stop:0 rgba(94, 129, 255, 0.42),\n"
"        stop:1 rgba(94, 129, 255, 0.14));\n"
"}\n"
"\n"
"/* \u0443\u0431\u0438\u0440\u0430\u0435\u043c \u0440\u0430\u043c\u043a\u0443/\u043f\u0443\u043d\u043a\u0442\u0438\u0440 \u043f\u0440\u0438 \u0444\u043e\u043a\u0443\u0441\u0435 */\n"
"QListWidget:focus,\n"
"QListWidget::item:focus {\n"
"    outline: none;\n"
"    border: none;\n"
"}\n"
"\n"
"/* \u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500 \u0412\u0435\u0440\u0442\u0438\u043a\u0430\u043b\u044c\u043d\u044b\u0439 \u0441\u043a\u0440\u043e\u043b\u043b\u0431\u0430\u0440 \u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500 */\n"
"QScrollBar:vertical {\n"
"    background: transparent;\n"
"    width: 10px;\n"
"    margin: 4px 2px;\n"
"    border-radius: 5px;\n"
"}\n"
"QScrollBar::handle:vertical {"
                        "\n"
"    background: rgba(255, 255, 255, 0.18);\n"
"    min-height: 30px;\n"
"    border-radius: 5px;\n"
"}\n"
"QScrollBar::handle:vertical:hover {\n"
"    background: rgba(255, 255, 255, 0.32);\n"
"}\n"
"QScrollBar::add-line:vertical,\n"
"QScrollBar::sub-line:vertical { height: 0; }\n"
"QScrollBar::add-page:vertical,\n"
"QScrollBar::sub-page:vertical { background: transparent; }\n"
"\n"
"/* \u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500 \u0413\u043e\u0440\u0438\u0437\u043e\u043d\u0442\u0430\u043b\u044c\u043d\u044b\u0439 \u0441\u043a\u0440\u043e\u043b\u043b\u0431\u0430\u0440 \u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500 */\n"
"QScrollBar:horizontal {\n"
"    background: transparent;\n"
"    height: 10px;\n"
"    margin: 2px 4px;\n"
"    border-radius: 5px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background: rgba(255, 255, 255, 0.18);\n"
"    min-width: 30px;\n"
"    border-radius: 5px;\n"
"}\n"
"QScrollBar::handle:horizontal:hover {\n"
""
                        "    background: rgba(255, 255, 255, 0.32);\n"
"}\n"
"QScrollBar::add-line:horizontal,\n"
"QScrollBar::sub-line:horizontal { width: 0; }\n"
"QScrollBar::add-page:horizontal,\n"
"QScrollBar::sub-page:horizontal { background: transparent; }\n"
"")
        self.listWidget_sborka.setTabKeyNavigation(False)
        self.listWidget_sborka.setAlternatingRowColors(False)

        self.verticalLayout_2.addWidget(self.listWidget_sborka)

        self.line_2 = QFrame(self.page_sborka)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_2.addWidget(self.line_2)

        self.text_sborka_1 = QWidget(self.page_sborka)
        self.text_sborka_1.setObjectName(u"text_sborka_1")
        self.verticalLayout_14 = QVBoxLayout(self.text_sborka_1)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(-1, 0, -1, 1)
        self.label_22 = QLabel(self.text_sborka_1)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setFont(font1)
        self.label_22.setStyleSheet(u"background: none;")

        self.verticalLayout_14.addWidget(self.label_22, 0, Qt.AlignmentFlag.AlignHCenter)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, 0, -1, -1)
        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_10)

        self.comboBox_position = QComboBox(self.text_sborka_1)
        self.comboBox_position.addItem("")
        self.comboBox_position.addItem("")
        self.comboBox_position.setObjectName(u"comboBox_position")
        font2 = QFont()
        font2.setPointSize(10)
        self.comboBox_position.setFont(font2)
        self.comboBox_position.setStyleSheet(u"QComboBox {\n"
"	padding: 5, 5, 5, 5;\n"
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

        self.horizontalLayout.addWidget(self.comboBox_position, 0, Qt.AlignmentFlag.AlignHCenter)

        self.label_6 = QLabel(self.text_sborka_1)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font2)
        self.label_6.setStyleSheet(u"background: none;")

        self.horizontalLayout.addWidget(self.label_6, 0, Qt.AlignmentFlag.AlignHCenter)

        self.comboBox_detail = QComboBox(self.text_sborka_1)
        self.comboBox_detail.setObjectName(u"comboBox_detail")
        self.comboBox_detail.setFont(font2)
        self.comboBox_detail.setStyleSheet(u"QComboBox {\n"
"	padding: 5, 5, 5, 5;\n"
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

        self.horizontalLayout.addWidget(self.comboBox_detail, 0, Qt.AlignmentFlag.AlignHCenter)

        self.label_11 = QLabel(self.text_sborka_1)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font2)
        self.label_11.setStyleSheet(u"background: none;")

        self.horizontalLayout.addWidget(self.label_11, 0, Qt.AlignmentFlag.AlignHCenter)

        self.spinBox_pos = QSpinBox(self.text_sborka_1)
        self.spinBox_pos.setObjectName(u"spinBox_pos")
        font3 = QFont()
        font3.setPointSize(11)
        self.spinBox_pos.setFont(font3)
        self.spinBox_pos.setStyleSheet(u"QSpinBox {\n"
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
"QSpinBox:disabled {\n"
"	color: rgb(120, 106, 107);\n"
"	background: rgba(255, 255, 255, 20);\n"
"}\n"
"\n"
"QSpinBox:hover {\n"
"	color: rgb(255, 255, 255)\n"
"}\n"
"\n"
"QSpinBox:pressed {\n"
"	border-bottom: 1px solid white;\n"
"}\n"
"")
        self.spinBox_pos.setMinimum(1)
        self.spinBox_pos.setMaximum(100)
        self.spinBox_pos.setValue(1)

        self.horizontalLayout.addWidget(self.spinBox_pos, 0, Qt.AlignmentFlag.AlignHCenter)

        self.label_12 = QLabel(self.text_sborka_1)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font2)
        self.label_12.setStyleSheet(u"background: none;")

        self.horizontalLayout.addWidget(self.label_12, 0, Qt.AlignmentFlag.AlignHCenter)

        self.comboBox_detail_2 = QComboBox(self.text_sborka_1)
        self.comboBox_detail_2.addItem("")
        self.comboBox_detail_2.addItem("")
        self.comboBox_detail_2.setObjectName(u"comboBox_detail_2")
        self.comboBox_detail_2.setFont(font2)
        self.comboBox_detail_2.setStyleSheet(u"QComboBox {\n"
"	padding: 5, 5, 5, 5;\n"
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

        self.horizontalLayout.addWidget(self.comboBox_detail_2, 0, Qt.AlignmentFlag.AlignHCenter)

        self.horizontalSpacer_20 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_20)


        self.verticalLayout_14.addLayout(self.horizontalLayout)


        self.verticalLayout_2.addWidget(self.text_sborka_1)

        self.stackedWidget.addWidget(self.page_sborka)
        self.page__svarka = QWidget()
        self.page__svarka.setObjectName(u"page__svarka")
        self.verticalLayout_4 = QVBoxLayout(self.page__svarka)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.listWidget_svarka = QListWidget(self.page__svarka)
        QListWidgetItem(self.listWidget_svarka)
        QListWidgetItem(self.listWidget_svarka)
        QListWidgetItem(self.listWidget_svarka)
        QListWidgetItem(self.listWidget_svarka)
        self.listWidget_svarka.setObjectName(u"listWidget_svarka")
        sizePolicy.setHeightForWidth(self.listWidget_svarka.sizePolicy().hasHeightForWidth())
        self.listWidget_svarka.setSizePolicy(sizePolicy)
        self.listWidget_svarka.setMinimumSize(QSize(200, 0))
        self.listWidget_svarka.setFont(font1)
        self.listWidget_svarka.viewport().setProperty(u"cursor", QCursor(Qt.CursorShape.PointingHandCursor))
        self.listWidget_svarka.setStyleSheet(u"\n"
"/* \u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500 \u0421\u0430\u043c \u0441\u043f\u0438\u0441\u043e\u043a \u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500 */\n"
"QListWidget {\n"
"    background: transparent;\n"
"    font-size: 10pt;\n"
"	border: none;\n"
"    color: #E8EAF0;\n"
"}\n"
"\n"
"/* \u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500 \u042d\u043b\u0435\u043c\u0435\u043d\u0442\u044b \u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500 */\n"
"QListWidget::item {\n"
"    background: transparent;\n"
"    border: none;\n"
"    border-radius: 12px;\n"
"    margin: 2px 6px;\n"
"    color: rgba(255, 255, 255, 0.72);\n"
"}\n"
"\n"
"QListWidget::item:hover {\n"
"    background: rgba(255, 255, 255, 0.07);\n"
"    color: #FFFFFF;\n"
"}\n"
"\n"
"QListWidget::item:selected {\n"
"    background: qlineargradient(x1:0, y1:0, x2:1, y2:0,\n"
"        stop:0 rgba(94, 129, 255, 0.32),\n"
"        stop:"
                        "1 rgba(94, 129, 255, 0.08));\n"
"    color: #FFFFFF;\n"
"}\n"
"\n"
"QListWidget::item:selected:hover {\n"
"    background: qlineargradient(x1:0, y1:0, x2:1, y2:0,\n"
"        stop:0 rgba(94, 129, 255, 0.42),\n"
"        stop:1 rgba(94, 129, 255, 0.14));\n"
"}\n"
"\n"
"/* \u0443\u0431\u0438\u0440\u0430\u0435\u043c \u0440\u0430\u043c\u043a\u0443/\u043f\u0443\u043d\u043a\u0442\u0438\u0440 \u043f\u0440\u0438 \u0444\u043e\u043a\u0443\u0441\u0435 */\n"
"QListWidget:focus,\n"
"QListWidget::item:focus {\n"
"    outline: none;\n"
"    border: none;\n"
"}\n"
"\n"
"/* \u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500 \u0412\u0435\u0440\u0442\u0438\u043a\u0430\u043b\u044c\u043d\u044b\u0439 \u0441\u043a\u0440\u043e\u043b\u043b\u0431\u0430\u0440 \u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500 */\n"
"QScrollBar:vertical {\n"
"    background: transparent;\n"
"    width: 10px;\n"
"    margin: 4px 2px;\n"
"    border-radius: 5px;\n"
"}\n"
"QScrollBar::handle:vertical {"
                        "\n"
"    background: rgba(255, 255, 255, 0.18);\n"
"    min-height: 30px;\n"
"    border-radius: 5px;\n"
"}\n"
"QScrollBar::handle:vertical:hover {\n"
"    background: rgba(255, 255, 255, 0.32);\n"
"}\n"
"QScrollBar::add-line:vertical,\n"
"QScrollBar::sub-line:vertical { height: 0; }\n"
"QScrollBar::add-page:vertical,\n"
"QScrollBar::sub-page:vertical { background: transparent; }\n"
"\n"
"/* \u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500 \u0413\u043e\u0440\u0438\u0437\u043e\u043d\u0442\u0430\u043b\u044c\u043d\u044b\u0439 \u0441\u043a\u0440\u043e\u043b\u043b\u0431\u0430\u0440 \u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500 */\n"
"QScrollBar:horizontal {\n"
"    background: transparent;\n"
"    height: 10px;\n"
"    margin: 2px 4px;\n"
"    border-radius: 5px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background: rgba(255, 255, 255, 0.18);\n"
"    min-width: 30px;\n"
"    border-radius: 5px;\n"
"}\n"
"QScrollBar::handle:horizontal:hover {\n"
""
                        "    background: rgba(255, 255, 255, 0.32);\n"
"}\n"
"QScrollBar::add-line:horizontal,\n"
"QScrollBar::sub-line:horizontal { width: 0; }\n"
"QScrollBar::add-page:horizontal,\n"
"QScrollBar::sub-page:horizontal { background: transparent; }\n"
"")
        self.listWidget_svarka.setTabKeyNavigation(False)
        self.listWidget_svarka.setAlternatingRowColors(False)

        self.verticalLayout_4.addWidget(self.listWidget_svarka)

        self.line_3 = QFrame(self.page__svarka)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.Shape.HLine)
        self.line_3.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_4.addWidget(self.line_3)

        self.text_svarka_3 = QWidget(self.page__svarka)
        self.text_svarka_3.setObjectName(u"text_svarka_3")
        self.verticalLayout_13 = QVBoxLayout(self.text_svarka_3)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.label_24 = QLabel(self.text_svarka_3)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setFont(font1)
        self.label_24.setStyleSheet(u"background: none;")

        self.verticalLayout_13.addWidget(self.label_24, 0, Qt.AlignmentFlag.AlignHCenter)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(-1, -1, 20, -1)
        self.horizontalSpacer_18 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_18)

        self.label_18 = QLabel(self.text_svarka_3)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setFont(font2)
        self.label_18.setStyleSheet(u"background: none;")

        self.horizontalLayout_13.addWidget(self.label_18)

        self.horizontalSpacer_19 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_19)


        self.verticalLayout_13.addLayout(self.horizontalLayout_13)


        self.verticalLayout_4.addWidget(self.text_svarka_3)

        self.text_svarka_1 = QWidget(self.page__svarka)
        self.text_svarka_1.setObjectName(u"text_svarka_1")
        self.verticalLayout_7 = QVBoxLayout(self.text_svarka_1)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.label_20 = QLabel(self.text_svarka_1)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setFont(font1)
        self.label_20.setStyleSheet(u"background: none;")

        self.verticalLayout_7.addWidget(self.label_20, 0, Qt.AlignmentFlag.AlignHCenter)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(-1, -1, 20, -1)
        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_12)

        self.comboBox_position_type = QComboBox(self.text_svarka_1)
        self.comboBox_position_type.addItem("")
        self.comboBox_position_type.addItem("")
        self.comboBox_position_type.setObjectName(u"comboBox_position_type")
        self.comboBox_position_type.setFont(font2)
        self.comboBox_position_type.setStyleSheet(u"QComboBox {\n"
"	padding: 5, 5, 5, 5;\n"
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

        self.horizontalLayout_9.addWidget(self.comboBox_position_type)

        self.label_16 = QLabel(self.text_svarka_1)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setFont(font2)
        self.label_16.setStyleSheet(u"background: none;")

        self.horizontalLayout_9.addWidget(self.label_16)

        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_11)


        self.verticalLayout_7.addLayout(self.horizontalLayout_9)


        self.verticalLayout_4.addWidget(self.text_svarka_1)

        self.text_svarka_2 = QWidget(self.page__svarka)
        self.text_svarka_2.setObjectName(u"text_svarka_2")
        self.verticalLayout_5 = QVBoxLayout(self.text_svarka_2)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 20)
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, -1, 0, -1)
        self.label_19 = QLabel(self.text_svarka_2)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setFont(font1)
        self.label_19.setStyleSheet(u"background: none;")

        self.verticalLayout_6.addWidget(self.label_19, 0, Qt.AlignmentFlag.AlignHCenter)

        self.widget_zach = QWidget(self.text_svarka_2)
        self.widget_zach.setObjectName(u"widget_zach")
        self.verticalLayout_10 = QVBoxLayout(self.widget_zach)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.box_details_zach = QGridLayout()
        self.box_details_zach.setObjectName(u"box_details_zach")
        self.box_details_zach.setContentsMargins(-1, -1, 0, -1)

        self.verticalLayout_10.addLayout(self.box_details_zach)


        self.verticalLayout_6.addWidget(self.widget_zach)

        self.widget_obez = QWidget(self.text_svarka_2)
        self.widget_obez.setObjectName(u"widget_obez")
        self.verticalLayout_12 = QVBoxLayout(self.widget_obez)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.box_details_obez = QGridLayout()
        self.box_details_obez.setObjectName(u"box_details_obez")
        self.box_details_obez.setContentsMargins(-1, -1, 0, -1)

        self.verticalLayout_12.addLayout(self.box_details_obez)


        self.verticalLayout_6.addWidget(self.widget_obez)


        self.verticalLayout_5.addLayout(self.verticalLayout_6)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(-1, -1, -1, 20)
        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_7)

        self.pushButton_add_detail = QPushButton(self.text_svarka_2)
        self.pushButton_add_detail.setObjectName(u"pushButton_add_detail")
        self.pushButton_add_detail.setStyleSheet(u"QPushButton {\n"
"	border: 1px solid;\n"
"	border-color: white;\n"
"	border-radius: 5px;\n"
"	height: 20px;\n"
"	background-color: none;\n"
"	padding: 2 5 2 5\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(0, 111, 171)\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: rgb(0, 53, 93)\n"
"}")

        self.horizontalLayout_4.addWidget(self.pushButton_add_detail, 0, Qt.AlignmentFlag.AlignHCenter)

        self.pushButton_del_detail = QPushButton(self.text_svarka_2)
        self.pushButton_del_detail.setObjectName(u"pushButton_del_detail")
        self.pushButton_del_detail.setStyleSheet(u"QPushButton {\n"
"	border: 1px solid;\n"
"	border-color: white;\n"
"	border-radius: 5px;\n"
"	height: 20px;\n"
"	background-color: none;\n"
"	padding: 2 5 2 5\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(0, 111, 171)\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: rgb(0, 53, 93)\n"
"}")

        self.horizontalLayout_4.addWidget(self.pushButton_del_detail, 0, Qt.AlignmentFlag.AlignHCenter)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_8)


        self.verticalLayout_5.addLayout(self.horizontalLayout_4)

        self.label = QLabel(self.text_svarka_2)
        self.label.setObjectName(u"label")
        self.label.setFont(font2)
        self.label.setStyleSheet(u"background: none;")

        self.verticalLayout_5.addWidget(self.label, 0, Qt.AlignmentFlag.AlignHCenter)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(-1, 0, -1, -1)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer)

        self.label_2 = QLabel(self.text_svarka_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font2)
        self.label_2.setStyleSheet(u"background: none;")

        self.horizontalLayout_8.addWidget(self.label_2, 0, Qt.AlignmentFlag.AlignHCenter)

        self.spinBox_width_min = QSpinBox(self.text_svarka_2)
        self.spinBox_width_min.setObjectName(u"spinBox_width_min")
        self.spinBox_width_min.setFont(font3)
        self.spinBox_width_min.setStyleSheet(u"QSpinBox {\n"
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
"QSpinBox:disabled {\n"
"	color: rgb(120, 106, 107);\n"
"	background: rgba(255, 255, 255, 20);\n"
"}\n"
"\n"
"QSpinBox:hover {\n"
"	color: rgb(255, 255, 255)\n"
"}\n"
"\n"
"QSpinBox:pressed {\n"
"	border-bottom: 1px solid white;\n"
"}\n"
"")
        self.spinBox_width_min.setMinimum(1)
        self.spinBox_width_min.setMaximum(100)
        self.spinBox_width_min.setValue(10)

        self.horizontalLayout_8.addWidget(self.spinBox_width_min, 0, Qt.AlignmentFlag.AlignHCenter)

        self.label_3 = QLabel(self.text_svarka_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font2)
        self.label_3.setStyleSheet(u"background: none;")

        self.horizontalLayout_8.addWidget(self.label_3, 0, Qt.AlignmentFlag.AlignHCenter)

        self.spinBox_width_max = QSpinBox(self.text_svarka_2)
        self.spinBox_width_max.setObjectName(u"spinBox_width_max")
        self.spinBox_width_max.setFont(font3)
        self.spinBox_width_max.setStyleSheet(u"QSpinBox {\n"
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
"QSpinBox:disabled {\n"
"	color: rgb(120, 106, 107);\n"
"	background: rgba(255, 255, 255, 20);\n"
"}\n"
"\n"
"QSpinBox:hover {\n"
"	color: rgb(255, 255, 255)\n"
"}\n"
"\n"
"QSpinBox:pressed {\n"
"	border-bottom: 1px solid white;\n"
"}\n"
"")
        self.spinBox_width_max.setMinimum(1)
        self.spinBox_width_max.setMaximum(100)
        self.spinBox_width_max.setValue(15)

        self.horizontalLayout_8.addWidget(self.spinBox_width_max, 0, Qt.AlignmentFlag.AlignHCenter)

        self.label_4 = QLabel(self.text_svarka_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font2)
        self.label_4.setStyleSheet(u"background: none;")

        self.horizontalLayout_8.addWidget(self.label_4)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_4)


        self.verticalLayout_5.addLayout(self.horizontalLayout_8)


        self.verticalLayout_4.addWidget(self.text_svarka_2)

        self.stackedWidget.addWidget(self.page__svarka)
        self.page_meh = QWidget()
        self.page_meh.setObjectName(u"page_meh")
        self.verticalLayout_3 = QVBoxLayout(self.page_meh)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.listWidget_meh = QListWidget(self.page_meh)
        QListWidgetItem(self.listWidget_meh)
        self.listWidget_meh.setObjectName(u"listWidget_meh")
        sizePolicy.setHeightForWidth(self.listWidget_meh.sizePolicy().hasHeightForWidth())
        self.listWidget_meh.setSizePolicy(sizePolicy)
        self.listWidget_meh.setMinimumSize(QSize(200, 0))
        self.listWidget_meh.setFont(font1)
        self.listWidget_meh.viewport().setProperty(u"cursor", QCursor(Qt.CursorShape.PointingHandCursor))
        self.listWidget_meh.setStyleSheet(u"\n"
"/* \u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500 \u0421\u0430\u043c \u0441\u043f\u0438\u0441\u043e\u043a \u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500 */\n"
"QListWidget {\n"
"    background: transparent;\n"
"    font-size: 10pt;\n"
"	border: none;\n"
"    color: #E8EAF0;\n"
"}\n"
"\n"
"/* \u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500 \u042d\u043b\u0435\u043c\u0435\u043d\u0442\u044b \u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500 */\n"
"QListWidget::item {\n"
"    background: transparent;\n"
"    border: none;\n"
"    border-radius: 12px;\n"
"    margin: 2px 6px;\n"
"    color: rgba(255, 255, 255, 0.72);\n"
"}\n"
"\n"
"QListWidget::item:hover {\n"
"    background: rgba(255, 255, 255, 0.07);\n"
"    color: #FFFFFF;\n"
"}\n"
"\n"
"QListWidget::item:selected {\n"
"    background: qlineargradient(x1:0, y1:0, x2:1, y2:0,\n"
"        stop:0 rgba(94, 129, 255, 0.32),\n"
"        stop:"
                        "1 rgba(94, 129, 255, 0.08));\n"
"    color: #FFFFFF;\n"
"}\n"
"\n"
"QListWidget::item:selected:hover {\n"
"    background: qlineargradient(x1:0, y1:0, x2:1, y2:0,\n"
"        stop:0 rgba(94, 129, 255, 0.42),\n"
"        stop:1 rgba(94, 129, 255, 0.14));\n"
"}\n"
"\n"
"/* \u0443\u0431\u0438\u0440\u0430\u0435\u043c \u0440\u0430\u043c\u043a\u0443/\u043f\u0443\u043d\u043a\u0442\u0438\u0440 \u043f\u0440\u0438 \u0444\u043e\u043a\u0443\u0441\u0435 */\n"
"QListWidget:focus,\n"
"QListWidget::item:focus {\n"
"    outline: none;\n"
"    border: none;\n"
"}\n"
"\n"
"/* \u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500 \u0412\u0435\u0440\u0442\u0438\u043a\u0430\u043b\u044c\u043d\u044b\u0439 \u0441\u043a\u0440\u043e\u043b\u043b\u0431\u0430\u0440 \u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500 */\n"
"QScrollBar:vertical {\n"
"    background: transparent;\n"
"    width: 10px;\n"
"    margin: 4px 2px;\n"
"    border-radius: 5px;\n"
"}\n"
"QScrollBar::handle:vertical {"
                        "\n"
"    background: rgba(255, 255, 255, 0.18);\n"
"    min-height: 30px;\n"
"    border-radius: 5px;\n"
"}\n"
"QScrollBar::handle:vertical:hover {\n"
"    background: rgba(255, 255, 255, 0.32);\n"
"}\n"
"QScrollBar::add-line:vertical,\n"
"QScrollBar::sub-line:vertical { height: 0; }\n"
"QScrollBar::add-page:vertical,\n"
"QScrollBar::sub-page:vertical { background: transparent; }\n"
"\n"
"/* \u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500 \u0413\u043e\u0440\u0438\u0437\u043e\u043d\u0442\u0430\u043b\u044c\u043d\u044b\u0439 \u0441\u043a\u0440\u043e\u043b\u043b\u0431\u0430\u0440 \u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500 */\n"
"QScrollBar:horizontal {\n"
"    background: transparent;\n"
"    height: 10px;\n"
"    margin: 2px 4px;\n"
"    border-radius: 5px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background: rgba(255, 255, 255, 0.18);\n"
"    min-width: 30px;\n"
"    border-radius: 5px;\n"
"}\n"
"QScrollBar::handle:horizontal:hover {\n"
""
                        "    background: rgba(255, 255, 255, 0.32);\n"
"}\n"
"QScrollBar::add-line:horizontal,\n"
"QScrollBar::sub-line:horizontal { width: 0; }\n"
"QScrollBar::add-page:horizontal,\n"
"QScrollBar::sub-page:horizontal { background: transparent; }\n"
"")
        self.listWidget_meh.setTabKeyNavigation(False)
        self.listWidget_meh.setAlternatingRowColors(False)

        self.verticalLayout_3.addWidget(self.listWidget_meh)

        self.line = QFrame(self.page_meh)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_3.addWidget(self.line)

        self.label_21 = QLabel(self.page_meh)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setFont(font1)
        self.label_21.setStyleSheet(u"background: none;")

        self.verticalLayout_3.addWidget(self.label_21, 0, Qt.AlignmentFlag.AlignHCenter)

        self.text_meh_1 = QWidget(self.page_meh)
        self.text_meh_1.setObjectName(u"text_meh_1")
        self.horizontalLayout_3 = QHBoxLayout(self.text_meh_1)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, 1, -1, 1)
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_5)

        self.label_5 = QLabel(self.text_meh_1)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font2)
        self.label_5.setStyleSheet(u"background: none;")

        self.horizontalLayout_3.addWidget(self.label_5)

        self.doubleSpinBox_faska = QDoubleSpinBox(self.text_meh_1)
        self.doubleSpinBox_faska.setObjectName(u"doubleSpinBox_faska")
        self.doubleSpinBox_faska.setStyleSheet(u"QDoubleSpinBox {\n"
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
        self.doubleSpinBox_faska.setDecimals(1)
        self.doubleSpinBox_faska.setMaximum(10.000000000000000)
        self.doubleSpinBox_faska.setSingleStep(0.500000000000000)
        self.doubleSpinBox_faska.setValue(0.500000000000000)

        self.horizontalLayout_3.addWidget(self.doubleSpinBox_faska, 0, Qt.AlignmentFlag.AlignHCenter)

        self.label_7 = QLabel(self.text_meh_1)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font3)
        self.label_7.setStyleSheet(u"background: none;")

        self.horizontalLayout_3.addWidget(self.label_7)

        self.spinBox_angle = QSpinBox(self.text_meh_1)
        self.spinBox_angle.setObjectName(u"spinBox_angle")
        self.spinBox_angle.setFont(font3)
        self.spinBox_angle.setStyleSheet(u"QSpinBox {\n"
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
"QSpinBox:disabled {\n"
"	color: rgb(120, 106, 107);\n"
"	background: rgba(255, 255, 255, 20);\n"
"}\n"
"\n"
"QSpinBox:hover {\n"
"	color: rgb(255, 255, 255)\n"
"}\n"
"\n"
"QSpinBox:pressed {\n"
"	border-bottom: 1px solid white;\n"
"}\n"
"")
        self.spinBox_angle.setMinimum(1)
        self.spinBox_angle.setMaximum(100)
        self.spinBox_angle.setValue(45)

        self.horizontalLayout_3.addWidget(self.spinBox_angle, 0, Qt.AlignmentFlag.AlignHCenter)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_6)


        self.verticalLayout_3.addWidget(self.text_meh_1)

        self.stackedWidget.addWidget(self.page_meh)

        self.verticalLayout.addWidget(self.stackedWidget)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.pushButton_save_result = QPushButton(DialogSlesarnaya)
        self.pushButton_save_result.setObjectName(u"pushButton_save_result")
        self.pushButton_save_result.setStyleSheet(u"QPushButton {\n"
"	border: 1px solid;\n"
"	border-color: white;\n"
"	border-radius: 10px;\n"
"	height: 20px;\n"
"	width: 110px;\n"
"	background-color: none;\n"
"	padding: 2 5 2 5\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(0, 111, 171)\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: rgb(0, 53, 93)\n"
"}")

        self.verticalLayout.addWidget(self.pushButton_save_result, 0, Qt.AlignmentFlag.AlignHCenter)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.pushButton_close = QPushButton(DialogSlesarnaya)
        self.pushButton_close.setObjectName(u"pushButton_close")
        self.pushButton_close.setStyleSheet(u"QPushButton {\n"
"	border: 1px solid;\n"
"	border-color: white;\n"
"	border-radius: 10px;\n"
"	height: 20px;\n"
"	width: 110px;\n"
"	background-color: rgba(247, 38, 38, 40);\n"
"	padding: 2 5 2 5\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(0, 111, 171)\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: rgb(0, 53, 93)\n"
"}")

        self.verticalLayout.addWidget(self.pushButton_close, 0, Qt.AlignmentFlag.AlignHCenter)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_3)


        self.retranslateUi(DialogSlesarnaya)

        self.stackedWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(DialogSlesarnaya)
    # setupUi

    def retranslateUi(self, DialogSlesarnaya):
        DialogSlesarnaya.setWindowTitle(QCoreApplication.translate("DialogSlesarnaya", u"\u0421\u043b\u0435\u0441\u0430\u0440\u043d\u0430\u044f", None))
        self.label_8.setText(QCoreApplication.translate("DialogSlesarnaya", u"\u0421\u043b\u0435\u0441\u0430\u0440\u043d\u0430\u044f", None))
        self.groupBox.setTitle("")
        self.btn_meh.setText(QCoreApplication.translate("DialogSlesarnaya", u"\u041c\u0435\u0445. \u043e\u0431\u0440\u0430\u0431\u043e\u0442\u043a\u0430", None))
        self.btn_svarka.setText(QCoreApplication.translate("DialogSlesarnaya", u"\u0421\u0432\u0430\u0440\u043a\u0430", None))
        self.btn_sborka.setText(QCoreApplication.translate("DialogSlesarnaya", u"\u0421\u0431\u043e\u0440\u043a\u0430", None))

        __sortingEnabled = self.listWidget_sborka.isSortingEnabled()
        self.listWidget_sborka.setSortingEnabled(False)
        ___qlistwidgetitem = self.listWidget_sborka.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("DialogSlesarnaya", u"\u041f\u0440\u043e\u0442\u0438\u0440\u043a\u0430", None))
        self.listWidget_sborka.setSortingEnabled(__sortingEnabled)

        self.label_22.setText(QCoreApplication.translate("DialogSlesarnaya", u"\u0423\u043a\u0430\u0436\u0438\u0442\u0435 \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u044b:", None))
        self.comboBox_position.setItemText(0, QCoreApplication.translate("DialogSlesarnaya", u"\u0412\u043d\u0443\u0442\u0440\u0435\u043d\u043d\u044e\u044e", None))
        self.comboBox_position.setItemText(1, QCoreApplication.translate("DialogSlesarnaya", u"\u0412\u043d\u0435\u0448\u043d\u044e\u044e", None))

        self.label_6.setText(QCoreApplication.translate("DialogSlesarnaya", u"\u043f\u043e\u0432\u0435\u0440\u0445\u043d\u043e\u0441\u0442\u044c", None))
        self.label_11.setText(QCoreApplication.translate("DialogSlesarnaya", u"\u043f\u043e\u0437.", None))
        self.spinBox_pos.setSuffix("")
        self.label_12.setText(QCoreApplication.translate("DialogSlesarnaya", u"\u043f\u0440\u043e\u0442\u0435\u0440\u0435\u0442\u044c", None))
        self.comboBox_detail_2.setItemText(0, QCoreApplication.translate("DialogSlesarnaya", u"\u0441\u043f\u0438\u0440\u0442\u043e\u043c", None))
        self.comboBox_detail_2.setItemText(1, QCoreApplication.translate("DialogSlesarnaya", u"\u0443\u0430\u0439\u0442-\u0441\u043f\u0438\u0440\u0438\u0442\u043e\u043c", None))


        __sortingEnabled1 = self.listWidget_svarka.isSortingEnabled()
        self.listWidget_svarka.setSortingEnabled(False)
        ___qlistwidgetitem1 = self.listWidget_svarka.item(0)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("DialogSlesarnaya", u"\u0423\u0441\u0442\u0430\u043d\u043e\u0432\u043a\u0430 / \u0421\u043d\u044f\u0442\u0438\u0435 \u043f\u0440\u0438\u0441\u043f\u043e\u0441\u043e\u0431\u043b\u0435\u043d\u0438\u044f", None))
        ___qlistwidgetitem2 = self.listWidget_svarka.item(1)
        ___qlistwidgetitem2.setText(QCoreApplication.translate("DialogSlesarnaya", u"\u0417\u0430\u0447\u0438\u0441\u0442\u043a\u0430 \u0434\u0435\u0442\u0430\u043b\u0435\u0439 \u043f\u0435\u0440\u0435\u0434 \u0441\u0432\u0430\u0440\u043a\u043e\u0439", None))
        ___qlistwidgetitem3 = self.listWidget_svarka.item(2)
        ___qlistwidgetitem3.setText(QCoreApplication.translate("DialogSlesarnaya", u"\u041e\u0431\u0435\u0437\u0436\u0438\u0440\u0438\u0432\u0430\u043d\u0438\u0435 \u0434\u0435\u0442\u0430\u043b\u0435\u0439 \u043f\u0435\u0440\u0435\u0434 \u0441\u0432\u0430\u0440\u043a\u043e\u0439", None))
        ___qlistwidgetitem4 = self.listWidget_svarka.item(3)
        ___qlistwidgetitem4.setText(QCoreApplication.translate("DialogSlesarnaya", u"\u0417\u0430\u0447\u0438\u0441\u0442\u043a\u0430 \u0441\u0432\u0430\u0440\u043d\u044b\u0445 \u0448\u0432\u043e\u0432", None))
        self.listWidget_svarka.setSortingEnabled(__sortingEnabled1)

        self.label_24.setText(QCoreApplication.translate("DialogSlesarnaya", u"\u0422\u0435\u043a\u0441\u0442 \u0431\u0435\u0437 \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u043e\u0432:", None))
        self.label_18.setText(QCoreApplication.translate("DialogSlesarnaya", u"\u0417\u0430\u0447\u0438\u0441\u0442\u0438\u0442\u044c \u0441\u0432\u0430\u0440\u043d\u044b\u0435 \u0448\u0432\u044b \u043e\u0442 \u0446\u0432\u0435\u0442\u043e\u0432 \u043f\u043e\u0431\u0435\u0436\u0430\u043b\u043e\u0441\u0442\u0438 ", None))
        self.label_20.setText(QCoreApplication.translate("DialogSlesarnaya", u"\u0423\u043a\u0430\u0436\u0438\u0442\u0435 \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440:", None))
        self.comboBox_position_type.setItemText(0, QCoreApplication.translate("DialogSlesarnaya", u"\u0423\u0441\u0442\u0430\u043d\u043e\u0432\u0438\u0442\u044c", None))
        self.comboBox_position_type.setItemText(1, QCoreApplication.translate("DialogSlesarnaya", u"\u0421\u043d\u044f\u0442\u044c", None))

        self.label_16.setText(QCoreApplication.translate("DialogSlesarnaya", u"\u0441\u0442\u044f\u0433\u0438\u0432\u0430\u044e\u0449\u0435\u0435 \u043f\u0440\u0438\u0441\u043f\u043e\u0441\u043e\u0431\u043b\u0435\u043d\u0438\u0435", None))
        self.label_19.setText(QCoreApplication.translate("DialogSlesarnaya", u"\u0423\u043a\u0430\u0436\u0438\u0442\u0435 \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u044b:", None))
        self.pushButton_add_detail.setText(QCoreApplication.translate("DialogSlesarnaya", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0434\u0435\u0442\u0430\u043b\u044c", None))
        self.pushButton_del_detail.setText(QCoreApplication.translate("DialogSlesarnaya", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c \u0434\u0435\u0442\u0430\u043b\u044c", None))
        self.label.setText(QCoreApplication.translate("DialogSlesarnaya", u"\u0428\u0438\u0440\u0438\u043d\u0430 \u0437\u0430\u0447\u0438\u0441\u0442\u043a\u0438:", None))
        self.label_2.setText(QCoreApplication.translate("DialogSlesarnaya", u"\u043e\u0442", None))
        self.spinBox_width_min.setSuffix("")
        self.label_3.setText(QCoreApplication.translate("DialogSlesarnaya", u"\u0434\u043e", None))
        self.spinBox_width_max.setSuffix("")
        self.label_4.setText(QCoreApplication.translate("DialogSlesarnaya", u"\u043c\u043c", None))

        __sortingEnabled2 = self.listWidget_meh.isSortingEnabled()
        self.listWidget_meh.setSortingEnabled(False)
        ___qlistwidgetitem5 = self.listWidget_meh.item(0)
        ___qlistwidgetitem5.setText(QCoreApplication.translate("DialogSlesarnaya", u"\u041e\u0431\u0440\u0430\u0431\u043e\u0442\u043a\u0430 \u043a\u0440\u043e\u043c\u043a\u0438", None))
        self.listWidget_meh.setSortingEnabled(__sortingEnabled2)

        self.label_21.setText(QCoreApplication.translate("DialogSlesarnaya", u"\u0423\u043a\u0430\u0436\u0438\u0442\u0435 \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440:", None))
        self.label_5.setText(QCoreApplication.translate("DialogSlesarnaya", u"\u041e\u0441\u0442\u0440\u044b\u0435 \u043a\u0440\u043e\u043c\u043a\u0438 \u043f\u0440\u0438\u0442\u0443\u043f\u0438\u0442\u044c \u0444\u0430\u0441\u043a\u043e\u0439", None))
        self.label_7.setText(QCoreApplication.translate("DialogSlesarnaya", u"\u0445", None))
        self.spinBox_angle.setSuffix(QCoreApplication.translate("DialogSlesarnaya", u"\u00b0", None))
        self.pushButton_save_result.setText(QCoreApplication.translate("DialogSlesarnaya", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0442\u0435\u043a\u0441\u0442", None))
        self.pushButton_close.setText(QCoreApplication.translate("DialogSlesarnaya", u"\u0417\u0430\u043a\u0440\u044b\u0442\u044c \u043e\u043a\u043d\u043e", None))
    # retranslateUi

