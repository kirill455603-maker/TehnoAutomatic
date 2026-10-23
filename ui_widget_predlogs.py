# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_widget_predlogs.ui'
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

class Ui_WidgetPredlogs(object):
    def setupUi(self, WidgetPredlogs):
        if not WidgetPredlogs.objectName():
            WidgetPredlogs.setObjectName(u"WidgetPredlogs")
        WidgetPredlogs.resize(400, 300)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(WidgetPredlogs.sizePolicy().hasHeightForWidth())
        WidgetPredlogs.setSizePolicy(sizePolicy)
        self.verticalLayout = QVBoxLayout(WidgetPredlogs)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.comboBox_predlogs = QComboBox(WidgetPredlogs)
        self.comboBox_predlogs.addItem("")
        self.comboBox_predlogs.addItem("")
        self.comboBox_predlogs.addItem("")
        self.comboBox_predlogs.addItem("")
        self.comboBox_predlogs.addItem("")
        self.comboBox_predlogs.setObjectName(u"comboBox_predlogs")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.comboBox_predlogs.sizePolicy().hasHeightForWidth())
        self.comboBox_predlogs.setSizePolicy(sizePolicy1)
        self.comboBox_predlogs.setStyleSheet(u"QComboBox {\n"
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

        self.verticalLayout.addWidget(self.comboBox_predlogs, 0, Qt.AlignmentFlag.AlignHCenter)


        self.retranslateUi(WidgetPredlogs)

        QMetaObject.connectSlotsByName(WidgetPredlogs)
    # setupUi

    def retranslateUi(self, WidgetPredlogs):
        WidgetPredlogs.setWindowTitle(QCoreApplication.translate("WidgetPredlogs", u"Form", None))
        self.comboBox_predlogs.setItemText(0, QCoreApplication.translate("WidgetPredlogs", u"\u0412", None))
        self.comboBox_predlogs.setItemText(1, QCoreApplication.translate("WidgetPredlogs", u"C", None))
        self.comboBox_predlogs.setItemText(2, QCoreApplication.translate("WidgetPredlogs", u"\u041d\u0430", None))
        self.comboBox_predlogs.setItemText(3, QCoreApplication.translate("WidgetPredlogs", u"\u041f\u043e\u0434", None))
        self.comboBox_predlogs.setItemText(4, QCoreApplication.translate("WidgetPredlogs", u"\u041d\u0430\u0434", None))

    # retranslateUi

