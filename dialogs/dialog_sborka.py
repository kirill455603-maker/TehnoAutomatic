from ui_dialog_sborka import Ui_DialogSborka
from PySide6.QtWidgets import QDialog, QLabel, QHBoxLayout, QSpacerItem, QSizePolicy
from PySide6.QtCore import Qt, Signal
from views.widgets.widget_predlogs import WidgetPredlogs
from views.widgets.widget_details import WidgetDetails
from views.widgets.widget_deistvie import WidgetDeistvie
from views.widgets.widget_row import WidgetRow
from views.widgets.widget_bolts import WidgetBolts


class DialogSborka(QDialog):
    btn_save_clicked = Signal(dict)

    def __init__(self, details, deistviya, metrick_rezba, parent=None):
        super().__init__(parent)
        self.ui = Ui_DialogSborka()
        self.ui.setupUi(self)
        self.list_all_widgets = []
        self.list_rows = []
        self.count_rows = 0
        self.count_column = 0
        self.details = details
        self.deistviya = deistviya
        self.metric_rezba = metrick_rezba
        self.count_predlogs = 0
        self.count_deistvie = 0
        self.in_key = False
        self.type_padeg = 'винительный'  # Задаем дефолтное значение

        self.ui.pushButton_add_predlog.clicked.connect(
            lambda: self._add_el(self.ui.pushButton_add_predlog.text())
        )
        self.ui.pushButton_add_detail.clicked.connect(
            lambda: self._add_el(self.ui.pushButton_add_detail.text())
        )
        self.ui.pushButton_add_deistvie.clicked.connect(
            lambda: self._add_el(self.ui.pushButton_add_deistvie.text())
        )
        self.ui.pushButton_add_bolts.clicked.connect(
            lambda: self._add_el(self.ui.pushButton_add_bolts.text())
        )

        self.ui.btn_delete_el.clicked.connect(self._remove_last_el)
        self.ui.pushButton_save_result.clicked.connect(self._btn_save_clicked)

    def _btn_save_clicked(self):
        d = {'текст': self.ui.label_text_input.text()}
        self.btn_save_clicked.emit(d)

    def _get_padeg(self, predlog_text):
        """Вспомогательный метод для определения падежа по предлогу"""
        predlog = predlog_text.lower()
        if predlog in ['в', 'на']:
            return 'винительный'
        elif predlog in ['под', 'над']:
            return 'творительный'
        elif predlog in ['c']:
            return 'родительный'
        return 'винительный'

    def _remove_last_el(self):
        """Удаляет последний добавленный элемент"""
        if not self.list_all_widgets:
            return

        last_widget = None
        while self.list_all_widgets:
            item = self.list_all_widgets[-1]
            if item == ', ':
                self.list_all_widgets.pop()
                continue
            last_widget = item
            self.list_all_widgets.pop()
            break

        if last_widget is None:
            return

        current_row = self.list_rows[-1]
        current_row.row().removeWidget(last_widget)
        last_widget.setParent(None)
        last_widget.deleteLater()

        self.count_column -= 1

        if isinstance(last_widget, WidgetPredlogs):
            self.count_predlogs -= 1

        if self.count_column == 0 and len(self.list_rows) > 1:
            self.list_rows.pop()
            current_row.setParent(None)
            current_row.deleteLater()
            self.count_rows -= 1
            if self.list_rows:
                prev_row = self.list_rows[-1]
                self.count_column = prev_row.row().count()

        self.update_text_export()

    def _add_el(self, text):
        self.control_rows_and_columns()
        widget = None

        if 'предлог' in text:
            widget = WidgetPredlogs()
            if self.count_predlogs == 1 or self.list_all_widgets:
                widget.resize_title()
            self.count_predlogs += 1

            # Используем вспомогательный метод
            self.type_padeg = self._get_padeg(widget.text())

            widget.edit_combobox.connect(
                lambda w=widget: self.edit_type_details(w)
            )
            widget.edit_combobox.connect(self.update_text_export)

        elif 'деталь' in text:
            widget = WidgetDetails()
            # Передаем текущий падеж
            widget.set_padeg(self.type_padeg, self.details)
            widget.edit_position.connect(self.update_text_export)
            widget.edit_combo_box.connect(self.update_text_export)

        elif 'действие' in text:
            widget = WidgetDeistvie()
            widget.add_text_in_combo_box(self.deistviya)
            if self.list_all_widgets:
                widget.resize_title()
            widget.edit_combobox.connect(self.update_text_export)

        elif 'болт' in text:
            widget = WidgetBolts()
            widget.metrick_rezba = self.metric_rezba
            widget.add_in_rezba()

            widget.edit_rezba.connect(self.update_text_export)
            widget.edit_s.connect(self.update_text_export)
            widget.edit_spinbox.connect(self.update_text_export)
            widget.edit_type.connect(self.update_text_export)
            widget.edit_position.connect(self.update_text_export)

        if self.list_all_widgets and self.list_all_widgets[-1].name() == 'Деталь' and widget.name() == 'Деталь':
            self.list_all_widgets.append(', ')

        self.list_all_widgets.append(widget)
        self.list_rows[-1].row().addWidget(widget)
        self.count_column += 1
        self.update_text_export()

    def edit_type_details(self, widget):
        """Обновляет падеж только у детали, идущей непосредственно после данного предлога"""
        # 1. Определяем новый падеж
        self.type_padeg = self._get_padeg(widget.text())

        # 2. Находим индекс этого предлога в общем списке
        try:
            predlog_index = self.list_all_widgets.index(widget)
        except ValueError:
            return

        # 3. Ищем ПЕРВУЮ деталь после предлога (пропуская запятые)
        for i in range(predlog_index + 1, len(self.list_all_widgets)):
            next_widget = self.list_all_widgets[i]

            # Пропускаем запятые
            if next_widget == ', ':
                continue

            # Если нашли деталь — обновляем её падеж и выходим
            if next_widget.name() == 'Деталь':
                next_widget.set_padeg(self.type_padeg, self.details)
                break

            # Если встретили что-то другое (предлог, действие, болт) —
            # значит детали после этого предлога нет, выходим
            break

    def update_text_export(self):
        text_export = ''
        for widget in self.list_all_widgets:
            if widget == ', ':
                text_export += ', '
                continue
            text_export += widget.text()
            text_export += ' '
        self.ui.label_text_input.setText(text_export)

    def control_rows_and_columns(self):
        if self.count_column == 3 or len(self.list_rows) == 0:
            self.count_rows += 1
            row = WidgetRow()
            self.list_rows.append(row)
            self.ui.verticalLayout_2.addWidget(row)
            self.count_column = 0