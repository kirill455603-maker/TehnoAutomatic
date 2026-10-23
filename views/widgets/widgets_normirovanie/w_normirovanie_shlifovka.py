from PySide6.QtWidgets import QWidget
from PySide6.QtCore import QTimer
from ui_widget_normirovanie_shlifovka import Ui_Shlifovka

class Shlifovka(QWidget):
    def __init__(self, material, parent=None):
        super().__init__(parent)
        self.ui = Ui_Shlifovka()
        self.ui.setupUi(self)

        self._add_material(material)

    def _add_material(self, d:dict):
        for key in d:
            self.ui.comboBox_material.addItem(key)


    def get_value(self):
        d = {
            'диаметр': self.ui.doubleSpinBox_diameter.value(),
            'материал': self.ui.comboBox_material.currentText(),
            'длина': self.ui.doubleSpinBox_length.value(),
            'припуск': self.ui.doubleSpinBox_length_2.value()
        }
        return d

    def show_label_info(self, text):
        self.ui.label_info.setText(text)

    def edit_style_error(self):
        self.ui.widget.setStyleSheet('background: rgba(167, 12, 12, 30);\n'
                                     'border-bottom: 1px solid white;')
        QTimer.singleShot(1000,
                          lambda: self.ui.widget.setStyleSheet('background: none;\n'
                                     'border-bottom: 1px solid white;'))
    def edit_style_apply(self):
        self.ui.widget.setStyleSheet('background: rgba(37, 189, 14, 30);\n'
                                     'border-bottom: 1px solid white;')
        QTimer.singleShot(1000,
                          lambda: self.ui.widget.setStyleSheet('background: none;\n'
                                     'border-bottom: 1px solid white;'))
