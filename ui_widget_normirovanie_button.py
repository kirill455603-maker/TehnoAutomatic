# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_widget_normirovanie_button.ui'
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
from PySide6.QtWidgets import (QApplication, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_ButtonList(object):
    def setupUi(self, ButtonList):
        if not ButtonList.objectName():
            ButtonList.setObjectName(u"ButtonList")
        ButtonList.resize(400, 300)
        self.verticalLayout = QVBoxLayout(ButtonList)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.pushButton = QPushButton(ButtonList)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setStyleSheet(u"QPushButton {\n"
"	height: 20px;\n"
"	background-color: rgba(37, 131, 255, 50);\n"
"	border-radius: 5px;\n"
"	padding: 2 10 5 10;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgba(37, 131, 255, 90)\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: rgb(0, 53, 93)\n"
"}")

        self.verticalLayout.addWidget(self.pushButton)


        self.retranslateUi(ButtonList)

        QMetaObject.connectSlotsByName(ButtonList)
    # setupUi

    def retranslateUi(self, ButtonList):
        ButtonList.setWindowTitle(QCoreApplication.translate("ButtonList", u"Form", None))
        self.pushButton.setText(QCoreApplication.translate("ButtonList", u"\u0422\u0435\u043a\u0441\u0442", None))
    # retranslateUi

