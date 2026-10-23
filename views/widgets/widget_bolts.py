from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Signal
from ui_widget_bolts import Ui_WidgetBolts

class WidgetBolts(QWidget):
    edit_spinbox = Signal()
    edit_type = Signal()
    edit_rezba = Signal()
    edit_s = Signal()
    edit_position = Signal()
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_WidgetBolts()
        self.ui.setupUi(self)
        self.metrick_rezba = None

        self.ui.comboBox_rezba.currentTextChanged.connect(
            lambda: self.add_in_step()
        )
        self.ui.spinBox_count.valueChanged.connect(self._edit_type)
        self.ui.comboBox_type.currentTextChanged.connect(
            lambda: self.edit_type.emit()
        )
        self.ui.comboBox_rezba.currentTextChanged.connect(
            lambda: self.edit_rezba.emit()
        )
        self.ui.comboBox_s.currentTextChanged.connect(
            lambda: self.edit_s.emit()
        )
        self.ui.spinBox_position.valueChanged.connect(
            lambda: self.edit_position.emit()
        )

    def name(self):
        return 'Болт'

    def text(self):
        text = None
        if self.ui.spinBox_count.value() < 5:
            num = self.ui.spinBox_count.value()
            if 'болт' in self.ui.comboBox_type.currentText():
                if num == 1:
                    text = 'один'
                elif num == 2:
                    text = 'два'
                elif num == 3:
                    text = 'три'
                elif num == 4:
                    text = 'четыре'
            elif 'га' in self.ui.comboBox_type.currentText():
                if num == 1:
                    text = 'одну'
                elif num == 2:
                    text = 'две'
                elif num == 3:
                    text = 'три'
                elif num == 4:
                    text = 'четыре'
            elif 'винт' in self.ui.comboBox_type.currentText():
                if num == 1:
                    text = 'один'
                elif num == 2:
                    text = 'два'
                elif num == 3:
                    text = 'три'
                elif num == 4:
                    text = 'четыре'
            elif 'шпил' in self.ui.comboBox_type.currentText():
                if num == 1:
                    text = 'одну'
                elif num == 2:
                    text = 'две'
                elif num == 3:
                    text = 'три'
                elif num == 4:
                    text = 'четыре'
        else:
            text = self.ui.spinBox_count.value()
        return f'{text} {self.ui.comboBox_type.currentText()} {self.ui.comboBox_rezba.currentText()}х{self.ui.comboBox_s.currentText()} поз. {self.ui.spinBox_position.value()}'

    def _edit_type(self):
        count = self.ui.spinBox_count.value()
        edit_text_1 = self.pluralize_ru(count, ('болт', 'болта', 'болтов'))
        edit_text_2 = self.pluralize_ru(count, ('гайку', 'гайки', 'гаек'))
        edit_text_3 = self.pluralize_ru(count, ('винт', 'винта', 'винтов'))
        edit_text_4 = self.pluralize_ru(count, ('шпильку', 'шпильки', 'шпилек'))
        for row in range(self.ui.comboBox_type.count()):
            text = self.ui.comboBox_type.itemText(row)
            if 'болт' in text:
                self.ui.comboBox_type.setItemText(row, edit_text_1)
            elif 'га' in text:
                self.ui.comboBox_type.setItemText(row, edit_text_2)
            elif 'винт' in text:
                self.ui.comboBox_type.setItemText(row, edit_text_3)
            elif 'шпил' in text:
                self.ui.comboBox_type.setItemText(row, edit_text_4)
        self.edit_spinbox.emit()

    def add_in_rezba(self):
        for key in self.metrick_rezba:
            key = self.format_num(key)
            self.ui.comboBox_rezba.addItem(f'М{key}'.replace('.', ','))

    def add_in_step(self):
        self.ui.comboBox_s.clear()
        rezba = float(self.ui.comboBox_rezba.currentText()[1:].replace(',', '.'))
        for step in self.metrick_rezba[rezba]:
            step = self.format_num(float(step))
            self.ui.comboBox_s.addItem(str(step).replace('.', ','))

    def pluralize_ru(self, count: int, forms: tuple) -> str:
        """
        Универсальная функция склонения для русского языка.
        forms: кортеж из 3 строк (форма для 1, форма для 2, форма для 5).
        Пример forms для 'отверстие': ("отверстие", "отверстия", "отверстий")
        """
        count = abs(int(count))

        if count % 10 == 1 and count % 100 != 11:
            idx = 0
        elif 2 <= count % 10 <= 4 and not (12 <= count % 100 <= 14):
            idx = 1
        else:
            idx = 2

        return f"{forms[idx]}"

    def format_num(self, num: float):
        """Убирает .0 у целых чисел для красивого вывода."""
        return int(num) if num == int(num) else num

