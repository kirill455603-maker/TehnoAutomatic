
from PySide6.QtWidgets import QWidget, QComboBox, QSizePolicy, QLabel, QSpinBox
from PySide6.QtCore import Signal
from ui_window_slesarnaya import Ui_WindowSlesarnaya

class WindowSlesarnaya(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_WindowSlesarnaya()
        self.ui.setupUi(self)

