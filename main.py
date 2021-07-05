import sys
import Design
from PyQt5 import QtWidgets
import Logic

class Application(QtWidgets.QMainWindow, Design.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setUpi(self)
        self.inputLine.returnPressed.connect(self.PressEnter)

def main():
    app = QtWidgets.QApplication(sys.argv)
    windowApp = Application()

    windowApp.show()
    app.exec_()

if __name__ == '__main__':
    print(Logic.ShowMessage("Москва"))