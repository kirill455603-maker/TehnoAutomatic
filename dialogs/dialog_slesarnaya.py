from PySide6.QtWidgets import QDialog, QLabel

from logic.constants import row
from ui_dialog_slesarnaya import Ui_DialogSlesarnaya
from PySide6.QtCore import Signal
from views.rows.row_detail import RowDetail

class DialogSlesarnaya(QDialog):
    btn_save_result_clicked = Signal(dict)
    btn_add_row_clicked = Signal()
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_DialogSlesarnaya()
        self.ui.setupUi(self)
        self.hide_all()
        self.data = {'зачистка': {'счетчик строк': 0,
                                  'счетчик деталей': 0,
                                  'детали': []},
                     'обезжиривание': {'счетчик строк': 0,
                                  'счетчик деталей': 0,
                                  'детали': []},
                     }
        self.ui.stackedWidget.setCurrentIndex(0)

        self.ui.btn_sborka.clicked.connect(
            lambda: self.ui.stackedWidget.setCurrentIndex(0)
        )
        self.ui.btn_svarka.clicked.connect(
            lambda: self.ui.stackedWidget.setCurrentIndex(1)
        )
        self.ui.btn_meh.clicked.connect(
            lambda: self.ui.stackedWidget.setCurrentIndex(2)
        )
        self.ui.listWidget_meh.clicked.connect(self._clicked_on_meh)
        self.ui.listWidget_sborka.clicked.connect(self._clicked_on_sborka)
        self.ui.listWidget_svarka.clicked.connect(self._clicked_on_svarka)
        self.ui.pushButton_save_result.clicked.connect(self._on_button_save_result)
        self.ui.pushButton_add_detail.clicked.connect(self._on_clicked_add_row)
        self.ui.pushButton_del_detail.clicked.connect(self.del_row)
        self.ui.pushButton_close.clicked.connect(
            lambda: self.close()
        )


    def len_data_zachistka(self):
        return len(self.data['зачистка']['детали'])

    def len_data_obez(self):
        return len(self.data['обезжиривание']['детали'])

    def _clicked_on_svarka(self):
        self.hide_all()
        row = self.ui.listWidget_svarka.currentRow()
        if row == 0:
            self.ui.text_svarka_1.show()
        elif row == 1:
            self.ui.widget_zach.show()
            self.ui.widget_obez.hide()
            self.ui.text_svarka_2.show()
        elif row == 2:
            self.ui.widget_zach.hide()
            self.ui.widget_obez.show()
            self.ui.text_svarka_2.show()
        elif row == 3:
            self.ui.text_svarka_3.show()


    def _on_button_save_result(self):
        data = {}
        if self.ui.btn_meh.isChecked():
            data = {'фаска': self.ui.doubleSpinBox_faska.value(),
                    'угол': self.ui.spinBox_angle.value()}
        elif self.ui.btn_sborka.isChecked():
            data = {'положение': self.ui.comboBox_position.currentText(),
                    'деталь': self.ui.comboBox_detail.currentText(),
                    'позиция': self.ui.spinBox_pos.value(),
                    'инструмент': self.ui.comboBox_detail_2.currentText()}
        elif self.ui.btn_svarka.isChecked():
            if self.get_curent_row_svarka() == 0:
                data = {'положение': self.ui.comboBox_position_type.currentText()}

            elif self.get_curent_row_svarka() == 1 or self.get_curent_row_svarka() == 2:
                data = {'детали': {},
                        'ширина_от': self.ui.spinBox_width_min.value(),
                        'ширина_до': self.ui.spinBox_width_max.value()}
                if self.get_curent_row_svarka() == 1:
                    for item in self.data['зачистка']['детали']:
                        data['детали'][item.get_current_text()] = item.get_position_detail()
                elif self.get_curent_row_svarka() == 2:
                    for item in self.data['обезжиривание']['детали']:
                        data['детали'][item.get_current_text()] = item.get_position_detail()
            elif self.get_curent_row_svarka() == 3:
                data = {}

        self.btn_save_result_clicked.emit(data)

    def _clicked_on_meh(self):
        self.hide_all()
        row = self.ui.listWidget_meh.currentRow()
        if row == 0:
            self.ui.text_meh_1.show()

    def _clicked_on_sborka(self):
        self.hide_all()
        row = self.ui.listWidget_sborka.currentRow()
        if row == 0:
            self.ui.text_sborka_1.show()

    def hide_all(self):
        self.ui.text_meh_1.hide()
        self.ui.text_sborka_1.hide()
        self.ui.text_svarka_1.hide()
        self.ui.text_svarka_2.hide()
        self.ui.text_svarka_3.hide()

    def add_details(self, d:dict):
        for key, value in d.items():
            self.ui.comboBox_detail.addItem(value['родительный'])

    def button_click(self):
        if self.ui.btn_meh.isChecked():
            return 'мех. обработка'
        elif self.ui.btn_svarka.isChecked():
            return 'сварка', self.ui.listWidget_svarka.currentRow()
        elif self.ui.btn_sborka.isChecked():
            return 'сборка'

    def get_current_row(self):
        return self.ui.listWidget_sborka.currentRow()

    def _on_clicked_add_row(self):
        self.btn_add_row_clicked.emit()

    def add_row(self, d):
        self.row = RowDetail(self)
        self.row.add_items(d)
        if self.get_curent_row_svarka() == 1:
            count = self.data['зачистка']['счетчик деталей']
            count_rows = self.data['зачистка']['счетчик строк']
            self.row.edit_label(count + 1)
            if count <= 3:
                self.ui.box_details_zach.addWidget(self.row, count_rows, 0)
            elif 3 < count <= 7:
                self.ui.box_details_zach.addWidget(self.row, count_rows - 4, 1)
            if count <= 7:
                self.data['зачистка']['детали'].append(self.row)
                self.data['зачистка']['счетчик деталей'] = self.data['зачистка'].get('счетчик деталей') + 1
                self.data['зачистка']['счетчик строк'] = self.data['зачистка'].get('счетчик строк') + 1
        elif self.get_curent_row_svarka() == 2:
            count = self.data['обезжиривание']['счетчик деталей']
            count_rows = self.data['обезжиривание']['счетчик строк']
            self.row.edit_label(count + 1)
            if count <= 3:
                self.ui.box_details_obez.addWidget(self.row, count_rows, 0)
            elif 3 < count <= 7:
                self.ui.box_details_obez.addWidget(self.row, count_rows - 4, 1)
            if count <= 7:
                self.data['обезжиривание']['детали'].append(self.row)
                self.data['обезжиривание']['счетчик деталей'] = self.data['обезжиривание'].get('счетчик деталей') + 1
                self.data['обезжиривание']['счетчик строк'] = self.data['обезжиривание'].get('счетчик строк') + 1
        print(self.data)


    def del_row(self):
        if self.get_curent_row_svarka() == 1:
            if self.data['зачистка']['детали']:
                row = self.data['зачистка']['детали'].pop()
                self.ui.box_details_zach.removeWidget(row)
                self.data['зачистка']['счетчик деталей'] = self.data['зачистка'].get('счетчик деталей') - 1
                self.data['зачистка']['счетчик строк'] = self.data['зачистка'].get('счетчик строк') - 1
                row.deleteLater()
        elif self.get_curent_row_svarka() == 2:
            if self.data['обезжиривание']['детали']:
                row = self.data['обезжиривание']['детали'].pop()
                self.ui.box_details_obez.removeWidget(row)
                self.data['обезжиривание']['счетчик деталей'] = self.data['обезжиривание'].get('счетчик деталей') - 1
                self.data['обезжиривание']['счетчик строк'] = self.data['обезжиривание'].get('счетчик строк') - 1
                row.deleteLater()


    def clear_all_in_svarka(self):
        self.data = {'зачистка': {'счетчик строк': 0,
                                  'счетчик деталей': 0,
                                  'детали': []},
                     'обезжиривание': {'счетчик строк': 0,
                                       'счетчик деталей': 0,
                                       'детали': []},
                     }

    def get_curent_row_svarka(self):
        return self.ui.listWidget_svarka.currentRow()








