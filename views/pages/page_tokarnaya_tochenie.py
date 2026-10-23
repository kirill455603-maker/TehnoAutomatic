from PySide6.QtWidgets import QWidget, QHeaderView
from PySide6.QtCore import Signal
from ui_page_tokarnaya_tochenie import Ui_PageTokarnayaTochenie

class PageTokarnayaTochenie(QWidget):
    btn_home_tochenie_clicked = Signal()
    btn_save_result_clicked = Signal(dict)
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_PageTokarnayaTochenie()
        self.ui.setupUi(self)

        self.connect_signals()

        self.ui.table_widget.horizontalHeader().setSectionResizeMode(0, QHeaderView.Fixed)
        self.ui.table_widget.horizontalHeader().setSectionResizeMode(1, QHeaderView.Stretch)
        self.ui.table_widget.horizontalHeader().resizeSection(0, 400)
        self.ui.table_widget.horizontalHeader().setStretchLastSection(True)
        self.ui.table_widget.setRowCount(1)

    def connect_signals(self):
        self.ui.btn_home.clicked.connect(self._on_button_home_clicked)
        self.ui.btn_save.clicked.connect(self._save_result)
        self.ui.cancel_surf_rad.clicked.connect(
            lambda: self._cancel_surfs(self.ui.l_surfs_rad)
        )
        self.ui.cancel_surf_tor.clicked.connect(
            lambda: self._cancel_surfs(self.ui.l_surfs_tor)
        )

    def set_show_error_tochenie(self, text):
        self.ui.text_error_tochenie.setText(text)


    def _save_result(self):
        my_dict = {'диаметр': self.ui.value_diameter.value(),
                   'квалитет_д': self.ui.kvalitet_diameter.text(),
                   'допуск_д_1': self.ui.dopusk_diameter_1.value(),
                   'допуск_д_2': self.ui.dopusk_diameter_2.value(),
                   'длина': self.ui.value_length.value(),
                   'квалитет_дл': self.ui.kvalitet_length.text(),
                   'допуск_дл_1': self.ui.dopusk_length_1.value(),
                   'допуск_дл_2': self.ui.dopusk_length_2.value(),
                   'шероховатость': None,
                   'шероховатость_торцевая': None,
                   'биение_радиальное': self.ui.bienie_rad.value(),
                   'база_радиальная': self.ui.baza_rad.text(),
                   'биение_торцевое': self.ui.bienie_tor.value(),
                   'база_торцевая': self.ui.baza_tor.text()
                   }
        if self.ui.kvalitet_diameter.text():
            my_dict['квалитет_д'] = self.ui.kvalitet_diameter.text()
        else:
            my_dict['квалитет_д'] = 0
        if self.ui.kvalitet_length.text():
            my_dict['квалитет_дл'] = self.ui.kvalitet_length.text()
        else:
            my_dict['квалитет_дл'] = 0
        if self.ui.radioButton_ra1.isChecked():
            surf = 0.8
        elif self.ui.radioButton_ra2.isChecked():
            surf = 1.6
        elif self.ui.radioButton_ra3.isChecked():
            surf = 3.2
        elif self.ui.radioButton_ra4.isChecked():
            surf = 6.3
        elif self.ui.radioButton_ra5.isChecked():
            surf = 12.5
        else:
            surf = 0
        if self.ui.radioButton_ra1_2.isChecked():
            surf_tor = 0.8
        elif self.ui.radioButton_ra2_2.isChecked():
            surf_tor = 1.6
        elif self.ui.radioButton_ra3_2.isChecked():
            surf_tor = 3.2
        elif self.ui.radioButton_ra4_2.isChecked():
            surf_tor = 6.3
        elif self.ui.radioButton_ra5_2.isChecked():
            surf_tor = 12.5
        else:
            surf_tor = 0
        my_dict['шероховатость'] = surf
        my_dict['шероховатость_торцевая'] = surf_tor

        self.btn_save_result_clicked.emit(my_dict)

    def _on_button_home_clicked(self):
        self._clear_all()
        self.btn_home_tochenie_clicked.emit()

    def set_show_error(self, text):
        self.ui.text_error_tochenie.setText(text)

    def show_result(self, text, instrument):
        self.ui.table_widget.setItem(0, 0, instrument)
        self.ui.table_widget.setItem(0, 1, text)

    def _clear_all(self):
        pass

    def _cancel_surfs(self, layout):
        buttons = []
        for i in range(layout.count()):
            item = layout.itemAt(i)
            widget = item.widget()
            buttons.append(widget)

        for button in buttons:
            button.setAutoExclusive(False)

        for button in buttons:
            button.setChecked(False)

        for button in buttons:
            button.setAutoExclusive(True)



