# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_widget_normirovanie_cutting.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDoubleSpinBox, QHBoxLayout,
    QLabel, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_WidgetCutting(object):
    def setupUi(self, WidgetCutting):
        if not WidgetCutting.objectName():
            WidgetCutting.setObjectName(u"WidgetCutting")
        WidgetCutting.resize(579, 300)
        WidgetCutting.setStyleSheet(u"")
        self.verticalLayout_2 = QVBoxLayout(WidgetCutting)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, -1, -1, 0)
        self.label_3 = QLabel(WidgetCutting)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"background: none;\n"
"padding: 5 2 2 5;\n"
"color: rgb(214, 214, 214);\n"
"border-bottom: 1px solid white;\n"
"\n"
"")

        self.verticalLayout_2.addWidget(self.label_3, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignBottom)

        self.verticalWidget = QWidget(WidgetCutting)
        self.verticalWidget.setObjectName(u"verticalWidget")
        self.verticalWidget.setStyleSheet(u"background: none;")
        self.verticalLayout = QVBoxLayout(self.verticalWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.label = QLabel(self.verticalWidget)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"background: none;\n"
"border: none;")

        self.horizontalLayout.addWidget(self.label)

        self.doubleSpinBox = QDoubleSpinBox(self.verticalWidget)
        self.doubleSpinBox.setObjectName(u"doubleSpinBox")
        self.doubleSpinBox.setStyleSheet(u"QDoubleSpinBox {\n"
"	padding: 2 5 2 5;	\n"
"	border: none;\n"
"	border-bottom: 1px solid white;\n"
"	border-radius: none;\n"
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
        self.doubleSpinBox.setMaximum(10000.000000000000000)

        self.horizontalLayout.addWidget(self.doubleSpinBox)

        self.label_4 = QLabel(self.verticalWidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"background: none;\n"
"border: none;")

        self.horizontalLayout.addWidget(self.label_4)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)

        self.label_2 = QLabel(self.verticalWidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"background: none;\n"
"border: none;")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.comboBox_details = QComboBox(self.verticalWidget)
        self.comboBox_details.setObjectName(u"comboBox_details")
        self.comboBox_details.setMinimumSize(QSize(300, 0))
        self.comboBox_details.setStyleSheet(u"QComboBox {\n"
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
        self.comboBox_details.setEditable(False)
        self.comboBox_details.setInsertPolicy(QComboBox.InsertPolicy.NoInsert)

        self.horizontalLayout_2.addWidget(self.comboBox_details)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_4)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.verticalLayout_2.addWidget(self.verticalWidget, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)


        self.retranslateUi(WidgetCutting)

        QMetaObject.connectSlotsByName(WidgetCutting)
    # setupUi

    def retranslateUi(self, WidgetCutting):
        WidgetCutting.setWindowTitle(QCoreApplication.translate("WidgetCutting", u"Form", None))
        self.label_3.setText(QCoreApplication.translate("WidgetCutting", u"\u041e\u043f\u0435\u0440\u0430\u0446\u0438\u044f: \u041e\u0442\u0440\u0435\u0437\u043d\u0430\u044f", None))
        self.label.setText(QCoreApplication.translate("WidgetCutting", u"\u0414\u0438\u0430\u043c\u0435\u0442\u0440:", None))
        self.label_4.setText(QCoreApplication.translate("WidgetCutting", u"\u043c\u043c.", None))
        self.label_2.setText(QCoreApplication.translate("WidgetCutting", u"\u041c\u0430\u0442\u0435\u0440\u0438\u0430\u043b:", None))
        self.comboBox_details.setCurrentText("")
        self.comboBox_details.setPlaceholderText(QCoreApplication.translate("WidgetCutting", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u043c\u0430\u0442\u0435\u0440\u0438\u0430\u043b...", None))
    # retranslateUi

