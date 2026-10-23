from PySide6.QtWidgets import QDialog
from ui_dialog_normirovanie_select_turning_operation import Ui_Dialog

class SelectTurningOperation(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

    @property
    def operation(self):
        return self.ui.comboBox_operations.currentText()

    @property
    def material(self):
        return self.ui.comboBox_material.currentText()

    def add_material(self, d:dict):
        for key in d:
            self.ui.comboBox_material.addItem(key)

    def show_error(self, text):
        self.ui.label_error.setText(text)


