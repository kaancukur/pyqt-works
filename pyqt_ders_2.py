import sys

from PyQt5 import QtWidgets,QtGui


def pencere():
    app=QtWidgets.QApplication(sys.argv)
    pencere=QtWidgets.QWidget()
    pencere.setWindowTitle("Pyqt5 Ders 2 ")
    pencere.setGeometry(600,300,300,300)
    label1=QtWidgets.QLabel(pencere)
    label2=QtWidgets.QLabel(pencere)

    label1.setText("Burası yazı yazdığımız kısım")
    label1.move(100,30)
    label2.setPixmap(QtGui.QPixmap("universe-stars-moon-space-night-sky-hd-wallpaper-preview.jpg"))
    label2.move(500,30)

    pencere.show()
    sys.exit(app.exec_())


pencere()
