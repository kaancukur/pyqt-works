import sys

from PyQt5 import QtWidgets

def pencere():
    app=QtWidgets.QApplication(sys.argv)
    pencere=QtWidgets.QWidget()
    pencere.setWindowTitle("Pyqt5 Ders 1 ")
    pencere.show()


    sys.exit(app.exec_())


pencere()
