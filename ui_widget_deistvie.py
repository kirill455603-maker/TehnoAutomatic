# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_widget_deistvie.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_WidgetDeistvie(object):
    def setupUi(self, WidgetDeistvie):
        if not WidgetDeistvie.objectName():
            WidgetDeistvie.setObjectName(u"WidgetDeistvie")
        WidgetDeistvie.resize(400, 300)
        self.verticalLayout = QVBoxLayout(WidgetDeistvie)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.comboBox_deistvie = QComboBox(WidgetDeistvie)
        self.comboBox_deistvie.setObjectName(u"comboBox_deistvie")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_deistvie.sizePolicy().hasHeightForWidth())
        self.comboBox_deistvie.setSizePolicy(sizePolicy)
        self.comboBox_deistvie.setStyleSheet(u"QComboBox {\n"
"	padding: 5, 5, 5, 5;\n"
"	border: none;\n"
"	border-bottom: 1px solid white;\n"
"	background: rgba(255, 255, 255, 0);\n"
"	transition: color 0.3s ease;\n"
"	transition: border-bottom 0.4s ease;\n"
"	color: rgb(204, 204, 204);\n"
"	font-size: 10pt;\n"
"	width: 90px;\n"
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

        self.verticalLayout.addWidget(self.comboBox_deistvie, 0, Qt.AlignmentFlag.AlignHCenter)


        self.retranslateUi(WidgetDeistvie)

        QMetaObject.connectSlotsByName(WidgetDeistvie)
    # setupUi

    def retranslateUi(self, WidgetDeistvie):
        WidgetDeistvie.setWindowTitle(QCoreApplication.translate("WidgetDeistvie", u"Form", None))
    # retranslateUi

