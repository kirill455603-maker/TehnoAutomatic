# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_row_detail.ui'
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
    QSizePolicy, QSpacerItem, QSpinBox, QWidget)

class Ui_RowDetail(object):
    def setupUi(self, RowDetail):
        if not RowDetail.objectName():
            RowDetail.setObjectName(u"RowDetail")
        RowDetail.resize(400, 300)
        self.horizontalLayout = QHBoxLayout(RowDetail)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.label = QLabel(RowDetail)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"background: none;")

        self.horizontalLayout.addWidget(self.label)

        self.comboBox_detail = QComboBox(RowDetail)
        self.comboBox_detail.setObjectName(u"comboBox_detail")
        font = QFont()
        font.setPointSize(10)
        self.comboBox_detail.setFont(font)
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

        self.horizontalLayout.addWidget(self.comboBox_detail)

        self.label_18 = QLabel(RowDetail)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setFont(font)
        self.label_18.setStyleSheet(u"background: none;")

        self.horizontalLayout.addWidget(self.label_18)

        self.spinBox_pos = QSpinBox(RowDetail)
        self.spinBox_pos.setObjectName(u"spinBox_pos")
        font1 = QFont()
        font1.setPointSize(11)
        self.spinBox_pos.setFont(font1)
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

        self.horizontalLayout.addWidget(self.spinBox_pos)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.retranslateUi(RowDetail)

        QMetaObject.connectSlotsByName(RowDetail)
    # setupUi

    def retranslateUi(self, RowDetail):
        RowDetail.setWindowTitle(QCoreApplication.translate("RowDetail", u"Form", None))
        self.label.setText(QCoreApplication.translate("RowDetail", u"\u0414\u0435\u0442\u0430\u043b\u044c \u2116 1:", None))
        self.label_18.setText(QCoreApplication.translate("RowDetail", u"\u043f\u043e\u0437.", None))
        self.spinBox_pos.setSuffix("")
    # retranslateUi

