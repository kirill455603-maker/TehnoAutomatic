from ui_page_sverlilnaya_faska import Ui_PageSverlilnayaFaska
from PySide6.QtWidgets import QWidget

class PageSverlilnayaFaska(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_PageSverlilnayaFaska()
        self.ui.setupUi(self)

    def clear_all(self):
        self.ui.doubleSpinBox_diameter.setValue(0)
        self.ui.doubleSpinBox_length.setValue(1)
        self.ui.spinBox_angle.setValue(45)
        self.ui.doubleSpinBox_diameter_big.setValue(0)

    def get_value(self):
        data = {'диаметр': self.ui.doubleSpinBox_diameter.value(),
                'длина': self.ui.doubleSpinBox_length.value(),
                'угол': self.ui.spinBox_angle.value(),
                'количество': self.ui.spinBox_count.value(),
                'расположение': self.ui.doubleSpinBox_diameter_big.value()
                }
        return data



