from PySide6.QtWidgets import QWidget
from ui_row_detail import Ui_RowDetail

class RowDetail(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_RowDetail()
        self.ui.setupUi(self)


    def add_items(self, d:dict):
        for k, v in d.items():
            self.ui.comboBox_detail.addItem(v['винительный'])

    def edit_label(self, count):
        self.ui.label.setText(f'Деталь №{count}:')

    def get_current_text(self):
        return self.ui.comboBox_detail.currentText()

    def get_position_detail(self):
        return self.ui.spinBox_pos.value()