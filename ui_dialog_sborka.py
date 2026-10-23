# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_dialog_sborka.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QGridLayout, QLabel,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_DialogSborka(object):
    def setupUi(self, DialogSborka):
        if not DialogSborka.objectName():
            DialogSborka.setObjectName(u"DialogSborka")
        DialogSborka.resize(584, 300)
        DialogSborka.setStyleSheet(u"color: white;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(0, 57, 95), stop:1 rgb(0, 83, 122))")
        self.verticalLayout = QVBoxLayout(DialogSborka)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_8 = QLabel(DialogSborka)
        self.label_8.setObjectName(u"label_8")
        font = QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet(u"background: none;\n"
"")

        self.verticalLayout.addWidget(self.label_8, 0, Qt.AlignmentFlag.AlignHCenter)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, 20, -1, -1)

        self.verticalLayout.addLayout(self.verticalLayout_2)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.label_9 = QLabel(DialogSborka)
        self.label_9.setObjectName(u"label_9")
        font1 = QFont()
        font1.setPointSize(10)
        font1.setBold(False)
        self.label_9.setFont(font1)
        self.label_9.setStyleSheet(u"background: none;\n"
"")

        self.verticalLayout.addWidget(self.label_9, 0, Qt.AlignmentFlag.AlignHCenter)

        self.label_text_input = QLabel(DialogSborka)
        self.label_text_input.setObjectName(u"label_text_input")
        self.label_text_input.setStyleSheet(u"background: none;")

        self.verticalLayout.addWidget(self.label_text_input, 0, Qt.AlignmentFlag.AlignHCenter)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.pushButton_add_detail = QPushButton(DialogSborka)
        self.pushButton_add_detail.setObjectName(u"pushButton_add_detail")
        self.pushButton_add_detail.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
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

        self.gridLayout.addWidget(self.pushButton_add_detail, 0, 1, 1, 1)

        self.pushButton_add_predlog = QPushButton(DialogSborka)
        self.pushButton_add_predlog.setObjectName(u"pushButton_add_predlog")
        self.pushButton_add_predlog.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_add_predlog.setStyleSheet(u"QPushButton {\n"
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

        self.gridLayout.addWidget(self.pushButton_add_predlog, 0, 0, 1, 1)

        self.pushButton_add_bolts = QPushButton(DialogSborka)
        self.pushButton_add_bolts.setObjectName(u"pushButton_add_bolts")
        self.pushButton_add_bolts.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_add_bolts.setStyleSheet(u"QPushButton {\n"
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

        self.gridLayout.addWidget(self.pushButton_add_bolts, 1, 0, 1, 1)

        self.pushButton_add_deistvie = QPushButton(DialogSborka)
        self.pushButton_add_deistvie.setObjectName(u"pushButton_add_deistvie")
        self.pushButton_add_deistvie.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_add_deistvie.setStyleSheet(u"QPushButton {\n"
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

        self.gridLayout.addWidget(self.pushButton_add_deistvie, 0, 2, 1, 1)

        self.btn_delete_el = QPushButton(DialogSborka)
        self.btn_delete_el.setObjectName(u"btn_delete_el")
        self.btn_delete_el.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_delete_el.setStyleSheet(u"QPushButton {\n"
"	border: 1px solid;\n"
"	border-color: white;\n"
"	border-radius: 5px;\n"
"	height: 20px;\n"
"	background-color: rgb(255, 44, 16);\n"
"	padding: 2 5 2 5\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(139, 11, 11)\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: rgb(0, 53, 93)\n"
"}")

        self.gridLayout.addWidget(self.btn_delete_el, 1, 2, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.pushButton_save_result = QPushButton(DialogSborka)
        self.pushButton_save_result.setObjectName(u"pushButton_save_result")
        self.pushButton_save_result.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_save_result.setStyleSheet(u"QPushButton {\n"
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

        self.verticalLayout.addWidget(self.pushButton_save_result, 0, Qt.AlignmentFlag.AlignHCenter)


        self.retranslateUi(DialogSborka)

        QMetaObject.connectSlotsByName(DialogSborka)
    # setupUi

    def retranslateUi(self, DialogSborka):
        DialogSborka.setWindowTitle(QCoreApplication.translate("DialogSborka", u"\u0421\u0431\u043e\u0440\u043a\u0430", None))
        self.label_8.setText(QCoreApplication.translate("DialogSborka", u"\u0421\u0431\u043e\u0440\u043a\u0430", None))
        self.label_9.setText(QCoreApplication.translate("DialogSborka", u"\u0422\u0435\u043a\u0441\u0442 \u0432\u044b\u0432\u043e\u0434\u0430:", None))
        self.label_text_input.setText("")
        self.pushButton_add_detail.setText(QCoreApplication.translate("DialogSborka", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0434\u0435\u0442\u0430\u043b\u044c", None))
        self.pushButton_add_predlog.setText(QCoreApplication.translate("DialogSborka", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u043f\u0440\u0435\u0434\u043b\u043e\u0433", None))
        self.pushButton_add_bolts.setText(QCoreApplication.translate("DialogSborka", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0431\u043e\u043b\u0442, \u0433\u0430\u0439\u043a\u0443, \u0432\u0438\u043d\u0442, \u0448\u043f\u0438\u043b\u044c\u043a\u0443", None))
        self.pushButton_add_deistvie.setText(QCoreApplication.translate("DialogSborka", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0434\u0435\u0439\u0441\u0442\u0432\u0438\u0435", None))
        self.btn_delete_el.setText(QCoreApplication.translate("DialogSborka", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c \u043f\u043e\u0441\u043b\u0435\u0434\u043d\u0438\u0439 \u044d\u043b\u0435\u043c\u0435\u043d\u0442", None))
        self.pushButton_save_result.setText(QCoreApplication.translate("DialogSborka", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u0442\u0435\u043a\u0441\u0442 \u0432\u044b\u0432\u043e\u0434\u0430", None))
    # retranslateUi

