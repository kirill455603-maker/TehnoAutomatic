from PySide6.QtWidgets import QWidget, QHeaderView
from PySide6.QtCore import Signal, Qt
from ui_page_shlifovanie_osnovnoe import Ui_ShlifovanieOsnovnoe

class PageShlifovanieOsnovnoe(QWidget):
    btn_home = Signal()
    btn_save = Signal()
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_ShlifovanieOsnovnoe()
        self.ui.setupUi(self)
        self._connect_buttons()
        self._start_settings()

    def _connect_buttons(self):
        self.ui.btn_home.clicked.connect(self._on_btn_home)
        self.ui.btn_save_result_start.clicked.connect(
            lambda: self.btn_save.emit()
        )

    def _start_settings(self):
        self.ui.table_widget.horizontalHeader().setSectionResizeMode(0, QHeaderView.Fixed)
        self.ui.table_widget.horizontalHeader().setSectionResizeMode(1, QHeaderView.Stretch)
        self.ui.table_widget.horizontalHeader().resizeSection(0, 400)
        self.ui.table_widget.horizontalHeader().setStretchLastSection(True)
        self.ui.stackedWidget.setCurrentIndex(1)


    def _on_btn_home(self):
        self._clear_table()
        self.btn_home.emit()

    def _clear_table(self):
        self.ui.table_widget.clear()
        self.ui.table_widget.setHorizontalHeaderLabels(['Инструмент', 'Описание'])

    def set_show_result(self, text, instrument):
        self.ui.table_widget.setRowCount(self.ui.table_widget.rowCount() + 1)
        row =self.ui.table_widget.rowCount() - 1
        self.ui.table_widget.setItem(row, 0, instrument)
        self.ui.table_widget.setItem(row, 1, text)

    def set_show_error(self, text:str):
        self.ui.text_error_start.setText(text)

    def get_result(self):
        d = {
            'тип': None,
            'диаметр': self.ui.diameter.value(),
            'длина': self.ui.length.value(),
            'шероховатость': None,
            'квалитет_диаметер': self.ui.kvalitet_diameter_2.text(),
            'допуск_д_1': self.ui.dopusk_d_1.value(),
            'допуск_д_2': self.ui.dopusk_d_2.value(),
            'квалитет_длина': self.ui.kvalitet_length.text(),
            'допуск_дл_1': self.ui.dopusk_length_1.value(),
            'допуск_дл_2': self.ui.dopusk_length_2.value(),
        }
        if self.ui.btn_in.isChecked():
            d['тип'] = 'внутреннее'
        else:
            d['тип'] = 'внешнее'

        if self.ui.radioButton_ra3.isChecked():
            d['шероховатость'] = 'Ra 0,2'
        elif self.ui.radioButton_ra2.isChecked():
            d['шероховатость'] = 'Ra 0,4'
        elif self.ui.radioButton_ra1.isChecked():
            d['шероховатость'] = 'Ra 0,8'
        return d