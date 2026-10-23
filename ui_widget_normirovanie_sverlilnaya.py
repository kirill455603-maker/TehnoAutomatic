# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_widget_normirovanie_sverlilnaya.ui'
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
    QLabel, QPushButton, QSizePolicy, QSpacerItem,
    QSpinBox, QVBoxLayout, QWidget)

class Ui_Sverlilnaya(object):
    def setupUi(self, Sverlilnaya):
        if not Sverlilnaya.objectName():
            Sverlilnaya.setObjectName(u"Sverlilnaya")
        Sverlilnaya.resize(445, 300)
        self.verticalLayout_2 = QVBoxLayout(Sverlilnaya)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.widget = QWidget(Sverlilnaya)
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

        self.doubleSpinBox_diameter = QDoubleSpinBox(self.widget)
        self.doubleSpinBox_diameter.setObjectName(u"doubleSpinBox_diameter")
        self.doubleSpinBox_diameter.setStyleSheet(u"QDoubleSpinBox {\n"
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
        self.doubleSpinBox_diameter.setMaximum(10000.000000000000000)

        self.horizontalLayout.addWidget(self.doubleSpinBox_diameter)

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

        self.doubleSpinBox_length = QDoubleSpinBox(self.widget)
        self.doubleSpinBox_length.setObjectName(u"doubleSpinBox_length")
        self.doubleSpinBox_length.setStyleSheet(u"QDoubleSpinBox {\n"
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
        self.doubleSpinBox_length.setMaximum(10000.000000000000000)

        self.horizontalLayout_4.addWidget(self.doubleSpinBox_length)

        self.label_6 = QLabel(self.widget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setStyleSheet(u"background: none;\n"
"border: none;")

        self.horizontalLayout_4.addWidget(self.label_6)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_8)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_9)

        self.label_7 = QLabel(self.widget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setStyleSheet(u"background: none;\n"
"border: none;")

        self.horizontalLayout_5.addWidget(self.label_7)

        self.spinBox_count = QSpinBox(self.widget)
        self.spinBox_count.setObjectName(u"spinBox_count")
        self.spinBox_count.setStyleSheet(u"QSpinBox {\n"
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
        self.spinBox_count.setMinimum(1)
        self.spinBox_count.setValue(1)

        self.horizontalLayout_5.addWidget(self.spinBox_count)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_10)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_11)

        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"background: none;\n"
"border: none;")

        self.horizontalLayout_6.addWidget(self.label_3, 0, Qt.AlignmentFlag.AlignHCenter)

        self.comboBox_material = QComboBox(self.widget)
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

        self.horizontalLayout_6.addWidget(self.comboBox_material)

        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_12)


        self.verticalLayout.addLayout(self.horizontalLayout_6)

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


        self.retranslateUi(Sverlilnaya)

        QMetaObject.connectSlotsByName(Sverlilnaya)
    # setupUi

    def retranslateUi(self, Sverlilnaya):
        Sverlilnaya.setWindowTitle(QCoreApplication.translate("Sverlilnaya", u"Form", None))
        self.label_5.setText(QCoreApplication.translate("Sverlilnaya", u"\u041e\u043f\u0435\u0440\u0430\u0446\u0438\u044f: \u0441\u0432\u0435\u0440\u043b\u0438\u043b\u044c\u043d\u0430\u044f", None))
        self.label.setText(QCoreApplication.translate("Sverlilnaya", u"\u0414\u0438\u0430\u043c\u0435\u0442\u0440 \u0441\u0432\u0435\u0440\u043b\u0430", None))
        self.label_4.setText(QCoreApplication.translate("Sverlilnaya", u"\u043c\u043c.", None))
        self.label_2.setText(QCoreApplication.translate("Sverlilnaya", u"\u0413\u043b\u0443\u0431\u0438\u043d\u0430", None))
        self.label_6.setText(QCoreApplication.translate("Sverlilnaya", u"\u043c\u043c.", None))
        self.label_7.setText(QCoreApplication.translate("Sverlilnaya", u"\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e", None))
        self.label_3.setText(QCoreApplication.translate("Sverlilnaya", u"\u041c\u0430\u0442\u0435\u0440\u0438\u0430\u043b:", None))
        self.comboBox_material.setCurrentText("")
        self.comboBox_material.setPlaceholderText(QCoreApplication.translate("Sverlilnaya", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u043c\u0430\u0442\u0435\u0440\u0438\u0430\u043b...", None))
        self.label_info.setText("")
        self.pushButton_delete_operation.setText(QCoreApplication.translate("Sverlilnaya", u"\U0001f5d1\U0000fe0f \U00000423\U00000434\U00000430\U0000043b\U00000438\U00000442\U0000044c \U00000441\U00000432\U00000435\U00000440\U0000043b\U00000438\U0000043b\U0000044c\U0000043d\U00000443\U0000044e \U0000043e\U0000043f\U00000435\U00000440\U00000430\U00000446\U00000438\U0000044e", None))
    # retranslateUi

