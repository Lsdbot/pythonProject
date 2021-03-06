import Design
import Logic
import shelve
from PyQt5 import QtWidgets,QtCore

class Application(QtWidgets.QMainWindow, Design.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.inputButton.clicked.connect(lambda: self.Game(self.inputLine.text()))
        self.helpButton.clicked.connect(lambda: self.Help())
        self.counter = True
        self.chosedCity = ""

    def Help(self):
        self.labelProgramme.setText("Пошел нахер, загугли")

    def keyPressEvent(self, e):
        if e.key() == QtCore.Qt.Key.Key_Return:
            self.Game(self.inputLine.text())
        e.accept()

    def Game(self, City):
        if self.counter:
            self.labelProgramme.setText(Logic.FirstStepOfGame(citiesDb, usedCities,self, City))
            self.inputLine.clear()
            self.counter = False
        else:
            self.labelProgramme.setText(Logic.MainOfGame(citiesDb, usedCities,self, City))
            self.inputLine.clear()

def main():
    import sys
    app = QtWidgets.QApplication(sys.argv)
    windowApp = Application()
    windowApp.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    citiesDb = shelve.open("dbOfWordsGame")
    usedCities = []
    main()
    citiesDb.close()