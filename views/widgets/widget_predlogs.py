from ui_widget_predlogs import Ui_WidgetPredlogs
from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Signal

class WidgetPredlogs(QWidget):
    edit_combobox = Signal()
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_WidgetPredlogs()
        self.ui.setupUi(self)

        self.ui.comboBox_predlogs.currentTextChanged.connect(
            lambda: self.edit_combobox.emit()
        )

    def text(self):
        return self.ui.comboBox_predlogs.currentText()

    def name(self):
        return 'Предлог'

    def resize_title(self):
        rows = self.ui.comboBox_predlogs.count()
        for row in range(rows):
            text = self.ui.comboBox_predlogs.itemText(row)
            self.ui.comboBox_predlogs.setItemText(row, text.lower())