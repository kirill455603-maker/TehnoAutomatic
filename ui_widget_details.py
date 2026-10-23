# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_widget_details.ui'
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

class Ui_WidgetDetails(object):
    def setupUi(self, WidgetDetails):
        if not WidgetDetails.objectName():
            WidgetDetails.setObjectName(u"WidgetDetails")
        WidgetDetails.resize(400, 300)
        self.horizontalLayout = QHBoxLayout(WidgetDetails)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.comboBox_details = QComboBox(WidgetDetails)
        self.comboBox_details.setObjectName(u"comboBox_details")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_details.sizePolicy().hasHeightForWidth())
        self.comboBox_details.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(10)
        self.comboBox_details.setFont(font)
        self.comboBox_details.setStyleSheet(u"QComboBox {\n"
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

        self.horizontalLayout.addWidget(self.comboBox_details)

        self.label = QLabel(WidgetDetails)
        self.label.setObjectName(u"label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)
        font1 = QFont()
        font1.setPointSize(11)
        self.label.setFont(font1)
        self.label.setStyleSheet(u"background: none;")

        self.horizontalLayout.addWidget(self.label)

        self.spinBox_position = QSpinBox(WidgetDetails)
        self.spinBox_position.setObjectName(u"spinBox_position")
        sizePolicy.setHeightForWidth(self.spinBox_position.sizePolicy().hasHeightForWidth())
        self.spinBox_position.setSizePolicy(sizePolicy)
        self.spinBox_position.setFont(font1)
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


        self.retranslateUi(WidgetDetails)

        QMetaObject.connectSlotsByName(WidgetDetails)
    # setupUi

    def retranslateUi(self, WidgetDetails):
        WidgetDetails.setWindowTitle(QCoreApplication.translate("WidgetDetails", u"Form", None))
        self.label.setText(QCoreApplication.translate("WidgetDetails", u"\u043f\u043e\u0437. ", None))
    # retranslateUi

