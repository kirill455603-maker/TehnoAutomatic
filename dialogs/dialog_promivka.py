from ui_dialog_promivka import Ui_DialogPromivka
from PySide6.QtCore import Signal
from PySide6.QtWidgets import QDialog

class DialogPromivka(QDialog):
    btn_save_clicked = Signal()
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_DialogPromivka()
        self.ui.setupUi(self)

        self.ui.pushButton_save_result.clicked.connect(self._on_button_save)
        self.ui.pushButton_close.clicked.connect(
            lambda: self.close()
        )

    def _on_button_save(self):
        self.btn_save_clicked.emit()
