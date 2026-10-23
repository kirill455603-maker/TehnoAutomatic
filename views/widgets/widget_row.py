from ui_widget_row import Ui_WidgetRow
from PySide6.QtWidgets import QWidget

class WidgetRow(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_WidgetRow()
        self.ui.setupUi(self)


    def row(self):
        return self.ui.horizontalLayout_2