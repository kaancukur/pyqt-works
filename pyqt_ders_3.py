import sys

from PyQt5 import QtWidgets,QtGui


def pencere():
    app=QtWidgets.QApplication(sys.argv)
    pencere=QtWidgets.QWidget()
    pencere.setWindowTitle("Pyqt5 Ders 3 ")
    pencere.setGeometry(600,300,300,300)

    buton=QtWidgets.QPushButton(pencere)
    buton.setText("First Button")
    etiket=QtWidgets.QLabel(pencere)
    etiket.setText("Hello Pyqt")

    etiket.move(150,150)

    pencere.show()
    sys.exit(app.exec_())


pencere()
