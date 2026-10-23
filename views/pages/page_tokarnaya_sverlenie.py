from PySide6.QtWidgets import QWidget, QHeaderView
from PySide6.QtCore import Signal
from ui_page_tokarnaya_sverlenie import Ui_PageTokarnayaSverlenie

class PageTokarnayaSverlenie(QWidget):
    btn_home_sverlenie_clicked = Signal()
    btn_save_result_sverlenie_clicked = Signal(float, float)
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_PageTokarnayaSverlenie()
        self.ui.setupUi(self)
        self.start_settings()
        self.signals()

        self.ui.table_widget_sverlenie.horizontalHeader().setSectionResizeMode(0, QHeaderView.Fixed)
        self.ui.table_widget_sverlenie.horizontalHeader().setSectionResizeMode(1, QHeaderView.Stretch)
        self.ui.table_widget_sverlenie.horizontalHeader().resizeSection(0, 400)
        self.ui.table_widget_sverlenie.horizontalHeader().setStretchLastSection(True)
        self.ui.table_widget_sverlenie.setRowCount(1)

    def signals(self):
        self.ui.checkbox_length.clicked.connect(self.edit_checkbox_length)
        self.ui.btn_home_tokarnaya_sverlenie.clicked.connect(self._on_button_home_clicked)
        self.ui.btn_save_result_sverlenie.clicked.connect(self.export_result)

    def add_sverla(self, sverla:list):
        self.ui.comboBox_sverlenie.addItems(sverla)

    def export_result(self):
        self.ui.text_error_start.setText('')
        diameter = float(self.ui.comboBox_sverlenie.currentText())
        length = self.ui.double_spin_length.value()
        self.btn_save_result_sverlenie_clicked.emit(diameter, length)

    def _on_button_home_clicked(self):
        self.clear_all()
        self.btn_home_sverlenie_clicked.emit()



    def start_settings(self):
        self.ui.widget_length.hide()

    def edit_checkbox_length(self):
        if self.ui.checkbox_length.isChecked():
            self.ui.widget_length.show()
        elif not self.ui.checkbox_length.isChecked():
            self.ui.double_spin_length.setValue(0)
            self.ui.widget_length.hide()
    def edit_error(self, text):
        self.ui.text_error_start.setText(text)

    def show_result(self, text, instrument):
        self.ui.table_widget_sverlenie.setItem(0, 0, instrument)
        self.ui.table_widget_sverlenie.setItem(0, 1, text)

    def clear_all(self):
        self.ui.comboBox_sverlenie.setCurrentIndex(0)
        self.ui.double_spin_length.setValue(0)
        self.ui.checkbox_length.setChecked(False)
        self.ui.text_error_start.setText('')
        self.ui.table_widget_sverlenie.clear()
        self.ui.table_widget_sverlenie.setHorizontalHeaderLabels(['Инструмент', 'Описание'])