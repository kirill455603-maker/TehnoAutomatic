# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_dialog_predlog.ui'
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
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QTextEdit, QVBoxLayout, QWidget)

class Ui_DialogPredlog(object):
    def setupUi(self, DialogPredlog):
        if not DialogPredlog.objectName():
            DialogPredlog.setObjectName(u"DialogPredlog")
        DialogPredlog.resize(633, 439)
        DialogPredlog.setStyleSheet(u"color: white;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(0, 57, 95), stop:1 rgb(0, 83, 122))")
        self.verticalLayout = QVBoxLayout(DialogPredlog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_8 = QLabel(DialogPredlog)
        self.label_8.setObjectName(u"label_8")
        font = QFont()
        font.setPointSize(11)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet(u"background: none;\n"
"border: none;\n"
"\n"
"border-radius: none;")

        self.verticalLayout.addWidget(self.label_8, 0, Qt.AlignmentFlag.AlignHCenter)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_6 = QLabel(DialogPredlog)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font)
        self.label_6.setStyleSheet(u"background: none;\n"
"border: none;\n"
"\n"
"border-radius: none;")

        self.horizontalLayout.addWidget(self.label_6)

        self.lineEdit = QLineEdit(DialogPredlog)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setStyleSheet(u"QLineEdit {\n"
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

        self.horizontalLayout.addWidget(self.lineEdit, 0, Qt.AlignmentFlag.AlignHCenter)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_9 = QLabel(DialogPredlog)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font)
        self.label_9.setStyleSheet(u"background: none;\n"
"border: none;\n"
"\n"
"border-radius: none;")

        self.horizontalLayout_2.addWidget(self.label_9)

        self.lineEdit_2 = QLineEdit(DialogPredlog)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setStyleSheet(u"QLineEdit {\n"
"	padding: 2 5 2 5;	\n"
"	width: 300;\n"
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

        self.horizontalLayout_2.addWidget(self.lineEdit_2, 0, Qt.AlignmentFlag.AlignHCenter)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.label_7 = QLabel(DialogPredlog)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font)
        self.label_7.setStyleSheet(u"background: none;\n"
"border: none;\n"
"\n"
"border-radius: none;")

        self.verticalLayout.addWidget(self.label_7)

        self.textEdit = QTextEdit(DialogPredlog)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setStyleSheet(u"QTextEdit {\n"
"	padding: 2 5 2 5;	\n"
"	border: none;\n"
"	border: 1px solid white;\n"
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

        self.verticalLayout.addWidget(self.textEdit)

        self.btn_save_result_predlog = QPushButton(DialogPredlog)
        self.btn_save_result_predlog.setObjectName(u"btn_save_result_predlog")
        font1 = QFont()
        font1.setBold(True)
        self.btn_save_result_predlog.setFont(font1)
        self.btn_save_result_predlog.setStyleSheet(u"QPushButton {\n"
"	border: 1px solid;\n"
"	border-color: white;\n"
"	border-radius: 10px;\n"
"	height: 30px;\n"
"	width: 150px;\n"
"	background-color: none;\n"
"	padding: 2 5 2 5\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(0, 111, 171)\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: rgb(0, 53, 93)\n"
"}")

        self.verticalLayout.addWidget(self.btn_save_result_predlog, 0, Qt.AlignmentFlag.AlignHCenter)


        self.retranslateUi(DialogPredlog)

        QMetaObject.connectSlotsByName(DialogPredlog)
    # setupUi

    def retranslateUi(self, DialogPredlog):
        DialogPredlog.setWindowTitle(QCoreApplication.translate("DialogPredlog", u"\u041f\u0440\u0435\u0434\u043b\u043e\u0436\u0435\u043d\u0438\u044f \u043f\u043e \u0443\u043b\u0443\u0447\u0448\u0435\u043d\u0438\u044e", None))
        self.label_8.setText(QCoreApplication.translate("DialogPredlog", u"\u041e\u0442\u043f\u0440\u0430\u0432\u043a\u0430 \u043f\u0440\u0435\u0434\u043b\u043e\u0436\u0435\u043d\u0438\u044f \u0434\u043b\u044f \u0443\u043b\u0443\u0447\u0448\u0435\u043d\u0438\u044f \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u044b", None))
        self.label_6.setText(QCoreApplication.translate("DialogPredlog", u"\u0418\u043c\u044f:", None))
        self.label_9.setText(QCoreApplication.translate("DialogPredlog", u"\u0422\u0435\u043c\u0430:", None))
        self.label_7.setText(QCoreApplication.translate("DialogPredlog", u"\u041f\u0440\u0435\u0434\u043b\u043e\u0436\u0435\u043d\u0438\u0435: ", None))
        self.btn_save_result_predlog.setText(QCoreApplication.translate("DialogPredlog", u"\u041e\u0442\u043f\u0440\u0430\u0432\u0438\u0442\u044c \u043f\u0440\u0435\u0434\u043b\u043e\u0436\u0435\u043d\u0438\u0435", None))
    # retranslateUi

