from PySide6.QtWidgets import QWidget
from ui_widget_normirovanie_turning_button import Ui_WidgetTurningButton

class TurningButton(QWidget):
    def __init__(self, name, parent=None):
        super().__init__(parent)
        self.ui = Ui_WidgetTurningButton()
        self.ui.setupUi(self)
        self.name = name

        self.widgets_list = []

    def edit_btn_text(self, text):
        text_btn = self.ui.pushButton_add_operation_turning.text()
        self.ui.pushButton_add_operation_turning.setText(text_btn.replace('токарную', text))


    def add_widget_in_layout(self, widget):
        self.ui.layout_with_turning.addWidget(widget)
        self.widgets_list.append(widget)

    def clear_widgets(self):
        for widget in self.widgets_list:
            widget.setParent(None)
            widget.deleteLater()
        self.widgets_list.clear()

    def delete_widget(self, widget):
        for widget_in_list in self.widgets_list:
            if widget == widget_in_list:
                widget.setParent(None)
                widget.deleteLater()
                index = self.widgets_list.index(widget_in_list)
                print(index)
                self.widgets_list.pop(self.widgets_list.index(widget_in_list))

