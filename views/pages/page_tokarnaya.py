# pages/page_tokarnaya.py
from PySide6.QtWidgets import QPushButton, QHeaderView, QWidget, QHBoxLayout
from PySide6.QtCore import Signal, Qt
from PySide6.QtGui import QCursor
from ui_page_tokarnaya import Ui_PageTokarnaya


class PageTokarnaya(QWidget):
    btn_click_delete = Signal(int)
    btn_clear_table_clicked = Signal()
    btn_start_obrabotki_clicked = Signal()
    btn_podrezka_clicked = Signal()
    btn_home_clicked = Signal()
    btn_tochenie_clicked = Signal()
    btn_sverlenie_clicked = Signal()
    btn_save_and_export = Signal()
    btn_rastachivanie_clicked = Signal()
    btn_rezba_clicked = Signal()
    btn_faska_clicked = Signal()
    btn_angle_clicked = Signal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_PageTokarnaya()
        self.ui.setupUi(self)

        self.ui.table_widget_tokarnaya.horizontalHeader().setSectionResizeMode(0, QHeaderView.Fixed)
        self.ui.table_widget_tokarnaya.horizontalHeader().setSectionResizeMode(1, QHeaderView.Fixed)
        self.ui.table_widget_tokarnaya.horizontalHeader().setSectionResizeMode(2, QHeaderView.Stretch)
        self.ui.table_widget_tokarnaya.horizontalHeader().resizeSection(0, 500)
        self.ui.table_widget_tokarnaya.horizontalHeader().resizeSection(1, 500)
        self.ui.table_widget_tokarnaya.horizontalHeader().setStretchLastSection(True)
        self.ui.table_widget_tokarnaya.verticalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)

        # ВАЖНО: храним ссылки на кнопки, чтобы сборщик мусора их не удалил
        self._delete_buttons = []

        self.ui.btn_start_obrabotki.clicked.connect(self._on_button_start_obrabotki_clicked)
        self.ui.btn_podrezka.clicked.connect(self._on_button_podrezka_clicked)
        self.ui.btn_home.clicked.connect(self._on_button_home_clicked)
        self.ui.btn_tochenie.clicked.connect(self._on_button_tochenie_clicked)
        self.ui.btn_sverlenie.clicked.connect(self._on_button_sverlenie_clicked)
        self.ui.btn_save_and_export.clicked.connect(self._on_button_save_and_export)
        self.ui.btn_clear_table.clicked.connect(self._on_button_clear_table)
        self.ui.btn_rastochka.clicked.connect(self._on_button_rastachivanie_clicked)
        self.ui.btn_rezba.clicked.connect(self._on_button_rezba_clicked)
        self.ui.btn_faska.clicked.connect(self._on_button_faska_clicked)
        self.ui.btn_angle.clicked.connect(self._on_button_angle_clicked)

    def _on_button_angle_clicked(self):
        self.btn_angle_clicked.emit()

    def _on_button_faska_clicked(self):
        self.btn_faska_clicked.emit()

    def _on_button_rezba_clicked(self):
        self.btn_rezba_clicked.emit()

    def _on_button_rastachivanie_clicked(self):
        self.btn_rastachivanie_clicked.emit()

    def _on_button_clear_table(self):
        self.btn_clear_table_clicked.emit()

    def _on_button_save_and_export(self):
        self.btn_save_and_export.emit()

    def _on_button_sverlenie_clicked(self):
        self.btn_sverlenie_clicked.emit()

    def _on_button_tochenie_clicked(self):
        self.btn_tochenie_clicked.emit()

    def _on_button_podrezka_clicked(self):
        self.btn_podrezka_clicked.emit()

    def _on_button_home_clicked(self):
        self.btn_home_clicked.emit()

    def _on_button_start_obrabotki_clicked(self):
        self.btn_start_obrabotki_clicked.emit()

    def edit_button_start(self, param: bool):
        self.ui.btn_start_obrabotki.setEnabled(param)

    def add_row(self):
        if self.ui.table_widget_tokarnaya.item(self.ui.table_widget_tokarnaya.rowCount() - 1, 0):
            self.ui.table_widget_tokarnaya.setRowCount(self.ui.table_widget_tokarnaya.rowCount() + 1)

    # ================= УНИВЕРСАЛЬНЫЙ МЕТОД =================
    # Этот метод вызывается базовым контроллером через get_target_page()
    def show_result(self, text, instrument, key_count):
        """Добавляет новую строку в таблицу."""
        self.ui.table_widget_tokarnaya.setRowCount(self.ui.table_widget_tokarnaya.rowCount() + 1)
        row = self.ui.table_widget_tokarnaya.rowCount() - 1

        self.ui.table_widget_tokarnaya.setItem(row, 1, text)
        self.ui.table_widget_tokarnaya.setItem(row, 0, instrument)

        btn_delete = QPushButton()
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

        self.ui.table_widget_tokarnaya.setCellWidget(row, 2, con)

    # Старый метод для обратной совместимости (можно удалить, если не используется)
    def add_item_in_table_widget(self, item_about, item_instrument, num: int):
        self.show_result(text=item_about, instrument=item_instrument, key_count=num)

    def clear_table(self):
        self.ui.table_widget_tokarnaya.clear()
        self.ui.table_widget_tokarnaya.setHorizontalHeaderLabels(['Инструмент', 'Описание [Можно изменять]', ''])
        self.ui.table_widget_tokarnaya.setRowCount(0)
        self._delete_buttons.clear()  # Очищаем список кнопок

    def on_delete_clicked(self, r):
        self.btn_click_delete.emit(r)

    def delete_row(self, r):
        self.ui.table_widget_tokarnaya.removeRow(r)

    def get_index_row(self, item):
        return self.ui.table_widget_tokarnaya.row(item)