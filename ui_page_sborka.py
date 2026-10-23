# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_page_sborka.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QHBoxLayout,
    QHeaderView, QLabel, QPushButton, QSizePolicy,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_PageSborka(object):
    def setupUi(self, PageSborka):
        if not PageSborka.objectName():
            PageSborka.setObjectName(u"PageSborka")
        PageSborka.resize(1200, 737)
        PageSborka.setMinimumSize(QSize(1000, 700))
        PageSborka.setStyleSheet(u"color: white;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(0, 57, 95), stop:1 rgb(0, 83, 122))")
        self.verticalLayout_3 = QVBoxLayout(PageSborka)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(5, 0, 5, -1)
        self.btn_home_1 = QPushButton(PageSborka)
        self.btn_home_1.setObjectName(u"btn_home_1")
        self.btn_home_1.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_home_1.setStyleSheet(u"QPushButton {\n"
"	border: 1px solid;\n"
"	border-color: white;\n"
"	border-radius: 10px;\n"
"	height: 20px;\n"
"	width: 100px;\n"
"	background-color: none;\n"
"	padding: 2 5 5 2;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(0, 111, 171)\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: rgb(0, 53, 93)\n"
"}")

        self.horizontalLayout_6.addWidget(self.btn_home_1, 0, Qt.AlignmentFlag.AlignLeft)


        self.verticalLayout_3.addLayout(self.horizontalLayout_6)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, -1, 0, -1)
        self.widget = QWidget(PageSborka)
        self.widget.setObjectName(u"widget")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setStyleSheet(u"background: rgb(11, 59, 103)")
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.checkBox_only_find = QCheckBox(self.widget)
        self.checkBox_only_find.setObjectName(u"checkBox_only_find")
        self.checkBox_only_find.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.checkBox_only_find.setStyleSheet(u"QCheckBox::indicator {\n"
"  width: 10px;          \n"
"  height: 10px;         \n"
"  border: 2px solid white;         \n"
"  border-radius: 2px; /* \u0421\u043a\u0440\u0443\u0433\u043b\u0435\u043d\u043d\u044b\u0435 \u0443\u0433\u043b\u044b */          \n"
"  background-color: #FFFFFF;      \n"
"}\n"
"QCheckBox {\n"
"	spacing: 15px; /* \u0420\u0430\u0441\u0441\u0442\u043e\u044f\u043d\u0438\u0435 \u043c\u0435\u0436\u0434\u0443 \u043a\u0432\u0430\u0434\u0440\u0430\u0442\u0438\u043a\u043e\u043c \u0438 \u0442\u0435\u043a\u0441\u0442\u043e\u043c */          \n"
"	border: none;	\n"
"	color: rgb(255, 255, 255) ;	\n"
"	background: none;\n"
"	font-size: 14px;\n"
"	margin-right: 0px\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"  width: 10px;          \n"
"  height: 10px;         \n"
"  border: 2px solid white;         \n"
"  border-radius: 2px; /* \u0421\u043a\u0440\u0443\u0433\u043b\u0435\u043d\u043d\u044b\u0435 \u0443\u0433\u043b\u044b */          \n"
"  background-color: rgb(77, 77, 77);    \n"
"}\n"
"QCheckBox::ind"
                        "icator:hover {\n"
"  width: 10px;          \n"
"  height: 10px;         \n"
"  border: 2px solid rgb(136, 136, 136);         \n"
"  border-radius: 2px; /* \u0421\u043a\u0440\u0443\u0433\u043b\u0435\u043d\u043d\u044b\u0435 \u0443\u0433\u043b\u044b */          \n"
"  background-color: rgb(77, 77, 77);         \n"
"}\n"
"QCheckBox::indicator:disabled {\n"
"  width: 10px;          \n"
"  height: 10px;         \n"
"  border: 2px solid rgb(136, 136, 136);         \n"
"  border-radius: 2px; /* \u0421\u043a\u0440\u0443\u0433\u043b\u0435\u043d\u043d\u044b\u0435 \u0443\u0433\u043b\u044b */          \n"
"  background-color: rgb(86, 86, 86);         \n"
"}")

        self.verticalLayout.addWidget(self.checkBox_only_find, 0, Qt.AlignmentFlag.AlignHCenter)

        self.tableWidget_operations = QTableWidget(self.widget)
        if (self.tableWidget_operations.columnCount() < 1):
            self.tableWidget_operations.setColumnCount(1)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget_operations.setHorizontalHeaderItem(0, __qtablewidgetitem)
        self.tableWidget_operations.setObjectName(u"tableWidget_operations")
        self.tableWidget_operations.setStyleSheet(u"/* \u0421\u0430\u043c \u0432\u0438\u0434\u0436\u0435\u0442 \u2014 \u043f\u0440\u043e\u0437\u0440\u0430\u0447\u043d\u044b\u0439 \u0444\u043e\u043d */\n"
"QTableWidget {\n"
"    background: transparent;\n"
"    border: none;\n"
"    color: rgba(255, 255, 255, 80);\n"
"	gridline-color: rgba(255, 255, 255, 0);\n"
"    selection-background-color: rgba(255, 255, 255, 0);\n"
"    selection-color: #ffffff;\n"
"}\n"
"\n"
"/* \u042f\u0447\u0435\u0439\u043a\u0438 \u2014 \u0431\u0435\u0437 \u0444\u043e\u043d\u0430, \u0431\u0435\u043b\u044b\u0439 \u0442\u0435\u043a\u0441\u0442 */\n"
"QTableWidget::item {\n"
"    background: transparent;\n"
"    border: none;\n"
"	border-bottom: 1px solid rgba(255, 255, 255, 0.36)\n"
"\n"
"}\n"
"\n"
"QTableWidget::item:hover {\n"
"    background: rgba(255, 255, 255, 0.08);\n"
"}\n"
"\n"
"QTableWidget::item:selected {\n"
"    background: rgba(255, 255, 255, 0.2);\n"
"    color: #ffffff;\n"
"}\n"
"\n"
"/* \u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043a\u0438 \u2014 \u0415\u0414\u0418\u041d\u0421"
                        "\u0422\u0412\u0415\u041d\u041d\u041e\u0415 \u043c\u0435\u0441\u0442\u043e \u0441 \u0444\u043e\u043d\u043e\u043c */\n"
"QHeaderView::section {\n"
"    background-color: rgb(21, 69, 140);\n"
"    color: #ffffff;\n"
"    padding: 6px 8px;\n"
"    border: none;\n"
"    border-right: 1px solid rgba(255, 255, 255, 0.1);\n"
"    border-bottom: 1px solid rgba(255, 255, 255, 0.2);\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QHeaderView::section:hover {\n"
"    background-color: #3a3a3a;\n"
"}\n"
"\n"
"/* \u0423\u0433\u043b\u043e\u0432\u0430\u044f \u043a\u043d\u043e\u043f\u043a\u0430 (\u043f\u0435\u0440\u0435\u0441\u0435\u0447\u0435\u043d\u0438\u0435 \u0437\u0430\u0433\u043e\u043b\u043e\u0432\u043a\u043e\u0432) */\n"
"QTableCornerButton::section {\n"
"    background-color:  rgb(21, 69, 140);\n"
"    border: none;\n"
"    border-right: 1px solid rgba(255, 255, 255, 0.1);\n"
"    border-bottom: 1px solid rgba(255, 255, 255, 0.2);\n"
"}\n"
"\n"
"/* \u0421\u043a\u0440\u043e\u043b\u043b\u0431\u0430\u0440\u044b \u2014 \u043c\u0438"
                        "\u043d\u0438\u043c\u0430\u043b\u044c\u043d\u043e, \u0447\u0442\u043e\u0431\u044b \u043d\u0435 \u043c\u0435\u0448\u0430\u043b\u0438 */\n"
"QTableWidget QScrollBar:vertical {\n"
"    background: transparent;\n"
"    width: 8px;\n"
"}\n"
"\n"
"QTableWidget QScrollBar::handle:vertical {\n"
"    background: rgba(255, 255, 255, 0.3);\n"
"    border-radius: 4px;\n"
"    min-height: 20px;\n"
"}\n"
"\n"
"QTableWidget QScrollBar::handle:vertical:hover {\n"
"    background: rgba(255, 255, 255, 0.5);\n"
"}\n"
"\n"
"QTableWidget QScrollBar::add-line:vertical,\n"
"QTableWidget QScrollBar::sub-line:vertical,\n"
"QTableWidget QScrollBar::add-page:vertical,\n"
"QTableWidget QScrollBar::sub-page:vertical {\n"
"    background: transparent;\n"
"    height: 0px;\n"
"}\n"
"\n"
"QTableWidget QScrollBar:horizontal {\n"
"    background: transparent;\n"
"    height: 8px;\n"
"}\n"
"\n"
"QTableWidget QScrollBar::handle:horizontal {\n"
"    background: rgba(255, 255, 255, 0.3);\n"
"    border-radius: 4px;\n"
"    min-width: 20px;\n"
"}\n"
""
                        "\n"
"QTableWidget QScrollBar::handle:horizontal:hover {\n"
"    background: rgba(255, 255, 255, 0.5);\n"
"}\n"
"\n"
"QTableWidget QScrollBar::add-line:horizontal,\n"
"QTableWidget QScrollBar::sub-line:horizontal,\n"
"QTableWidget QScrollBar::add-page:horizontal,\n"
"QTableWidget QScrollBar::sub-page:horizontal {\n"
"    background: transparent;\n"
"    width: 0px;\n"
"}\n"
"QPushButton {\n"
"	border: 1px solid white;\n"
"	margin-top: 25px;\n"
"	margin-bottom: 25px;\n"
"	margin-left: 20px;\n"
"	margin-right: 20px;\n"
"	border-radius: 8px;\n"
"}\n"
"QPushButton:hover {\n"
"	border: 2px solid white;\n"
"	background: rgb(15, 65, 159)\n"
"}")
        self.tableWidget_operations.horizontalHeader().setMinimumSectionSize(100)
        self.tableWidget_operations.horizontalHeader().setDefaultSectionSize(130)
        self.tableWidget_operations.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_operations.verticalHeader().setVisible(False)
        self.tableWidget_operations.verticalHeader().setMinimumSectionSize(30)
        self.tableWidget_operations.verticalHeader().setDefaultSectionSize(30)

        self.verticalLayout.addWidget(self.tableWidget_operations)


        self.horizontalLayout.addWidget(self.widget)

        self.widget_2 = QWidget(PageSborka)
        self.widget_2.setObjectName(u"widget_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(4)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy1)
        self.widget_2.setStyleSheet(u"background: rgba(255, 255, 255, 0)")
        self.verticalLayout_2 = QVBoxLayout(self.widget_2)
        self.verticalLayout_2.setSpacing(10)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(self.widget_2)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(10)
        self.label.setFont(font)

        self.verticalLayout_2.addWidget(self.label, 0, Qt.AlignmentFlag.AlignHCenter)

        self.line = QFrame(self.widget_2)
        self.line.setObjectName(u"line")
        self.line.setStyleSheet(u"background: rgb(255, 255, 255)")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_2.addWidget(self.line)

        self.btn_update_table = QPushButton(self.widget_2)
        self.btn_update_table.setObjectName(u"btn_update_table")
        self.btn_update_table.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_update_table.setStyleSheet(u"QPushButton {\n"
"	border: 1px solid;\n"
"	border-color: white;\n"
"	border-radius: 10px;\n"
"	height: 20px;\n"
"	background-color: none;\n"
"	padding: 2 5 2 5\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(0, 111, 171)\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: rgb(0, 53, 93)\n"
"}")

        self.verticalLayout_2.addWidget(self.btn_update_table, 0, Qt.AlignmentFlag.AlignHCenter)

        self.tableWidget_find_operations = QTableWidget(self.widget_2)
        if (self.tableWidget_find_operations.columnCount() < 1):
            self.tableWidget_find_operations.setColumnCount(1)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget_find_operations.setHorizontalHeaderItem(0, __qtablewidgetitem1)
        self.tableWidget_find_operations.setObjectName(u"tableWidget_find_operations")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(2)
        sizePolicy2.setVerticalStretch(2)
        sizePolicy2.setHeightForWidth(self.tableWidget_find_operations.sizePolicy().hasHeightForWidth())
        self.tableWidget_find_operations.setSizePolicy(sizePolicy2)
        self.tableWidget_find_operations.setMinimumSize(QSize(400, 0))
        self.tableWidget_find_operations.setStyleSheet(u"/* \u0421\u0430\u043c \u0432\u0438\u0434\u0436\u0435\u0442 \u2014 \u043f\u0440\u043e\u0437\u0440\u0430\u0447\u043d\u044b\u0439 \u0444\u043e\u043d */\n"
"QTableWidget {\n"
"    background: transparent;\n"
"    border: none;\n"
"    color: rgb(255, 255, 255);\n"
"	gridline-color: rgba(255, 255, 255, 0);\n"
"    selection-background-color: rgba(255, 255, 255, 0);\n"
"    selection-color: #ffffff;\n"
"}\n"
"\n"
"/* \u042f\u0447\u0435\u0439\u043a\u0438 \u2014 \u0431\u0435\u0437 \u0444\u043e\u043d\u0430, \u0431\u0435\u043b\u044b\u0439 \u0442\u0435\u043a\u0441\u0442 */\n"
"QTableWidget::item {\n"
"    background: transparent;\n"
"    border: none;\n"
"	border-bottom: 1px solid rgba(255, 255, 255, 0.36)\n"
"\n"
"}\n"
"\n"
"QTableWidget::item:hover {\n"
"    background: rgba(255, 255, 255, 0.08);\n"
"}\n"
"\n"
"QTableWidget::item:selected {\n"
"    background: rgba(255, 255, 255, 0.2);\n"
"    color: #ffffff;\n"
"}\n"
"\n"
"/* \u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043a\u0438 \u2014 \u0415\u0414\u0418\u041d\u0421\u0422"
                        "\u0412\u0415\u041d\u041d\u041e\u0415 \u043c\u0435\u0441\u0442\u043e \u0441 \u0444\u043e\u043d\u043e\u043c */\n"
"QHeaderView::section {\n"
"    background-color: rgb(21, 69, 140);\n"
"    color: #ffffff;\n"
"    padding: 6px 8px;\n"
"    border: none;\n"
"    border-right: 1px solid rgba(255, 255, 255, 0.1);\n"
"    border-bottom: 1px solid rgba(255, 255, 255, 0.2);\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QHeaderView::section:hover {\n"
"    background-color: #3a3a3a;\n"
"}\n"
"\n"
"/* \u0423\u0433\u043b\u043e\u0432\u0430\u044f \u043a\u043d\u043e\u043f\u043a\u0430 (\u043f\u0435\u0440\u0435\u0441\u0435\u0447\u0435\u043d\u0438\u0435 \u0437\u0430\u0433\u043e\u043b\u043e\u0432\u043a\u043e\u0432) */\n"
"QTableCornerButton::section {\n"
"    background-color:  rgb(21, 69, 140);\n"
"    border: none;\n"
"    border-right: 1px solid rgba(255, 255, 255, 0.1);\n"
"    border-bottom: 1px solid rgba(255, 255, 255, 0.2);\n"
"}\n"
"\n"
"/* \u0421\u043a\u0440\u043e\u043b\u043b\u0431\u0430\u0440\u044b \u2014 \u043c\u0438\u043d"
                        "\u0438\u043c\u0430\u043b\u044c\u043d\u043e, \u0447\u0442\u043e\u0431\u044b \u043d\u0435 \u043c\u0435\u0448\u0430\u043b\u0438 */\n"
"QTableWidget QScrollBar:vertical {\n"
"    background: transparent;\n"
"    width: 8px;\n"
"}\n"
"\n"
"QTableWidget QScrollBar::handle:vertical {\n"
"    background: rgba(255, 255, 255, 0.3);\n"
"    border-radius: 4px;\n"
"    min-height: 20px;\n"
"}\n"
"\n"
"QTableWidget QScrollBar::handle:vertical:hover {\n"
"    background: rgba(255, 255, 255, 0.5);\n"
"}\n"
"\n"
"QTableWidget QScrollBar::add-line:vertical,\n"
"QTableWidget QScrollBar::sub-line:vertical,\n"
"QTableWidget QScrollBar::add-page:vertical,\n"
"QTableWidget QScrollBar::sub-page:vertical {\n"
"    background: transparent;\n"
"    height: 0px;\n"
"}\n"
"\n"
"QTableWidget QScrollBar:horizontal {\n"
"    background: transparent;\n"
"    height: 8px;\n"
"}\n"
"\n"
"QTableWidget QScrollBar::handle:horizontal {\n"
"    background: rgba(255, 255, 255, 0.3);\n"
"    border-radius: 4px;\n"
"    min-width: 20px;\n"
"}\n"
"\n"
""
                        "QTableWidget QScrollBar::handle:horizontal:hover {\n"
"    background: rgba(255, 255, 255, 0.5);\n"
"}\n"
"\n"
"QTableWidget QScrollBar::add-line:horizontal,\n"
"QTableWidget QScrollBar::sub-line:horizontal,\n"
"QTableWidget QScrollBar::add-page:horizontal,\n"
"QTableWidget QScrollBar::sub-page:horizontal {\n"
"    background: transparent;\n"
"    width: 0px;\n"
"}\n"
"QPushButton {\n"
"	border: 1px solid white;\n"
"	margin-top: 25px;\n"
"	margin-bottom: 25px;\n"
"	margin-left: 20px;\n"
"	margin-right: 20px;\n"
"	border-radius: 8px;\n"
"}\n"
"QPushButton:hover {\n"
"	border: 2px solid white;\n"
"	background: rgb(15, 65, 159)\n"
"}")
        self.tableWidget_find_operations.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_find_operations.verticalHeader().setStretchLastSection(False)

        self.verticalLayout_2.addWidget(self.tableWidget_find_operations, 0, Qt.AlignmentFlag.AlignHCenter)

        self.widget_4 = QWidget(self.widget_2)
        self.widget_4.setObjectName(u"widget_4")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(3)
        sizePolicy3.setHeightForWidth(self.widget_4.sizePolicy().hasHeightForWidth())
        self.widget_4.setSizePolicy(sizePolicy3)
        self.widget_4.setStyleSheet(u"")
        self.verticalLayout_6 = QVBoxLayout(self.widget_4)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setSpacing(10)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 6, -1)
        self.text_info = QLabel(self.widget_4)
        self.text_info.setObjectName(u"text_info")
        self.text_info.setFont(font)
        self.text_info.setStyleSheet(u"background:none;\n"
"color: rgb(255, 85, 85);")
        self.text_info.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_4.addWidget(self.text_info)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, 0, -1, -1)
        self.label_6 = QLabel(self.widget_4)
        self.label_6.setObjectName(u"label_6")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy4.setHorizontalStretch(3)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy4)
        font1 = QFont()
        font1.setFamilies([u"Onyx"])
        font1.setPointSize(13)
        self.label_6.setFont(font1)
        self.label_6.setStyleSheet(u"background-color: none")
        self.label_6.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label_6)

        self.btn_clear_table = QPushButton(self.widget_4)
        self.btn_clear_table.setObjectName(u"btn_clear_table")
        self.btn_clear_table.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_clear_table.setStyleSheet(u"QPushButton {\n"
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

        self.horizontalLayout_2.addWidget(self.btn_clear_table)


        self.verticalLayout_4.addLayout(self.horizontalLayout_2)

        self.table_widget_sborka = QTableWidget(self.widget_4)
        if (self.table_widget_sborka.columnCount() < 3):
            self.table_widget_sborka.setColumnCount(3)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.table_widget_sborka.setHorizontalHeaderItem(0, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.table_widget_sborka.setHorizontalHeaderItem(1, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.table_widget_sborka.setHorizontalHeaderItem(2, __qtablewidgetitem4)
        self.table_widget_sborka.setObjectName(u"table_widget_sborka")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.table_widget_sborka.sizePolicy().hasHeightForWidth())
        self.table_widget_sborka.setSizePolicy(sizePolicy5)
        self.table_widget_sborka.setMinimumSize(QSize(0, 100))
        self.table_widget_sborka.setFont(font)
        self.table_widget_sborka.setStyleSheet(u"/* \u0421\u0430\u043c \u0432\u0438\u0434\u0436\u0435\u0442 \u2014 \u043f\u0440\u043e\u0437\u0440\u0430\u0447\u043d\u044b\u0439 \u0444\u043e\u043d */\n"
"QTableWidget {\n"
"    background: transparent;\n"
"    border: none;\n"
"    color: #ffffff;\n"
"    gridline-color: rgba(255, 255, 255, 0.15);\n"
"    selection-background-color: rgba(255, 255, 255, 0.25);\n"
"    selection-color: #ffffff;\n"
"}\n"
"\n"
"/* \u042f\u0447\u0435\u0439\u043a\u0438 \u2014 \u0431\u0435\u0437 \u0444\u043e\u043d\u0430, \u0431\u0435\u043b\u044b\u0439 \u0442\u0435\u043a\u0441\u0442 */\n"
"QTableWidget::item {\n"
"    background: transparent;\n"
"    color: #ffffff;\n"
"    padding: 4px 6px;\n"
"    border: none;\n"
"	border-left: 1px solid rgba(255, 255, 255, 0.15);\n"
"	border-bottom: 1px solid rgba(255, 255, 255, 0.15)\n"
"\n"
"}\n"
"\n"
"QTableWidget::item:hover {\n"
"    background: rgba(255, 255, 255, 0.08);\n"
"}\n"
"\n"
"QTableWidget::item:selected {\n"
"    background: rgba(255, 255, 255, 0.2);\n"
"    color: #ffffff;\n"
"}\n"
""
                        "\n"
"/* \u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043a\u0438 \u2014 \u0415\u0414\u0418\u041d\u0421\u0422\u0412\u0415\u041d\u041d\u041e\u0415 \u043c\u0435\u0441\u0442\u043e \u0441 \u0444\u043e\u043d\u043e\u043c */\n"
"QHeaderView::section {\n"
"    background-color: rgb(21, 69, 140);\n"
"    color: #ffffff;\n"
"    padding: 6px 8px;\n"
"    border: none;\n"
"    border-right: 1px solid rgba(255, 255, 255, 0.1);\n"
"    border-bottom: 1px solid rgba(255, 255, 255, 0.2);\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QHeaderView::section:hover {\n"
"    background-color: #3a3a3a;\n"
"}\n"
"\n"
"/* \u0423\u0433\u043b\u043e\u0432\u0430\u044f \u043a\u043d\u043e\u043f\u043a\u0430 (\u043f\u0435\u0440\u0435\u0441\u0435\u0447\u0435\u043d\u0438\u0435 \u0437\u0430\u0433\u043e\u043b\u043e\u0432\u043a\u043e\u0432) */\n"
"QTableCornerButton::section {\n"
"    background-color:  rgb(21, 69, 140);\n"
"    border: none;\n"
"    border-right: 1px solid rgba(255, 255, 255, 0.1);\n"
"    border-bottom: 1px solid rgba(255, 255, 255, 0"
                        ".2);\n"
"}\n"
"\n"
"/* \u0421\u043a\u0440\u043e\u043b\u043b\u0431\u0430\u0440\u044b \u2014 \u043c\u0438\u043d\u0438\u043c\u0430\u043b\u044c\u043d\u043e, \u0447\u0442\u043e\u0431\u044b \u043d\u0435 \u043c\u0435\u0448\u0430\u043b\u0438 */\n"
"QTableWidget QScrollBar:vertical {\n"
"    background: transparent;\n"
"    width: 8px;\n"
"}\n"
"\n"
"QTableWidget QScrollBar::handle:vertical {\n"
"    background: rgba(255, 255, 255, 0.3);\n"
"    border-radius: 4px;\n"
"    min-height: 20px;\n"
"}\n"
"\n"
"QTableWidget QScrollBar::handle:vertical:hover {\n"
"    background: rgba(255, 255, 255, 0.5);\n"
"}\n"
"\n"
"QTableWidget QScrollBar::add-line:vertical,\n"
"QTableWidget QScrollBar::sub-line:vertical,\n"
"QTableWidget QScrollBar::add-page:vertical,\n"
"QTableWidget QScrollBar::sub-page:vertical {\n"
"    background: transparent;\n"
"    height: 0px;\n"
"}\n"
"\n"
"QTableWidget QScrollBar:horizontal {\n"
"    background: transparent;\n"
"    height: 8px;\n"
"}\n"
"\n"
"QTableWidget QScrollBar::handle:horizontal {\n"
""
                        "    background: rgba(255, 255, 255, 0.3);\n"
"    border-radius: 4px;\n"
"    min-width: 20px;\n"
"}\n"
"\n"
"QTableWidget QScrollBar::handle:horizontal:hover {\n"
"    background: rgba(255, 255, 255, 0.5);\n"
"}\n"
"\n"
"QTableWidget QScrollBar::add-line:horizontal,\n"
"QTableWidget QScrollBar::sub-line:horizontal,\n"
"QTableWidget QScrollBar::add-page:horizontal,\n"
"QTableWidget QScrollBar::sub-page:horizontal {\n"
"    background: transparent;\n"
"    width: 0px;\n"
"}\n"
"QPushButton {\n"
"	border: 1px solid white;\n"
"	margin-top: 25px;\n"
"	margin-bottom: 25px;\n"
"	margin-left: 20px;\n"
"	margin-right: 20px;\n"
"	border-radius: 8px;\n"
"}\n"
"QPushButton:hover {\n"
"	border: 2px solid white;\n"
"	background: rgb(15, 65, 159)\n"
"}")
        self.table_widget_sborka.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.table_widget_sborka.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.table_widget_sborka.setAutoScroll(False)
        self.table_widget_sborka.setShowGrid(True)
        self.table_widget_sborka.setRowCount(0)
        self.table_widget_sborka.setColumnCount(3)
        self.table_widget_sborka.horizontalHeader().setVisible(True)
        self.table_widget_sborka.horizontalHeader().setStretchLastSection(True)
        self.table_widget_sborka.verticalHeader().setVisible(False)
        self.table_widget_sborka.verticalHeader().setMinimumSectionSize(90)
        self.table_widget_sborka.verticalHeader().setDefaultSectionSize(100)
        self.table_widget_sborka.verticalHeader().setProperty(u"showSortIndicator", False)
        self.table_widget_sborka.verticalHeader().setStretchLastSection(False)

        self.verticalLayout_4.addWidget(self.table_widget_sborka)


        self.verticalLayout_6.addLayout(self.verticalLayout_4)

        self.btn_save_and_export = QPushButton(self.widget_4)
        self.btn_save_and_export.setObjectName(u"btn_save_and_export")
        self.btn_save_and_export.setMaximumSize(QSize(16777215, 16777215))
        font2 = QFont()
        font2.setPointSize(11)
        self.btn_save_and_export.setFont(font2)
        self.btn_save_and_export.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_save_and_export.setStyleSheet(u"QPushButton {\n"
"	border: 1px solid;\n"
"	border-color: white;\n"
"	border-radius: 10px;\n"
"	height: 20px;	\n"
"	background-color: rgb(185, 57, 41);\n"
"	padding: 2 5 5 5;\n"
"	font-size: 11pt;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(0, 111, 171)\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: rgb(0, 53, 93)\n"
"}")

        self.verticalLayout_6.addWidget(self.btn_save_and_export, 0, Qt.AlignmentFlag.AlignHCenter)


        self.verticalLayout_2.addWidget(self.widget_4)


        self.horizontalLayout.addWidget(self.widget_2)


        self.verticalLayout_3.addLayout(self.horizontalLayout)


        self.retranslateUi(PageSborka)

        QMetaObject.connectSlotsByName(PageSborka)
    # setupUi

    def retranslateUi(self, PageSborka):
        PageSborka.setWindowTitle(QCoreApplication.translate("PageSborka", u"\u041f\u0440\u043e\u0447\u0438\u0435 \u043e\u043f\u0435\u0440\u0430\u0446\u0438\u0438", None))
        self.btn_home_1.setText(QCoreApplication.translate("PageSborka", u"\u0414\u043e\u043c\u043e\u0439", None))
        self.checkBox_only_find.setText(QCoreApplication.translate("PageSborka", u"\u0422\u043e\u043b\u044c\u043a\u043e \u043d\u0430\u0439\u0434\u0435\u043d\u043d\u044b\u0435 \u0432 \u0422\u0435\u0445\u043d\u043e\u041f\u0440\u043e", None))
        ___qtablewidgetitem = self.tableWidget_operations.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("PageSborka", u"\u041e\u043f\u0435\u0440\u0430\u0446\u0438\u0438", None))
        self.label.setText(QCoreApplication.translate("PageSborka", u"1. \u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435, \u043a \u043a\u0430\u043a\u043e\u0439 \u043e\u043f\u0435\u0440\u0430\u0446\u0438\u0438 \u043f\u043e \u0441\u0447\u0435\u0442\u0443 \u0432\u044b \u0445\u043e\u0442\u0438\u0442\u0435 \u0434\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u043f\u0435\u0440\u0435\u0445\u043e\u0434", None))
        self.btn_update_table.setText(QCoreApplication.translate("PageSborka", u"\u041e\u0431\u043d\u043e\u0432\u0438\u0442\u044c \u0441\u043f\u0438\u0441\u043e\u043a \u043e\u043f\u0435\u0440\u0430\u0446\u0438\u0439", None))
        ___qtablewidgetitem1 = self.tableWidget_find_operations.horizontalHeaderItem(0)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("PageSborka", u"\u041d\u0430\u0439\u0434\u0435\u043d\u043d\u044b\u0435 \u043e\u043f\u0435\u0440\u0430\u0446\u0438\u0438", None))
        self.text_info.setText("")
        self.label_6.setText(QCoreApplication.translate("PageSborka", u"\u041f\u0435\u0440\u0435\u0445\u043e\u0434\u044b, \u043a\u043e\u0442\u043e\u0440\u044b\u0435 \u0431\u0443\u0434\u0443\u0442 \u0434\u043e\u0431\u0430\u0432\u043b\u0435\u043d\u044b:", None))
        self.btn_clear_table.setText(QCoreApplication.translate("PageSborka", u"\u041e\u0447\u0438\u0441\u0442\u0438\u0442\u044c \u0442\u0430\u0431\u043b\u0438\u0446\u0443", None))
        ___qtablewidgetitem2 = self.table_widget_sborka.horizontalHeaderItem(0)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("PageSborka", u"\u0418\u043d\u0441\u0442\u0440\u0443\u043c\u0435\u043d\u0442", None))
        ___qtablewidgetitem3 = self.table_widget_sborka.horizontalHeaderItem(1)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("PageSborka", u"\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 [\u041c\u043e\u0436\u043d\u043e \u0438\u0437\u043c\u0435\u043d\u044f\u0442\u044c]", None))
        self.btn_save_and_export.setText(QCoreApplication.translate("PageSborka", u"\u041f\u0435\u0440\u0435\u043d\u0435\u0441\u0442\u0438 \u043f\u0435\u0440\u0435\u0445\u043e\u0434\u044b \u0432 \u0422\u0435\u0445\u043d\u043e\u041f\u0440\u043e", None))
    # retranslateUi

