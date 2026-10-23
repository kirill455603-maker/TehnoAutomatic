from controllers.base_controller import BaseOperationController
from logic.operation_kontrol_otk import KontrolOtk
from PySide6.QtWidgets import QTableWidgetItem
from PySide6.QtCore import Qt
from logic.automation import TechnoproAutomation
from ui_autoinput import Ui_MainWindow

class KontrolOtkController(BaseOperationController):
    def __init__(self, ui, parent=None):
        super().__init__(ui, KontrolOtk(), TechnoproAutomation(), parent)
        self.ui:Ui_MainWindow = ui
        self.model:KontrolOtk = KontrolOtk()
        self.automation:TechnoproAutomation = TechnoproAutomation()
        self._connect_signals()

    def get_operation_name(self) -> str:
        return 'Контроль ОТК'

    def get_target_page(self):
        return self.ui.page_kontrol_otk

    def clear_all(self):
        """Очистка всех данных операции."""
        self.model.clear_all()
        self.model.all_instrument.clear()
        self.ui.page_kontrol_otk.clear_table()
        self.ui.page_kontrol_otk.show_label('Записанные данные в таблицу успешно удалены!')


    def _connect_signals(self):
        self.ui.page_kontrol_otk.btn_home_clicked.connect(self._go_to_main_page)
        self.ui.page_kontrol_otk.btn_add_clicked.connect(self.add_elements)
        self.ui.page_kontrol_otk.btn_click_delete.connect(self.delete_row)
        self.ui.page_kontrol_otk.btn_hole_clicked.connect(self.add_rezba)
        self.ui.page_kontrol_otk.combobox_rezba_changed.connect(self.add_steps)
        self.ui.page_kontrol_otk.btn_clear_clicked.connect(self.clear_all)
        self.ui.page_kontrol_otk.btn_save_and_export_clicked.connect(self.go_to_technopro)
        self.ui.page_kontrol_otk.btn_add_rezba_diameter.connect(self.add_rezba_diameter)
        self.ui.page_kontrol_otk.combobox_rezba_changed_diameter.connect(self.add_steps_diameter)
        self.ui.page_kontrol_otk.r_btn_otv_clicked.connect(
            lambda: self.ui.page_kontrol_otk.add_dopusk_diameter_page(self.model.thread_tolerances)
        )
        self.ui.page_kontrol_otk.r_btn_val_clicked.connect(
            lambda: self.ui.page_kontrol_otk.add_dopusk_diameter_page(self.model.thread_tolerances)
        )

    def add_rezba_diameter(self):
        value_dict = self.model.metric_thread_pitches
        value_result = []
        for key in value_dict:
            value = self.model.format_num(key)
            value_result.append(value)
        self.ui.page_kontrol_otk.add_rezba_diameter_page(value_result)
        self.ui.page_kontrol_otk.add_dopusk_diameter_page(self.model.thread_tolerances)


    def add_rezba(self):
        value_dict = self.model.metric_thread_pitches
        value_result = []
        for key in value_dict:
            value = self.model.format_num(key)
            value_result.append(value)
        self.ui.page_kontrol_otk.add_rezba(value_result)
        self.ui.page_kontrol_otk.add_dopusk(self.model.thread_tolerances['внутренняя'])

    def add_steps(self, d):
        value_list = self.model.metric_thread_pitches[d]
        value_result = []
        for el in value_list:
            value = self.model.format_num(float(el))
            value_result.append(value)
        self.ui.page_kontrol_otk.add_step(value_result)

    def add_steps_diameter(self, d):
        value_list = self.model.metric_thread_pitches[d]
        value_result = []
        for el in value_list:
            value = self.model.format_num(float(el))
            value_result.append(value)
        self.ui.page_kontrol_otk.add_step_diameter(value_result)

    def _go_to_main_page(self):
        self.ui.page_kontrol_otk.clear_table()
        self.exit_to_main_menu_requested.emit()

    def go_to_main_page(self):
        self.ui.stackedWidget.setCurrentIndex(16)

    def add_elements(self, d):
        if self.ui.page_kontrol_otk.get_button_active() == 'диаметр':
            if 'шаг' not in d:
                if d['диаметр'] == 0:
                    self.ui.page_kontrol_otk.show_label('Ошибка: Значение диаметра не может быть "0"')
                    return
                result = self.model.diameter(d)
                msg = self._process_and_save_result(result)
                self.ui.page_kontrol_otk.show_label(msg)
            else:
                if d['диаметр'] == '':
                    self.ui.page_kontrol_otk.show_label('Ошибка: Необходимо выбрать резьбу')
                    return
                result = self.model.diameter_rezba(d)
                msg = self._process_and_save_result(result)
                self.ui.page_kontrol_otk.show_label(msg)
        elif self.ui.page_kontrol_otk.get_button_active() == 'длина':
            if d['длина'] == 0:
                self.ui.page_kontrol_otk.show_label('Ошибка: Значение длины не может быть "0"')
                return
            result = self.model.length(d)
            msg = self._process_and_save_result(result)
            self.ui.page_kontrol_otk.show_label(msg)
        elif self.ui.page_kontrol_otk.get_button_active() == 'отверстие':
            if d['диаметр'] == 0 or d['диаметр'] == '':
                self.ui.page_kontrol_otk.show_label('Ошибка: Укажите значение диаметра или резьбы')
                return
            if d['статус глубины'] and d['глубина'] == 0:
                self.ui.page_kontrol_otk.show_label('Ошибка: Укажите глубину или уберите "галочку" с указания глубины')
                return
            if d['тип'] == 'гладкие':
                result = self.model.hole_gladkoe(d)
                msg = self._process_and_save_result(result)
                self.ui.page_kontrol_otk.show_label(msg)
            elif d['тип'] == 'резьбовые':
                if d['статус глубины'] and d['глубина'] == 0 and d['глубина резьбы'] == 0:
                    self.ui.page_kontrol_otk.show_label('Ошибка: Укажите глубину или уберите "галочку" с указания глубины')
                    return
                result = self.model.hole_rezba(d)
                msg = self._process_and_save_result(result)
                self.ui.page_kontrol_otk.show_label(msg)

    def _process_and_save_result(self, result: dict) -> str:
        """
        Не Универсальный метод сохранения операции, только для Контроль ОТК.
        target_page определяется через get_target_page().
        """
        item_about = QTableWidgetItem(str(result['описание']))
        item_instrument = QTableWidgetItem(str('\n'.join(result['инструмент'])))
        item_instrument.setFlags(Qt.ItemFlag.ItemIsSelectable | Qt.ItemFlag.ItemIsEnabled)

        # Сохраняем в модель
        self.model.operations[self.model.count] = {
            'описание': item_about,
            'инструмент': item_instrument
        }

        # Показываем в таблице через универсальный метод show_result
        target_page = self.get_target_page()
        target_page.show_result(
            text=item_about,
            instrument=item_instrument,
            key_count=self.model.count
        )

        self.model.count += 1
        return 'Переход добавлен в таблицу!'

    def delete_row(self, r):
        """Удаляет строку из таблицы и модели."""
        item = self.model.operations[r]['описание']
        if self.model.operations[r]['инструмент'].text() != '':
            item_instrument = self.model.operations[r]['инструмент'].text()
            self.model.find_and_delete_from_all_instrument(item_instrument.split('\n'))
        row_index = self.ui.page_kontrol_otk.get_index_row(item)
        self.ui.page_kontrol_otk.show_label(f'Строка №{row_index + 1} успешно удалена!')
        self.ui.page_kontrol_otk.delete_row(row_index)
        del self.model.operations[r]



