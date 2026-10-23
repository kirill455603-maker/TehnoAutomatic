# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_widget_normirovanie_turning_button.ui'
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
from PySide6.QtWidgets import (QApplication, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_WidgetTurningButton(object):
    def setupUi(self, WidgetTurningButton):
        if not WidgetTurningButton.objectName():
            WidgetTurningButton.setObjectName(u"WidgetTurningButton")
        WidgetTurningButton.resize(400, 300)
        self.verticalLayout = QVBoxLayout(WidgetTurningButton)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.layout_with_turning = QVBoxLayout()
        self.layout_with_turning.setObjectName(u"layout_with_turning")

        self.verticalLayout.addLayout(self.layout_with_turning)

        self.pushButton_add_operation_turning = QPushButton(WidgetTurningButton)
        self.pushButton_add_operation_turning.setObjectName(u"pushButton_add_operation_turning")
        self.pushButton_add_operation_turning.setStyleSheet(u"QPushButton {\n"
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

        self.verticalLayout.addWidget(self.pushButton_add_operation_turning, 0, Qt.AlignmentFlag.AlignHCenter)

        self.verticalSpacer = QSpacerItem(379, 236, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.retranslateUi(WidgetTurningButton)

        QMetaObject.connectSlotsByName(WidgetTurningButton)
    # setupUi

    def retranslateUi(self, WidgetTurningButton):
        WidgetTurningButton.setWindowTitle(QCoreApplication.translate("WidgetTurningButton", u"Form", None))
        self.pushButton_add_operation_turning.setText(QCoreApplication.translate("WidgetTurningButton", u" \u2795  \u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0442\u043e\u043a\u0430\u0440\u043d\u0443\u044e \u043e\u043f\u0435\u0440\u0430\u0446\u0438\u044e", None))
    # retranslateUi

