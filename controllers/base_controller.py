# controllers/base_controller.py
import time
from PySide6.QtCore import QObject, Signal, Qt
from PySide6.QtWidgets import QTableWidgetItem
from dialogs.exit_dialog import ExitDialog


class BaseOperationController(QObject):
    """Базовый класс для всех контроллеров операций."""
    exit_to_main_menu_requested = Signal()

    def __init__(self, ui, model, automation, parent=None):
        super().__init__(parent)
        self.ui = ui
        self.model = model
        self.automation = automation

    # ================= АБСТРАКТНЫЕ МЕТОДЫ =================
    # Должны быть переопределены в наследниках

    def get_operation_name(self) -> str:
        """Название операции для Technopro."""
        raise NotImplementedError

    def get_target_page(self):
        """Возвращает страницу-таблицу этой операции."""
        raise NotImplementedError

    def clear_all(self):
        """Очистка всех данных операции."""
        raise NotImplementedError

    def _connect_signals(self):
        """Подключение сигналов. Переопределяется в наследниках."""
        raise NotImplementedError

    # ================= ОБЩИЕ МЕТОДЫ =================

    def _process_and_save_result(self, result: dict) -> str:
        """
        Универсальный метод сохранения операции.
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

    def go_to_technopro(self):
        """Переход на страницу Technopro."""
        count = self.model.take_value_matches()
        if count > 0:
            self.ui.page_input_technopro.add_item_table(
                count=count,
                operation=self.get_operation_name()
            )
        else:
            self.ui.page_input_technopro.show_error(self.get_operation_name())
        self.ui.stackedWidget.setCurrentIndex(6)

    def process_technopro_start(self, value, result_clear):
        """Общий метод для запуска из Technopro."""
        if len(self.model.operations) == 0:
            self.ui.page_input_technopro.error_start('Ошибка: у вас нет операций для заполнения')
            return
        if value == -1:
            self.ui.page_input_technopro.error_start('Ошибка: вы не выбрали операцию!')
            return

        self.model.index = value
        self.automation.start(
            operations=self.model.operations,
            index=value,
            image_find=self.model.image
        )


        time.sleep(1)
        if result_clear == 'стереть':
            self.clear_all()
        self.ui.page_input_technopro.error_start('Заполнение завершено!')

