# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_dialog_termichka.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QComboBox, QDialog,
    QDialogButtonBox, QFrame, QHBoxLayout, QLabel,
    QListWidget, QListWidgetItem, QPushButton, QSizePolicy,
    QSpacerItem, QSpinBox, QVBoxLayout, QWidget)

class Ui_DialogTermichka(object):
    def setupUi(self, DialogTermichka):
        if not DialogTermichka.objectName():
            DialogTermichka.setObjectName(u"DialogTermichka")
        DialogTermichka.resize(673, 577)
        DialogTermichka.setWindowOpacity(0.950000000000000)
        DialogTermichka.setStyleSheet(u"color: white;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(0, 57, 95), stop:1 rgb(0, 83, 122))")
        self.verticalLayout = QVBoxLayout(DialogTermichka)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_8 = QLabel(DialogTermichka)
        self.label_8.setObjectName(u"label_8")
        font = QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet(u"background: none;")

        self.verticalLayout.addWidget(self.label_8, 0, Qt.AlignmentFlag.AlignHCenter)

        self.label_9 = QLabel(DialogTermichka)
        self.label_9.setObjectName(u"label_9")
        font1 = QFont()
        font1.setPointSize(10)
        font1.setBold(True)
        self.label_9.setFont(font1)
        self.label_9.setStyleSheet(u"background: none;")

        self.verticalLayout.addWidget(self.label_9, 0, Qt.AlignmentFlag.AlignHCenter)

        self.listWidget = QListWidget(DialogTermichka)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        self.listWidget.setObjectName(u"listWidget")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listWidget.sizePolicy().hasHeightForWidth())
        self.listWidget.setSizePolicy(sizePolicy)
        self.listWidget.setMinimumSize(QSize(200, 0))
        self.listWidget.setFont(font1)
        self.listWidget.viewport().setProperty(u"cursor", QCursor(Qt.CursorShape.PointingHandCursor))
        self.listWidget.setStyleSheet(u"\n"
"/* \u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500 \u0421\u0430\u043c \u0441\u043f\u0438\u0441\u043e\u043a \u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500 */\n"
"QListWidget {\n"
"    background: transparent;\n"
"    font-size: 10pt;\n"
"	border: none;\n"
"    color: #E8EAF0;\n"
"}\n"
"\n"
"/* \u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500 \u042d\u043b\u0435\u043c\u0435\u043d\u0442\u044b \u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500 */\n"
"QListWidget::item {\n"
"    background: transparent;\n"
"    border: none;\n"
"    border-radius: 12px;\n"
"    margin: 2px 6px;\n"
"    color: rgba(255, 255, 255, 0.72);\n"
"}\n"
"\n"
"QListWidget::item:hover {\n"
"    background: rgba(255, 255, 255, 0.07);\n"
"    color: #FFFFFF;\n"
"}\n"
"\n"
"QListWidget::item:selected {\n"
"    background: qlineargradient(x1:0, y1:0, x2:1, y2:0,\n"
"        stop:0 rgba(94, 129, 255, 0.32),\n"
"        stop:"
                        "1 rgba(94, 129, 255, 0.08));\n"
"    color: #FFFFFF;\n"
"}\n"
"\n"
"QListWidget::item:selected:hover {\n"
"    background: qlineargradient(x1:0, y1:0, x2:1, y2:0,\n"
"        stop:0 rgba(94, 129, 255, 0.42),\n"
"        stop:1 rgba(94, 129, 255, 0.14));\n"
"}\n"
"\n"
"/* \u0443\u0431\u0438\u0440\u0430\u0435\u043c \u0440\u0430\u043c\u043a\u0443/\u043f\u0443\u043d\u043a\u0442\u0438\u0440 \u043f\u0440\u0438 \u0444\u043e\u043a\u0443\u0441\u0435 */\n"
"QListWidget:focus,\n"
"QListWidget::item:focus {\n"
"    outline: none;\n"
"    border: none;\n"
"}\n"
"\n"
"/* \u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500 \u0412\u0435\u0440\u0442\u0438\u043a\u0430\u043b\u044c\u043d\u044b\u0439 \u0441\u043a\u0440\u043e\u043b\u043b\u0431\u0430\u0440 \u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500 */\n"
"QScrollBar:vertical {\n"
"    background: transparent;\n"
"    width: 10px;\n"
"    margin: 4px 2px;\n"
"    border-radius: 5px;\n"
"}\n"
"QScrollBar::handle:vertical {"
                        "\n"
"    background: rgba(255, 255, 255, 0.18);\n"
"    min-height: 30px;\n"
"    border-radius: 5px;\n"
"}\n"
"QScrollBar::handle:vertical:hover {\n"
"    background: rgba(255, 255, 255, 0.32);\n"
"}\n"
"QScrollBar::add-line:vertical,\n"
"QScrollBar::sub-line:vertical { height: 0; }\n"
"QScrollBar::add-page:vertical,\n"
"QScrollBar::sub-page:vertical { background: transparent; }\n"
"\n"
"/* \u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500 \u0413\u043e\u0440\u0438\u0437\u043e\u043d\u0442\u0430\u043b\u044c\u043d\u044b\u0439 \u0441\u043a\u0440\u043e\u043b\u043b\u0431\u0430\u0440 \u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500 */\n"
"QScrollBar:horizontal {\n"
"    background: transparent;\n"
"    height: 10px;\n"
"    margin: 2px 4px;\n"
"    border-radius: 5px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background: rgba(255, 255, 255, 0.18);\n"
"    min-width: 30px;\n"
"    border-radius: 5px;\n"
"}\n"
"QScrollBar::handle:horizontal:hover {\n"
""
                        "    background: rgba(255, 255, 255, 0.32);\n"
"}\n"
"QScrollBar::add-line:horizontal,\n"
"QScrollBar::sub-line:horizontal { width: 0; }\n"
"QScrollBar::add-page:horizontal,\n"
"QScrollBar::sub-page:horizontal { background: transparent; }\n"
"")
        self.listWidget.setTabKeyNavigation(False)
        self.listWidget.setAlternatingRowColors(False)

        self.verticalLayout.addWidget(self.listWidget)

        self.line = QFrame(DialogTermichka)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout.addWidget(self.line)

        self.text_1 = QWidget(DialogTermichka)
        self.text_1.setObjectName(u"text_1")
        self.verticalLayout_2 = QVBoxLayout(self.text_1)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, 1, -1, 1)
        self.label_20 = QLabel(self.text_1)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setFont(font1)
        self.label_20.setStyleSheet(u"background: none;")

        self.verticalLayout_2.addWidget(self.label_20, 0, Qt.AlignmentFlag.AlignHCenter)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(-1, -1, 0, -1)
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_2)

        self.label_4 = QLabel(self.text_1)
        self.label_4.setObjectName(u"label_4")
        font2 = QFont()
        font2.setPointSize(10)
        self.label_4.setFont(font2)
        self.label_4.setStyleSheet(u"background: none;")

        self.horizontalLayout_4.addWidget(self.label_4)

        self.comboBox_position = QComboBox(self.text_1)
        self.comboBox_position.addItem("")
        self.comboBox_position.addItem("")
        self.comboBox_position.setObjectName(u"comboBox_position")
        self.comboBox_position.setFont(font2)
        self.comboBox_position.setStyleSheet(u"QComboBox {\n"
"	padding: 5, 5, 5, 5;\n"
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

        self.horizontalLayout_4.addWidget(self.comboBox_position)

        self.label_2 = QLabel(self.text_1)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font2)
        self.label_2.setStyleSheet(u"background: none;")

        self.horizontalLayout_4.addWidget(self.label_2)

        self.comboBox_detail = QComboBox(self.text_1)
        self.comboBox_detail.setObjectName(u"comboBox_detail")
        self.comboBox_detail.setFont(font2)
        self.comboBox_detail.setStyleSheet(u"QComboBox {\n"
"	padding: 5, 5, 5, 5;\n"
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

        self.horizontalLayout_4.addWidget(self.comboBox_detail)

        self.label_3 = QLabel(self.text_1)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font2)
        self.label_3.setStyleSheet(u"background: none;")

        self.horizontalLayout_4.addWidget(self.label_3)

        self.spinBox_pos = QSpinBox(self.text_1)
        self.spinBox_pos.setObjectName(u"spinBox_pos")
        font3 = QFont()
        font3.setPointSize(11)
        self.spinBox_pos.setFont(font3)
        self.spinBox_pos.setStyleSheet(u"QSpinBox {\n"
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
        self.spinBox_pos.setMinimum(1)
        self.spinBox_pos.setMaximum(100)
        self.spinBox_pos.setValue(1)

        self.horizontalLayout_4.addWidget(self.spinBox_pos)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)


        self.verticalLayout.addWidget(self.text_1)

        self.text_2 = QWidget(DialogTermichka)
        self.text_2.setObjectName(u"text_2")
        self.verticalLayout_3 = QVBoxLayout(self.text_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(-1, 0, -1, 0)
        self.label_21 = QLabel(self.text_2)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setFont(font1)
        self.label_21.setStyleSheet(u"background: none;")

        self.verticalLayout_3.addWidget(self.label_21, 0, Qt.AlignmentFlag.AlignHCenter)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, -1, -1, 0)
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_5)

        self.label_5 = QLabel(self.text_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font2)
        self.label_5.setStyleSheet(u"background: none;")

        self.horizontalLayout.addWidget(self.label_5)

        self.spinBox_temp = QSpinBox(self.text_2)
        self.spinBox_temp.setObjectName(u"spinBox_temp")
        self.spinBox_temp.setFont(font3)
        self.spinBox_temp.setStyleSheet(u"QSpinBox {\n"
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
        self.spinBox_temp.setMinimum(1)
        self.spinBox_temp.setMaximum(1000)
        self.spinBox_temp.setValue(1)

        self.horizontalLayout.addWidget(self.spinBox_temp)

        self.label_7 = QLabel(self.text_2)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font3)
        self.label_7.setStyleSheet(u"background: none;")

        self.horizontalLayout.addWidget(self.label_7)

        self.spinBox_temp_d = QSpinBox(self.text_2)
        self.spinBox_temp_d.setObjectName(u"spinBox_temp_d")
        self.spinBox_temp_d.setFont(font3)
        self.spinBox_temp_d.setStyleSheet(u"QSpinBox {\n"
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
        self.spinBox_temp_d.setMinimum(1)
        self.spinBox_temp_d.setMaximum(100)
        self.spinBox_temp_d.setValue(1)

        self.horizontalLayout.addWidget(self.spinBox_temp_d)

        self.label_6 = QLabel(self.text_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font3)
        self.label_6.setStyleSheet(u"background: none;")

        self.horizontalLayout.addWidget(self.label_6)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_6)


        self.verticalLayout_3.addLayout(self.horizontalLayout)


        self.verticalLayout.addWidget(self.text_2)

        self.text_3 = QWidget(DialogTermichka)
        self.text_3.setObjectName(u"text_3")
        self.verticalLayout_4 = QVBoxLayout(self.text_3)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(-1, 1, -1, 0)
        self.label_22 = QLabel(self.text_3)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setFont(font1)
        self.label_22.setStyleSheet(u"background: none;")

        self.verticalLayout_4.addWidget(self.label_22, 0, Qt.AlignmentFlag.AlignHCenter)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, 0, -1, -1)
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)

        self.label = QLabel(self.text_3)
        self.label.setObjectName(u"label")
        self.label.setFont(font2)
        self.label.setStyleSheet(u"background: none;")

        self.horizontalLayout_3.addWidget(self.label)

        self.comboBox_inout = QComboBox(self.text_3)
        self.comboBox_inout.addItem("")
        self.comboBox_inout.addItem("")
        self.comboBox_inout.setObjectName(u"comboBox_inout")
        self.comboBox_inout.setFont(font2)
        self.comboBox_inout.setStyleSheet(u"QComboBox {\n"
"	padding: 5, 5, 5, 5;\n"
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

        self.horizontalLayout_3.addWidget(self.comboBox_inout)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_4)


        self.verticalLayout_4.addLayout(self.horizontalLayout_3)


        self.verticalLayout.addWidget(self.text_3)

        self.verticalSpacer_2 = QSpacerItem(20, 15, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.pushButton_save_result = QPushButton(DialogTermichka)
        self.pushButton_save_result.setObjectName(u"pushButton_save_result")
        self.pushButton_save_result.setStyleSheet(u"QPushButton {\n"
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

        self.verticalLayout.addWidget(self.pushButton_save_result, 0, Qt.AlignmentFlag.AlignHCenter)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.buttonBox = QDialogButtonBox(DialogTermichka)
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
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Close)
        self.buttonBox.setCenterButtons(True)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(DialogTermichka)

        QMetaObject.connectSlotsByName(DialogTermichka)
    # setupUi

    def retranslateUi(self, DialogTermichka):
        DialogTermichka.setWindowTitle(QCoreApplication.translate("DialogTermichka", u"\u0422\u0435\u0440\u043c\u0438\u0447\u0435\u0441\u043a\u0430\u044f \u043e\u0431\u0440\u0430\u0431\u043e\u0442\u043a\u0430", None))
        self.label_8.setText(QCoreApplication.translate("DialogTermichka", u"\u0422\u0435\u0440\u043c\u0438\u0447\u0435\u0441\u043a\u0430\u044f \u043e\u0431\u0440\u0430\u0431\u043e\u0442\u043a\u0430 \u0434\u0435\u0442\u0430\u043b\u0438", None))
        self.label_9.setText(QCoreApplication.translate("DialogTermichka", u"\u0421\u043f\u0438\u0441\u043e\u043a \u043f\u0435\u0440\u0435\u0445\u043e\u0434\u043e\u0432:", None))

        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        ___qlistwidgetitem = self.listWidget.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("DialogTermichka", u"\u0423\u0441\u0442\u0430\u043d\u043e\u0432\u043a\u0430 \u0434\u0435\u0442\u0430\u043b\u0438 \u043d\u0430 \u043f\u043e\u0434\u0434\u043e\u043d", None))
        ___qlistwidgetitem1 = self.listWidget.item(1)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("DialogTermichka", u"\u041d\u0430\u0433\u0440\u0435\u0432 \u0434\u0435\u0442\u0430\u043b\u0438", None))
        ___qlistwidgetitem2 = self.listWidget.item(2)
        ___qlistwidgetitem2.setText(QCoreApplication.translate("DialogTermichka", u"\u0423\u0441\u0442\u0430\u043d\u043e\u0432\u043a\u0430 \u043f\u043e\u0434\u0434\u043e\u043d\u0430 \u0432 \u043f\u0435\u0447\u044c \\ \u0418\u0437\u0432\u043b\u0435\u0447\u0435\u043d\u0438\u0435 \u043f\u043e\u0434\u0434\u043e\u043d\u0430 \u0438\u0437 \u043f\u0435\u0447\u0438", None))
        self.listWidget.setSortingEnabled(__sortingEnabled)

        self.label_20.setText(QCoreApplication.translate("DialogTermichka", u"\u0423\u043a\u0430\u0436\u0438\u0442\u0435 \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u044b:", None))
        self.label_4.setText(QCoreApplication.translate("DialogTermichka", u"\u041d\u0430 \u043f\u043e\u0434\u0434\u043e\u043d \u0446\u0435\u0445\u043e\u0432\u043e\u0439 \u0432", None))
        self.comboBox_position.setItemText(0, QCoreApplication.translate("DialogTermichka", u"\u0432\u0435\u0440\u0442\u0438\u043a\u0430\u043b\u044c\u043d\u043e\u043c", None))
        self.comboBox_position.setItemText(1, QCoreApplication.translate("DialogTermichka", u"\u0433\u043e\u0440\u0438\u0437\u043e\u043d\u0442\u0430\u043b\u044c\u043d\u043e\u043c", None))

        self.label_2.setText(QCoreApplication.translate("DialogTermichka", u"\u043f\u043e\u043b\u043e\u0436\u0435\u043d\u0438\u0438 \u0443\u0441\u0442\u0430\u043d\u043e\u0432\u0438\u0442\u044c", None))
        self.label_3.setText(QCoreApplication.translate("DialogTermichka", u"\u043f\u043e\u0437.", None))
        self.spinBox_pos.setSuffix("")
        self.label_21.setText(QCoreApplication.translate("DialogTermichka", u"\u0423\u043a\u0430\u0436\u0438\u0442\u0435 \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u044b:", None))
        self.label_5.setText(QCoreApplication.translate("DialogTermichka", u"\u041d\u0430\u0433\u0440\u0435\u0442\u044c \u0434\u043e \u0442\u0435\u043c\u043f\u0435\u0440\u0430\u0442\u0443\u0440\u044b", None))
        self.spinBox_temp.setSuffix("")
        self.label_7.setText(QCoreApplication.translate("DialogTermichka", u"\u00b1", None))
        self.spinBox_temp_d.setSuffix("")
        self.label_6.setText(QCoreApplication.translate("DialogTermichka", u"\u2103", None))
        self.label_22.setText(QCoreApplication.translate("DialogTermichka", u"\u0423\u043a\u0430\u0436\u0438\u0442\u0435 \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440:", None))
        self.label.setText(QCoreApplication.translate("DialogTermichka", u"\u041f\u043e\u0434\u0434\u043e\u043d \u0446\u0435\u0445\u043e\u0432\u043e\u0439", None))
        self.comboBox_inout.setItemText(0, QCoreApplication.translate("DialogTermichka", u"\u0443\u0441\u0442\u0430\u043d\u043e\u0432\u0438\u0442\u044c \u0432 \u043f\u0435\u0447\u044c", None))
        self.comboBox_inout.setItemText(1, QCoreApplication.translate("DialogTermichka", u"\u0438\u0437\u0432\u043b\u0435\u0447\u044c \u0438\u0437 \u043f\u0435\u0447\u0438", None))

        self.pushButton_save_result.setText(QCoreApplication.translate("DialogTermichka", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0442\u0435\u043a\u0441\u0442", None))
    # retranslateUi

