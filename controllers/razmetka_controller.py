# controllers/razmetka_controller.py
from controllers.base_controller import BaseOperationController
from logic.operation_razmetka import Razmetka
from logic.automation import TechnoproAutomation


class RazmetkaController(BaseOperationController):
    def __init__(self, ui, parent=None):
        super().__init__(ui, Razmetka(), TechnoproAutomation(), parent)
        self._connect_signals()

    # ================= РЕАЛИЗАЦИЯ АБСТРАКТНЫХ МЕТОДОВ =================

    def get_operation_name(self) -> str:
        return 'Разметка'

    def get_target_page(self):
        return self.ui.page_razmetka

    def clear_all(self):
        self.model.count = 0
        self.model.operations.clear()
        self.model.all_instrument.clear()
        self.ui.page_razmetka.clear_table()

    def _connect_signals(self):
        self.ui.page_razmetka.btn_home_clicked.connect(self._go_to_main_page)
        self.ui.page_razmetka.btn_save_result_clicked.connect(self.save_razmetka)
        self.ui.page_razmetka.btn_click_delete.connect(self.delete_row)
        self.ui.page_razmetka.btn_clear_table_clicked.connect(self.clear_all)
        self.ui.page_razmetka.btn_save_and_export_clicked.connect(self.go_to_technopro)

    # ================= НАВИГАЦИЯ =================

    def go_to_main_page(self):
        self.ui.page_razmetka.show_d_rezb(self.model.list_d_rezba)
        self.ui.stackedWidget.setCurrentIndex(11)

    def _go_to_main_page(self):
        self.ui.page_razmetka.clear_table()
        self.exit_to_main_menu_requested.emit()

    # ================= ЛОГИКА СОХРАНЕНИЯ =================

    def save_razmetka(self, data: dict):
        if data['диаметр разметки'] == 0:
            self.ui.page_razmetka.show_label('Ошибка: Диаметр разметки не может быть нулевым')
            return
        if data['допуск'] != 0 and data['база'] == '':
            self.ui.page_razmetka.show_label('Ошибка: Укажите базу')
            return
        if data['резьба'] == '' and data['без резьбы'] == 0:
            self.ui.page_razmetka.show_label('Ошибка: Укажите обозначение отверстия(-ий)')
            return

        result = self.model.razmetka(data)
        msg = self._process_and_save_result(result)
        self.ui.page_razmetka.show_label(msg)

    # ================= УДАЛЕНИЕ =================

    def delete_row(self, r):
        item = self.model.operations[r]['описание']
        if self.model.operations[r]['инструмент'].text() != '':
            item_instrument = self.model.operations[r]['инструмент'].text()
            self.model.find_and_delete_from_all_instrument(item_instrument.split('\n'))
        row_index = self.ui.page_razmetka.get_index_row(item)
        self.ui.page_razmetka.delete_row(row_index)
        del self.model.operations[r]