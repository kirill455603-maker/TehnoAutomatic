

from controllers.base_controller import BaseOperationController
from dialogs.dialog_normirovanie_markirovanie import DialogMarkirovanie
from logic.normirovanie_logic import NormirovanieLogic
from ui_autoinput import Ui_MainWindow
from views.widgets.widgets_normirovanie.w_normirovanie_cutting import Cutting
from views.widgets.widgets_normirovanie.w_normirovanie_turning_button import TurningButton
from views.widgets.widgets_normirovanie.w_normirovanie_turning import Turning
from dialogs.dialog_normirovanie_select_turning_operation import SelectTurningOperation
from views.widgets.widgets_normirovanie.w_normirovanie_turning_kanavka import TurningKanavka
from views.widgets.widgets_normirovanie.w_normirovanie_turning_podrezka import TurningPodrezka
from views.widgets.widgets_normirovanie.w_normirovanie_sverlilnaya import Sverlilnaya
from views.widgets.widgets_normirovanie.w_normirovanie_shlifovka import Shlifovka

class NormirovanieController(BaseOperationController):
    def __init__(self, ui, parent=None):
        super().__init__(ui, NormirovanieLogic(), parent)
        self.ui:Ui_MainWindow = ui
        self.model:NormirovanieLogic = NormirovanieLogic()
        self.markirovanie = DialogMarkirovanie()
        self.select_turning = SelectTurningOperation()

        self.widgets = []



        self.ui.page_normirovanie.btn_home_clicked.connect(self._go_to_main_page)
        self.ui.page_normirovanie.editing_combobox.connect(self._add_widgets)
        self.ui.page_normirovanie.btn_result_clicked.connect(self._get_value_widgets)
        self.ui.page_normirovanie.btn_show_operations_clicked.connect(self._add_find_operation_tehno_pro)

        self.select_turning.ui.pushButton_show_btn_operations.clicked.connect(self._add_turning_operation)
        self.select_turning.ui.pushButton_show_btn_operations_2.clicked.connect(
            lambda: self.select_turning.close()
        )

        self.select_turning.add_material(self.model.rezhimi)


#Добавляем виджет при смене
    def _add_widgets(self):
        self.ui.page_normirovanie.ui.plainTextEdit_log.hide()
        operation = self.ui.page_normirovanie.get_value()[1]
        self.widgets.clear()
        widget = None
        if 'отрезная' in operation.lower():
            widget = Cutting('отрезная')
            widget.add_material(self.model.rezhimi)
            self.ui.page_normirovanie.add_widgets(widget)
        elif 'токарная' in operation.lower() or 'токарно' in operation.lower():
            widget = TurningButton('токарная')
            self.ui.page_normirovanie.add_widgets(widget)
            widget.ui.pushButton_add_operation_turning.clicked.connect(
                lambda: self.select_turning.show()
            )
        elif 'сверлильная' in operation.lower():
            #Добавляем слой, куда будем добавлять сверловку отверстий
            widget = TurningButton('сверлильная')
            widget.edit_btn_text('сверлильную')
            widget.ui.pushButton_add_operation_turning.clicked.connect(self._add_sverlenie_operation)
            self.ui.page_normirovanie.add_widgets(widget)
        elif 'шлифовальная' in operation.lower():
            widget = TurningButton('шлифовальная')
            widget.edit_btn_text('шлифовальную')
            widget.ui.pushButton_add_operation_turning.clicked.connect(self._add_shlifovka_operation)
            self.ui.page_normirovanie.add_widgets(widget)
        self.widgets.append(widget)
        if self.widgets:
            self.ui.page_normirovanie.ui.plainTextEdit_log.show()
            self.ui.page_normirovanie.add_log(f'Выбрана операция: {operation.lower()}')

#Добавление токарных обработок здесь
    def _add_turning_operation(self):
        if not self.select_turning.material:
            self.select_turning.show_error(
                '❌ Ошибка: Материал не выбран'
            )
            return
        operation = self.select_turning.operation.lower()
        material = self.select_turning.material
        widget = None
        if 'точение' in operation:
            widget = Turning()
        elif 'канавок' in operation:
            widget = TurningKanavka()
        elif 'подрезка' in operation:
            widget = TurningPodrezka()
        widget.edit_type_material(material)
        widget.ui.pushButton_delete_operation.clicked.connect(
            lambda: self._on_clicked_delete_operation(widget)
        )
        self.widgets[0].add_widget_in_layout(widget)
        self.select_turning.close()
        self.select_turning.show_error('')
        self.ui.page_normirovanie.auto_scroll_down()

#Добавление сверльной операции (виджет) в слой
    def _add_sverlenie_operation(self):
        widget = Sverlilnaya(self.model.rezhimi)
        widget.ui.pushButton_delete_operation.clicked.connect(
            lambda: self._on_clicked_delete_operation(widget)
        )
        self.widgets[0].add_widget_in_layout(widget)
        self.ui.page_normirovanie.auto_scroll_down()

# Добавление шлифовальной операции (виджет) в слой
    def _add_shlifovka_operation(self):
        widget = Shlifovka(self.model.rezhimi)
        widget.ui.pushButton_delete_operation.clicked.connect(
            lambda: self._on_clicked_delete_operation(widget)
        )
        self.widgets[0].add_widget_in_layout(widget)
        self.ui.page_normirovanie.auto_scroll_down()

    def _on_clicked_delete_operation(self, widget):
        self.widgets[0].delete_widget(widget)


#Выводим результат в таблицу от сюда
    def _get_value_widgets(self):
        detail, operation = self.ui.page_normirovanie.get_value()
        if not detail:
            self.ui.page_normirovanie.show_text(
                '❌ Ошибка: Вы не выбрали деталь для расчета'
            )
            return
        if not operation:
            self.ui.page_normirovanie.show_text(
                '❌ Ошибка: Вы не выбрали операцию для расчета'
            )
            return
        operation = self.ui.page_normirovanie.get_value()[1]
        time = None
        if 'отрезная' in operation.lower():
            time = self._calculation_cutting()
            if time:
                msg = self._save_result(time)
                self.ui.page_normirovanie.show_text(msg)
        elif 'токарная' in operation.lower() or 'токарно' in operation.lower():
            time = self._calculation_turning()
            if time:
                msg = self._save_result(time)
                self.ui.page_normirovanie.show_text(msg)
        elif 'сверлильная' in operation.lower():
            time = self._calculation_sverlilnaya()
            if time:
                msg = self._save_result(time)
                self.ui.page_normirovanie.show_text(msg)
        elif 'шлифовальная' in operation.lower():
            time = self._calculation_shlifovka()
            if time:
                msg = self._save_result(time)
                self.ui.page_normirovanie.show_text(msg)
        else:
            self.ui.page_normirovanie.show_text(
                '❌ Ошибка: Данная операция еще не настроенна на расчет времени'
            )
            return
        if time:
            self.ui.page_normirovanie.add_log(
                f'Время: {time} мин. | Деталь: {detail} | Операция: {operation} | Запись: Успешно'
            )
#Отрезная
    def _calculation_cutting(self):
        params = self.widgets[0].get_params()
        if not params['материал']:
            self.ui.page_normirovanie.show_text(
                '❌ Ошибка: Вы не выбрали материал для расчета'
            )
            return None
        if not params['диаметр']:
            self.ui.page_normirovanie.show_text(
                '❌ Ошибка: Вы не указали диаметр для расчета'
            )
            return None
        self.ui.page_normirovanie.show_text('')
        time = self.model.cutting(params)
        return time

#Токарное точение
    def _calculation_turning(self):
        count = 0
        count_isTrue = 0
        widgets_list = self.widgets[0].widgets_list
        if not widgets_list:
            self.ui.page_normirovanie.show_text(
                '❌ Ошибка: Вы не добавили ни одной токарной операции для расчета'
            )
            return None
        for widget in widgets_list:
            time = None
            # Точение
            if widget.operation_name == 'точение':
                params = widget.get_value()
                if params['длина'] == 0:
                    widget.show_label_info(
                        '❌ Ошибка: Необходимо указать длину для расчета'
                    )
                    widget.edit_style_error()
                    continue
                if params['диаметр заготовки'] == 0 or params['диаметр заготовки'] < params['диаметр детали']:
                    widget.show_label_info(
                        '❌ Ошибка: Диаметр заготовки не может быть равен 0 или меньше диаметра детали'
                    )
                    widget.edit_style_error()
                    continue
                if params['глубина'] == 0:
                    widget.show_label_info(
                        '❌ Ошибка: Глубина резания не может быть равна 0'
                    )
                    widget.edit_style_error()
                    continue
                time = self.model.turnining_prodolnoe(d=params, material=self.select_turning.material)
            # Канавка
            elif widget.operation_name == 'канавка':
                params = widget.get_value()
                if params['глубина'] == 0:
                    widget.show_label_info(
                        '❌ Ошибка: Глубина канавки не может быть равна 0'
                    )
                    widget.edit_style_error()
                    continue
                if params['ширина'] == 0:
                    widget.show_label_info(
                        '❌ Ошибка: Ширина канавки не может быть равна 0'
                    )
                    widget.edit_style_error()
                    continue
                if params['резец'] == 0:
                    widget.show_label_info(
                        '❌ Ошибка: Ширина резца не может быть равна 0'
                    )
                    widget.edit_style_error()
                    continue
                if params['резец'] > params['ширина']:
                    widget.show_label_info(
                        '❌ Ошибка: Ширина резца БОЛЬШЕ ширина канавки'
                    )
                    widget.edit_style_error()
                    continue
                time = self.model.turning_kanavka(d=params, material=self.select_turning.material)
            elif widget.operation_name == 'подрезка':
                params = widget.get_value()
                if params['диаметр начальный'] == 0:
                    widget.show_label_info(
                        '❌ Ошибка: Начальный диаметр не может быть равен 0'
                    )
                    widget.edit_style_error()
                    continue
                if params['диаметр конечный'] > params['диаметр начальный']:
                    widget.show_label_info(
                        '❌ Ошибка: Конечный диаметр не может быть больше начального'
                    )
                    widget.edit_style_error()
                    continue
                time = self.model.turning_podrezka(d=params, material=self.select_turning.material)

            # Для всех виджетов
            count_isTrue += 1
            count += time
            widget.show_label_info(
                f'⏳ Время обработки: {time} мин.'
            )
            widget.edit_style_apply()
        if count_isTrue != len(widgets_list):
            self.ui.page_normirovanie.show_text(
                f'❌ Ошибка: Результат не был записан в файл! Проверьте заполненные данные!'
            )
            return None
        else:
            return count

    def _calculation_sverlilnaya(self):
        count = 0
        count_isTrue = 0
        widgets_list = self.widgets[0].widgets_list
        if not widgets_list:
            self.ui.page_normirovanie.show_text(
                '❌ Ошибка: Вы не добавили ни одной сверлильной операции для расчета'
            )
            return None
        for widget in widgets_list:
            params = widget.get_value()
            if params['длина'] == 0:
                widget.show_label_info(
                    '❌ Ошибка: Глубина отверстия не может быть равна 0'
                )
                widget.edit_style_error()
                continue
            if params['диаметр'] == 0:
                widget.show_label_info(
                    '❌ Ошибка: Диаметр сверла не может быть равен 0'
                )
                widget.edit_style_error()
                continue
            if params['длина'] == 0:
                widget.show_label_info(
                    '❌ Ошибка: Глубина резания не может быть равна 0'
                )
                widget.edit_style_error()
                continue
            if not params['материал']:
                widget.show_label_info(
                    '❌ Ошибка: Необходимо выбрать материал'
                )
                widget.edit_style_error()
                continue
            time = self.model.sverlenie(d=params)
            count_isTrue += 1
            count += time
            widget.show_label_info(
                f'⏳ Время обработки: {time} мин.'
            )
            widget.edit_style_apply()
        if count_isTrue != len(widgets_list):
            self.ui.page_normirovanie.show_text(
                f'❌ Ошибка: Результат не был записан в файл! Проверьте заполненные данные!'
            )
            return None
        else:
            return count

    def _calculation_shlifovka(self):
        count = 0
        count_isTrue = 0
        widgets_list = self.widgets[0].widgets_list
        if not widgets_list:
            self.ui.page_normirovanie.show_text(
                '❌ Ошибка: Вы не добавили ни одной шлифовальной операции для расчета'
            )
            return None
        for widget in widgets_list:
            params = widget.get_value()
            if params['длина'] == 0:
                widget.show_label_info(
                    '❌ Ошибка: Длина обработки не может быть равна 0'
                )
                widget.edit_style_error()
                continue
            if params['диаметр'] == 0:
                widget.show_label_info(
                    '❌ Ошибка: Диаметр поверхности обработки не может быть равен 0'
                )
                widget.edit_style_error()
                continue
            if params['припуск'] == 0:
                widget.show_label_info(
                    '❌ Ошибка: Припуск не может быть равен 0'
                )
                widget.edit_style_error()
                continue
            if not params['материал']:
                widget.show_label_info(
                    '❌ Ошибка: Необходимо выбрать материал'
                )
                widget.edit_style_error()
                continue
            time = self.model.shlifovka(d=params)
            count_isTrue += 1
            count += time
            widget.show_label_info(
                f'⏳ Время обработки: {time} мин.'
            )
            widget.edit_style_apply()
        if count_isTrue != len(widgets_list):
            self.ui.page_normirovanie.show_text(
                f'❌ Ошибка: Результат не был записан в файл! Проверьте заполненные данные!'
            )
            return None
        else:
            return count

    def _save_result(self, time):
        row, col = self.ui.page_normirovanie.get_row_and_col()
        if row is None:
            return f'❌ Ошибка: Деталь не найдена в файле'
        if col is None:
            return '❌ Ошибка: Операция не найдена в файле'
        col_letter = self._convert_col_in_letter(col)
        self.ui.page_normirovanie.save_result_in_excel(row, col, time)
        return f'⏳ Время: {time} мин. ✅ Результат записан в ячейку [{row}:{col_letter}]!'

    def _convert_col_in_letter(self, col):
        num_a = ord('A')
        num_col = num_a + col - 1
        if num_col > ord('Z'):
            letter = f'A{chr(num_col)}'
        elif num_col > ord('A') + ord('Z'):
            letter = f'B{chr(num_col)}'
        else:
            letter = chr(num_col)
        return letter

    def _add_find_operation_tehno_pro(self):
        count = 1
        for operation in self.model.operations_tehno:
            is_watch = self.model.find_operations(operation['кнопка'])
            if (not is_watch
                    or operation['операция'].lower() == 'входной контроль'
                    or operation['операция'].lower() == 'перемещение'
            ):
                continue
            else:
                self.ui.page_normirovanie.add_button_in_layout(num=count, text=operation['операция'])
                count += 1

    def show_markirovanie(self):
        self.markirovanie.show()

    def get_operation_name(self) -> str:
        return 'Нормирование'

    def get_target_page(self):
        return self.ui.page_normirovanie

    def go_to_main_page(self):
        self.ui.stackedWidget.setCurrentIndex(15)

    def _go_to_main_page(self):
        self.exit_to_main_menu_requested.emit()





