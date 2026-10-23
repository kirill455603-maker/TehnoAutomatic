# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_page_sverlilnaya_faska.ui'
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
from PySide6.QtWidgets import (QApplication, QDoubleSpinBox, QFrame, QHBoxLayout,
    QLabel, QSizePolicy, QSpacerItem, QSpinBox,
    QVBoxLayout, QWidget)

class Ui_PageSverlilnayaFaska(object):
    def setupUi(self, PageSverlilnayaFaska):
        if not PageSverlilnayaFaska.objectName():
            PageSverlilnayaFaska.setObjectName(u"PageSverlilnayaFaska")
        PageSverlilnayaFaska.resize(843, 300)
        PageSverlilnayaFaska.setStyleSheet(u"color: white;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(0, 57, 95), stop:1 rgb(0, 83, 122))")
        self.verticalLayout = QVBoxLayout(PageSverlilnayaFaska)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(PageSverlilnayaFaska)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setStyleSheet(u"border: none;\n"
"background: none;\n"
"")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, 10, -1, -1)
        self.line = QFrame(PageSverlilnayaFaska)
        self.line.setObjectName(u"line")
        self.line.setStyleSheet(u"background: rgba(255, 255, 255, 20);")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_2.addWidget(self.line)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, 0, -1, -1)
        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_7)

        self.label_10 = QLabel(PageSverlilnayaFaska)
        self.label_10.setObjectName(u"label_10")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy)
        font1 = QFont()
        font1.setFamilies([u"Onyx"])
        font1.setPointSize(11)
        self.label_10.setFont(font1)
        self.label_10.setStyleSheet(u"background-color: none")
        self.label_10.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label_10)

        self.doubleSpinBox_diameter = QDoubleSpinBox(PageSverlilnayaFaska)
        self.doubleSpinBox_diameter.setObjectName(u"doubleSpinBox_diameter")
        self.doubleSpinBox_diameter.setStyleSheet(u"QDoubleSpinBox {\n"
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
        self.doubleSpinBox_diameter.setMaximum(1000.000000000000000)

        self.horizontalLayout_3.addWidget(self.doubleSpinBox_diameter)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_8)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.length_div = QWidget(PageSverlilnayaFaska)
        self.length_div.setObjectName(u"length_div")
        self.length_div.setStyleSheet(u"background: none;")
        self.horizontalLayout_4 = QHBoxLayout(self.length_div)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(-1, 1, -1, -1)
        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_9)

        self.label_11 = QLabel(self.length_div)
        self.label_11.setObjectName(u"label_11")
        sizePolicy.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy)
        self.label_11.setFont(font1)
        self.label_11.setStyleSheet(u"background-color: none")
        self.label_11.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_4.addWidget(self.label_11)

        self.doubleSpinBox_length = QDoubleSpinBox(self.length_div)
        self.doubleSpinBox_length.setObjectName(u"doubleSpinBox_length")
        self.doubleSpinBox_length.setStyleSheet(u"QDoubleSpinBox {\n"
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
        self.doubleSpinBox_length.setMaximum(1000.000000000000000)
        self.doubleSpinBox_length.setValue(1.000000000000000)

        self.horizontalLayout_4.addWidget(self.doubleSpinBox_length)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_10)


        self.verticalLayout_2.addWidget(self.length_div)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(-1, 0, -1, -1)
        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_13)

        self.label_13 = QLabel(PageSverlilnayaFaska)
        self.label_13.setObjectName(u"label_13")
        sizePolicy.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy)
        self.label_13.setFont(font1)
        self.label_13.setStyleSheet(u"background-color: none")
        self.label_13.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_5.addWidget(self.label_13)

        self.spinBox_angle = QSpinBox(PageSverlilnayaFaska)
        self.spinBox_angle.setObjectName(u"spinBox_angle")
        self.spinBox_angle.setStyleSheet(u"QSpinBox {\n"
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
        self.spinBox_angle.setMinimum(0)
        self.spinBox_angle.setMaximum(180)
        self.spinBox_angle.setValue(45)

        self.horizontalLayout_5.addWidget(self.spinBox_angle)

        self.horizontalSpacer_14 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_14)


        self.verticalLayout_2.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, 0, -1, -1)
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_5)

        self.label_9 = QLabel(PageSverlilnayaFaska)
        self.label_9.setObjectName(u"label_9")
        sizePolicy.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy)
        self.label_9.setFont(font1)
        self.label_9.setStyleSheet(u"background-color: none")
        self.label_9.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label_9)

        self.spinBox_count = QSpinBox(PageSverlilnayaFaska)
        self.spinBox_count.setObjectName(u"spinBox_count")
        self.spinBox_count.setStyleSheet(u"QSpinBox {\n"
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
        self.spinBox_count.setMinimum(1)
        self.spinBox_count.setMaximum(100)
        self.spinBox_count.setValue(1)

        self.horizontalLayout_2.addWidget(self.spinBox_count)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_6)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.widget_length_2 = QWidget(PageSverlilnayaFaska)
        self.widget_length_2.setObjectName(u"widget_length_2")
        self.widget_length_2.setStyleSheet(u"background: none;")
        self.horizontalLayout_6 = QHBoxLayout(self.widget_length_2)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(-1, 0, -1, 0)
        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_11)

        self.label_12 = QLabel(self.widget_length_2)
        self.label_12.setObjectName(u"label_12")
        sizePolicy.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy)
        self.label_12.setFont(font1)
        self.label_12.setStyleSheet(u"background-color: none")
        self.label_12.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_6.addWidget(self.label_12)

        self.doubleSpinBox_diameter_big = QDoubleSpinBox(self.widget_length_2)
        self.doubleSpinBox_diameter_big.setObjectName(u"doubleSpinBox_diameter_big")
        self.doubleSpinBox_diameter_big.setStyleSheet(u"QDoubleSpinBox {\n"
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
        self.doubleSpinBox_diameter_big.setMaximum(1000.000000000000000)

        self.horizontalLayout_6.addWidget(self.doubleSpinBox_diameter_big)

        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_12)


        self.verticalLayout_2.addWidget(self.widget_length_2)

        self.label_2 = QLabel(PageSverlilnayaFaska)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"background: none;")

        self.verticalLayout_2.addWidget(self.label_2, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)


        self.verticalLayout.addLayout(self.verticalLayout_2)

        self.verticalSpacer = QSpacerItem(714, 45, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.retranslateUi(PageSverlilnayaFaska)

        QMetaObject.connectSlotsByName(PageSverlilnayaFaska)
    # setupUi

    def retranslateUi(self, PageSverlilnayaFaska):
        PageSverlilnayaFaska.setWindowTitle(QCoreApplication.translate("PageSverlilnayaFaska", u"Form", None))
        self.label.setText(QCoreApplication.translate("PageSverlilnayaFaska", u"\u0421\u043e\u0437\u0434\u0430\u043d\u0438\u0435 \u0444\u0430\u0441\u043a\u0438", None))
        self.label_10.setText(QCoreApplication.translate("PageSverlilnayaFaska", u"\u0414\u0438\u0430\u043c\u0435\u0442\u0440 \u043e\u0442\u0432\u0435\u0440\u0441\u0442\u0438\u044f, \u0432 \u043a\u043e\u0442\u043e\u0440\u043e\u043c \u043d\u0430\u0434\u043e \u0441\u0434\u0435\u043b\u0430\u0442\u044c \u0444\u0430\u0441\u043a\u0443:", None))
        self.doubleSpinBox_diameter.setPrefix(QCoreApplication.translate("PageSverlilnayaFaska", u"\u00d8 ", None))
        self.doubleSpinBox_diameter.setSuffix("")
        self.label_11.setText(QCoreApplication.translate("PageSverlilnayaFaska", u"\u0417\u043d\u0430\u0447\u0435\u043d\u0438\u0435 \u0444\u0430\u0441\u043a\u0438:", None))
        self.doubleSpinBox_length.setPrefix(QCoreApplication.translate("PageSverlilnayaFaska", u"L = ", None))
        self.doubleSpinBox_length.setSuffix("")
        self.label_13.setText(QCoreApplication.translate("PageSverlilnayaFaska", u"\u0423\u0433\u043e\u043b \u0444\u0430\u0441\u043a\u0438:", None))
        self.label_9.setText(QCoreApplication.translate("PageSverlilnayaFaska", u"\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u043e\u0442\u0432\u0435\u0440\u0441\u0442\u0438\u0439:", None))
        self.spinBox_count.setSuffix(QCoreApplication.translate("PageSverlilnayaFaska", u" \u0448\u0442.", None))
        self.label_12.setText(QCoreApplication.translate("PageSverlilnayaFaska", u"\u041d\u043e\u043c\u0438\u043d\u0430\u043b\u044c\u043d\u044b\u0439 \u0434\u0438\u0430\u043c\u0435\u0442\u0440 \u0440\u0430\u0441\u043f\u043e\u043b\u043e\u0436\u0435\u043d\u0438\u044f:", None))
        self.doubleSpinBox_diameter_big.setPrefix(QCoreApplication.translate("PageSverlilnayaFaska", u"\u00d8 ", None))
        self.doubleSpinBox_diameter_big.setSuffix("")
        self.label_2.setText(QCoreApplication.translate("PageSverlilnayaFaska", u"(\u041d\u0435\u043e\u0431\u044f\u0437\u0430\u0442\u0435\u043b\u044c\u043d\u043e)", None))
    # retranslateUi

