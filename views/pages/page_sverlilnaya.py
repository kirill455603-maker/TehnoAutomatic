from PySide6.QtWidgets import QWidget, QHeaderView, QPushButton
from PySide6.QtCore import Signal
from ui_page_sverlilnaya import Ui_PageSverlilnaya

class PageSverlilnaya(QWidget):
    btn_home_clicked = Signal()
    btn_save_result_clicked = Signal(dict)
    btn_clear_table_clicked = Signal()
    btn_click_delete = Signal(int)
    btn_save_and_export_clicked = Signal()
    btn_click_page = Signal(int)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_PageSverlilnaya()
        self.ui.setupUi(self)

        self.ui.table_widget_sverlilnaya.horizontalHeader().setSectionResizeMode(0, QHeaderView.Fixed)
        self.ui.table_widget_sverlilnaya.horizontalHeader().setSectionResizeMode(1, QHeaderView.Fixed)
        self.ui.table_widget_sverlilnaya.horizontalHeader().setSectionResizeMode(2, QHeaderView.Stretch)
        self.ui.table_widget_sverlilnaya.horizontalHeader().resizeSection(0, 400)
        self.ui.table_widget_sverlilnaya.horizontalHeader().resizeSection(1, 400)
        self.ui.table_widget_sverlilnaya.horizontalHeader().setStretchLastSection(True)

        self._delete_buttons = []

        self.ui.btn_home_1.clicked.connect(self._on_button_clicked)
        self.ui.btn_save_result.clicked.connect(self._on_save_clicked)
        self.ui.btn_clear_table.clicked.connect(self._on_clear_clicked)
        self.ui.btn_save_and_export.clicked.connect(self._on_save_and_export_clicked)


        self.ui.btn_page1.clicked.connect(self.find_page_click)
        self.ui.btn_page2.clicked.connect(self.find_page_click)
        self.ui.btn_page3.clicked.connect(self.find_page_click)
        self.ui.btn_page4.clicked.connect(self.find_page_click)
        self.ui.btn_page5.clicked.connect(self.find_page_click)



    def find_page_click(self):
        if self.ui.btn_page1.isChecked():
            self.btn_click_page.emit(0)
        if self.ui.btn_page2.isChecked():
            self.btn_click_page.emit(1)
        if self.ui.btn_page3.isChecked():
            self.btn_click_page.emit(2)
        if self.ui.btn_page4.isChecked():
            self.btn_click_page.emit(3)
        if self.ui.btn_page5.isChecked():
            self.btn_click_page.emit(4)

    def switch_page(self, number):
        self.ui.stackedWidget_pages.setCurrentIndex(number)

    def _on_button_clicked(self):
        self.btn_home_clicked.emit()

    def _on_save_clicked(self):
        data = None
        if self.get_current_page() == 0:
            data = self.ui.page_sverlilnaya_start.get_value()
        elif self.get_current_page() == 1:
            data = self.ui.page_sverlilnaya_expanding_hole.get_value()
        elif self.get_current_page() == 2:
            data = self.ui.page_sverlilnaya_chistovaya.get_value()
        elif self.get_current_page() == 3:
            data = self.ui.page_sverlilnaya_rezba.get_value()
        elif self.get_current_page() == 4:
            data = self.ui.page_sverlilnaya_faska.get_value()
        self.btn_save_result_clicked.emit(data)

    def _on_clear_clicked(self):
        self.btn_clear_table_clicked.emit()

    def _on_save_and_export_clicked(self):
        self.btn_save_and_export_clicked.emit()

    def show_result(self, text, instrument, key_count):
        """Добавляет строку в таблицу. Сигнатура ОБЯЗАТЕЛЬНА!"""
        self.ui.table_widget_sverlilnaya.setRowCount(
            self.ui.table_widget_sverlilnaya.rowCount() + 1
        )
        row = self.ui.table_widget_sverlilnaya.rowCount() - 1

        self.ui.table_widget_sverlilnaya.setItem(row, 0, instrument)
        self.ui.table_widget_sverlilnaya.setItem(row, 1, text)

        btn_delete = QPushButton('Удалить')
        btn_delete.clicked.connect(
            lambda checked, r=key_count: self.on_delete_clicked(r)
        )

        # Сохраняем ссылку, чтобы сборщик мусора не удалил
        self._delete_buttons.append(btn_delete)
        btn_delete.resize(50, 20)
        self.ui.table_widget_sverlilnaya.setCellWidget(row, 2, btn_delete)

    def on_delete_clicked(self, r):
        self.btn_click_delete.emit(r)

    def clear_table(self):
        """Очистка таблицы. ОБЯЗАТЕЛЬНЫЙ метод."""
        self.ui.table_widget_sverlilnaya.clear()
        self.ui.table_widget_sverlilnaya.setRowCount(0)
        self.ui.table_widget_sverlilnaya.setHorizontalHeaderLabels(
            ['Инструмент', 'Описание[Можно изменять]', '']
        )
        self._delete_buttons.clear()

    def get_index_row(self, item):
        """Возвращает индекс строки. ОБЯЗАТЕЛЬНЫЙ метод."""
        return self.ui.table_widget_sverlilnaya.row(item)

    def delete_row(self, r):
        """Удаляет строку. ОБЯЗАТЕЛЬНЫЙ метод."""
        self.ui.table_widget_sverlilnaya.removeRow(r)

    def show_label(self, text):
        """Показывает сообщение. ОБЯЗАТЕЛЬНЫЙ метод."""
        self.ui.text_info.setText(text)

    def get_current_page(self):
        return self.ui.stackedWidget_pages.currentIndex()


