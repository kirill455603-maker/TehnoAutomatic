from ui_page_shlifovanie_start import Ui_ShlifovanieStart
from PySide6.QtWidgets import QWidget, QHeaderView
from PySide6.QtCore import Signal, Qt

class PageShlifovanieStart(QWidget):
    btn_save = Signal()
    btn_home = Signal()
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_ShlifovanieStart()
        self.ui.setupUi(self)
        self._connect_signals()
        self._start_settings()

    def _connect_signals(self):
        self._switch_pages()
        #Тип оправки
        self.ui.btn_opravka_ceh.clicked.connect(
            lambda: self.ui.type_opravka.hide()
        )
        self.ui.btn_opravka_number.clicked.connect(
            lambda: self.ui.type_opravka.show()
        )
        #Сохранить значения
        self.ui.btn_save_result_start.clicked.connect(
            lambda: self.btn_save.emit()
        )
        self.ui.btn_home.clicked.connect(self._on_btn_home)

    def _on_btn_home(self):
        self._clear_table()
        self.btn_home.emit()

    def _start_settings(self):
        self.ui.table_widget_start.horizontalHeader().setSectionResizeMode(0, QHeaderView.Fixed)
        self.ui.table_widget_start.horizontalHeader().setSectionResizeMode(1, QHeaderView.Stretch)
        self.ui.table_widget_start.horizontalHeader().resizeSection(0, 400)
        self.ui.table_widget_start.horizontalHeader().setStretchLastSection(True)
        self.ui.type_opravka.hide()
        self.ui.btn_centr.setChecked(True)
        self.ui.stackedWidget.setCurrentIndex(0)

    def _switch_pages(self):
        self.ui.btn_centr.clicked.connect(
            lambda: self.ui.stackedWidget.setCurrentIndex(0)
        )
        self.ui.btn_patron.clicked.connect(
            lambda: self.ui.stackedWidget.setCurrentIndex(1)
        )
        self.ui.btn_opravka.clicked.connect(
            lambda: self.ui.stackedWidget.setCurrentIndex(2)
        )

    def type_ystanovka(self):
        if self.ui.btn_centr.isChecked():
            return 'В центрах'
        elif self.ui.btn_patron.isChecked():
            return 'В патроне'
        elif self.ui.btn_opravka.isChecked():
            return 'На оправке'

    def data_on_center(self):
        d = {'зажим': self.ui.d_zazhim_centr.value(),
             'выставление': self.ui.d_vist_centr.value(),
             'диаметр шлифовки': self.ui.d_shlifovka_centr.value(),
             'биение': self.ui.bienie_centr.value()}
        return d

    def data_on_patron(self):
        d = {'зажим': self.ui.d_zazhim_patron.value(),
             'длина зажима': self.ui.length_zazhim_patron.value(),
             'диаметр шлифовки': self.ui.d_shlifovka_patron.value(),
             'выставление': self.ui.d_vist_patron.value(),
             'биение': self.ui.bienie_patron.value()}
        return d

    def _clear_table(self):
        self.ui.table_widget_start.clear()
        self.ui.table_widget_start.setRowCount(0)
        self.ui.table_widget_start.setHorizontalHeaderLabels(['Инструмент', 'Описание'])

    def data_on_opravka(self):
        d = {'оправка': None,
             'установочное отверстие': self.ui.d_ystanovka_opravka.value()}

        if self.ui.btn_opravka_number.isChecked():
            d['оправка'] = f'{self.ui.number_opravka_1.value()}—{self.ui.number_opravka_2.value()}'
        else:
            d['оправка'] = None
        return d

    def set_show_result(self, text, instrument):
        self.ui.table_widget_start.setRowCount(1)
        self.ui.table_widget_start.setItem(0, 0, instrument)
        self.ui.table_widget_start.setItem(0, 1, text)

    def set_show_error(self, text:str):
        self.ui.text_error_start.setText(text)