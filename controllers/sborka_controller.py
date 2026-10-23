from controllers.base_controller import BaseOperationController
from logic.operation_sborka import Sborka
from logic.automation import TechnoproAutomation
from ui_autoinput import Ui_MainWindow
from PySide6.QtWidgets import QTableWidgetItem
from PySide6.QtCore import Qt
from dialogs.dialog_termichka import DialogTermichka
from dialogs.dialog_slesarnaya import DialogSlesarnaya
from dialogs.dialog_promivka import DialogPromivka
from dialogs.dialog_sborka import DialogSborka
from views.rows.row_detail import RowDetail


class SborkaController(BaseOperationController):
    def __init__(self, ui, parent=None):
        self.ui:Ui_MainWindow = ui
        self.model:Sborka = Sborka()
        self.automation: TechnoproAutomation = TechnoproAutomation()
        super().__init__(ui, self.model, self.automation, parent)
        self.dialog_termichka = DialogTermichka()
        self.dialog_slesarnaya = DialogSlesarnaya()
        self.dialog_promivka = DialogPromivka()
        self.dialog_sborka = DialogSborka(details=self.model.details,
                                          deistviya=self.model.deistviya,
                                          metrick_rezba=self.model.metric_thread_pitches)
        self.row_detail = RowDetail()

        self._connect_signals_dialogs()

        self.add_items_all()

        self.ui.page_sborka.btn_home_clicked.connect(self._go_to_main_page)
        self.ui.page_sborka.checkbox_clicked.connect(self.go_to_main_page)
        self.ui.page_sborka.table_select_clicked.connect(self.show_operations)
        self.ui.page_sborka.btn_click_delete.connect(self.delete_row)
        self.ui.page_sborka.btn_clear_table.connect(self.clear_all)
        self.ui.page_sborka.btn_export_clicked.connect(self.export_operations)
        self.ui.page_sborka.btn_update_clicked.connect(self.update_table)

    def _connect_signals_dialogs(self):
        self.dialog_termichka.btn_save_result_clicked.connect(self.add_items_termichka_in_table)
        self.dialog_slesarnaya.btn_save_result_clicked.connect(self.save_result_slesarnaya)
        self.dialog_slesarnaya.btn_add_row_clicked.connect(
            lambda: self.dialog_slesarnaya.add_row(self.model.details)
        )
        self.dialog_promivka.btn_save_clicked.connect(self.save_result_promivka)
        self.dialog_sborka.btn_save_clicked.connect(self.save_result_sborka)

    def save_result_sborka(self, d):
        result = self.model.sborka(d)
        msg = self._process_and_save_result(result)
        self.ui.page_sborka.show_label(msg)


    def clear_all(self):
        self.ui.page_sborka.clear_table_sborka()
        self.model.clear_all()
        self.model.all_instrument.clear()
        if self.model.operations:
            self.ui.page_sborka.show_label('Записанные данные в таблицу были удалены!')

    def get_target_page(self):
        """Возвращает страницу-таблицу этой операции."""
        return self.ui.page_sborka

    def _go_to_main_page(self):
        self.clear_all()
        self.exit_to_main_menu_requested.emit()

    def go_to_main_page(self):
        self.ui.page_sborka.clear_table_operations()
        self.add_operations_in_table()
        self.ui.stackedWidget.setCurrentIndex(14)

    def add_operations_in_table(self):
        if self.ui.page_sborka.is_checkbox_find():
            for operation in self.model.show_in_program():
                operation_item = QTableWidgetItem(operation)
                self.ui.page_sborka.add_items_operations(operation_item)
        else:
            for operation in self.model.operations_sborka:
                operation_item = QTableWidgetItem(operation['операция'])
                self.ui.page_sborka.add_items_operations(operation_item)

    def show_operations(self, value):
        self.update_table()
        self.show_dialog(value)

    def update_table(self):
        value = self.ui.page_sborka.get_text_table_operations()
        print(value)
        self.ui.page_sborka.clear_table_with_find_operations()
        count = self.model.get_count_operations(value)
        if count > 0:
            for _ in range(count):
                operation_item = QTableWidgetItem(value)
                self.ui.page_sborka.add_items_find_operations(operation=operation_item)

    def show_dialog(self, operation_name):
        self.close_all_dialogs()
        if operation_name == 'Термическая обработка':
            self.dialog_termichka.show()
        elif operation_name == 'Слесарная':
            self.dialog_slesarnaya.show()
        elif operation_name == 'Промывка':
            self.dialog_promivka.show()
        elif operation_name == 'Сборка':
            self.dialog_sborka.show()



    def add_items_termichka_in_table(self):
        data, row = self.dialog_termichka.get_result()
        result = self.model.termichka(data, row)
        msg = self._process_and_save_result(result)
        self.ui.page_sborka.show_label(msg)

    def delete_row(self, r):
        """Удаляет строку из таблицы и модели."""
        item = self.model.operations[r]['описание']
        if self.model.operations[r]['инструмент'].text() != '':
            item_instrument = self.model.operations[r]['инструмент'].text()
            self.model.find_and_delete_from_all_instrument(item_instrument.split('\n'))
        row_index = self.ui.page_sborka.get_index_row(item)
        self.ui.page_sborka.show_label(f'Строка №{row_index + 1} успешно удалена!')
        self.ui.page_sborka.delete_row(row_index)
        del self.model.operations[r]

    def close_all_dialogs(self):
        self.dialog_slesarnaya.close()
        self.dialog_termichka.close()

    def add_items_all(self):
        details = self.model.details
        self.dialog_termichka.add_items(details)
        self.dialog_slesarnaya.add_details(details)


    def save_result_slesarnaya(self, value:dict):
        msg = ''
        if self.dialog_slesarnaya.button_click() == 'мех. обработка':
            result = self.model.slesarnaya_meh(value)
            msg = self._process_and_save_result(result)
        elif self.dialog_slesarnaya.button_click() == 'сборка':
            if self.dialog_slesarnaya.get_current_row() == 0:
                result = self.model.slesarnaya_sborka_protirka(value)
                msg = self._process_and_save_result(result)
        elif self.dialog_slesarnaya.button_click()[0] == 'сварка':
            if self.dialog_slesarnaya.get_curent_row_svarka() == 0:
                result = self.model.svarka_start(value)
                msg = self._process_and_save_result(result)

            elif self.dialog_slesarnaya.get_curent_row_svarka() == 1 or self.dialog_slesarnaya.get_curent_row_svarka() == 2:
                if value['ширина_от'] > value['ширина_до']:
                    self.ui.page_sborka.show_label('Ширина "ОТ" не может быть больше, чем ширина "ДО"')
                    return
                if self.dialog_slesarnaya.button_click()[1] == 1:
                    if self.dialog_slesarnaya.len_data_zachistka() == 0:
                        self.ui.page_sborka.show_label('Необходимо добавить деталь')
                        return
                    result = self.model.slesarnaya_svarka_zachistka_and_obez(value, 'Зачистить')
                    msg = self._process_and_save_result(result)
                elif self.dialog_slesarnaya.button_click()[1] == 2:
                    if self.dialog_slesarnaya.len_data_obez() == 0:
                        self.ui.page_sborka.show_label('Необходимо добавить деталь')
                        return
                    result = self.model.slesarnaya_svarka_zachistka_and_obez(value, 'Обезжирить')
                    msg = self._process_and_save_result(result)
            elif self.dialog_slesarnaya.get_curent_row_svarka() == 3:
                result = self.model.svarka_zach_shvov(value)
                msg = self._process_and_save_result(result)
        self.ui.page_sborka.show_label(msg)

    def export_operations(self):
        index_row = self.ui.page_sborka.get_index_number_operations()
        text = self.ui.page_sborka.get_text_operations()
        image = None
        if text == 0:
            self.ui.page_sborka.show_label('Ошибка: В списке "Найденные операции" необходимо выбрать операцию')
            return
        for item in self.model.operations_sborka:
            if item['операция'] == text:
                image = item['кнопка']
                break
        self.model.automation.start(
            operations=self.model.operations,
            index=index_row,
            image_find=image
        )



    def save_result_promivka(self):
        result = self.model.save_result_promivka()
        msg = self._process_and_save_result(result)
        self.ui.page_sborka.show_label(msg)









