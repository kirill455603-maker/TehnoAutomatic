from PySide6.QtWidgets import QWidget, QHeaderView
from PySide6.QtCore import Signal
from ui_page_tokarnaya_start import Ui_PageTokarnayaStart


class PageTokarnayaStart(QWidget):
    btn_home_tokarnaya_clicked = Signal()
    btn_save_result_clicked = Signal(dict)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_PageTokarnayaStart()
        self.ui.setupUi(self)
        self.signals()
        self.ui.widget.hide()
        self.ui.layout_baza.hide()

        self.ui.table_widget_start.horizontalHeader().setSectionResizeMode(0, QHeaderView.Fixed)
        self.ui.table_widget_start.horizontalHeader().setSectionResizeMode(1, QHeaderView.Stretch)
        self.ui.table_widget_start.horizontalHeader().resizeSection(0, 400)
        self.ui.table_widget_start.horizontalHeader().setStretchLastSection(True)
        self.ui.table_widget_start.setRowCount(1)

    def signals(self):
        #Сигналы на отправку
        self.ui.btn_home_tokarnaya.clicked.connect(self._on_button_home_tokarnaya_clicked)

        #Внутренние сигналы
        self.ui.checkBox.clicked.connect(self._on_click_checkbox)
        self.ui.btn_diameter.clicked.connect(self._on_btn_diameter)
        self.ui.btn_baza.clicked.connect(self._on_btn_baza)


        self.ui.btn_save_result_start.clicked.connect(self._on_button_clicked_save_result)

    def _on_click_checkbox(self):
        if self.ui.checkBox.isChecked():
            self.ui.widget.show()
        else:
            self.ui.widget.hide()


    def _on_button_home_tokarnaya_clicked(self):
        self.clear_all()
        self.btn_home_tokarnaya_clicked.emit()

    def _on_btn_diameter(self):
        self.ui.layout_diameter.show()
        self.ui.layout_baza.hide()
        self.ui.line_edit_baza.setText('')

    def _on_btn_baza(self):
        self.ui.layout_diameter.hide()
        self.ui.layout_baza.show()
        self.ui.double_spin_start_diameter_2.setValue(0)

    def _on_button_clicked_save_result(self):
        d = {'диаметр установки': self.ui.double_spin_start_diameter.value(),
             'статус чек': self.ui.checkBox.isChecked(),
             'по диаметру': self.ui.double_spin_start_diameter_2.value(),
             'по базе': self.ui.line_edit_baza.text(),
             'биение радиальное': self.ui.double_spin_start_diameter_3.value(),
             'биение торцевое': self.ui.double_spin_start_diameter_4.value(),
             'диаметр заготовки': self.ui.double_spin_start_diameter.value()}
        self.btn_save_result_clicked.emit(d)

    def set_show_error(self, text:str):
        self.ui.text_error_start.setText(text)

    def set_show_result(self, text, instrument):
        self.ui.text_error_start.setText('')
        self.ui.table_widget_start.setItem(0, 0, instrument)
        self.ui.table_widget_start.setItem(0, 1, text)

    def clear_all(self):
        self.ui.double_spin_start_diameter.setValue(0)
        self.ui.text_error_start.setText('')
        self.ui.table_widget_start.clear()
        self.ui.table_widget_start.setHorizontalHeaderLabels(['Инструмент', 'Описание'])
        self.ui.widget.hide()
        self.ui.checkBox.setChecked(False)
        self.ui.btn_diameter.click()
        self.ui.line_edit_baza.setText('')
        self.ui.double_spin_start_diameter_2.setValue(0)
        self.ui.double_spin_start_diameter_3.setValue(0)
