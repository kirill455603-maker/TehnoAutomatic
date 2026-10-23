from PySide6.QtWidgets import QWidget, QHeaderView
from ui_page_tokarnaya_faska import Ui_PageTokarnayaFaska
from PySide6.QtCore import Signal

class PageTokarnayaFaska(QWidget):
    btn_home_clicked = Signal()
    btn_save_result_clicked = Signal(dict)
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_PageTokarnayaFaska()
        self.ui.setupUi(self)

        self.ui.table_widget_faska.horizontalHeader().setSectionResizeMode(0, QHeaderView.Fixed)
        self.ui.table_widget_faska.horizontalHeader().setSectionResizeMode(1, QHeaderView.Stretch)
        self.ui.table_widget_faska.horizontalHeader().resizeSection(0, 400)
        self.ui.table_widget_faska.horizontalHeader().setStretchLastSection(True)
        self.ui.table_widget_faska.setRowCount(1)
        self.ui.btn_home_tokarnaya_faska.clicked.connect(self._go_to_tokarnaya)
        self.ui.btn_save_result_faska.clicked.connect(self.save_result)


    def save_result(self):
        dict_faska = {'длина': self.ui.doubleSpinBox_len.value(),
                      'угол': self.ui.spinBox_angle.value(),
                      'количество': self.ui.spinBox_count.value(),
                      'расположение': 'внешняя' if self.ui.radioButton_out_2.isChecked() else 'внутренняя'}
        self.btn_save_result_clicked.emit(dict_faska)

    def _go_to_tokarnaya(self):
        self.clear_all()
        self.btn_home_clicked.emit()

    def clear_all(self):
        self.ui.doubleSpinBox_len.setValue(1)
        self.ui.spinBox_angle.setValue(45)
        self.ui.table_widget_faska.clear()
        self.ui.table_widget_faska.setHorizontalHeaderLabels(['Инструмент', 'Описание'])
        self.ui.text_error_faska.setText('')
        self.ui.spinBox_count.setValue(1)

    def show_result(self, text, instrument):
        self.ui.table_widget_faska.setRowCount(1)
        self.ui.table_widget_faska.setItem(0, 0, instrument)
        self.ui.table_widget_faska.setItem(0, 1, text)

    def show_label(self, text):
        self.ui.text_error_faska.setText(text)