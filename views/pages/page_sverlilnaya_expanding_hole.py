from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Signal
from ui_page_sverlilnaya_expanding_hole import Ui_PageSverlilnayaExpandingHole

class PageSverlilnayaExpandingHole(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_PageSverlilnayaExpandingHole()
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

    def clear_all(self):
        self.ui.doubleSpinBox_diameter.setValue(0)
        self.ui.comboBox_diameter.setCurrentIndex(0)
        self.ui.spinBox_count.setValue(0)
        self.ui.doubleSpinBox_diameter_big.setValue(0)
        self.ui.doubleSpinBox_length.setValue(0)

    def get_value(self):
        data = {'отверстие': self.ui.doubleSpinBox_diameter.value(),
                'сверло': float(self.ui.comboBox_diameter.currentText()[2:]),
                'расположение': self.ui.doubleSpinBox_diameter_big.value(),
                'количество': self.ui.spinBox_count.value(),
                'глубина': self.ui.doubleSpinBox_length.value()}
        return data

    def add_items(self, data:list):
        self.ui.comboBox_diameter.setCurrentIndex(0)
        data = sorted(data)
        data = ['Ø ' + str(d) for d in data]
        self.ui.comboBox_diameter.addItems(data)



