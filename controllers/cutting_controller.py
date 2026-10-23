from ui_autoinput import Ui_MainWindow
from views.pages.page_shlifovanie import PageShlifovanie
from controllers.base_controller import BaseOperationController
from logic.operation_shlifovanie import OperationShlifovanie
from logic.automation import TechnoproAutomation

class ShlifovanieController(BaseOperationController):
    def __init__(self, ui, parent=None):
        super().__init__(ui, OperationShlifovanie(), TechnoproAutomation(), parent)
        self.ui:Ui_MainWindow = ui
        self.model:OperationShlifovanie = OperationShlifovanie()
        self._home_page_index = 18
        self.automation:TechnoproAutomation = TechnoproAutomation()
        self._connect_signals()

        self.ui.page_shlifovanie.btn_home_clicked.connect(self._go_to_main_page)
        self.ui.page_shlifovanie.btn_save_and_export.connect(self.go_to_technopro)

    def _connect_signals(self):
        #Установка детали шлифовки
        self.ui.page_shlifovanie.btn_start.connect(
            lambda: self.ui.stackedWidget.setCurrentIndex(19)
        )
        self.ui.page_shlifovanie_start.btn_save.connect(self._save_result_start)
        self.ui.page_shlifovanie_osnovnoe.btn_save.connect(self._save_result_osnovnoe)
        self.ui.page_shlifovanie_start.btn_home.connect(
            lambda: self.ui.stackedWidget.setCurrentIndex(self._home_page_index)
        )
        self.ui.page_shlifovanie.btn_poverh.connect(
            lambda: self.ui.stackedWidget.setCurrentIndex(20)
        )
        self.ui.page_shlifovanie_osnovnoe.btn_home.connect(
            lambda: self.ui.stackedWidget.setCurrentIndex(self._home_page_index)
        )
        self.ui.page_shlifovanie.btn_click_delete.connect(self.delete_row)
        self.ui.page_shlifovanie.btn_clear_table_clicked.connect(self.clear_all)

    def clear_all(self):
        """Очистка всех данных операции."""
        self.model.count = 0
        self.model.clear_all()
        self.model.all_instrument.clear()
        self.ui.page_shlifovanie.clear_table()

    def get_operation_name(self) -> str:
        return 'Шлифовальная'

    def get_target_page(self):
        return self.ui.page_shlifovanie

    def go_to_main_page(self):
        self.ui.stackedWidget.setCurrentIndex(18)

    def _go_to_main_page(self):
        self.exit_to_main_menu_requested.emit()

    def delete_row(self, r):
        item = self.model.operations[r]['описание']
        if self.model.operations[r]['инструмент'].text() != '':
            item_instrument = self.model.operations[r]['инструмент'].text()
            self.model.find_and_delete_from_all_instrument(item_instrument.split('\n'))
        row_index = self.ui.page_shlifovanie.get_index_row(item)
        self.ui.page_shlifovanie.delete_row(row_index)
        del self.model.operations[r]
