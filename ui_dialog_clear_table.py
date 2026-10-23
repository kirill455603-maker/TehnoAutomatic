# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_dialog_clear_table.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QSizePolicy, QSpacerItem, QTextBrowser, QVBoxLayout,
    QWidget)

class Ui_DialogClearTable(object):
    def setupUi(self, DialogClearTable):
        if not DialogClearTable.objectName():
            DialogClearTable.setObjectName(u"DialogClearTable")
        DialogClearTable.resize(400, 300)
        DialogClearTable.setWindowOpacity(0.900000000000000)
        DialogClearTable.setAutoFillBackground(False)
        DialogClearTable.setStyleSheet(u"color: white;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(0, 57, 95), stop:1 rgb(0, 83, 122))")
        self.verticalLayout = QVBoxLayout(DialogClearTable)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.textBrowser = QTextBrowser(DialogClearTable)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setStyleSheet(u"border: none;\n"
"background: transparent;")

        self.verticalLayout.addWidget(self.textBrowser)

        self.buttonBox = QDialogButtonBox(DialogClearTable)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setStyleSheet(u"QPushButton {\n"
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
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)
        self.buttonBox.setCenterButtons(True)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(DialogClearTable)
        self.buttonBox.accepted.connect(DialogClearTable.accept)
        self.buttonBox.rejected.connect(DialogClearTable.reject)

        QMetaObject.connectSlotsByName(DialogClearTable)
    # setupUi

    def retranslateUi(self, DialogClearTable):
        DialogClearTable.setWindowTitle(QCoreApplication.translate("DialogClearTable", u"Dialog", None))
        self.textBrowser.setHtml(QCoreApplication.translate("DialogClearTable", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">\u0415\u0441\u043b\u0438 \u0438\u0437\u043c\u0435\u043d\u0438\u0442\u044c \u043e\u043f\u0435\u0440\u0430\u0446\u0438\u044e, \u0442\u0430\u0431\u043b\u0438\u0446\u0430 \u0441 \u0437\u0430\u043f\u0438\u0441\u0430\u043d\u043d\u044b\u043c\u0438 \u043f\u0435\u0440\u0435\u0445\u043e\u0434\u0430\u043c\u0438 \u0431\u0443\u0434\u0435\u0442 \u0441\u0442\u0451\u0440"
                        "\u0442\u0430!</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:11pt;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">\u041d\u0430\u0436\u043c\u0438\u0442\u0435 &quot;</span><span style=\" font-size:11pt; font-weight:700; color:#ff6118;\">\u041e\u041a</span><span style=\" font-size:11pt;\">&quot;, \u0435\u0441\u043b\u0438 \u0436\u0435\u043b\u0430\u0435\u0442\u0435</span><span style=\" font-size:11pt; color:#c30f0f;\"> </span><span style=\" font-size:11pt; font-weight:700; color:#ff6118;\">\u0441\u0442\u0435\u0440\u0435\u0442\u044c</span><span style=\" font-size:11pt;\"> \u0434\u0430\u043d\u043d\u044b\u0435 \u0432 \u0442\u0430\u0431\u043b\u0438\u0446\u0435</span></p></body></html>", None))
    # retranslateUi

