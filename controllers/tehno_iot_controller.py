from PySide6.QtWidgets import QTableWidgetItem
from PySide6.QtCore import Qt

from logic.automation import TechnoproAutomation
from controllers.base_controller import BaseOperationController
from ui_autoinput import Ui_MainWindow
from logic.operation_tehno_iot import TehnoIot
import time


class TehnoIotController(BaseOperationController):
    def __init__(self, ui, parent=None):
        super().__init__(ui, TehnoIot(), Ui_MainWindow, parent)
        self.ui: Ui_MainWindow = ui
        self.model_tehno: TehnoIot = TehnoIot()

        self.ui.page_tehno_iot.btn_home_clicked.connect(self._go_to_main_page)
        self.ui.page_tehno_iot.btn_start_clicked.connect(self._go_to_start_input)
        self.ui.page_tehno_iot.btn_update_clicked.connect(self.go_to_main_page)

    def get_target_page(self):
        return self.ui.page_tehno_iot

    def go_to_main_page(self):
        self.ui.page_tehno_iot.clear_table_tehno()
        self.update_window()
        self.ui.stackedWidget.setCurrentIndex(13)

    def _go_to_main_page(self):
        self.exit_to_main_menu_requested.emit()

    def _go_to_start_input(self):
        result = self.ui.page_tehno_iot.get_result()
        self.model_tehno.start(result[0], result[1], status=self.ui.page_tehno_iot.status_del_instrument())

    def update_window(self):
        data = self.model_tehno.find_operation()
        if data:
            self.ui.page_tehno_iot.show_main()
            for item in data:
                item_operation = QTableWidgetItem(item['описание'])
                item_iot = QTableWidgetItem(item['иот']['текст_иот'])
                item_operation.setFlags(Qt.ItemFlag.ItemIsSelectable | Qt.ItemFlag.ItemIsEnabled)
                item_operation.setCheckState(Qt.Checked)
                item_operation.setFlags(Qt.ItemFlag.ItemIsUserCheckable | Qt.ItemFlag.ItemIsEnabled | Qt.ItemFlag.ItemIsSelectable)
                item_iot.setFlags(Qt.ItemFlag.ItemIsSelectable | Qt.ItemFlag.ItemIsEnabled)
                self.ui.page_tehno_iot.add_items_tehno(operation=item_operation,iot=item_iot, instruments=item['оборудование'])
        else:
            self.ui.page_tehno_iot.hide_main()
            self.ui.page_tehno_iot.show_msg(text='Операции не были найдены!',
                                            text_2='Убедитесь, что программа ТехноПро в зоне видимости и нажмите кнопку "обновить страницу"')




