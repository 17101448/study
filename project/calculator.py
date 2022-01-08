from PyQt5.QtWidgets import *
from PyQt5 import uic
import sys 

ui_file = "./calculator.ui"
class MainDialog(QDialog):
    def __init__(self):
        QDialog.__init__(self, None)
        uic.loadUi(ui_file, self)
        self.equalbutton.clicked.connect(self.calculate) 

    def calculate(self):
        equation = self.inputbox.text()
        result = eval(equation)
        self.history.setText(str(result))



QApplication.setStyle("fusion")
app = QApplication(sys.argv)
main_dialog = MainDialog()
main_dialog.show()
sys.exit(app.exec())