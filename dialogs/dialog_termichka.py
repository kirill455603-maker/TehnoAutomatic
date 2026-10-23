from ui_dialog_termichka import Ui_DialogTermichka
from PySide6.QtWidgets import QDialog
from PySide6.QtCore import Signal

class DialogTermichka(QDialog):
    btn_save_result_clicked = Signal()
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_DialogTermichka()
        self.ui.setupUi(self)
        self.hide_all()

        self.ui.listWidget.clicked.connect(self._on_button_list_widget)
        self.ui.pushButton_save_result.clicked.connect(self._on_button_save_result)
        self.ui.buttonBox.clicked.connect(
            lambda: self.close()
        )

    def hide_all(self):
        self.ui.text_1.hide()
        self.ui.text_2.hide()
        self.ui.text_3.hide()

    def _on_button_list_widget(self):
        self.hide_all()
        row = self.ui.listWidget.currentRow()
        result = {}
        if row == 0:
            self.ui.text_1.show()
        elif row == 1:
            self.ui.text_2.show()
        elif row == 2:
            self.ui.text_3.show()

    def get_result(self):
        row = self.ui.listWidget.currentRow()
        result = {}
        if row == 0:
            result = {
                'положение': self.ui.comboBox_position.currentText(),
                'деталь': self.ui.comboBox_detail.currentText(),
                'поз': self.ui.spinBox_pos.value()
            }

        elif row == 1:
            result = {
                'температура': self.ui.spinBox_temp.value(),
                'допуск': self.ui.spinBox_temp_d.value(),
            }
        elif row == 2:
            result = {
                'установка': self.ui.comboBox_inout.currentText()
            }
        return result, row

    def _on_button_save_result(self):
        self.btn_save_result_clicked.emit()

    def add_items(self, value:dict):
        for k, v in value.items():
            self.ui.comboBox_detail.addItem(v['винительный'])









