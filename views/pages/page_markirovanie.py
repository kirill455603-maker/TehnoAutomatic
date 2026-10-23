from ui_page_markirovanie import Ui_PageMarkirovanie
from PySide6.QtCore import Signal, QTimer
from PySide6.QtWidgets import QWidget, QHeaderView
class PageMarkirovanie(QWidget):
    btn_save_clicked = Signal()
    btn_home_clicked = Signal()
    btn_export_clicked = Signal()
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_PageMarkirovanie()
        self.ui.setupUi(self)

        self.ui.table_widget.horizontalHeader().setSectionResizeMode(0, QHeaderView.Fixed)
        self.ui.table_widget.horizontalHeader().setSectionResizeMode(1, QHeaderView.Stretch)
        self.ui.table_widget.horizontalHeader().resizeSection(0, 400)
        self.ui.table_widget.horizontalHeader().setStretchLastSection(True)

        self.ui.btn_save_result.clicked.connect(self._on_button_save_result)
        self.ui.btn_home.clicked.connect(self._on_button_home_clicked)
        self.ui.pushButton_save.clicked.connect(self._on_button_export_clicked)

    def _on_button_export_clicked(self):
        self.btn_export_clicked.emit()

    def _on_button_save_result(self):
        self.btn_save_clicked.emit()

    def _on_button_home_clicked(self):
        self.btn_home_clicked.emit()

    def get_result(self):
        result = {}
        result['метод'] = 'ударный' if self.ui.btn_panch.isChecked() else 'маркерный'
        result['объект'] = 'сборочной единицы' if self.ui.btn_sborka.isChecked() else 'детали'
        result['номер'] = int(self.ui.doubleSpinBox_nom_diameter.value())
        result['чертеж'] = self.ui.lineEdit.text()
        return result

    def show_label(self, text):
        self.ui.label_error.setText(text)

    def error_style_sheet(self):
        style = self.ui.lineEdit.styleSheet()
        self.ui.lineEdit.setStyleSheet(f'{style}\nborder: none;\nborder: 1px solid red;')
        self.ui.lineEdit.setPlaceholderText('Введите номер чертежа!')
        QTimer.singleShot(2000,
                          lambda: self.edit_style(style))

    def edit_style(self, style):
        self.ui.lineEdit.setPlaceholderText('Номер чертежа...')
        self.ui.lineEdit.setStyleSheet(style)

    def set_show_result(self, text, instrument):
        self.ui.table_widget.setRowCount(1)
        self.ui.table_widget.setItem(0, 0, instrument)
        self.ui.table_widget.setItem(0, 1, text)

    def show_result(self, text, instrument, key_count):
        pass

    def clear_table(self):
        self.ui.table_widget.clear()
        self.ui.table_widget.setHorizontalHeaderLabels(['Инструмент', 'Описание [Можно изменять]', ''])
        self.ui.table_widget.setRowCount(0)
