from ui_dialog_normirovanie_markirovanie import Ui_DialogMarkirovanie
from PySide6.QtWidgets import QDialog
from PySide6.QtCore import Signal

class DialogMarkirovanie(QDialog):
    btn_save_clicked = Signal()
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_DialogMarkirovanie()
        self.ui.setupUi(self)

        self.ui.btn_save.clicked.connect(self._on_button_save)

    def _on_button_save(self):
        self.btn_save_clicked.emit()

    def get_value(self):
       return self.ui.spinBox.value()
