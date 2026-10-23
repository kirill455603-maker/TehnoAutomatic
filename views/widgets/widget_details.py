from ui_widget_details import Ui_WidgetDetails
from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Signal


class WidgetDetails(QWidget):
    edit_combo_box = Signal()
    edit_position = Signal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_WidgetDetails()
        self.ui.setupUi(self)

        self.ui.comboBox_details.currentTextChanged.connect(
            lambda: self.edit_combo_box.emit()
        )
        self.ui.spinBox_position.valueChanged.connect(
            lambda: self.edit_position.emit()
        )

    def text(self):
        return f'{self.ui.comboBox_details.currentText()} поз. {self.ui.spinBox_position.value()}'

    def set_padeg(self, type, values: dict):
        print(type)

        """Очищает комбобокс и заполняет его значениями в нужном падеже"""
        self.ui.comboBox_details.clear()
        for key in values:
            self.ui.comboBox_details.addItem(values[key][type])

    def name(self):
        return 'Деталь'