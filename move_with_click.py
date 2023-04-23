import sys
from PyQt5 import QtWidgets

class Pencere(QtWidgets.QWidget): # qtwidgets'dan miras almasını istiyorum.Ektsra özelliklerde eklenecek.
    def __init__(self): # normal bire pencere olması için init fonk. kullanmam gerekiyor.
        super().__init__()
        self.init_ui()
    def init_ui(self):
        self.yazi_alani1=QtWidgets.QLabel("-")
        self.yazi_alani2=QtWidgets.QLabel("-")
        self.yazi_alani3=QtWidgets.QLabel("-")
        self.yazi_alani4=QtWidgets.QLabel("-")
        self.buton=QtWidgets.QPushButton("Tıkla!")
        self.char='O'
        self.say=0

        v_box=QtWidgets.QVBoxLayout()
        v_box.addStretch()
        v_box.addWidget(self.yazi_alani1)
        v_box.addWidget(self.buton)
        v_box.addWidget(self.yazi_alani3)
        v_box.addStretch()

        h_box=QtWidgets.QHBoxLayout()
        h_box.addStretch()
        h_box.addWidget(self.yazi_alani4)
        h_box.addLayout(v_box)
        h_box.addWidget(self.yazi_alani2)
        h_box.addStretch()

        self.setLayout(h_box) # öncesinde v_box tı

        self.buton.clicked.connect(self.change)
        self.show()
    def change(self):
        self.say+=1
        if self.say%4==1:
            self.yazi_alani1.setText(str(self.char))
            self.yazi_alani2.setText("-")
            self.yazi_alani3.setText("-")
            self.yazi_alani4.setText("-")
        elif self.say%4==2:
            self.yazi_alani2.setText(str(self.char))
            self.yazi_alani1.setText("-")
            self.yazi_alani3.setText("-")
            self.yazi_alani4.setText("-")
        elif self.say%4==3:
            self.yazi_alani3.setText(str(self.char))
            self.yazi_alani1.setText("-")
            self.yazi_alani2.setText("-")
            self.yazi_alani4.setText("-")
        elif self.say%4==0:
            self.yazi_alani4.setText(str(self.char))
            self.yazi_alani1.setText("-")
            self.yazi_alani3.setText("-")
            self.yazi_alani2.setText("-")


app=QtWidgets.QApplication(sys.argv)
pencere=Pencere()
sys.exit(app.exec_())