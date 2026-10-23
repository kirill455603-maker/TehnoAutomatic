from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Signal
from ui_page_sverlilnaya_chistovaya import Ui_PageSverlilnayaChistovaya

class PageSverlilnayaChistovaya(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_PageSverlilnayaChistovaya()
        self.ui.setupUi(self)
        self.ui.length_div.hide()

        self.ui.pushButton.clicked.connect(self.show_or_hide_length)
        self.ui.pushButton_with_length.clicked.connect(self.show_or_hide_length)

    def show_or_hide_length(self):
        if self.ui.pushButton.isChecked():
            self.ui.doubleSpinBox_length.setValue(0)
            self.ui.length_div.hide()
        if self.ui.pushButton_with_length.isChecked():
            self.ui.length_div.show()

    def add_items(self, data:list):
        self.ui.comboBox_dopusk.addItems(data)

    def clear_all(self):
        self.ui.comboBox_diameter.setCurrentIndex(0)
        self.ui.doubleSpinBox_diameter_end.setValue(0)
        self.ui.comboBox_dopusk.setCurrentIndex(0)
        self.ui.spinBox_count.setValue(0)
        self.ui.comboBox_dopusk_surf.setCurrentIndex(0)
        self.ui.doubleSpinBox_diameter_2.setValue(0)
        self.ui.doubleSpinBox_length.setValue(0)

    def add_items_surf(self, data:list):
        self.ui.comboBox_dopusk_surf.addItems(data)

    def add_items_razvertka(self, data:list):
        data = sorted(data)
        data = ['Ø ' + str(d) for d in data]
        self.ui.comboBox_diameter.addItems(data)

    def get_value(self):
        data = {'номинальный диаметр': float(self.ui.comboBox_diameter.currentText()[2:]),
                'текущий диаметр': self.ui.doubleSpinBox_diameter_end.value(),
                'допуск': self.ui.comboBox_dopusk.currentText(),
                'шероховатость': self.ui.comboBox_dopusk_surf.currentText(),
                'количество': self.ui.spinBox_count.value(),
                'расположение': self.ui.doubleSpinBox_diameter_2.value(),
                'длина': self.ui.doubleSpinBox_length.value()}
        return data


