from PySide6.QtWidgets import QWidget, QHeaderView
from PySide6.QtCore import Signal
from ui_page_tokarnaya_rezba import Ui_PageTokarnayaRezba

class PageTokarnayaRezba(QWidget):
    btn_home_clicked = Signal()
    btn_save_result = Signal(dict)
    btn_radio_in_click = Signal()
    btn_radio_out_click = Signal()
    list_diamter_rezba_edit = Signal(float)
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_PageTokarnayaRezba()
        self.ui.setupUi(self)

        self.ui.table_widget_rezba.horizontalHeader().setSectionResizeMode(0, QHeaderView.Fixed)
        self.ui.table_widget_rezba.horizontalHeader().setSectionResizeMode(1, QHeaderView.Stretch)
        self.ui.table_widget_rezba.horizontalHeader().resizeSection(0, 400)
        self.ui.table_widget_rezba.horizontalHeader().setStretchLastSection(True)
        self.ui.table_widget_rezba.setRowCount(1)

        self.ui.btn_home.clicked.connect(self._on_button_home_clicked)

        self.ui.btn_save_result_rezba.clicked.connect(self._on_button_save_result)
        self.ui.spinBox_diameter.currentIndexChanged.connect(self.edit_list_step)
        self.ui.radioButton_in.clicked.connect(self._on_button_radio_in)
        self.ui.radioButton_out.clicked.connect(self._on_button_radio_out)

    def _on_button_radio_out(self):
        self.btn_radio_out_click.emit()

    def _on_button_radio_in(self):
        self.btn_radio_in_click.emit()

    def _on_button_save_result(self):
        my_dict = {'диаметр': self.ui.spinBox_diameter.currentText(),
                   'шаг': self.ui.comboBox_step.currentText(),
                   'длина': self.ui.double_spin_length.value(),
                   'допуск': self.ui.comboBox_dopusk.currentText(),
                   'расположение': 'внутренняя' if self.ui.radioButton_in.isChecked() else 'внешняя',
                   'направление': 'правое' if self.ui.radioButton_right.isChecked() else 'левое'}
        self.btn_save_result.emit(my_dict)

    def edit_list_step(self):
        value = self.ui.spinBox_diameter.currentText()
        self.ui.comboBox_step.clear()
        self.list_diamter_rezba_edit.emit(float(value[1:]))

    def add_list_diameter(self, diameters:list):
        diameters = [f'М{diameter}' for diameter in diameters]
        self.ui.spinBox_diameter.addItems(diameters)
        self.ui.spinBox_diameter.setCurrentIndex(11)


    def edit_list_dopusk(self, dopuski:list):
        self.ui.comboBox_dopusk.clear()
        self.ui.comboBox_dopusk.addItems(dopuski)

    def add_list_step(self, steps:list):
        self.ui.comboBox_step.addItems(steps)



    def _on_button_home_clicked(self):
        self.clear_all()
        self.btn_home_clicked.emit()

    def show_result(self, text, instrument):
        self.ui.table_widget_rezba.setRowCount(1)
        self.ui.table_widget_rezba.setItem(0, 0, instrument)
        self.ui.table_widget_rezba.setItem(0, 1, text)

    def set_show_error(self, text):
        self.ui.text_error_start.setText(text)

    def clear_all(self):
        self.ui.table_widget_rezba.clear()
        self.ui.table_widget_rezba.setHorizontalHeaderLabels(['Инструмент', 'Описание'])
        self.ui.text_error_start.setText('')
        self.ui.spinBox_diameter.setCurrentIndex(11)
        self.ui.comboBox_step.setCurrentIndex(0)
        self.ui.double_spin_length.setValue(0)
        self.ui.comboBox_dopusk.setCurrentIndex(0)