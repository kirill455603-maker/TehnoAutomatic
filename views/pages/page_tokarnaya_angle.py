from PySide6.QtWidgets import QWidget, QHeaderView
from PySide6.QtCore import Signal
from ui_page_tokarnaya_angle import Ui_PageTokarnayaAngle

class PageTokarnayaAngle(QWidget):
    btn_save_result_clicked = Signal(dict)
    btn_home_clicked = Signal()
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_PageTokarnayaAngle()
        self.ui.setupUi(self)
        self.ui.table_widget_angle.horizontalHeader().setSectionResizeMode(0, QHeaderView.Fixed)
        self.ui.table_widget_angle.horizontalHeader().setSectionResizeMode(1, QHeaderView.Stretch)
        self.ui.table_widget_angle.horizontalHeader().resizeSection(0, 400)
        self.ui.table_widget_angle.horizontalHeader().setStretchLastSection(True)
        self.ui.table_widget_angle.setRowCount(1)

        self.ui.btn_home_tokarnaya_angle.clicked.connect(self._on_button_home_clicked)
        self.ui.btn_save_result_angle.clicked.connect(self.save_result)

    def _on_button_home_clicked(self):
        self.btn_home_clicked.emit()

    def save_result(self):
        dict_angle = {'старт': self.ui.doubleSpinBox_start_d.value(),
                      'конец': self.ui.doubleSpinBox_end_d.value(),
                      'угол': self.ui.spinBox_angle.value(),
                      'расположение': 'внутренний' if self.ui.radioButton_in.isChecked() else 'внешний',
                      'допуск': self.ui.spinBox_angle_2.value()}
        self.btn_save_result_clicked.emit(dict_angle)

    def clear_all(self):
        self.ui.doubleSpinBox_start_d.setValue(0)
        self.ui.doubleSpinBox_end_d.setValue(0)
        self.ui.spinBox_angle.setValue(45)
        self.ui.table_widget_angle.clear()
        self.ui.table_widget_angle.setHorizontalHeaderItem(['Инструмент', 'Описание'])
        self.ui.text_error_start.setText('')

    def show_result(self, text, instrument):
        self.ui.table_widget_angle.setRowCount(1)
        self.ui.table_widget_angle.setItem(0, 0, instrument)
        self.ui.table_widget_angle.setItem(0, 1, text)

    def show_label(self, text):
        self.ui.text_error_start.setText(text)