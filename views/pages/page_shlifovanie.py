from ui_page_shlifovanie import Ui_Shlifovanie #Поменять на свою
from PySide6.QtCore import Signal, Qt
from PySide6.QtGui import QCursor
from PySide6.QtWidgets import QWidget, QHeaderView, QPushButton, QTableWidgetItem, QHBoxLayout
class PageShlifovanie(QWidget): #Назвать свой класс
    btn_click_delete = Signal(int)
    btn_home_clicked = Signal()
    btn_save_and_export = Signal()
    btn_start = Signal()
    btn_poverh = Signal()
    btn_clear_table_clicked = Signal()
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Shlifovanie()
        self.ui.setupUi(self)
        self._connect_buttons()

        # Принудительно сбрасываем все фиксированные настройки вертикального заголовка
        self.ui.table_widget.verticalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.ui.table_widget.horizontalHeader().setSectionResizeMode(0, QHeaderView.Fixed)
        self.ui.table_widget.horizontalHeader().setSectionResizeMode(1, QHeaderView.Fixed)
        self.ui.table_widget.horizontalHeader().setSectionResizeMode(2, QHeaderView.Stretch)
        self.ui.table_widget.horizontalHeader().resizeSection(0, 400)
        self.ui.table_widget.horizontalHeader().resizeSection(1, 600)
        self.ui.table_widget.setWordWrap(True)

        # ВАЖНО: храним ссылки на кнопки, чтобы сборщик мусора их не удалил
        self._delete_buttons = []


    def _connect_buttons(self):
        self.ui.btn_start_obrabotki.clicked.connect(
            lambda: self.btn_start.emit()
        )
        self.ui.btn_shlifovka_poverh.clicked.connect(
            lambda: self.btn_poverh.emit()
        )
        self.ui.btn_home.clicked.connect(self._on_button_home_clicked)
        self.ui.btn_save_and_export.clicked.connect(self._on_button_save_and_export_clicked)
        self.ui.btn_clear_table.clicked.connect(self._on_button_clear_table)

    def _on_button_save_and_export_clicked(self):
        self.btn_save_and_export.emit()

    def _on_button_home_clicked(self):
        self.btn_home_clicked.emit()

    def _on_button_clear_table(self):
        print("Нажал")
        self.btn_clear_table_clicked.emit()

    def add_row(self):
        if self.ui.table_widget.item(self.ui.table_widget.rowCount() - 1, 0):
            self.ui.table_widget.setRowCount(self.ui.table_widget.rowCount() + 1)

    # ================= УНИВЕРСАЛЬНЫЙ МЕТОД =================
    # Этот метод вызывается базовым контроллером через get_target_page()
    def show_result(self, text, instrument, key_count):
        """Добавляет новую строку в таблицу."""
        self.ui.table_widget.setRowCount(self.ui.table_widget.rowCount() + 1)
        row = self.ui.table_widget.rowCount() - 1

        self.ui.table_widget.setItem(row, 1, text)
        self.ui.table_widget.setItem(row, 0, instrument)

        btn_delete = QPushButton()
        btn_delete.resize(50,50)
        btn_delete.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        con = QWidget()
        con.setFixedSize(50, 130)
        layout = QHBoxLayout(con)
        layout.setAlignment(Qt.AlignCenter)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(btn_delete)
        btn_delete.clicked.connect(lambda checked, r=key_count: self.on_delete_clicked(r))

        # ВАЖНО: сохраняем ссылку на кнопку
        self._delete_buttons.append(btn_delete)
        self.ui.table_widget.setCellWidget(row, 2, con)

    # Старый метод для обратной совместимости (можно удалить, если не используется)
    def add_item_in_table_widget(self, item_about, item_instrument, num: int):
        self.show_result(text=item_about, instrument=item_instrument, key_count=num)

    def clear_table(self):
        print('Очистка')
        self.ui.table_widget.clear()
        self.ui.table_widget.setHorizontalHeaderLabels(['Инструмент', 'Описание [Можно изменять]', ''])
        self.ui.table_widget.setRowCount(0)
        self._delete_buttons.clear()  # Очищаем список кнопок

    def on_delete_clicked(self, r):
        self.btn_click_delete.emit(r)

    def delete_row(self, r):
        self.ui.table_widget.removeRow(r)

    def get_index_row(self, item):
        return self.ui.table_widget.row(item)