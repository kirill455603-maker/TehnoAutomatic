from PySide6.QtWidgets import QWidget, QHeaderView, QPushButton
from PySide6.QtCore import Signal

from ui_page_sborka import Ui_PageSborka


class PageSborka(QWidget):
    btn_home_clicked = Signal()
    checkbox_clicked = Signal()
    table_select_clicked = Signal(str)
    table_number_operation_clicked = Signal(str)
    btn_click_delete = Signal(int)
    btn_clear_table = Signal()
    btn_export_clicked = Signal()
    btn_update_clicked = Signal()
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_PageSborka()
        self.ui.setupUi(self)

        self.ui.table_widget_sborka.horizontalHeader().setSectionResizeMode(2, QHeaderView.Stretch)
        self.ui.table_widget_sborka.horizontalHeader().resizeSection(0, 280)
        self.ui.table_widget_sborka.horizontalHeader().resizeSection(1, 280)
        self.ui.table_widget_sborka.horizontalHeader().resizeSection(2, 150)
        self.ui.table_widget_sborka.horizontalHeader().setStretchLastSection(True)


        self.ui.btn_home_1.clicked.connect(self._on_button_home_clicked)
        self.ui.checkBox_only_find.clicked.connect(self._on_checkbox_clicked)
        self.ui.tableWidget_operations.cellClicked.connect(self._on_select_operation)
        self.ui.tableWidget_find_operations.cellClicked.connect(self._on_select_number_operation)
        self.ui.btn_clear_table.clicked.connect(self._on_button_clear_table)
        self.ui.btn_update_table.clicked.connect(self._on_button_update_table)


        self.ui.btn_save_and_export.clicked.connect(self._on_button_save)

        self._delete_buttons = []

    def _on_button_update_table(self):
        self.btn_update_clicked.emit()

    def _on_button_save(self):
        self.btn_export_clicked.emit()

    def _on_button_clear_table(self):
        self.btn_clear_table.emit()
    def _on_button_home_clicked(self):
        self.btn_home_clicked.emit()

    def add_items_operations(self, operation):
        self.ui.tableWidget_operations.setRowCount(
            self.ui.tableWidget_operations.rowCount() + 1
        )
        row = self.ui.tableWidget_operations.rowCount() - 1
        self.ui.tableWidget_operations.setItem(row, 0, operation)

    def is_checkbox_find(self):
        return self.ui.checkBox_only_find.isChecked()

    def clear_table_operations(self):
        self.ui.tableWidget_operations.clear()
        self.ui.tableWidget_operations.setHorizontalHeaderLabels(['Операции'])
        self.ui.tableWidget_operations.setRowCount(0)

    def _on_checkbox_clicked(self):
        self.checkbox_clicked.emit()

    def _on_select_operation(self):
        value = self.ui.tableWidget_operations.currentItem().text()
        self.table_select_clicked.emit(value)

    def _on_select_number_operation(self):
        text = self.ui.tableWidget_find_operations.currentItem().text()
        row = self.ui.tableWidget_find_operations.currentItem().row()
        self.table_number_operation_clicked.emit(text)

    def clear_table_with_find_operations(self):
        self.ui.tableWidget_find_operations.clear()
        self.ui.tableWidget_find_operations.setHorizontalHeaderLabels(['Найденные операции'])
        self.ui.tableWidget_find_operations.setRowCount(0)

    def add_items_find_operations(self, operation):
        self.ui.tableWidget_find_operations.setRowCount(
            self.ui.tableWidget_find_operations.rowCount() + 1
            )
        row = self.ui.tableWidget_find_operations.rowCount() - 1
        self.ui.tableWidget_find_operations.setItem(row, 0, operation)

    def clear_table_sborka(self):
        self.ui.table_widget_sborka.clear()
        self.ui.table_widget_sborka.setHorizontalHeaderLabels(['Инструмент', 'Описание [Можно изменять]', ''])
        self.ui.table_widget_sborka.setRowCount(0)

    def show_result(self, text, instrument, key_count):
        self.show_label('')
        """Добавляет строку в таблицу. Сигнатура ОБЯЗАТЕЛЬНА!"""
        self.ui.table_widget_sborka.setRowCount(
            self.ui.table_widget_sborka.rowCount() + 1
        )
        row = self.ui.table_widget_sborka.rowCount() - 1

        self.ui.table_widget_sborka.setItem(row, 0, instrument)
        self.ui.table_widget_sborka.setItem(row, 1, text)

        btn_delete = QPushButton('Удалить')
        btn_delete.clicked.connect(
            lambda checked, r=key_count: self.on_delete_clicked(r)
        )

        # Сохраняем ссылку, чтобы сборщик мусора не удалил
        self._delete_buttons.append(btn_delete)
        btn_delete.resize(50, 20)
        self.ui.table_widget_sborka.setCellWidget(row, 2, btn_delete)

    def on_delete_clicked(self, r):
        self.btn_click_delete.emit(r)

    def show_label(self, text):
        self.ui.text_info.setText(text)

    def delete_row(self, r):
        """Удаляет строку. ОБЯЗАТЕЛЬНЫЙ метод."""
        self.ui.table_widget_sborka.removeRow(r)

    def get_index_row(self, item):
        """Возвращает индекс строки. ОБЯЗАТЕЛЬНЫЙ метод."""
        return self.ui.table_widget_sborka.row(item)

    def get_index_number_operations(self):
        item = self.ui.tableWidget_find_operations.currentItem()
        index = self.ui.tableWidget_find_operations.row(item)
        return index

    def get_text_operations(self):
        try:
            text = self.ui.tableWidget_find_operations.currentItem().text()
            return text
        except:
            return 0

    def get_text_table_operations(self):
        text = self.ui.tableWidget_operations.currentItem().text()
        return text








