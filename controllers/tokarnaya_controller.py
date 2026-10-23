# controllers/tokarnaya_controller.py
from controllers.base_controller import BaseOperationController
from logic.operation_tokarnaya import Tokarnaya
from logic.automation import TechnoproAutomation
from dialogs.exit_dialog import ExitDialog


class TokarnayaController(BaseOperationController):
    def __init__(self, ui, parent=None):
        super().__init__(ui, Tokarnaya(), TechnoproAutomation(), parent)
        self.model:Tokarnaya = Tokarnaya()
        self._connect_signals()

    # ================= РЕАЛИЗАЦИЯ АБСТРАКТНЫХ МЕТОДОВ =================

    def get_operation_name(self) -> str:
        return 'Токарная'

    def get_target_page(self):
        return self.ui.page_tokarnaya

    def clear_all(self):
        self.model.count = 0
        self.model.operations.clear()
        self.model.all_instrument.clear()
        self.ui.page_tokarnaya.clear_table()

    def _connect_signals(self):
        # --- НАВИГАЦИЯ ---
        self.ui.page_tokarnaya.btn_start_obrabotki_clicked.connect(self._go_to_start_obrabotki)
        self.ui.page_tokarnaya.btn_tochenie_clicked.connect(self._go_to_tochenie)
        self.ui.page_tokarnaya.btn_podrezka_clicked.connect(self._go_to_podrezka)
        self.ui.page_tokarnaya.btn_sverlenie_clicked.connect(self._go_to_sverlenie)
        self.ui.page_tokarnaya.btn_rastachivanie_clicked.connect(self._go_to_rastachivanie)
        self.ui.page_tokarnaya.btn_rezba_clicked.connect(self._go_to_rezba)
        self.ui.page_tokarnaya.btn_faska_clicked.connect(self._go_to_faska)
        self.ui.page_tokarnaya.btn_angle_clicked.connect(self._go_to_angle)

        # --- КНОПКИ "ДОМОЙ" ---
        self.ui.page_tokarnaya_start.btn_home_tokarnaya_clicked.connect(self._go_to_tokarnaya)
        self.ui.page_tokarnaya_podrezka.btn_home_tokarnaya_clicked.connect(self._go_to_tokarnaya)
        self.ui.page_tokarnaya_tochenie.btn_home_tochenie_clicked.connect(self._go_to_tokarnaya)
        self.ui.page_tokarnaya_sverlenie.btn_home_sverlenie_clicked.connect(self._go_to_tokarnaya)
        self.ui.page_tokarnaya_rastachivanie.btn_home_clicked.connect(self._go_to_tokarnaya)
        self.ui.page_tokarnaya_rezba.btn_home_clicked.connect(self._go_to_tokarnaya)
        self.ui.page_tokarnaya_faska.btn_home_clicked.connect(self._go_to_tokarnaya)
        self.ui.page_tokarnaya_angle.btn_home_clicked.connect(self._go_to_tokarnaya)

        # --- КНОПКИ "СОХРАНИТЬ" ---
        self.ui.page_tokarnaya_start.btn_save_result_clicked.connect(self.save_start_obrabotki)
        self.ui.page_tokarnaya_podrezka.btn_save_result_podrezka_clicked.connect(self.save_podrezka)
        self.ui.page_tokarnaya_tochenie.btn_save_result_clicked.connect(self.save_tochenie)
        self.ui.page_tokarnaya_sverlenie.btn_save_result_sverlenie_clicked.connect(self.save_sverlenie)
        self.ui.page_tokarnaya_rastachivanie.btn_save_result_clicked.connect(self.save_rastachivanie)
        self.ui.page_tokarnaya_rezba.btn_save_result.connect(self.save_rezba)
        self.ui.page_tokarnaya_faska.btn_save_result_clicked.connect(self.save_faska)
        self.ui.page_tokarnaya_angle.btn_save_result_clicked.connect(self.save_angle)

        # --- СПЕЦИФИЧНЫЕ СИГНАЛЫ (РЕЗЬБА) ---
        self.ui.page_tokarnaya_rezba.list_diamter_rezba_edit.connect(self.show_all_rezb_for_diameter)
        self.ui.page_tokarnaya_rezba.btn_radio_in_click.connect(self.edit_dopusk_rezba_on_in)
        self.ui.page_tokarnaya_rezba.btn_radio_out_click.connect(self.edit_dopusk_rezba_on_out)

        # --- ОБЩИЕ КНОПКИ СТРАНИЦЫ ТОКАРНОЙ ---
        self.ui.page_tokarnaya.btn_home_clicked.connect(self.show_dialog_exit)
        self.ui.page_tokarnaya.btn_clear_table_clicked.connect(self.clear_all)
        self.ui.page_tokarnaya.btn_click_delete.connect(self.delete_row)
        self.ui.page_tokarnaya.btn_save_and_export.connect(self.go_to_technopro)

    # ================= НАВИГАЦИЯ =================

    def go_to_main_page(self):
        self.ui.stackedWidget.setCurrentIndex(1)

    def _go_to_tokarnaya(self):
        self.ui.stackedWidget.setCurrentIndex(1)

    def _go_to_start_obrabotki(self):
        self.ui.stackedWidget.setCurrentIndex(2)

    def _go_to_podrezka(self):
        self.ui.stackedWidget.setCurrentIndex(3)

    def _go_to_tochenie(self):
        self.ui.stackedWidget.setCurrentIndex(4)

    def _go_to_sverlenie(self):
        sverla = [str(key) for key in self.model.dict_sverla]
        self.ui.page_tokarnaya_sverlenie.add_sverla(sverla=sverla)
        self.ui.stackedWidget.setCurrentIndex(5)

    def _go_to_rastachivanie(self):
        self.ui.stackedWidget.setCurrentIndex(7)

    def _go_to_rezba(self):
        self.ui.page_tokarnaya_rezba.add_list_diameter(self.model.list_d_rezba)
        self.ui.page_tokarnaya_rezba.edit_list_dopusk(self.model.thread_tolerances['внутренняя'])
        self.ui.stackedWidget.setCurrentIndex(8)

    def _go_to_faska(self):
        self.ui.stackedWidget.setCurrentIndex(9)

    def _go_to_angle(self):
        self.ui.stackedWidget.setCurrentIndex(10)

    # ================= ЛОГИКА СОХРАНЕНИЯ =================

    def save_start_obrabotki(self, d):
        if d['статус чек']:
            if d['биение радиальное'] == 0 and d['биение торцевое'] == 0 :
                self.ui.page_tokarnaya_start.set_show_error(
                    'Ошибка: Необходимо указать значение хотя бы одного типа биения')
                return
            if d['по диаметру'] == 0 and d['по базе'] == '':
                self.ui.page_tokarnaya_start.set_show_error(
                    'Ошибка: Не указано значение относительно чего позиционироваться')
                return
        if d['диаметр установки'] == 0:
            self.ui.page_tokarnaya_start.set_show_error('Ошибка: Диаметр установки не может быть равен нулю')
            return
        if d['диаметр заготовки'] == 0:
            self.ui.page_tokarnaya_start.set_show_error('Ошибка: Диаметр заготовки не может быть равен нулю')
            return
        if d['диаметр заготовки'] < d['диаметр установки']:
            self.ui.page_tokarnaya_start.set_show_error('Ошибка: Диаметр заготовки не может быть меньше диаметра установки')
            return

        result = self.model.start_obrabotki(d)
        self._process_and_save_result(result)
        self.ui.page_tokarnaya_start.set_show_result(
            text=self.model.operations[self.model.count - 1]['описание'].clone(),
            instrument=self.model.operations[self.model.count - 1]['инструмент'].clone()
        )
        self.ui.page_tokarnaya_start.set_show_error(
            'Переход операции "Начальная установка" был успешно сохранен! Изменить можно в "Токарная" -> "Таблица переходов"')

    def save_podrezka(self, dict_podrezka):
        result = self.model.podrezka(dict_podrezka)
        self._process_and_save_result(result)
        self.ui.page_tokarnaya_podrezka.show_text_result(
            text=self.model.operations[self.model.count - 1]['описание'].clone(),
            instrument=self.model.operations[self.model.count - 1]['инструмент'].clone()
        )
        self.ui.page_tokarnaya_podrezka.set_show_error(
            'Переход операции "Подрезка" был успешно сохранен! Изменить можно в "Токарная" -> "Таблица переходов"')

    def save_tochenie(self, dict_tochenie):
        if not dict_tochenie['диаметр']:
            self.ui.page_tokarnaya_tochenie.set_show_error_tochenie('Ошибка: Диаметр не может быть равен нулю')
            return
        if dict_tochenie['база_радиальная'] or dict_tochenie['биение_радиальное']:
            if not dict_tochenie['биение_радиальное']:
                self.ui.page_tokarnaya_tochenie.set_show_error_tochenie('Ошибка: Не указана значение радиального биения')
                return
            elif not dict_tochenie['база_радиальная']:
                self.ui.page_tokarnaya_tochenie.set_show_error_tochenie(
                    'Ошибка: Не указано обозначение баз(-ы) радиального биения')
                return
        if dict_tochenie['база_торцевая'] or dict_tochenie['биение_торцевое']:
            if not dict_tochenie['биение_торцевое']:
                self.ui.page_tokarnaya_tochenie.set_show_error_tochenie('Ошибка: Не указана значение торцевого биения')
                return
            elif not dict_tochenie['база_торцевая']:
                self.ui.page_tokarnaya_tochenie.set_show_error_tochenie(
                    'Ошибка: Не указано обозначение баз(-ы) торцевого биения')
                return
        result = self.model.tochenie(d=dict_tochenie)
        self._process_and_save_result(result)
        self.ui.page_tokarnaya_tochenie.show_result(
            text=self.model.operations[self.model.count - 1]['описание'].clone(),
            instrument=self.model.operations[self.model.count - 1]['инструмент'].clone()
        )
        self.ui.page_tokarnaya_tochenie.set_show_error(
            'Переход операции "Точение" был успешно сохранен! Изменить можно в "Токарная" -> "Таблица переходов"')

    def save_sverlenie(self, diameter, length):
        if diameter == 0:
            self.ui.page_tokarnaya_sverlenie.edit_error('Ошибка: Диаметр сверла не может быть равен нулю!')
            return
        result = self.model.sverlenie(diameter=diameter, length=length)
        self._process_and_save_result(result)
        self.ui.page_tokarnaya_sverlenie.show_result(
            text=self.model.operations[self.model.count - 1]['описание'].clone(),
            instrument=self.model.operations[self.model.count - 1]['инструмент'].clone()
        )
        self.ui.page_tokarnaya_sverlenie.edit_error(
            f'Переход операции "Сверление" был успешно сохранен! Изменить можно в "Токарная" -> "Таблица переходов"')

    def save_rastachivanie(self, dict_rastachivanie):
        if not dict_rastachivanie['диаметр']:
            self.ui.page_tokarnaya_rastachivanie.set_show_error_rastachivanie('Ошибка: Диаметр не может быть равен нулю')
            return
        if dict_rastachivanie['база_радиальная'] or dict_rastachivanie['биение_радиальное']:
            if not dict_rastachivanie['биение_радиальное']:
                self.ui.page_tokarnaya_rastachivanie.set_show_error_rastachivanie('Ошибка: Не указана значение радиального биения')
                return
            elif not dict_rastachivanie['база_радиальная']:
                self.ui.page_tokarnaya_rastachivanie.set_show_error_rastachivanie(
                    'Ошибка: Не указано обозначение баз(-ы) радиального биения')
                return
        if dict_rastachivanie['база_торцевая'] or dict_rastachivanie['биение_торцевое']:
            if not dict_rastachivanie['биение_торцевое']:
                self.ui.page_tokarnaya_rastachivanie.set_show_error_rastachivanie('Ошибка: Не указана значение торцевого биения')
                return
            elif not dict_rastachivanie['база_торцевая']:
                self.ui.page_tokarnaya_rastachivanie.set_show_error_rastachivanie(
                    'Ошибка: Не указано обозначение баз(-ы) торцевого биения')
                return
        result = self.model.rastachivanie(d=dict_rastachivanie)
        self._process_and_save_result(result)
        self.ui.page_tokarnaya_rastachivanie.show_result(
            text=self.model.operations[self.model.count - 1]['описание'].clone(),
            instrument=self.model.operations[self.model.count - 1]['инструмент'].clone()
        )
        self.ui.page_tokarnaya_rastachivanie.set_show_error_rastachivanie(
            'Переход операции "Растачивание" был успешно сохранен! Изменить можно в "Токарная" -> "Таблица переходов"')

    def save_rezba(self, dict_rezba):
        if dict_rezba['длина'] == 0:
            self.ui.page_tokarnaya_rezba.set_show_error('Ошибка: Вы не указали длину резьбы!')
            return
        result = self.model.rezba(d=dict_rezba)
        self._process_and_save_result(result)
        self.ui.page_tokarnaya_rezba.show_result(
            text=self.model.operations[self.model.count - 1]['описание'].clone(),
            instrument=self.model.operations[self.model.count - 1]['инструмент'].clone()
        )
        self.ui.page_tokarnaya_rezba.set_show_error(
            f'Переход операции "Нарезние резьбы" был успешно сохранен! Изменить можно в "Токарная" -> "Таблица переходов"')

    def save_faska(self, dict_faska):
        result = self.model.faska(d=dict_faska)
        self._process_and_save_result(result)
        self.ui.page_tokarnaya_faska.show_result(
            text=self.model.operations[self.model.count - 1]['описание'].clone(),
            instrument=self.model.operations[self.model.count - 1]['инструмент'].clone()
        )
        self.ui.page_tokarnaya_faska.show_label(
            'Переход операции "Обработка фаски" был успешно сохранен! Изменить можно в "Токарная" -> "Таблица переходов"')

    def save_angle(self, dict_angle):
        if dict_angle['старт'] == 0 and dict_angle['конец'] == 0:
            self.ui.page_tokarnaya_angle.show_label('Ошибка: Оба диаметра не могут быть равны нулю')
            return
        result = self.model.angle(d=dict_angle)
        self._process_and_save_result(result)
        self.ui.page_tokarnaya_angle.show_result(
            text=self.model.operations[self.model.count - 1]['описание'].clone(),
            instrument=self.model.operations[self.model.count - 1]['инструмент'].clone()
        )
        self.ui.page_tokarnaya_angle.show_label(
            'Переход операции "Обработка угла" был успешно сохранен! Изменить можно в "Токарная" -> "Таблица переходов"')

    # ================= ВСПОМОГАТЕЛЬНЫЕ =================

    def edit_dopusk_rezba_on_out(self):
        self.ui.page_tokarnaya_rezba.edit_list_dopusk(self.model.thread_tolerances['внешняя'])

    def edit_dopusk_rezba_on_in(self):
        self.ui.page_tokarnaya_rezba.edit_list_dopusk(self.model.thread_tolerances['внутренняя'])

    def show_all_rezb_for_diameter(self, value):
        steps = self.model.metric_thread_pitches[value]
        self.ui.page_tokarnaya_rezba.add_list_step(steps=steps)

    def delete_row(self, r):
        item = self.model.operations[r]['описание']
        if self.model.operations[r]['инструмент'].text() != '':
            item_instrument = self.model.operations[r]['инструмент'].text()
            self.model.find_and_delete_from_all_instrument(item_instrument.split('\n'))
        row_index = self.ui.page_tokarnaya.get_index_row(item)
        self.ui.page_tokarnaya.delete_row(row_index)
        del self.model.operations[r]

    def show_dialog_exit(self):
        if len(self.model.operations) > 0:
            print(self.model.operations)
            self.dialog = ExitDialog()
            self.dialog.show()
            self.dialog.accepted.connect(self.button_exit)
        else:
            self.exit_to_main_menu_requested.emit()

    def button_exit(self):
        self.ui.page_tokarnaya.clear_table()
        self.exit_to_main_menu_requested.emit()