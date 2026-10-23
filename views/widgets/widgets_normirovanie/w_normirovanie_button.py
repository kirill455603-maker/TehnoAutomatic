from ui_widget_normirovanie_button import Ui_ButtonList
from PySide6.QtWidgets import QWidget

class ButtonList(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_ButtonList()
        self.ui.setupUi(self)

    def edit_text(self, text):
        self.ui.pushButton.setText(text)

    def get_text_button(self):
        return self.ui.pushButton.text()


