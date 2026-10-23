# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_page_sverlilnaya_start.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDoubleSpinBox, QFrame,
    QGroupBox, QHBoxLayout, QLabel, QPushButton,
    QSizePolicy, QSpacerItem, QSpinBox, QVBoxLayout,
    QWidget)
import res_rc

class Ui_PageSverlilnayaStart(object):
    def setupUi(self, PageSverlilnayaStart):
        if not PageSverlilnayaStart.objectName():
            PageSverlilnayaStart.setObjectName(u"PageSverlilnayaStart")
        PageSverlilnayaStart.resize(830, 343)
        PageSverlilnayaStart.setStyleSheet(u"color: white;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(0, 57, 95), stop:1 rgb(0, 83, 122))")
        self.verticalLayout = QVBoxLayout(PageSverlilnayaStart)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(PageSverlilnayaStart)
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

        self.label_7 = QLabel(PageSverlilnayaStart)
        self.label_7.setObjectName(u"label_7")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        font1 = QFont()
        font1.setFamilies([u"Onyx"])
        font1.setPointSize(10)
        self.label_7.setFont(font1)
        self.label_7.setStyleSheet(u"background-color: none")
        self.label_7.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.label_7)

        self.horizontalGroupBox_4 = QGroupBox(PageSverlilnayaStart)
        self.horizontalGroupBox_4.setObjectName(u"horizontalGroupBox_4")
        self.horizontalGroupBox_4.setStyleSheet(u"QGroupBox {\n"
"	border: none;\n"
"}\n"
"QPushButton {\n"
"	background:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(12, 123, 147, 255), stop:1 rgba(0, 168, 204, 255));\n"
"	border: none;\n"
"	font-size: 11px;\n"
"	padding: 5 10 5 10;\n"
"	width: 100px;\n"
"	border: 1px solid qradialgradient(spread:pad, cx:0.506, cy:1, radius:1.147, fx:0.494318, fy:1, stop:0 rgba(12, 123, 147, 255), stop:1 rgba(255, 255, 255, 0));\n"
"}\n"
"QPushButton:hover {\n"
"	color: rgb(0, 168, 204);\n"
"	border-left: 1px solid rgb(10, 169, 255);\n"
"	border-right: 1px solid rgb(10, 169, 255);\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.477, x2:1, y2:0.518, stop:0 rgba(15, 109, 159, 64), stop:0.505682 rgba(15, 111, 149, 0), stop:1 rgba(15, 112, 139, 58));\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: rgb(0, 53, 93)\n"
"}\n"
"QPushButton:checked {\n"
"	background: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(12, 123, 147, 177), stop:1 rgba(39, 73, 109, 255"
                        "));\n"
"	color: rgb(0, 168, 204);\n"
"}")
        self.horizontalLayout_5 = QHBoxLayout(self.horizontalGroupBox_4)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer)

        self.pushButton_infinity = QPushButton(self.horizontalGroupBox_4)
        self.pushButton_infinity.setObjectName(u"pushButton_infinity")
        self.pushButton_infinity.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_infinity.setStyleSheet(u"")
        self.pushButton_infinity.setCheckable(True)
        self.pushButton_infinity.setChecked(True)
        self.pushButton_infinity.setAutoExclusive(True)

        self.horizontalLayout_5.addWidget(self.pushButton_infinity, 0, Qt.AlignmentFlag.AlignHCenter)

        self.pushButton_with_length = QPushButton(self.horizontalGroupBox_4)
        self.pushButton_with_length.setObjectName(u"pushButton_with_length")
        self.pushButton_with_length.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_with_length.setStyleSheet(u"")
        self.pushButton_with_length.setCheckable(True)
        self.pushButton_with_length.setAutoExclusive(True)

        self.horizontalLayout_5.addWidget(self.pushButton_with_length)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addWidget(self.horizontalGroupBox_4)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, 10, -1, -1)
        self.line = QFrame(PageSverlilnayaStart)
        self.line.setObjectName(u"line")
        self.line.setStyleSheet(u"background: rgba(255, 255, 255, 20);")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_2.addWidget(self.line)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, 0, -1, -1)
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)

        self.label_8 = QLabel(PageSverlilnayaStart)
        self.label_8.setObjectName(u"label_8")
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        font2 = QFont()
        font2.setFamilies([u"Onyx"])
        font2.setPointSize(11)
        self.label_8.setFont(font2)
        self.label_8.setStyleSheet(u"background-color: none;\n"
"")
        self.label_8.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout.addWidget(self.label_8)

        self.comboBox_diameter = QComboBox(PageSverlilnayaStart)
        self.comboBox_diameter.setObjectName(u"comboBox_diameter")
        font3 = QFont()
        font3.setPointSize(11)
        self.comboBox_diameter.setFont(font3)
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

        self.horizontalLayout.addWidget(self.comboBox_diameter)

        self.pushButton_find_sverlo = QPushButton(PageSverlilnayaStart)
        self.pushButton_find_sverlo.setObjectName(u"pushButton_find_sverlo")
        font4 = QFont()
        font4.setBold(True)
        self.pushButton_find_sverlo.setFont(font4)
        self.pushButton_find_sverlo.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_find_sverlo.setStyleSheet(u"QPushButton {\n"
"	width: 15;\n"
"	height: 15;\n"
"	background: rgba(0, 0, 0, 0);\n"
"	image: url(:/icons/find_white.png);\n"
"	\n"
"}\n"
"QPushButton:hover {\n"
"	image: url(:/icons/find_grey.png);\n"
"}\n"
"")
        self.pushButton_find_sverlo.setIconSize(QSize(16, 16))

        self.horizontalLayout.addWidget(self.pushButton_find_sverlo)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_4)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, 0, -1, -1)
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_5)

        self.label_9 = QLabel(PageSverlilnayaStart)
        self.label_9.setObjectName(u"label_9")
        sizePolicy.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy)
        self.label_9.setFont(font2)
        self.label_9.setStyleSheet(u"background-color: none")
        self.label_9.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label_9)

        self.spinBox_count = QSpinBox(PageSverlilnayaStart)
        self.spinBox_count.setObjectName(u"spinBox_count")
        self.spinBox_count.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
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

        self.widget_length = QWidget(PageSverlilnayaStart)
        self.widget_length.setObjectName(u"widget_length")
        self.widget_length.setStyleSheet(u"background: none;")
        self.horizontalLayout_4 = QHBoxLayout(self.widget_length)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(-1, 0, -1, 0)
        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_9)

        self.label_11 = QLabel(self.widget_length)
        self.label_11.setObjectName(u"label_11")
        sizePolicy.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy)
        self.label_11.setFont(font2)
        self.label_11.setStyleSheet(u"background-color: none")
        self.label_11.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_4.addWidget(self.label_11)

        self.doubleSpinBox_length = QDoubleSpinBox(self.widget_length)
        self.doubleSpinBox_length.setObjectName(u"doubleSpinBox_length")
        self.doubleSpinBox_length.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
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

        self.horizontalLayout_4.addWidget(self.doubleSpinBox_length)

        self.line_2 = QFrame(self.widget_length)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.Shape.VLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_4.addWidget(self.line_2)

        self.label_12 = QLabel(self.widget_length)
        self.label_12.setObjectName(u"label_12")
        sizePolicy.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy)
        self.label_12.setFont(font2)
        self.label_12.setStyleSheet(u"background-color: none")
        self.label_12.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_4.addWidget(self.label_12)

        self.doubleSpinBox_dopusk = QDoubleSpinBox(self.widget_length)
        self.doubleSpinBox_dopusk.setObjectName(u"doubleSpinBox_dopusk")
        self.doubleSpinBox_dopusk.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.doubleSpinBox_dopusk.setStyleSheet(u"QDoubleSpinBox {\n"
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
        self.doubleSpinBox_dopusk.setMaximum(1000.000000000000000)

        self.horizontalLayout_4.addWidget(self.doubleSpinBox_dopusk, 0, Qt.AlignmentFlag.AlignHCenter)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_10)


        self.verticalLayout_2.addWidget(self.widget_length)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, 0, -1, -1)
        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_7)

        self.label_10 = QLabel(PageSverlilnayaStart)
        self.label_10.setObjectName(u"label_10")
        sizePolicy.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy)
        self.label_10.setFont(font2)
        self.label_10.setStyleSheet(u"background-color: none")
        self.label_10.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label_10, 0, Qt.AlignmentFlag.AlignVCenter)

        self.doubleSpinBox_nom_diameter = QDoubleSpinBox(PageSverlilnayaStart)
        self.doubleSpinBox_nom_diameter.setObjectName(u"doubleSpinBox_nom_diameter")
        self.doubleSpinBox_nom_diameter.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.doubleSpinBox_nom_diameter.setStyleSheet(u"QDoubleSpinBox {\n"
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
        self.doubleSpinBox_nom_diameter.setMaximum(1000.000000000000000)

        self.horizontalLayout_3.addWidget(self.doubleSpinBox_nom_diameter, 0, Qt.AlignmentFlag.AlignVCenter)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_8)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)


        self.verticalLayout.addLayout(self.verticalLayout_2)

        self.label_2 = QLabel(PageSverlilnayaStart)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"background: none;")

        self.verticalLayout.addWidget(self.label_2, 0, Qt.AlignmentFlag.AlignHCenter)

        self.verticalSpacer = QSpacerItem(714, 56, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.retranslateUi(PageSverlilnayaStart)

        QMetaObject.connectSlotsByName(PageSverlilnayaStart)
    # setupUi

    def retranslateUi(self, PageSverlilnayaStart):
        PageSverlilnayaStart.setWindowTitle(QCoreApplication.translate("PageSverlilnayaStart", u"Form", None))
        self.label.setText(QCoreApplication.translate("PageSverlilnayaStart", u"\u0421\u0432\u0435\u0440\u043b\u0435\u043d\u0438\u0435 \u043e\u0442\u0432\u0435\u0440\u0441\u0442\u0438\u0439", None))
        self.label_7.setText(QCoreApplication.translate("PageSverlilnayaStart", u"\u0422\u0438\u043f \u043e\u0442\u0432\u0435\u0440\u0441\u0442\u0438\u044f:", None))
        self.horizontalGroupBox_4.setTitle("")
        self.pushButton_infinity.setText(QCoreApplication.translate("PageSverlilnayaStart", u"C\u043a\u0432\u043e\u0437\u043d\u043e\u0435", None))
        self.pushButton_with_length.setText(QCoreApplication.translate("PageSverlilnayaStart", u"\u0413\u043b\u0443\u0445\u043e\u0435", None))
        self.label_8.setText(QCoreApplication.translate("PageSverlilnayaStart", u"\u0414\u0438\u0430\u043c\u0435\u0442\u0440 \u0441\u0432\u0435\u0440\u043b\u0430: ", None))
        self.comboBox_diameter.setPlaceholderText(QCoreApplication.translate("PageSverlilnayaStart", u"\u0421\u0432\u0435\u0440\u043b\u043e...", None))
#if QT_CONFIG(tooltip)
        self.pushButton_find_sverlo.setToolTip(QCoreApplication.translate("PageSverlilnayaStart", u"<html><head/><body><p><span style=\" font-size:8pt; font-weight:300; color:#000000;\">\u041f\u043e\u0434\u043e\u0431\u0440\u0430\u0442\u044c \u0441\u0432\u0435\u0440\u043b\u043e \u043f\u043e\u0434 \u0440\u0435\u0437\u044c\u0431\u0443</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.pushButton_find_sverlo.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.pushButton_find_sverlo.setText("")
        self.label_9.setText(QCoreApplication.translate("PageSverlilnayaStart", u"\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u043e\u0442\u0432\u0435\u0440\u0441\u0442\u0438\u0439:", None))
        self.spinBox_count.setSuffix(QCoreApplication.translate("PageSverlilnayaStart", u" \u0448\u0442.", None))
        self.label_11.setText(QCoreApplication.translate("PageSverlilnayaStart", u"\u0413\u043b\u0443\u0431\u0438\u043d\u0430 \u043e\u0442\u0432\u0435\u0440\u0441\u0442\u0438\u0439:", None))
        self.doubleSpinBox_length.setPrefix(QCoreApplication.translate("PageSverlilnayaStart", u"L = ", None))
        self.doubleSpinBox_length.setSuffix("")
        self.label_12.setText(QCoreApplication.translate("PageSverlilnayaStart", u"\u0414\u043e\u043f\u0443\u0441\u043a:", None))
        self.doubleSpinBox_dopusk.setPrefix("")
        self.doubleSpinBox_dopusk.setSuffix("")
        self.label_10.setText(QCoreApplication.translate("PageSverlilnayaStart", u"\u041d\u043e\u043c\u0438\u043d\u0430\u043b\u044c\u043d\u044b\u0439 \u0434\u0438\u0430\u043c\u0435\u0442\u0440 \u0440\u0430\u0441\u043f\u043e\u043b\u043e\u0436\u0435\u043d\u0438\u044f: ", None))
#if QT_CONFIG(whatsthis)
        self.doubleSpinBox_nom_diameter.setWhatsThis(QCoreApplication.translate("PageSverlilnayaStart", u"<html><head/><body><p>\u041c\u043e\u0436\u043d\u043e \u043d\u0435 \u0443\u043a\u0430\u0437\u044b\u0432\u0430\u0442\u044c</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.doubleSpinBox_nom_diameter.setPrefix(QCoreApplication.translate("PageSverlilnayaStart", u"\u00d8 ", None))
        self.doubleSpinBox_nom_diameter.setSuffix("")
        self.label_2.setText(QCoreApplication.translate("PageSverlilnayaStart", u"(\u041d\u0435\u043e\u0431\u044f\u0437\u0430\u0442\u0435\u043b\u044c\u043d\u043e)", None))
    # retranslateUi

