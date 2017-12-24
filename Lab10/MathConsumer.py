import sys

from PySide.QtGui import *
from calculator import *

class MathConsumer(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MathConsumer, self).__init__(parent)
        self.setupUi(self)
        self.btnCalculate.clicked.connect(self.performOperation)

    def performOperation(self):
        num1 = self.edtNumber1.text()
        num2 = self.edtNumber2.text()
        mode = self.cboOperation.currentIndex()
        if num1 != "" and num2 != "":
            try:
                if mode == 0:
                    ans = float(num1) + float(num2)
                elif mode == 1:
                    ans = float(num1) - float(num2)
                elif mode == 2:
                    ans = float(num1) * float(num2)
                elif mode == 3:
                    ans = float(num1) / float(num2)
            except:
                ans = "E"
        else:
            ans = "E"

        ans = str(ans)
        self.edtResult.setText(ans)

if __name__ == "__main__":
    currentApp = QApplication(sys.argv)
    currentForm = MathConsumer()

    currentForm.show()
    currentApp.exec_()