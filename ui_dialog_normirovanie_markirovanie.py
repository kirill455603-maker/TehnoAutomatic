# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_dialog_normirovanie_markirovanie.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QHBoxLayout, QLabel,
    QPushButton, QSizePolicy, QSpacerItem, QSpinBox,
    QVBoxLayout, QWidget)

class Ui_DialogMarkirovanie(object):
    def setupUi(self, DialogMarkirovanie):
        if not DialogMarkirovanie.objectName():
            DialogMarkirovanie.setObjectName(u"DialogMarkirovanie")
        DialogMarkirovanie.resize(400, 300)
        DialogMarkirovanie.setStyleSheet(u"color: white;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(0, 57, 95), stop:1 rgb(0, 83, 122));\n"
"")
        self.verticalLayout = QVBoxLayout(DialogMarkirovanie)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_2 = QLabel(DialogMarkirovanie)
        self.label_2.setObjectName(u"label_2")
        font = QFont()
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"background: none;")

        self.verticalLayout.addWidget(self.label_2, 0, Qt.AlignmentFlag.AlignHCenter)

        self.label = QLabel(DialogMarkirovanie)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"background: none;")

        self.verticalLayout.addWidget(self.label, 0, Qt.AlignmentFlag.AlignHCenter)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, 20, -1, -1)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.label_3 = QLabel(DialogMarkirovanie)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"background: none;")

        self.horizontalLayout.addWidget(self.label_3, 0, Qt.AlignmentFlag.AlignHCenter)

        self.spinBox = QSpinBox(DialogMarkirovanie)
        self.spinBox.setObjectName(u"spinBox")
        self.spinBox.setStyleSheet(u"QSpinBox {\n"
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

        self.horizontalLayout.addWidget(self.spinBox, 0, Qt.AlignmentFlag.AlignHCenter)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.btn_save = QPushButton(DialogMarkirovanie)
        self.btn_save.setObjectName(u"btn_save")
        self.btn_save.setStyleSheet(u"QPushButton {\n"
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

        self.verticalLayout.addWidget(self.btn_save, 0, Qt.AlignmentFlag.AlignHCenter)


        self.retranslateUi(DialogMarkirovanie)

        QMetaObject.connectSlotsByName(DialogMarkirovanie)
    # setupUi

    def retranslateUi(self, DialogMarkirovanie):
        DialogMarkirovanie.setWindowTitle(QCoreApplication.translate("DialogMarkirovanie", u"\u041d\u043e\u0440\u043c\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u0435 - \u043c\u0430\u0440\u043a\u0438\u0440\u043e\u0432\u043e\u0447\u043d\u0430\u044f", None))
        self.label_2.setText(QCoreApplication.translate("DialogMarkirovanie", u"\u041d\u043e\u043c\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u0435 - \u041c\u0430\u0440\u043a\u0438\u0440\u043e\u0432\u043e\u0447\u043d\u0430\u044f", None))
        self.label.setText(QCoreApplication.translate("DialogMarkirovanie", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0435 \u0434\u043b\u044f \u0437\u0430\u043f\u043e\u043b\u043d\u0435\u043d\u0438\u044f", None))
        self.label_3.setText(QCoreApplication.translate("DialogMarkirovanie", u"\u0423\u0441\u0442\u0430\u043d\u043e\u0432\u0438\u0442\u044c \u0432\u0440\u0435\u043c\u044f \u0434\u043b\u044f \u0432\u044b\u0431\u0440\u0430\u043d\u043d\u044b\u0445 \u0434\u0435\u0442\u0430\u043b\u0435\u0439: ", None))
        self.btn_save.setText(QCoreApplication.translate("DialogMarkirovanie", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
    # retranslateUi

