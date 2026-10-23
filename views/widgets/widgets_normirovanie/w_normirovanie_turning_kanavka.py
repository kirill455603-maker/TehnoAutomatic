from ui_widget_normirovanie_turning_kanavka import Ui_TurningKanavka
from PySide6.QtWidgets import QWidget
from PySide6.QtCore import QTimer

class TurningKanavka(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_TurningKanavka()
        self.ui.setupUi(self)

    def edit_type_material(self, text):
        self.ui.label_type_material.setText(f'Материал: {text}')

    @property
    def operation_name(self):
        return 'канавка'

    def get_value(self):
        d = {
            'глубина': self.ui.doubleSpinBox_depth_kanavka.value(),
            'ширина': self.ui.doubleSpinBox_width_kanavka.value(),
            'количество': self.ui.spinBox_count.value(),
            'резец': self.ui.doubleSpinBox_width_rezec.value()
        }
        return d

    def show_label_info(self, text):
        self.ui.label_info.setText(text)

    def edit_style_error(self):
        self.ui.widget.setStyleSheet('background: rgba(167, 12, 12, 30);\n'
                                     'border-bottom: 1px solid white;')
        QTimer.singleShot(1000,
                          lambda: self.ui.widget.setStyleSheet('background: none;\n'
                                     'border-bottom: 1px solid white;'))
    def edit_style_apply(self):
        self.ui.widget.setStyleSheet('background: rgba(37, 189, 14, 30);\n'
                                     'border-bottom: 1px solid white;')
        QTimer.singleShot(1000,
                          lambda: self.ui.widget.setStyleSheet('background: none;\n'
                                     'border-bottom: 1px solid white;'))
