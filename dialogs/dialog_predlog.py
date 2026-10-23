from ui_dialog_predlog import Ui_DialogPredlog
from PySide6.QtWidgets import QDialog
from logic.logic_predlog import LogicPredlog

class DialogPredlog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_DialogPredlog()
        self.ui.setupUi(self)
        self.model = LogicPredlog()

        self.ui.btn_save_result_predlog.clicked.connect(self._save_result)

    def _save_result(self):
        if self.ui.lineEdit_2.text() == '':
            return
        d = {'имя': self.ui.lineEdit.text(),
             'предложение': self.ui.textEdit.toPlainText(),
             'тема': self.ui.lineEdit_2.text()}
        self.ui.lineEdit_2.setText('')
        self.ui.textEdit.setText('')
        self.model.save_result(d)
