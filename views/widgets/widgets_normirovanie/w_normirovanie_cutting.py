from PySide6.QtWidgets import QWidget
from ui_widget_normirovanie_cutting import Ui_WidgetCutting

class Cutting(QWidget):
    def __init__(self, name, parent=None):
        super().__init__(parent)
        self.ui = Ui_WidgetCutting()
        self.ui.setupUi(self)
        self.name = name

    def add_material(self, d:dict):
        for key in d:
            self.ui.comboBox_details.addItem(key)

    def get_params(self):
        d = {
            'диаметр': self.ui.doubleSpinBox.value(),
            'материал': self.ui.comboBox_details.currentText()
        }
        return d

    @property
    def operation(self):
        return self.name
