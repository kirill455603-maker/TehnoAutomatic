from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Signal
from ui_page_sverlilnaya_start import Ui_PageSverlilnayaStart

class PageSverlilnayaStart(QWidget):
    btn_find_sverlo = Signal()
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_PageSverlilnayaStart()
        self.ui.setupUi(self)
        self.ui.widget_length.hide()

        self.ui.pushButton_infinity.clicked.connect(self.show_or_hide_length)
        self.ui.pushButton_with_length.clicked.connect(self.show_or_hide_length)
        self.ui.pushButton_find_sverlo.clicked.connect(self._on_button_find_sverlo)

    def _on_button_find_sverlo(self):
        self.btn_find_sverlo.emit()

    def show_or_hide_length(self):
        if self.ui.pushButton_infinity.isChecked():
            self.ui.doubleSpinBox_length.setValue(0)
            self.ui.widget_length.hide()
        if self.ui.pushButton_with_length.isChecked():
            self.ui.widget_length.show()

    def clear_all(self):
        self.ui.comboBox_diameter.setCurrentIndex(0)
        self.ui.spinBox_count.setValue(0)
        self.ui.doubleSpinBox_length.setValue(0)
        self.ui.doubleSpinBox_nom_diameter.setValue(0)

    def get_value(self):
        data = {'диаметр': float(self.ui.comboBox_diameter.currentText()[2:]),
                'расположение': self.ui.doubleSpinBox_nom_diameter.value(),
                'количество': self.ui.spinBox_count.value(),
                'глубина': self.ui.doubleSpinBox_length.value(),
                'допуск': self.ui.doubleSpinBox_dopusk.value()}
        return data

    def add_items(self, data:list):
        data = sorted(data)
        data = ['Ø ' + str(d) for d in data]
        self.ui.comboBox_diameter.addItems(data)

    def is_have_sverlo(self, value):
        return self.ui.comboBox_diameter.findText(f'Ø {value}')

    def set_sverlo(self, value):
        print(value)
        index = self.ui.comboBox_diameter.findText(f'Ø {value}')
        print(index)
        self.ui.comboBox_diameter.setCurrentIndex(index)