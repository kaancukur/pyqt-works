import sys
from PyQt5 import QtWidgets

class Pencere(QtWidgets.QWidget): # qtwidgets'dan miras almasını istiyorum.Ektsra özelliklerde eklenecek.
    def __init__(self): # normal bire pencere olması için init fonk. kullanmam gerekiyor.
        super().__init__()
        self.init_ui()
    def init_ui(self):
        self.yazi_alani=QtWidgets.QLabel("Tıklanmadı.")
        self.buton=QtWidgets.QPushButton("Tıkla!")
        self.say=0

        v_box=QtWidgets.QVBoxLayout()
        v_box.addStretch()
        v_box.addWidget(self.buton)
        v_box.addWidget(self.yazi_alani)
        v_box.addStretch()

        h_box=QtWidgets.QHBoxLayout()
        h_box.addStretch()
        h_box.addLayout(v_box)
        h_box.addStretch()

        self.setLayout(h_box) # öncesinde v_box tı

        self.buton.clicked.connect(self.click_count)
        self.show()
    def click_count(self):
        self.say+=1
        self.yazi_alani.setText(str(self.say) + " defa tıklandı.")

app=QtWidgets.QApplication(sys.argv)
pencere=Pencere()
sys.exit(app.exec_())

