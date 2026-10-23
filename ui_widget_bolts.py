# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_widget_bolts.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QLabel,
    QSizePolicy, QSpinBox, QWidget)

class Ui_WidgetBolts(object):
    def setupUi(self, WidgetBolts):
        if not WidgetBolts.objectName():
            WidgetBolts.setObjectName(u"WidgetBolts")
        WidgetBolts.resize(405, 300)
        self.horizontalLayout = QHBoxLayout(WidgetBolts)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.spinBox_count = QSpinBox(WidgetBolts)
        self.spinBox_count.setObjectName(u"spinBox_count")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinBox_count.sizePolicy().hasHeightForWidth())
        self.spinBox_count.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(11)
        self.spinBox_count.setFont(font)
        self.spinBox_count.setStyleSheet(u"QSpinBox {\n"
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
        self.spinBox_count.setMinimum(1)

        self.horizontalLayout.addWidget(self.spinBox_count, 0, Qt.AlignmentFlag.AlignHCenter)

        self.comboBox_type = QComboBox(WidgetBolts)
        self.comboBox_type.addItem("")
        self.comboBox_type.addItem("")
        self.comboBox_type.addItem("")
        self.comboBox_type.addItem("")
        self.comboBox_type.setObjectName(u"comboBox_type")
        sizePolicy.setHeightForWidth(self.comboBox_type.sizePolicy().hasHeightForWidth())
        self.comboBox_type.setSizePolicy(sizePolicy)
        self.comboBox_type.setMinimumSize(QSize(60, 0))
        font1 = QFont()
        font1.setPointSize(10)
        self.comboBox_type.setFont(font1)
        self.comboBox_type.setStyleSheet(u"QComboBox {\n"
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

        self.horizontalLayout.addWidget(self.comboBox_type, 0, Qt.AlignmentFlag.AlignHCenter)

        self.comboBox_rezba = QComboBox(WidgetBolts)
        self.comboBox_rezba.setObjectName(u"comboBox_rezba")
        sizePolicy.setHeightForWidth(self.comboBox_rezba.sizePolicy().hasHeightForWidth())
        self.comboBox_rezba.setSizePolicy(sizePolicy)
        self.comboBox_rezba.setMinimumSize(QSize(70, 0))
        self.comboBox_rezba.setFont(font1)
        self.comboBox_rezba.setStyleSheet(u"QComboBox {\n"
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

        self.horizontalLayout.addWidget(self.comboBox_rezba, 0, Qt.AlignmentFlag.AlignHCenter)

        self.label = QLabel(WidgetBolts)
        self.label.setObjectName(u"label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)
        self.label.setFont(font)
        self.label.setStyleSheet(u"background: none;")

        self.horizontalLayout.addWidget(self.label)

        self.comboBox_s = QComboBox(WidgetBolts)
        self.comboBox_s.setObjectName(u"comboBox_s")
        sizePolicy.setHeightForWidth(self.comboBox_s.sizePolicy().hasHeightForWidth())
        self.comboBox_s.setSizePolicy(sizePolicy)
        self.comboBox_s.setMinimumSize(QSize(70, 0))
        self.comboBox_s.setFont(font1)
        self.comboBox_s.setStyleSheet(u"QComboBox {\n"
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

        self.horizontalLayout.addWidget(self.comboBox_s, 0, Qt.AlignmentFlag.AlignHCenter)

        self.label_2 = QLabel(WidgetBolts)
        self.label_2.setObjectName(u"label_2")
        sizePolicy1.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy1)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"background: none;")

        self.horizontalLayout.addWidget(self.label_2)

        self.spinBox_position = QSpinBox(WidgetBolts)
        self.spinBox_position.setObjectName(u"spinBox_position")
        sizePolicy.setHeightForWidth(self.spinBox_position.sizePolicy().hasHeightForWidth())
        self.spinBox_position.setSizePolicy(sizePolicy)
        self.spinBox_position.setFont(font)
        self.spinBox_position.setStyleSheet(u"QSpinBox {\n"
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
        self.spinBox_position.setMinimum(1)

        self.horizontalLayout.addWidget(self.spinBox_position)


        self.retranslateUi(WidgetBolts)

        QMetaObject.connectSlotsByName(WidgetBolts)
    # setupUi

    def retranslateUi(self, WidgetBolts):
        WidgetBolts.setWindowTitle(QCoreApplication.translate("WidgetBolts", u"Form", None))
        self.comboBox_type.setItemText(0, QCoreApplication.translate("WidgetBolts", u"\u0431\u043e\u043b\u0442", None))
        self.comboBox_type.setItemText(1, QCoreApplication.translate("WidgetBolts", u"\u0448\u043f\u0438\u043b\u044c\u043a\u0443", None))
        self.comboBox_type.setItemText(2, QCoreApplication.translate("WidgetBolts", u"\u0432\u0438\u043d\u0442", None))
        self.comboBox_type.setItemText(3, QCoreApplication.translate("WidgetBolts", u"\u0433\u0430\u0439\u043a\u0443", None))

        self.label.setText(QCoreApplication.translate("WidgetBolts", u"\u0425", None))
        self.label_2.setText(QCoreApplication.translate("WidgetBolts", u"\u043f\u043e\u0437. ", None))
    # retranslateUi

