from ui_widget_deistvie import Ui_WidgetDeistvie
from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Signal


class WidgetDeistvie(QWidget):
    edit_combobox = Signal()
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_WidgetDeistvie()
        self.ui.setupUi(self)

        self.ui.comboBox_deistvie.currentTextChanged.connect(
            lambda: self.edit_combobox.emit()
        )

    def add_text_in_combo_box(self, value:list):
        self.ui.comboBox_deistvie.addItems(value)

    def name(self):
        return 'Действие'

    def text(self):
        return self.ui.comboBox_deistvie.currentText()

    def resize_title(self):
        rows = self.ui.comboBox_deistvie.count()
        for row in range(rows):
            text = self.ui.comboBox_deistvie.itemText(row)
            print(text)
            self.ui.comboBox_deistvie.setItemText(row, text.lower())


