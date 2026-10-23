from PySide6.QtWidgets import QWidget, QTableWidgetItem
from PySide6.QtCore import Signal

from ui_page_input_technopro import Ui_PageInputTechnopro

class PageInputTechnopro(QWidget):
    btn_clicked_tokarnaya = Signal()
    btn_clicked_update = Signal()
    btn_clicked_start = Signal(int, str)
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_PageInputTechnopro()
        self.ui.setupUi(self)

        self.ui.btn_home_tokarnaya.clicked.connect(self._on_button_clicked_home)
        self.ui.button_start.clicked.connect(self._on_button_click_start)
        self.ui.btn_update.clicked.connect(self._on_button_click_update)

    def _on_button_click_update(self):
        self.btn_clicked_update.emit()

    def _on_button_click_start(self):
        number_operation = self.ui.tableWidget.currentRow()
        result_button_clear = 'стереть' if self.ui.checkBox_clear_table.isChecked() else 'оставить'
        self.btn_clicked_start.emit(number_operation, result_button_clear)

    def _on_button_clicked_home(self):
        self.ui.error_label_start.setText('')
        self.btn_clicked_tokarnaya.emit()

    def add_item_table(self, count, operation):
        self.ui.error_label.setText('')
        self.ui.menu.show()
        self.ui.tableWidget.setRowCount(count)
        for i in range(count):
            item = QTableWidgetItem(operation)
            self.ui.tableWidget.setItem(i, 0, item)

    def show_error(self, operation):
        self.ui.menu.hide()
        self.ui.error_label.setText(f'Ошибка: кнопка "{operation}" не была найдена!')

    def error_start(self, text):
        self.ui.error_label_start.setText(text)