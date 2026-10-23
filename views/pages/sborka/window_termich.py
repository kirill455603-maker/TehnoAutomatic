from PySide6.QtWidgets import QWidget
from ui_window_termich import Ui_WindowTermich

class WindowTermich(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_WindowTermich()
        self.ui.setupUi(self)