# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_dialog_find_sverlo.ui'
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

class Ui_FindSverlo(object):
    def setupUi(self, FindSverlo):
        if not FindSverlo.objectName():
            FindSverlo.setObjectName(u"FindSverlo")
        FindSverlo.resize(400, 300)
        FindSverlo.setStyleSheet(u"color: white;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(0, 57, 95), stop:1 rgb(0, 83, 122))")
        self.verticalLayout = QVBoxLayout(FindSverlo)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.label_2 = QLabel(FindSverlo)
        self.label_2.setObjectName(u"label_2")
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"background-color: none;\n"
"\n"
"")

        self.verticalLayout.addWidget(self.label_2, 0, Qt.AlignmentFlag.AlignHCenter)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, 0, -1, -1)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.comboBox_diameter = QComboBox(FindSverlo)
        self.comboBox_diameter.setObjectName(u"comboBox_diameter")
        font1 = QFont()
        font1.setPointSize(11)
        self.comboBox_diameter.setFont(font1)
        self.comboBox_diameter.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.comboBox_diameter.setStyleSheet(u"QComboBox {\n"
"	padding: 5, 5, 5, 5;\n"
"	width: 60px;\n"
"	border: none;\n"
"	border-bottom: 1px solid white;\n"
"	background: rgba(255, 255, 255, 0);\n"
"	transition: color 0.3s ease;\n"
"	transition: border-bottom 0.4s ease;\n"
"	color: rgb(204, 204, 204);\n"
"	font-size: 11pt;\n"
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

        self.horizontalLayout.addWidget(self.comboBox_diameter, 0, Qt.AlignmentFlag.AlignHCenter)

        self.label = QLabel(FindSverlo)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"background-color: none;\n"
"")

        self.horizontalLayout.addWidget(self.label, 0, Qt.AlignmentFlag.AlignHCenter)

        self.comboBox_step = QComboBox(FindSverlo)
        self.comboBox_step.setObjectName(u"comboBox_step")
        self.comboBox_step.setFont(font1)
        self.comboBox_step.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.comboBox_step.setStyleSheet(u"QComboBox {\n"
"	padding: 5, 5, 5, 5;\n"
"	width: 60px;\n"
"	border: none;\n"
"	border-bottom: 1px solid white;\n"
"	background: rgba(255, 255, 255, 0);\n"
"	transition: color 0.3s ease;\n"
"	transition: border-bottom 0.4s ease;\n"
"	color: rgb(204, 204, 204);\n"
"	font-size: 11pt;\n"
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

        self.horizontalLayout.addWidget(self.comboBox_step)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.label_3 = QLabel(FindSverlo)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"background: none;\n"
"color: rgba(255, 255, 255, 99)")

        self.verticalLayout.addWidget(self.label_3, 0, Qt.AlignmentFlag.AlignHCenter)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.label_text = QLabel(FindSverlo)
        self.label_text.setObjectName(u"label_text")
        self.label_text.setStyleSheet(u"background: none;\n"
"color: rgb(254, 95, 32)")

        self.verticalLayout.addWidget(self.label_text, 0, Qt.AlignmentFlag.AlignHCenter)

        self.pushButton_save = QPushButton(FindSverlo)
        self.pushButton_save.setObjectName(u"pushButton_save")
        self.pushButton_save.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_save.setStyleSheet(u"QPushButton {\n"
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

        self.verticalLayout.addWidget(self.pushButton_save)


        self.retranslateUi(FindSverlo)

        QMetaObject.connectSlotsByName(FindSverlo)
    # setupUi

    def retranslateUi(self, FindSverlo):
        FindSverlo.setWindowTitle(QCoreApplication.translate("FindSverlo", u"\u041f\u043e\u0434\u0431\u043e\u0440 \u0441\u0432\u0435\u0440\u043b\u0430", None))
        self.label_2.setText(QCoreApplication.translate("FindSverlo", u"\u041f\u043e\u0434\u0431\u043e\u0440 \u0441\u0432\u0435\u0440\u043b\u0430", None))
        self.comboBox_diameter.setPlaceholderText(QCoreApplication.translate("FindSverlo", u"\u0420\u0435\u0437\u044c\u0431\u0430...", None))
        self.label.setText(QCoreApplication.translate("FindSverlo", u"\u0445", None))
        self.comboBox_step.setPlaceholderText(QCoreApplication.translate("FindSverlo", u"\u0428\u0430\u0433...", None))
        self.label_3.setText(QCoreApplication.translate("FindSverlo", u"\u041f\u043e\u0434\u0441\u043a\u0430\u0437\u043a\u0430: \u041f\u0435\u0440\u0432\u044b\u0439 \u0428\u0410\u0413 \u0432 \u0441\u043f\u0438\u0441\u043a\u0435 - \u041e\u0421\u041d\u041e\u0412\u041d\u041e\u0419", None))
        self.label_text.setText("")
        self.pushButton_save.setText(QCoreApplication.translate("FindSverlo", u"\u041f\u043e\u0434\u043e\u0431\u0440\u0430\u0442\u044c", None))
    # retranslateUi

