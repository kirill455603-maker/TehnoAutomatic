from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Signal
from ui_page_sverlilnaya_rezba import Ui_PageSverlilnayaRezba

class PageSverlilnayaRezba(QWidget):
    combo_box_changed = Signal(float)
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_PageSverlilnayaRezba()
        self.ui.setupUi(self)
        self.ui.length_div.hide()

        self.ui.pushButton.clicked.connect(self.show_or_hide_length)
        self.ui.pushButton_with_length.clicked.connect(self.show_or_hide_length)

        self.ui.comboBox_diameter.currentIndexChanged.connect(self._changed_combo_box)

    def _changed_combo_box(self):
        current_value = self.ui.comboBox_diameter.currentText()[1:]
        print(current_value)
        if current_value:
            current_value = float(current_value)
            self.combo_box_changed.emit(current_value)

    def show_or_hide_length(self):
        if self.ui.pushButton.isChecked():
            self.ui.doubleSpinBox_length.setValue(0)
            self.ui.length_div.hide()
        if self.ui.pushButton_with_length.isChecked():
            self.ui.length_div.show()

    def clear_all(self):
        self.ui.comboBox_diameter.setCurrentIndex(0)
        self.ui.comboBox_diameter_2.setCurrentIndex(0)
        self.ui.spinBox_count.setValue(1)
        self.ui.doubleSpinBox_diameter_big.setValue(0)
        self.ui.doubleSpinBox_length.setValue(0)

    def add_items_rezba(self, data:list):
        data = [f'М{rezba}' for rezba in data]
        self.ui.comboBox_diameter.addItems(data)
        self.ui.comboBox_diameter.setCurrentText('')

    def add_items_step(self, data:list):
        self.ui.comboBox_diameter_2.clear()
        self.ui.comboBox_diameter_2.addItems(data)

    def add_items_dopusk(self, data:list):
        self.ui.comboBox_dopusk.addItems(data)

    def get_value(self):
        depth = self.ui.doubleSpinBox_length.value()
        rezba = self.ui.comboBox_diameter.currentText()
        step = self.ui.comboBox_diameter_2.currentText()
        data = {'резьба': float(rezba[1:]) if rezba else 0,
                'шаг': float(step) if step else 0,
                'количество': self.ui.spinBox_count.value(),
                'расположение': self.ui.doubleSpinBox_diameter_big.value(),
                'глубина': depth if depth else 0,
                'допуск': self.ui.comboBox_dopusk.currentText()}

        return data



