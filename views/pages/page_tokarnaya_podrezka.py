from PySide6.QtWidgets import QWidget, QHeaderView
from PySide6.QtCore import Signal
from ui_page_tokarnaya_podrezka import Ui_PageTokarnayaPodrezka


class PageTokarnayaPodrezka(QWidget):
    btn_save_result_podrezka_clicked = Signal(dict)
    btn_home_tokarnaya_clicked = Signal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_PageTokarnayaPodrezka()
        self.ui.setupUi(self)

        self.ui.table_widget.horizontalHeader().setSectionResizeMode(0, QHeaderView.Fixed)
        self.ui.table_widget.horizontalHeader().setSectionResizeMode(1, QHeaderView.Stretch)
        self.ui.table_widget.horizontalHeader().resizeSection(0, 400)
        self.ui.table_widget.horizontalHeader().setStretchLastSection(True)
        self.ui.table_widget.setRowCount(1)


        self.ui.btn_home_tokarnaya_podrezka.clicked.connect(self._on_button_home)
        self.ui.btn_save.clicked.connect(self._on_button_save_result_click)





    def _on_button_home(self):
        self.clear_text()
        self.btn_home_tokarnaya_clicked.emit()

    def clear_text(self):
        self.ui.text_error_podrezka.setText('')
        self.ui.table_widget.clear()
        self.ui.table_widget.setHorizontalHeaderLabels(['Инструмент', 'Описание'])

    def set_show_error(self, text):
        self.ui.text_error_podrezka.setText(text)



    def _on_button_save_result_click(self):
        if self.ui.radioButton_ra1.isChecked():
            surf = 0.8
        elif self.ui.radioButton_ra2.isChecked():
            surf = 1.6
        elif self.ui.radioButton_ra3.isChecked():
            surf = 3.2
        elif self.ui.radioButton_ra4.isChecked():
            surf = 6.3
        elif self.ui.radioButton_ra5.isChecked():
            surf = 12.5
        else:
            surf = 0
        result = {
            'длина': self.ui.value_length.value(),
            'шероховатость': surf,
            'квалитет': self.ui.kavalitet_length.text(),
            'допуск_1': self.ui.dopusk_length.value(),
            'допуск_2': self.ui.dopusk_length_2.value()
        }
        self.ui.text_error_podrezka.setText('')
        self.btn_save_result_podrezka_clicked.emit(result)

    def show_text_result(self, text, instrument):
        self.ui.table_widget.setItem(0, 0, instrument)
        self.ui.table_widget.setItem(0, 1, text)
