import sys

from PyQt5 import QtWidgets,QtGui


def pencere():
    app=QtWidgets.QApplication(sys.argv)
    pencere=QtWidgets.QWidget()
    pencere.setWindowTitle("Pyqt5 Ders 4 ")
    pencere.setGeometry(600,300,300,300)

    buton1=QtWidgets.QPushButton("tamam")
    buton2=QtWidgets.QPushButton("iptal")
    h_box=QtWidgets.QHBoxLayout()
    #h_box.addStretch()
    h_box.addWidget(buton1)
    #h_box.addStretch()
    h_box.addWidget(buton2)
    #pencere.setLayout(h_box)
    #h_box.addStretch()

    v_box = QtWidgets.QVBoxLayout()
    # h_box.addStretch()
    v_box.addWidget(buton1)
    # h_box.addStretch()
    v_box.addWidget(buton2)
    pencere.setLayout(v_box)


    pencere.show()
    sys.exit(app.exec_())


pencere()
