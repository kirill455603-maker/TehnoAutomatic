from controllers.base_controller import BaseOperationController
from logic.operation_sverlilnaya import Sverlilnaya
from logic.automation import TechnoproAutomation
from ui_autoinput import Ui_MainWindow
from dialogs.dialog_find_sverlo import FindSverlo


class SverlilnayaController(BaseOperationController):
    def __init__(self, ui, parent=None):
        super().__init__(ui, Sverlilnaya(), TechnoproAutomation(), parent)
        self.ui:Ui_MainWindow = ui
        self.model:Sverlilnaya = Sverlilnaya()
        self.automation:TechnoproAutomation = TechnoproAutomation()
        self.dialog = FindSverlo()
        self._connect_signals()
        self.ui.page_sverlilnaya.ui.page_sverlilnaya_start.add_items(list(self.model.dict_sverla.keys()))
        self.ui.page_sverlilnaya.ui.page_sverlilnaya_expanding_hole.add_items(list(self.model.dict_sverla.keys()))
        self.ui.page_sverlilnaya.ui.page_sverlilnaya_chistovaya.add_items(self.model.dopusk_razvertka)
        self.ui.page_sverlilnaya.ui.page_sverlilnaya_chistovaya.add_items_surf(self.model.dopusk_surf)
        self.ui.page_sverlilnaya.ui.page_sverlilnaya_chistovaya.add_items_razvertka(list(self.model.dict_razvetki.keys()))
        self.ui.page_sverlilnaya.ui.page_sverlilnaya_start.btn_find_sverlo.connect(self.show_find_sverlo)
        self.dialog.btn_save_clicked.connect(self.add_sverlo_in_start)

        self.ui.page_sverlilnaya.ui.page_sverlilnaya_rezba.add_items_rezba(self.model.list_d_rezba[:self.model.list_d_rezba.index('24') + 1])
        self.ui.page_sverlilnaya.ui.page_sverlilnaya_rezba.add_items_dopusk(self.model.thread_tolerances['внутренняя'])



    def get_operation_name(self) -> str:
        """Название операции для Technopro."""
        return 'Сверлильная'

    def get_target_page(self):
        """Возвращает страницу-таблицу этой операции."""
        return self.ui.page_sverlilnaya

    def clear_all(self):
        """Очистка всех данных операции."""
        self.model.clear_all()
        self.model.all_instrument.clear()
        self.ui.page_sverlilnaya.clear_table()
        self.ui.page_sverlilnaya.show_label('Записанные данные в таблицу успешно удалены!')


    def _connect_signals(self):
        self.ui.page_sverlilnaya.btn_home_clicked.connect(self._go_to_main_page)
        self.ui.page_sverlilnaya.btn_click_page.connect(self.switch_page)
        self.ui.page_sverlilnaya.btn_save_result_clicked.connect(self.save_result_in_table)
        self.ui.page_sverlilnaya.btn_clear_table_clicked.connect(self.clear_all)
        self.ui.page_sverlilnaya.btn_click_delete.connect(self.delete_row)
        self.ui.page_sverlilnaya.ui.page_sverlilnaya_rezba.combo_box_changed.connect(self._add_items_step)
        self.ui.page_sverlilnaya.btn_save_and_export_clicked.connect(self.go_to_technopro)

    def save_result_in_table(self, d:dict):
        page_num = self.ui.page_sverlilnaya.get_current_page()
        if page_num == 0:
            if d['диаметр'] == 0:
                self.ui.page_sverlilnaya.show_label(
                    'Ошибка: Укажите диметр необходимого отверстия'
                )

            result = self.model.start(d)
            msg = self._process_and_save_result(result)
            self.ui.page_sverlilnaya.show_label(msg)
        elif page_num == 1:
            if d['отверстие'] == 0:
                self.ui.page_sverlilnaya.show_label(
                    'Ошибка: Укажите диаметр отверстия, которое хотите увеличить'
                )
                return
            elif d['сверло'] <= d['отверстие']:
                self.ui.page_sverlilnaya.show_label(
                    'Ошибка: Данное сверло не увеличит отверстие'
                )
                return
            result = self.model.expanding(d)
            msg = self._process_and_save_result(result)
            self.ui.page_sverlilnaya.show_label(msg)
        elif page_num == 2:

            result = self.model.chistovaya(d)
            msg = self._process_and_save_result(result)
            self.ui.page_sverlilnaya.show_label(msg)

        elif page_num == 3:
            if d['шаг'] == 0:
                self.ui.page_sverlilnaya.show_label(
                    'Ошибка: Укажите шаг резьбы'
                )
                return
            if d['допуск'] == '':
                self.ui.page_sverlilnaya.show_label(
                    'Ошибка: Укажите поле допуска резьбы'
                )
                return
            result = self.model.rezba(d)
            msg = self._process_and_save_result(result)
            self.ui.page_sverlilnaya.show_label(msg)
        elif page_num == 4:
            if d['диаметр'] == 0:
                self.ui.page_sverlilnaya.show_label(
                    'Ошибка: Укажите диаметр отверстия в которой будет сделана фаска'
                )
                return
            if d['угол'] == 0:
                self.ui.page_sverlilnaya.show_label(
                    'Ошибка: Укажите угол фаски'
                )
                return
            if d['длина'] == 0:
                self.ui.page_sverlilnaya.show_label('Ошибка: Укажите значение фаски')
                return
            result = self.model.faska(d)
            msg = self._process_and_save_result(result)
            self.ui.page_sverlilnaya.show_label(msg)


    def _add_items_step(self, value):
        data = self.model.metric_thread_pitches[value]
        self.ui.page_sverlilnaya.ui.page_sverlilnaya_rezba.add_items_step(data)

    def switch_page(self, number_page:int):
        self.clear_pages(number_page)
        self.ui.page_sverlilnaya.switch_page(number=number_page)

    def _go_to_main_page(self):
        self.ui.page_sverlilnaya.clear_table()
        self.exit_to_main_menu_requested.emit()

    def go_to_main_page(self):
        self.ui.stackedWidget.setCurrentIndex(12)

    def save_sverlilnaya(self, data:dict):
        pass

    def clear_pages(self, num_page):
        if num_page == 0:
            self.ui.page_sverlilnaya.ui.page_sverlilnaya_start.clear_all()
        elif num_page == 1:
            self.ui.page_sverlilnaya.ui.page_sverlilnaya_expanding_hole.clear_all()
        elif num_page == 2:
            self.ui.page_sverlilnaya.ui.page_sverlilnaya_chistovaya.clear_all()
        elif num_page == 3:
            self.ui.page_sverlilnaya.ui.page_sverlilnaya_rezba.clear_all()
        elif num_page == 4:
            self.ui.page_sverlilnaya.ui.page_sverlilnaya_faska.clear_all()

    def delete_row(self, r):
        """Удаляет строку из таблицы и модели."""
        item = self.model.operations[r]['описание']
        if self.model.operations[r]['инструмент'].text() != '':
            item_instrument = self.model.operations[r]['инструмент'].text()
            self.model.find_and_delete_from_all_instrument(item_instrument.split('\n'))
        row_index = self.ui.page_sverlilnaya.get_index_row(item)
        self.ui.page_sverlilnaya.show_label(f'Строка №{row_index + 1} успешно удалена!')
        self.ui.page_sverlilnaya.delete_row(row_index)
        del self.model.operations[r]

    def show_find_sverlo(self):
        self.dialog.show()
        self.dialog.all_clear()
        self.dialog.dict_rezb = self.model.metric_thread_pitches
        self.dialog.add_rezba()

    def add_sverlo_in_start(self, value):
        if self.ui.page_sverlilnaya.ui.page_sverlilnaya_start.is_have_sverlo(value) == -1:
            self.dialog.add_text(f'Ошибка: Сверло ({value}) под данную резьбу не найдено в базе')
            return
        else:
            self.ui.page_sverlilnaya.ui.page_sverlilnaya_start.set_sverlo(value=value)
            self.dialog.close()