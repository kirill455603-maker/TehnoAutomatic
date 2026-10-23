from PySide6.QtWidgets import QDialog
from PySide6.QtCore import Signal
from ui_dialog_find_sverlo import Ui_FindSverlo

class FindSverlo(QDialog):
    cb_edit_rezba = Signal()
    btn_save_clicked = Signal(str)
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_FindSverlo()
        self.ui.setupUi(self)
        self.dict_rezb = None
        self.ui.comboBox_diameter.currentTextChanged.connect(self.add_steps)
        self.ui.pushButton_save.clicked.connect(self._on_button_save_clicked)


    def _on_button_save_clicked(self):
        if self.ui.comboBox_diameter.currentText() == '':
            self.add_text('Ошибка: Выберите резьбу для подбора!')
            return
        if self.ui.comboBox_step.currentText() == '':
            self.add_text('Ошибка: Выберите шаг резьбы для подбора!')
            return
        rezba = float(self.ui.comboBox_diameter.currentText())
        step = float(self.ui.comboBox_step.currentText())
        result = round(rezba - step, 1)
        print('123')
        print(result)
        self.btn_save_clicked.emit(str(result))


    def add_rezba(self):
        self.ui.comboBox_diameter.clear()
        if self.dict_rezb:
            for key in list(self.dict_rezb.keys()):
                self.ui.comboBox_diameter.addItem(str(key))

    def add_steps(self):
        self.ui.comboBox_step.clear()
        if self.ui.comboBox_diameter.currentText():
            l = self.dict_rezb[float(self.ui.comboBox_diameter.currentText())]
            for key in l:
                self.ui.comboBox_step.addItem(key)

    def add_text(self, value):
        self.ui.label_text.setText(value)

    def all_clear(self):
        self.ui.comboBox_diameter.clear()
        self.ui.comboBox_step.clear()
        self.ui.label_text.setText('')

