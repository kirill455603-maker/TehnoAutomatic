import time

from PySide6.QtWidgets import QWidget, QComboBox, QTableWidgetItem, QCheckBox, QHeaderView
from PySide6.QtCore import Signal, Qt, QTimer
from PySide6.QtGui import QCursor

from ui_page_tehno_iot import Ui_PageTehnoIot

class PageTehnoIot(QWidget):
    btn_home_clicked = Signal()
    btn_start_clicked = Signal()
    btn_update_clicked = Signal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_PageTehnoIot()
        self.ui.setupUi(self)

        self.ui.btn_home_1.clicked.connect(self._on_button_home_clicked)
        self.ui.button_start.clicked.connect(self._on_button_start_clicked)
        self.ui.btn_update_page.clicked.connect(self._on_button_update)
        self.ui.btn_select_all.clicked.connect(self.check_all)
        self.ui.btn_unsellect_all.clicked.connect(self.unchecked_all)
        self.ui.tableWidget.horizontalHeader().setSectionResizeMode(0, QHeaderView.Fixed)
        self.ui.tableWidget.horizontalHeader().resizeSection(0, 50)
        self.ui.tableWidget.horizontalHeader().setSectionResizeMode(2, QHeaderView.Stretch)
        self.ui.button_podbor.clicked.connect(self.podbor_stankov)
        self.ui.checkBox_del_instrument.clicked.connect(self._clicked_checkbox)

    def _clicked_checkbox(self):
        if self.ui.checkBox_del_instrument.isChecked():
            self.ui.label_4.setText('Внимание! Удалено будет только то оборудование, которое есть в выпадающием списке')
        else:
            self.ui.label_4.setText('')

    def podbor_stankov(self):
        diameter = self.ui.doubleSpinBox_nom_diameter.value()
        length = self.ui.doubleSpinBox_nom_diameter_2.value()
        rows = self.ui.tableWidget.rowCount()
        for row in range(rows):
            item_col_1 = self.ui.tableWidget.item(row, 0)
            print()
            text_find = None
            if item_col_1.checkState() == Qt.Checked:
                if item_col_1.text() == 'Отрезная':
                    if 400 < diameter <= 500:
                        text_find = 'Б Ленточнопильный станок, BS500CH'
                    elif 350 < diameter <= 400:
                        text_find = 'Б Ленточнопильный станок, Н-400'
                    elif 0 < diameter <= 350:
                        text_find = 'Б Ленточнопильный станок, S-350'
                elif item_col_1.text() == 'Токарная':
                    if diameter <= 220 and length <= 2000:
                        text_find = 'Б Токарно-винторезный станок, 16К20'
                    elif diameter <= 430 and length <= 3000:
                        text_find = 'Б Токарно-винторезный станок, 16К40Ф101'
                    elif diameter <= 400 and length <= 5000:
                        text_find = 'Б Токарно-винторезный станок, 1М63Б'
                    elif diameter <= 600 and length <= 3000:
                        text_find = 'Б Токарно-винторезный станок, 1М65Б'
                    elif diameter <= 1000 and length <= 1000:
                        text_find = 'Б Токарно-карусельный станок, 1512'
                elif item_col_1.text() == 'Термическая обработка':
                    if diameter <= 300 and length <= 350:
                        text_find = 'Б Электрическая печь СНОЛ 40/12'
                    elif diameter <= 400 and length <= 800:
                        text_find = 'Б Электрическая печь СНОЛ 120/12'
                    elif diameter <= 500 and length <= 750:
                        text_find = 'Б Электрическая печь СНОЛ 200/12'
                    elif diameter <= 800 and length <= 1600:
                        text_find = 'Б Электрическая печь СНОЛ 1000/12'
            if text_find:
                combo:QComboBox = self.ui.tableWidget.cellWidget(row, 2)
                if combo.currentText() != text_find:
                    combo.setStyleSheet(u"QComboBox {\n"
                                        "	width: 60px;\n"
                                        "	border: none;\n"
                                        "	border-bottom: 1px solid rgb(255, 147, 14);\n"
                                        "	background: rgba(255, 255, 255, 0);\n"
                                        "	transition: color 0.3s ease;\n"
                                        "	transition: border-bottom 0.4s ease;\n"
                                        "	color: rgb(255, 147, 14);\n"
                                        "   font-weight: semibold;\n"
                                        "	font-size: 9pt;\n"
                                        "}\n"
                                        "QComboBox:hover {\n"
                                        "   color: rgb(200, 200, 200);\n"
                                        "   cursor: pointer;\n"
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
                                        "	color:rgb(200, 200, 200);\n"
                                        "	border-bottom: 1px solid white;\n"
                                        "}\n"
                                        "\n"
                                        "")
                for combo_row in range(combo.count()):
                    if combo.itemText(combo_row) == text_find:
                        combo.setCurrentIndex(combo_row)
                        QTimer.singleShot(1000, lambda c=combo:self.edit_combo_box_timer(c))
            text_find = None

    def status_del_instrument(self):
        if self.ui.checkBox_del_instrument.isChecked():
            return True
        else:
            return False


    def _on_button_home_clicked(self):
        self.btn_home_clicked.emit()

    def _on_button_start_clicked(self):
        self.btn_start_clicked.emit()

    def _on_button_update(self):
        self.btn_update_clicked.emit()

    def add_items_tehno(self, operation, iot, instruments:list):
        self.ui.tableWidget.setRowCount(
            self.ui.tableWidget.rowCount() + 1
        )
        row = self.ui.tableWidget.rowCount() - 1

        combo = QComboBox()
        combo.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        combo.setStyleSheet(u"QComboBox {\n"      
                                             "	width: 60px;\n"
                                             "	border: none;\n"
                                             "	border-bottom: 1px solid white;\n"
                                             "	background: rgba(255, 255, 255, 0);\n"
                                             "	transition: color 0.3s ease;\n"
                                             "	transition: border-bottom 0.4s ease;\n"
                                             "	color: rgb(204, 204, 204);\n"
                                             "	font-size: 9pt;\n"
                                             "}\n"
                                             "QComboBox:hover {\n"
                                             "   color: rgb(200, 200, 200);\n"
                                             "   cursor: pointer;\n"
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
                                             "	color:rgb(200, 200, 200);\n"
                                             "	border-bottom: 1px solid white;\n"
                                             "}\n"
                                             "\n"
                                             "")
        for instrument in instruments:
            combo.addItem(instrument[0])
        self.ui.tableWidget.setItem(row, 0, operation)
        self.ui.tableWidget.setItem(row, 1, iot)
        self.ui.tableWidget.setCellWidget(row, 2, combo)

    def clear_table_tehno(self):
        self.ui.tableWidget.clear()
        self.ui.tableWidget.setRowCount(0)
        self.ui.tableWidget.setHorizontalHeaderLabels(['', 'Операция', 'ИОТ', 'Оборудование'])

    def get_result(self):
        rows = self.ui.tableWidget.rowCount()
        data = {}
        no_find = []
        for row in range(rows):
            item = self.ui.tableWidget.item(row, 0)
            if item.checkState() == Qt.Unchecked:
                no_find.append(item.text())
            else:
                combo = self.ui.tableWidget.cellWidget(row, 2)
                if combo:
                    value = combo.currentText()
                    operation = self.ui.tableWidget.item(row, 0).text()
                    data[operation] = value
        return data, no_find

    def get_count_row_table(self):
        return self.ui.tableWidget.rowCount()

    def hide_main(self):
        self.ui.main.hide()

    def show_main(self):
        self.ui.show_text.setText('')
        self.ui.show_text_2str.setText('')
        self.ui.main.show()

    def show_msg(self, text, text_2):
        self.ui.show_text.setText(text)
        self.ui.show_text_2str.setText(text_2)

    def check_all(self):
        for row in range(self.ui.tableWidget.rowCount()):
            item = self.ui.tableWidget.item(row, 0)
            item.setCheckState(Qt.Checked)

    def unchecked_all(self):
        for row in range(self.ui.tableWidget.rowCount()):
            item = self.ui.tableWidget.item(row, 0)
            item.setCheckState(Qt.Unchecked)

    def edit_combo_box_timer(self, combo):
        combo.setStyleSheet(u"QComboBox {\n"
                            "	width: 60px;\n"
                            "	border: none;\n"
                            "	border-bottom: 1px solid white;\n"
                            "	background: rgba(255, 255, 255, 0);\n"
                            "	transition: color 0.3s ease;\n"
                            "	transition: border-bottom 0.4s ease;\n"
                            "	color: rgb(204, 204, 204);\n"
                            "	font-size: 9pt;\n"
                            "}\n"
                            "QComboBox:hover {\n"
                            "   color: rgb(200, 200, 200);\n"
                            "   cursor: pointer;\n"
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
                            "	color:rgb(200, 200, 200);\n"
                            "	border-bottom: 1px solid white;\n"
                            "}\n"
                            "\n"
                            "")