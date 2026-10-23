# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_dialog_normirovanie_select_turning_operation.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QHBoxLayout,
    QLabel, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(444, 297)
        Dialog.setStyleSheet(u"color: white;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(0, 57, 95), stop:1 rgb(0, 83, 122));\n"
"")
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"background: none;")

        self.verticalLayout.addWidget(self.label, 0, Qt.AlignmentFlag.AlignHCenter)

        self.comboBox_operations = QComboBox(Dialog)
        self.comboBox_operations.addItem("")
        self.comboBox_operations.addItem("")
        self.comboBox_operations.addItem("")
        self.comboBox_operations.addItem("")
        self.comboBox_operations.setObjectName(u"comboBox_operations")
        self.comboBox_operations.setMinimumSize(QSize(250, 0))
        self.comboBox_operations.setStyleSheet(u"QComboBox {\n"
"	padding: 3, 3, 3, 3;\n"
"	width: 60px;\n"
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

        self.verticalLayout.addWidget(self.comboBox_operations, 0, Qt.AlignmentFlag.AlignHCenter)

        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"background: none;\n"
"border: none;")

        self.verticalLayout.addWidget(self.label_2, 0, Qt.AlignmentFlag.AlignHCenter)

        self.comboBox_material = QComboBox(Dialog)
        self.comboBox_material.setObjectName(u"comboBox_material")
        self.comboBox_material.setMinimumSize(QSize(300, 0))
        self.comboBox_material.setStyleSheet(u"QComboBox {\n"
"	padding: 3, 3, 3, 3;\n"
"	width: 60px;\n"
"	border: none;\n"
"	border-radius: none;\n"
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
"	border-bottom: 1px "
                        "solid white;\n"
"}\n"
"\n"
"")
        self.comboBox_material.setEditable(False)
        self.comboBox_material.setInsertPolicy(QComboBox.InsertPolicy.NoInsert)

        self.verticalLayout.addWidget(self.comboBox_material, 0, Qt.AlignmentFlag.AlignHCenter)

        self.label_error = QLabel(Dialog)
        self.label_error.setObjectName(u"label_error")
        self.label_error.setStyleSheet(u"background: none;")

        self.verticalLayout.addWidget(self.label_error, 0, Qt.AlignmentFlag.AlignHCenter)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton_show_btn_operations = QPushButton(Dialog)
        self.pushButton_show_btn_operations.setObjectName(u"pushButton_show_btn_operations")
        self.pushButton_show_btn_operations.setStyleSheet(u"QPushButton {\n"
"	height: 20px;\n"
"	background-color: rgba(37, 131, 255, 50);\n"
"	padding: 2 10 5 10;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgba(37, 131, 255, 90)\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: rgb(0, 53, 93)\n"
"}")

        self.horizontalLayout.addWidget(self.pushButton_show_btn_operations)

        self.pushButton_show_btn_operations_2 = QPushButton(Dialog)
        self.pushButton_show_btn_operations_2.setObjectName(u"pushButton_show_btn_operations_2")
        self.pushButton_show_btn_operations_2.setStyleSheet(u"QPushButton {\n"
"	height: 20px;\n"
"	background-color: rgba(37, 131, 255, 50);\n"
"	padding: 2 10 5 10;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgba(37, 131, 255, 90)\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: rgb(0, 53, 93)\n"
"}")

        self.horizontalLayout.addWidget(self.pushButton_show_btn_operations_2)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"\u0414\u043e\u0431\u0430\u0432\u043b\u0435\u043d\u0438\u0435 \u0442\u043e\u043a\u0430\u0440\u043d\u043e\u0439 \u043e\u043f\u0435\u0440\u0430\u0446\u0438\u0438", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u0442\u0438\u043f \u043e\u0431\u0440\u0430\u0431\u043e\u0442\u043a\u0438:", None))
        self.comboBox_operations.setItemText(0, QCoreApplication.translate("Dialog", u"\u041f\u0440\u043e\u0434\u043e\u043b\u044c\u043d\u043e\u0435 \u0442\u043e\u0447\u0435\u043d\u0438\u0435 / \u0440\u0430\u0441\u0441\u0442\u0430\u0447\u0438\u0432\u0430\u043d\u0438\u0435", None))
        self.comboBox_operations.setItemText(1, QCoreApplication.translate("Dialog", u"\u041d\u0430\u0440\u0435\u0437\u0430\u043d\u0438\u0435 \u0440\u0435\u0437\u044c\u0431\u044b", None))
        self.comboBox_operations.setItemText(2, QCoreApplication.translate("Dialog", u"\u041f\u043e\u0434\u0440\u0435\u0437\u043a\u0430 \u0442\u043e\u0440\u0446\u0430", None))
        self.comboBox_operations.setItemText(3, QCoreApplication.translate("Dialog", u"\u041e\u0431\u0440\u0430\u0431\u043e\u0442\u043a\u0430 \u043a\u0430\u043d\u0430\u0432\u043e\u043a", None))

        self.label_2.setText(QCoreApplication.translate("Dialog", u"\u041c\u0430\u0442\u0435\u0440\u0438\u0430\u043b:", None))
        self.comboBox_material.setCurrentText("")
        self.comboBox_material.setPlaceholderText(QCoreApplication.translate("Dialog", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u043c\u0430\u0442\u0435\u0440\u0438\u0430\u043b...", None))
        self.label_error.setText("")
        self.pushButton_show_btn_operations.setText(QCoreApplication.translate("Dialog", u"\u2795 \u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.pushButton_show_btn_operations_2.setText(QCoreApplication.translate("Dialog", u"\u041e\u0442\u043c\u0435\u043d\u0430", None))
    # retranslateUi

