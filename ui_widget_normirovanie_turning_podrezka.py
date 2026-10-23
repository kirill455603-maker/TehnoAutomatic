# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_widget_normirovanie_turning_podrezka.ui'
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
from PySide6.QtWidgets import (QApplication, QDoubleSpinBox, QHBoxLayout, QLabel,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_WidgetPodrezka(object):
    def setupUi(self, WidgetPodrezka):
        if not WidgetPodrezka.objectName():
            WidgetPodrezka.setObjectName(u"WidgetPodrezka")
        WidgetPodrezka.resize(414, 300)
        self.verticalLayout_2 = QVBoxLayout(WidgetPodrezka)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.widget = QWidget(WidgetPodrezka)
        self.widget.setObjectName(u"widget")
        self.widget.setStyleSheet(u"background: none;\n"
"border-bottom: 1px solid white;")
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalWidget = QWidget(self.widget)
        self.horizontalWidget.setObjectName(u"horizontalWidget")
        self.horizontalWidget.setStyleSheet(u"border-bottom: 1px solid white;\n"
"background: none;")
        self.horizontalLayout_3 = QHBoxLayout(self.horizontalWidget)
        self.horizontalLayout_3.setSpacing(10)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, -1, -1, 1)
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_5)

        self.label_5 = QLabel(self.horizontalWidget)
        self.label_5.setObjectName(u"label_5")
        font = QFont()
        font.setUnderline(False)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet(u"padding: 5 2 2 5;\n"
"color: rgb(214, 214, 214);\n"
"\n"
"")

        self.horizontalLayout_3.addWidget(self.label_5, 0, Qt.AlignmentFlag.AlignBottom)

        self.label_3 = QLabel(self.horizontalWidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"padding: 5 2 2 5;\n"
"color: rgb(214, 214, 214);\n"
"\n"
"")

        self.horizontalLayout_3.addWidget(self.label_3, 0, Qt.AlignmentFlag.AlignBottom)

        self.label_type_material = QLabel(self.horizontalWidget)
        self.label_type_material.setObjectName(u"label_type_material")
        self.label_type_material.setStyleSheet(u"padding: 5 2 2 5;\n"
"color: rgb(214, 214, 214);\n"
"\n"
"")

        self.horizontalLayout_3.addWidget(self.label_type_material, 0, Qt.AlignmentFlag.AlignBottom)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_6)


        self.verticalLayout.addWidget(self.horizontalWidget, 0, Qt.AlignmentFlag.AlignHCenter)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"background: none;\n"
"border: none;")

        self.horizontalLayout.addWidget(self.label)

        self.doubleSpinBox_diameter_zag = QDoubleSpinBox(self.widget)
        self.doubleSpinBox_diameter_zag.setObjectName(u"doubleSpinBox_diameter_zag")
        self.doubleSpinBox_diameter_zag.setStyleSheet(u"QDoubleSpinBox {\n"
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
        self.doubleSpinBox_diameter_zag.setMaximum(10000.000000000000000)

        self.horizontalLayout.addWidget(self.doubleSpinBox_diameter_zag)

        self.label_4 = QLabel(self.widget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"background: none;\n"
"border: none;")

        self.horizontalLayout.addWidget(self.label_4)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_7)

        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"background: none;\n"
"border: none;")

        self.horizontalLayout_4.addWidget(self.label_2)

        self.doubleSpinBox_diameter_det = QDoubleSpinBox(self.widget)
        self.doubleSpinBox_diameter_det.setObjectName(u"doubleSpinBox_diameter_det")
        self.doubleSpinBox_diameter_det.setStyleSheet(u"QDoubleSpinBox {\n"
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
        self.doubleSpinBox_diameter_det.setMaximum(10000.000000000000000)

        self.horizontalLayout_4.addWidget(self.doubleSpinBox_diameter_det)

        self.label_6 = QLabel(self.widget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setStyleSheet(u"background: none;\n"
"border: none;")

        self.horizontalLayout_4.addWidget(self.label_6)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_8)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.label_info = QLabel(self.widget)
        self.label_info.setObjectName(u"label_info")

        self.verticalLayout.addWidget(self.label_info, 0, Qt.AlignmentFlag.AlignHCenter)

        self.pushButton_delete_operation = QPushButton(self.widget)
        self.pushButton_delete_operation.setObjectName(u"pushButton_delete_operation")
        self.pushButton_delete_operation.setStyleSheet(u"QPushButton {\n"
"	height: 20px;\n"
"	background-color: rgba(255, 39, 39, 50);\n"
"	padding: 2 10 5 10;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgba(37, 131, 255, 90)\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: rgb(0, 53, 93)\n"
"}")

        self.verticalLayout.addWidget(self.pushButton_delete_operation, 0, Qt.AlignmentFlag.AlignHCenter)


        self.verticalLayout_2.addWidget(self.widget)


        self.retranslateUi(WidgetPodrezka)

        QMetaObject.connectSlotsByName(WidgetPodrezka)
    # setupUi

    def retranslateUi(self, WidgetPodrezka):
        WidgetPodrezka.setWindowTitle(QCoreApplication.translate("WidgetPodrezka", u"Form", None))
        self.label_5.setText(QCoreApplication.translate("WidgetPodrezka", u"\u041e\u043f\u0435\u0440\u0430\u0446\u0438\u044f: \u0442\u043e\u043a\u0430\u0440\u043d\u0430\u044f", None))
        self.label_3.setText(QCoreApplication.translate("WidgetPodrezka", u"\u0422\u0438\u043f: \u043f\u043e\u0434\u0440\u0435\u0437\u043a\u0430 \u0442\u043e\u0440\u0446\u0430", None))
        self.label_type_material.setText(QCoreApplication.translate("WidgetPodrezka", u"\u041c\u0430\u0442\u0435\u0440\u0438\u0430\u043b: ", None))
        self.label.setText(QCoreApplication.translate("WidgetPodrezka", u"\u0414\u0438\u0430\u043c\u0435\u0442\u0440 \u043d\u0430\u0447\u0430\u043b\u044c\u043d\u044b\u0439:", None))
        self.label_4.setText(QCoreApplication.translate("WidgetPodrezka", u"\u043c\u043c.", None))
        self.label_2.setText(QCoreApplication.translate("WidgetPodrezka", u"\u0414\u0438\u0430\u043c\u0435\u0442\u0440 \u043a\u043e\u043d\u0435\u0447\u043d\u044b\u0439:", None))
        self.label_6.setText(QCoreApplication.translate("WidgetPodrezka", u"\u043c\u043c.", None))
        self.label_info.setText("")
        self.pushButton_delete_operation.setText(QCoreApplication.translate("WidgetPodrezka", u"\U0001f5d1\U0000fe0f \U00000423\U00000434\U00000430\U0000043b\U00000438\U00000442\U0000044c \U00000442\U0000043e\U0000043a\U00000430\U00000440\U0000043d\U00000443\U0000044e \U0000043e\U0000043f\U00000435\U00000440\U00000430\U00000446\U00000438\U0000044e", None))
    # retranslateUi

