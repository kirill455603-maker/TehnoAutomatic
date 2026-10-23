from PySide6.QtWidgets import QDialog
from ui_dialog_exit import Ui_Dialog

class ExitDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)



