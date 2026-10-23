from PySide6.QtWidgets import QWidget
from PySide6.QtCore import QTimer

class TurnningBase(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

    def edit_style_error(self):
        self.setStyleSheet('background: rgba(167, 12, 12, 30);\n')
        QTimer.singleShot(1000,
                          lambda: self.setStyleSheet('background: none;\n'))

    def edit_style_apply(self):
        self.setStyleSheet('background: rgba(37, 189, 14, 30);\n')
        QTimer.singleShot(1000,
                          lambda: self.setStyleSheet('background: none;\n'))