from ui_page_kontrol_otk import Ui_PageKontrolOtk
from PySide6.QtWidgets import QWidget, QPushButton, QHeaderView
from PySide6.QtCore import Signal


class PageKontrolOtk(QWidget):
    btn_home_clicked = Signal()
    btn_add_clicked = Signal(dict)
    btn_click_delete = Signal(int)
    btn_hole_clicked = Signal()
    btn_clear_clicked = Signal()
    btn_save_and_export_clicked = Signal()
    btn_add_rezba_diameter = Signal()
    combobox_rezba_changed = Signal(float)
    combobox_rezba_changed_diameter = Signal(float)
    r_btn_otv_clicked = Signal()
    r_btn_val_clicked = Signal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_PageKontrolOtk()
        self.ui.setupUi(self)

        self.ui.pushButton_reset.clicked.connect(self._on_button_reset)
        self.ui.holes.hide()
        self.ui.length.hide()
        self.ui.rezba_holes.hide()
        self.ui.widget_2.hide()
        self.ui.rezba_holes_2.hide()


        # ===== НАСТРОЙКА ТАБЛИЦЫ (как в PageSverlilnaya) =====
        self.ui.table_widget_kontrol_otk.horizontalHeader().setSectionResizeMode(0, QHeaderView.Fixed)
        self.ui.table_widget_kontrol_otk.horizontalHeader().setSectionResizeMode(1, QHeaderView.Fixed)
        self.ui.table_widget_kontrol_otk.horizontalHeader().setSectionResizeMode(2, QHeaderView.Stretch)
        self.ui.table_widget_kontrol_otk.horizontalHeader().resizeSection(0, 500)
        self.ui.table_widget_kontrol_otk.horizontalHeader().resizeSection(1, 500)
        self.ui.table_widget_kontrol_otk.horizontalHeader().setStretchLastSection(True)
        self.ui.table_widget_kontrol_otk.verticalHeader().setMinimumSectionSize(90)
        self.ui.table_widget_kontrol_otk.verticalHeader().setDefaultSectionSize(100)

        # Автоматическая высота строк
        self.ui.table_widget_kontrol_otk.verticalHeader().setSectionResizeMode(
            QHeaderView.ResizeToContents
        )
        self.ui.table_widget_kontrol_otk.setWordWrap(True)
        # =====================================================

        self.ui.btn_home.clicked.connect(self._on_button_home_clicked)
        self._delete_buttons = []

        self.ui.btn_diameter.clicked.connect(self._on_clicked_type)
        self.ui.btn_length.clicked.connect(self._on_clicked_type)
        self.ui.btn_hole.clicked.connect(self._on_clicked_type)
        self.ui.pushButton_add_table.clicked.connect(self._on_clicked_add_element)
        self.ui.checkBox_add_length.clicked.connect(self._on_checkbox_clicked)
        self.ui.btn_gladkie.clicked.connect(self._switch_holes)
        self.ui.btn_rezba.clicked.connect(self._switch_holes)
        self.ui.comboBox_diameter.currentTextChanged.connect(self._add_step)
        self.ui.btn_clear_table.clicked.connect(self._on_clear_clicked)
        self.ui.btn_save_and_export.clicked.connect(self._on_save_and_export_clicked)
        self.ui.checkBox_rezba.clicked.connect(self._on_rezba_clicked)
        self.ui.comboBox_rezba_d.currentIndexChanged.connect(self._rezba_changed_diameter)
        self.ui.radioButton_otv.clicked.connect(
            lambda: self.r_btn_otv_clicked.emit()
        )
        self.ui.radioButton_val.clicked.connect(
            lambda: self.r_btn_val_clicked.emit()
        )

    def _rezba_changed_diameter(self):
        self.combobox_rezba_changed_diameter.emit(float(self.ui.comboBox_rezba_d.currentText()[1:]))

    def _on_rezba_clicked(self):
        self.btn_add_rezba_diameter.emit()
        if self.ui.checkBox_rezba.isChecked():
            self.ui.widget.hide()
            self.ui.rezba_holes_2.show()
        else:
            self.ui.widget.show()
            self.ui.rezba_holes_2.hide()

    def _on_save_and_export_clicked(self):
        self.btn_save_and_export_clicked.emit()

    def _on_clear_clicked(self):
        self.btn_clear_clicked.emit()

    def add_rezba(self, value:list):
        if self.ui.comboBox_diameter.count() == 0:
            for el in value:
                self.ui.comboBox_diameter.addItem('М' + str(el))

    def add_step(self, value:list):
        self.ui.comboBox_diameter_2.clear()
        for el in value:
            self.ui.comboBox_diameter_2.addItem(str(el))
        self.ui.comboBox_diameter_2.setCurrentIndex(0)

    def add_dopusk(self, value:list):
        self.ui.comboBox_dopusk.clear()
        self.ui.comboBox_dopusk.addItems(value)

    def add_dopusk_diameter_page(self, d:dict):
        self.ui.comboBox_dopusk_2.clear()
        if self.ui.radioButton_val.isChecked():
            self.ui.comboBox_dopusk_2.addItems(d['внешняя'])
        elif self.ui.radioButton_otv.isChecked():
            self.ui.comboBox_dopusk_2.addItems(d['внутренняя'])

    def _add_step(self):
        value = self.ui.comboBox_diameter.currentText()
        if value:
            self.combobox_rezba_changed.emit(float(value[1:]))

    def _switch_holes(self):
        if self.ui.btn_gladkie.isChecked():
            self.ui.rezba_holes.hide()
            self.ui.gladkie_holes.show()
            if self.ui.checkBox_add_length.isChecked():
                self.ui.widget_2.hide()
        elif self.ui.btn_rezba.isChecked():
            self.ui.rezba_holes.show()
            self.ui.gladkie_holes.hide()
            if self.ui.checkBox_add_length.isChecked():
                self.ui.widget_2.show()

    def _on_checkbox_clicked(self):
        self.clear_length()
        if self.ui.checkBox_add_length.isChecked():
            self.ui.length.show()
            if self.ui.btn_rezba.isChecked():
                self.ui.widget_2.show()
            if self.ui.btn_gladkie.isChecked():
                self.ui.widget_2.hide()
        else:
            self.ui.length.hide()
            self.ui.widget_2.hide()


    def clear_length(self):
        self.ui.doubleSpinBox_length.setValue(0)
        self.ui.lineEdit_kvalitet_length.setText('')
        self.ui.doubleSpinBox_dopusk_length.setValue(0)
        self.ui.doubleSpinBox_dopusk_length_2.setValue(0)
        self.ui.doubleSpinBox_length_rezba.setValue(0)
        self.ui.doubleSpinBox_dopusk_length_rezba.setValue(0)
        self.ui.doubleSpinBox_dopusk_length_rezba_2.setValue(0)



    def _on_button_reset(self):
        if self.ui.btn_length.isChecked():
            self.ui.doubleSpinBox_nom_diameter.setValue(0)
            self.ui.lineEdit_kvalitet.setText('')
            self.ui.doubleSpinBox_dopusk_1.setValue(0)
            self.ui.doubleSpinBox_dopusk_2.setValue(0)
        elif self.ui.btn_diameter.isChecked():
            self.ui.doubleSpinBox_nom_diameter.setValue(0)
            self.ui.lineEdit_kvalitet.setText('')
            self.ui.doubleSpinBox_dopusk_1.setValue(0)
            self.ui.doubleSpinBox_dopusk_2.setValue(0)
            self.ui.radioButton_otv.setChecked(True)
        elif self.ui.btn_hole.isChecked():
            if self.get_button_type_hole() == 'гладкие':
                self.ui.doubleSpinBox_nom_diameter_3.setValue(0)
                self.ui.lineEdit_kvalitet_2.setText('')
                self.ui.doubleSpinBox_dopusk_3.setValue(0)
                self.ui.doubleSpinBox_dopusk_4.setValue(0)
            elif self.get_button_type_hole() == 'резьбовые':
                self.ui.comboBox_diameter.setCurrentIndex(0)
                self.ui.comboBox_diameter_2.setCurrentIndex(0)
                self.ui.comboBox_dopusk.setCurrentIndex(0)
                self.ui.spinBox_count.setValue(1)
            self.ui.checkBox_add_length.setChecked(False)
            self.clear_length()


    def _on_clicked_type(self):
        if self.ui.btn_diameter.isChecked():
            self.ui.holes.hide()
            self.ui.verticalWidget.show()
            self.ui.groupBox.show()
            self.ui.checkBox_rezba.show()
            self.ui.doubleSpinBox_nom_diameter.setPrefix('Ø ')
        elif self.ui.btn_length.isChecked():
            self.ui.holes.hide()
            self.ui.verticalWidget.show()
            self.ui.widget.show()
            self.ui.rezba_holes_2.hide()
            self.ui.groupBox.hide()
            self.ui.checkBox_rezba.hide()
            self.ui.checkBox_rezba.setChecked(False)
            self.ui.doubleSpinBox_nom_diameter.setPrefix('L= ')
        elif self.ui.btn_hole.isChecked():
            self.ui.verticalWidget.hide()
            self.ui.holes.show()
            self.ui.rezba_holes_2.hide()
            self.ui.checkBox_rezba.setChecked(False)
            self.ui.checkBox_rezba.hide()
            self.btn_hole_clicked.emit()


    def _on_clicked_add_element(self):
        d = None
        if self.ui.btn_diameter.isChecked():
            if self.ui.checkBox_rezba.isChecked():
                d = {'диаметр': self.ui.comboBox_rezba_d.currentText(),
                     'шаг': self.ui.comboBox_step_d.currentText(),
                     'допуск': self.ui.comboBox_dopusk_2.currentText(),
                     'тип резьбы': None}
                if self.ui.radioButton_val.isChecked():
                    d['тип резьбы'] = 'внешняя'
                elif self.ui.radioButton_otv.isChecked():
                    d['тип резьбы'] = 'внутренняя'
            else:
                d = {
                    'диаметр': self.ui.doubleSpinBox_nom_diameter.value(),
                    'квалитет': self.ui.lineEdit_kvalitet.text(),
                    'допуск_1': self.ui.doubleSpinBox_dopusk_1.value(),
                    'допуск_2': self.ui.doubleSpinBox_dopusk_2.value(),
                    'кнопка': 'диаметр',
                    'тип': 'вал' if self.ui.radioButton_val.isChecked() else 'отверстие'
                }
        elif self.ui.btn_length.isChecked():
            d = {
                'длина': self.ui.doubleSpinBox_nom_diameter.value(),
                'квалитет': self.ui.lineEdit_kvalitet.text(),
                'допуск_1': self.ui.doubleSpinBox_dopusk_1.value(),
                'допуск_2': self.ui.doubleSpinBox_dopusk_2.value(),
                'кнопка': 'длина',
            }
        elif self.ui.btn_hole.isChecked():
            if self.get_button_type_hole() == 'гладкие':
                d = {
                    'диаметр': self.ui.doubleSpinBox_nom_diameter_3.value(),
                    'квалитет': self.ui.lineEdit_kvalitet_2.text(),
                    'допуск_1': self.ui.doubleSpinBox_dopusk_3.value(),
                    'допуск_2': self.ui.doubleSpinBox_dopusk_4.value(),
                    'количество': self.ui.spinBox_count.value(),
                    'статус глубины': self.ui.checkBox_add_length.isChecked(),
                    'глубина': self.ui.doubleSpinBox_length.value(),
                    'квалитет глубины': self.ui.lineEdit_kvalitet_length.text(),
                    'допуск_гл_1': self.ui.doubleSpinBox_dopusk_length.value(),
                    'допуск_гл_2': self.ui.doubleSpinBox_dopusk_length_2.value(),
                    'тип': 'гладкие'
                }
            elif self.get_button_type_hole() == 'резьбовые':
                d = {
                    'диаметр': float(self.ui.comboBox_diameter.currentText()[1:]),
                    'шаг': float(self.ui.comboBox_diameter_2.currentText()),
                    'допуск': self.ui.comboBox_dopusk.currentText(),
                    'количество': self.ui.spinBox_count.value(),
                    'статус глубины': self.ui.checkBox_add_length.isChecked(),
                    'глубина': self.ui.doubleSpinBox_length.value(),
                    'квалитет глубины': self.ui.lineEdit_kvalitet_length.text(),
                    'допуск_гл_1': self.ui.doubleSpinBox_dopusk_length.value(),
                    'допуск_гл_2': self.ui.doubleSpinBox_dopusk_length_2.value(),
                    'глубина резьбы': self.ui.doubleSpinBox_length_rezba.value(),
                    'допуск_дл_резьба_1': self.ui.doubleSpinBox_dopusk_length_rezba.value(),
                    'допуск_дл_резьба_2': self.ui.doubleSpinBox_dopusk_length_rezba_2.value(),
                    'тип': 'резьбовые'
                }

        self.btn_add_clicked.emit(d)

    def add_rezba_diameter_page(self, value: list):
        if self.ui.comboBox_rezba_d.count() == 0:
            for el in value:
                self.ui.comboBox_rezba_d.addItem('М' + str(el))

    def add_step_diameter(self, value: list):
        self.ui.comboBox_step_d.clear()
        for el in value:
            self.ui.comboBox_step_d.addItem(str(el))
        self.ui.comboBox_step_d.setCurrentIndex(0)

    def _on_button_home_clicked(self):
        self.btn_home_clicked.emit()

    def get_button_active(self):
        if self.ui.btn_diameter.isChecked():
            return 'диаметр'
        elif self.ui.btn_length.isChecked():
            return 'длина'
        elif self.ui.btn_hole.isChecked():
            return 'отверстие'

    def get_button_type_hole(self):
        if self.ui.btn_gladkie.isChecked():
            return 'гладкие'
        elif self.ui.btn_rezba.isChecked():
            return 'резьбовые'

    def show_result(self, text, instrument, key_count):
        """Добавляет строку в таблицу."""
        self.ui.table_widget_kontrol_otk.setRowCount(
            self.ui.table_widget_kontrol_otk.rowCount() + 1
        )
        row = self.ui.table_widget_kontrol_otk.rowCount() - 1

        self.ui.table_widget_kontrol_otk.setItem(row, 0, instrument)
        self.ui.table_widget_kontrol_otk.setItem(row, 1, text)

        btn_delete = QPushButton('Удалить')
        btn_delete.clicked.connect(
            lambda checked, r=key_count: self.on_delete_clicked(r)
        )

        self._delete_buttons.append(btn_delete)
        btn_delete.resize(50, 20)  # Как в PageSverlilnaya
        self.ui.table_widget_kontrol_otk.setCellWidget(row, 2, btn_delete)

    def on_delete_clicked(self, r):
        self.btn_click_delete.emit(r)

    def get_index_row(self, item):
        return self.ui.table_widget_kontrol_otk.row(item)

    def delete_row(self, r):
        self.ui.table_widget_kontrol_otk.removeRow(r)

    def show_label(self, text):
        self.ui.text_info.setText(text)

    def clear_table(self):
        """Очистка таблицы. ОБЯЗАТЕЛЬНЫЙ метод."""
        self.ui.table_widget_kontrol_otk.clear()
        self.ui.table_widget_kontrol_otk.setRowCount(0)
        self.ui.table_widget_kontrol_otk.setHorizontalHeaderLabels(
            ['Инструмент', 'Размеры', '']
        )
        self._delete_buttons.clear()

    def add_diameter(self):
        pass

    def add_length(self):
        pass

    def add_hole(self):
        pass

    def type_control(self):
        pass