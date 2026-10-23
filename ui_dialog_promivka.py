# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_dialog_promivka.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_DialogPromivka(object):
    def setupUi(self, DialogPromivka):
        if not DialogPromivka.objectName():
            DialogPromivka.setObjectName(u"DialogPromivka")
        DialogPromivka.resize(496, 225)
        DialogPromivka.setMaximumSize(QSize(500, 225))
        DialogPromivka.setStyleSheet(u"color: white;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(0, 57, 95), stop:1 rgb(0, 83, 122))")
        self.verticalLayout = QVBoxLayout(DialogPromivka)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_8 = QLabel(DialogPromivka)
        self.label_8.setObjectName(u"label_8")
        font = QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet(u"background: none;\n"
"")

        self.verticalLayout.addWidget(self.label_8, 0, Qt.AlignmentFlag.AlignHCenter)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.label_24 = QLabel(DialogPromivka)
        self.label_24.setObjectName(u"label_24")
        font1 = QFont()
        font1.setPointSize(10)
        font1.setBold(True)
        self.label_24.setFont(font1)
        self.label_24.setStyleSheet(u"background: none;")

        self.verticalLayout.addWidget(self.label_24, 0, Qt.AlignmentFlag.AlignHCenter)

        self.label_2 = QLabel(DialogPromivka)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"background: none;")

        self.verticalLayout.addWidget(self.label_2, 0, Qt.AlignmentFlag.AlignHCenter)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.pushButton_save_result = QPushButton(DialogPromivka)
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

        self.pushButton_close = QPushButton(DialogPromivka)
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


        self.retranslateUi(DialogPromivka)

        QMetaObject.connectSlotsByName(DialogPromivka)
    # setupUi

    def retranslateUi(self, DialogPromivka):
        DialogPromivka.setWindowTitle(QCoreApplication.translate("DialogPromivka", u"\u041f\u0440\u043e\u043c\u044b\u0432\u043a\u0430", None))
        self.label_8.setText(QCoreApplication.translate("DialogPromivka", u"\u041f\u0440\u043e\u043c\u044b\u0432\u043a\u0430", None))
        self.label_24.setText(QCoreApplication.translate("DialogPromivka", u"\u0422\u0435\u043a\u0441\u0442 \u0431\u0435\u0437 \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u043e\u0432:", None))
        self.label_2.setText(QCoreApplication.translate("DialogPromivka", u"\u041f\u0440\u043e\u043c\u044b\u0442\u044c \u0434\u0435\u0442\u0430\u043b\u044c, \u0441\u043e\u0431\u043b\u044e\u0434\u0430\u044f \u0442\u0440\u0435\u0431\u043e\u0432\u0430\u043d\u0438\u044f \u0442\u0435\u0445\u043d\u043e\u043b\u043e\u0433\u0438\u0447\u0435\u0441\u043a\u043e\u0439 \u0438\u043d\u0441\u0442\u0440\u0443\u043a\u0446\u0438\u0438 0601.25000.00041", None))
        self.pushButton_save_result.setText(QCoreApplication.translate("DialogPromivka", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0442\u0435\u043a\u0441\u0442", None))
        self.pushButton_close.setText(QCoreApplication.translate("DialogPromivka", u"\u0417\u0430\u043a\u0440\u044b\u0442\u044c \u043e\u043a\u043d\u043e", None))
    # retranslateUi

