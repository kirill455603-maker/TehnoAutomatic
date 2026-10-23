# pages/page_razmetka.py
from PySide6.QtWidgets import QWidget, QHeaderView, QPushButton
from PySide6.QtCore import Signal
from ui_page_razmetka import Ui_PageRazmetka


class PageRazmetka(QWidget):
    btn_home_clicked = Signal()
    btn_save_result_clicked = Signal(dict)
    btn_clear_table_clicked = Signal()
    btn_click_delete = Signal(int)
    btn_save_and_export_clicked = Signal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_PageRazmetka()
        self.ui.setupUi(self)

        self.ui.table_widget_razmetka.horizontalHeader().setSectionResizeMode(0, QHeaderView.Fixed)
        self.ui.table_widget_razmetka.horizontalHeader().setSectionResizeMode(1, QHeaderView.Fixed)
        self.ui.table_widget_razmetka.horizontalHeader().setSectionResizeMode(2, QHeaderView.Stretch)
        self.ui.table_widget_razmetka.horizontalHeader().resizeSection(0, 400)
        self.ui.table_widget_razmetka.horizontalHeader().resizeSection(1, 400)
        self.ui.table_widget_razmetka.horizontalHeader().setStretchLastSection(True)

        self._delete_buttons = []

        self.ui.btn_home_2.clicked.connect(self._on_button_home_clicked)
        self.ui.btn_save_result.clicked.connect(self._on_button_save_clicked)
        self.ui.btn_clear_table.clicked.connect(self._on_button_clear_table_clicked)
        self.ui.btn_save_and_export.clicked.connect(self._on_button_save_and_export)
        self.ui.pushButton_rezba.clicked.connect(self.show_and_hide_stacked)
        self.ui.pushButton_no_rezba.clicked.connect(self.show_and_hide_stacked)

    def show_and_hide_stacked(self):
        if self.ui.pushButton_rezba.isChecked():
            self.ui.stackedWidget.setCurrentIndex(1)
            self.clear_stacked_no_rezba()
        if self.ui.pushButton_no_rezba.isChecked():
            self.ui.stackedWidget.setCurrentIndex(0)
            self.clear_stacked_rezba()

    def clear_stacked_rezba(self):
        self.ui.spinBox_diameter.setCurrentIndex(-1)
    def clear_stacked_no_rezba(self):
        self.ui.doubleSpinBox_diameter.setValue(0)

    def _on_button_save_and_export(self):
        self.btn_save_and_export_clicked.emit()

    def _on_button_clear_table_clicked(self):
        self.btn_clear_table_clicked.emit()

    def _on_button_home_clicked(self):
        self.btn_home_clicked.emit()

    def _on_button_save_clicked(self):
        data = {
            'резьба': self.ui.spinBox_diameter.currentText(),
            'без резьбы': self.ui.doubleSpinBox_diameter.value(),
            'диаметр разметки': self.ui.doubleSpinBox_diameter_position.value(),
            'количество': self.ui.spinBox_count.value(),
            'угол': self.ui.spinBox_angle.value(),
            'допуск': self.ui.doubleSpinBox_dopusk.value(),
            'база': self.ui.lineEdit_baza.text()
        }
        self.btn_save_result_clicked.emit(data)

    def show_result(self, text, instrument, key_count):
        """УНИВЕРСАЛЬНЫЙ МЕТОД — сигнатура такая же, как у PageTokarnaya."""
        self.ui.table_widget_razmetka.setRowCount(self.ui.table_widget_razmetka.rowCount() + 1)
        row = self.ui.table_widget_razmetka.rowCount() - 1

        self.ui.table_widget_razmetka.setItem(row, 0, instrument)
        self.ui.table_widget_razmetka.setItem(row, 1, text)

        btn_delete = QPushButton('Удалить')
        btn_delete.resize(50, 30)
        btn_delete.clicked.connect(lambda checked, r=key_count: self.on_delete_clicked(r))

        # Сохраняем ссылку
        self._delete_buttons.append(btn_delete)

        self.ui.table_widget_razmetka.setCellWidget(row, 2, btn_delete)

    def on_delete_clicked(self, r):
        self.btn_click_delete.emit(r)

    def clear_table(self):
        self.ui.table_widget_razmetka.clear()
        self.ui.table_widget_razmetka.setRowCount(0)
        self.ui.table_widget_razmetka.setHorizontalHeaderLabels(['Инструмент', 'Описание [Можно изменять]', ''])
        self._delete_buttons.clear()

    def show_label(self, text):
        self.ui.text_info.setText(text)

    def show_d_rezb(self, d_list: list):
        data = [f'М{item}' for item in d_list]
        self.ui.spinBox_diameter.addItems(data)

    def get_index_row(self, item):
        return self.ui.table_widget_razmetka.row(item)

    def delete_row(self, r):
        self.ui.table_widget_razmetka.removeRow(r)