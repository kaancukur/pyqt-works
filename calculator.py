import sys
from PyQt5 import QtWidgets

import sys
from PyQt5 import QtWidgets


class Pencere(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.buton0 = QtWidgets.QPushButton("0")
        self.buton1 = QtWidgets.QPushButton("1")
        self.buton2 = QtWidgets.QPushButton("2")
        self.buton3 = QtWidgets.QPushButton("3")
        self.buton4 = QtWidgets.QPushButton("4")
        self.buton5 = QtWidgets.QPushButton("5")
        self.buton6 = QtWidgets.QPushButton("6")
        self.buton7 = QtWidgets.QPushButton("7")
        self.buton8 = QtWidgets.QPushButton("8")
        self.buton9 = QtWidgets.QPushButton("9")
        self.buton_carp = QtWidgets.QPushButton("X")
        self.buton_topla = QtWidgets.QPushButton("+")
        self.buton_cıkar = QtWidgets.QPushButton("-")
        self.buton_bol = QtWidgets.QPushButton("/")
        self.buton_ce = QtWidgets.QPushButton('C')
        self.buton_esit = QtWidgets.QPushButton('=')
        self.buton_nokta = QtWidgets.QPushButton('.')
        self.buton_sil = QtWidgets.QPushButton('<|')

        self.lineEdit = QtWidgets.QLineEdit()
        self.lineEdit.setText("Start Calculate!")
        self.scrn = ''
        self.result = 0

        v_box1 = QtWidgets.QVBoxLayout()
        v_box1.addWidget(self.buton1)
        v_box1.addWidget(self.buton4)
        v_box1.addWidget(self.buton7)
        v_box1.addWidget(self.buton_nokta)


        v_box2 = QtWidgets.QVBoxLayout()
        v_box2.addWidget(self.buton2)
        v_box2.addWidget(self.buton5)
        v_box2.addWidget(self.buton8)
        v_box2.addWidget(self.buton0)

        v_box3 = QtWidgets.QVBoxLayout()
        v_box3.addWidget(self.buton3)
        v_box3.addWidget(self.buton6)
        v_box3.addWidget(self.buton9)
        v_box3.addWidget(self.buton_sil)



        v_box4 = QtWidgets.QVBoxLayout()
        v_box4.addWidget(self.buton_carp)
        v_box4.addWidget(self.buton_bol)
        v_box4.addWidget(self.buton_topla)
        v_box4.addWidget(self.buton_cıkar)

        h_box_le = QtWidgets.QHBoxLayout()
        h_box_le.addWidget(self.lineEdit)

        h_box_ce = QtWidgets.QHBoxLayout()
        h_box_ce.addWidget(self.buton_ce)

        h_box2 = QtWidgets.QHBoxLayout()
        h_box2.addWidget(self.buton_esit)

        h_box3 = QtWidgets.QHBoxLayout()
        h_box3.addLayout(v_box1)
        h_box3.addLayout(v_box2)
        h_box3.addLayout(v_box3)
        h_box3.addLayout(v_box4)

        v_box = QtWidgets.QVBoxLayout()
        v_box.addLayout(h_box_le)
        v_box.addLayout(h_box_ce)
        v_box.addLayout(h_box3)
        v_box.addLayout(h_box2)
        self.setLayout(v_box)

        self.buton_ce.clicked.connect(self.screen_clean)
        self.buton0.clicked.connect(self.press_0)
        self.buton1.clicked.connect(self.press_1)
        self.buton2.clicked.connect(self.press_2)
        self.buton3.clicked.connect(self.press_3)
        self.buton4.clicked.connect(self.press_4)
        self.buton5.clicked.connect(self.press_5)
        self.buton6.clicked.connect(self.press_6)
        self.buton7.clicked.connect(self.press_7)
        self.buton8.clicked.connect(self.press_8)
        self.buton9.clicked.connect(self.press_9)
        self.buton_bol.clicked.connect(self.press_bol)
        self.buton_carp.clicked.connect(self.press_carp)
        self.buton_topla.clicked.connect(self.press_topla)
        self.buton_cıkar.clicked.connect(self.press_cikar)
        self.buton_nokta.clicked.connect(self.press_nokta)
        self.buton_sil.clicked.connect(self.del_char)
        self.buton_esit.clicked.connect(self.get_result)


        self.show()

    def screen_clean(self):
        self.lineEdit.setText("Calculate Again!")
        self.scrn = ""

    def get_result(self):
        opr = ""
        indx = 0
        number1 = 0
        number2 = 0
        result=0
        for i in self.scrn:
            if not i.isnumeric():
                opr += i
        opr_list=[]
        for i in opr:
            if not i==".":
                opr_list.append(i)
        if len(opr_list)==1 :
            opr=opr_list[0]
        elif (len(opr_list)==2) and (opr_list[0]=="-") and (opr_list[1]=="-") :
            opr=opr_list[0]
        elif (len(opr_list)==2) and ((opr_list[0]=="-") or (opr_list[1]=="-")):
            opr_list.remove("-")
            opr = opr_list[0]
        elif (len(opr_list)==3):
            opr=opr_list[1]
        else:
            self.lineEdit.setText("Fuckk")

        indx = self.scrn.index(opr)
        number1 = float(self.scrn[:indx])
        number2 = float(self.scrn[indx + 1:])

        if opr[0] == "x":
            result = number1 * number2
        elif opr[0] == "/":
            result = number1 / number2
        elif opr[0] == "+":
            result = number1 + number2
        elif opr[0] == "-":
            result = number1 - number2
        result=str(result)
        self.lineEdit.setText(result)
        self.scrn=result

    def del_char(self):
        self.scrn =self.scrn[0:-1]
        self.lineEdit.setText(self.scrn)

    def press_nokta(self):
        self.scrn += "."
        self.lineEdit.setText(self.scrn)
    def press_0(self):
        self.scrn += "0"
        self.lineEdit.setText(self.scrn)

    def press_1(self):
        self.scrn += "1"
        self.lineEdit.setText(self.scrn)

    def press_2(self):
        self.scrn += "2"
        self.lineEdit.setText(self.scrn)

    def press_3(self):
        self.scrn += "3"
        self.lineEdit.setText(self.scrn)

    def press_4(self):
        self.scrn += "4"
        self.lineEdit.setText(self.scrn)

    def press_5(self):
        self.scrn += "5"
        self.lineEdit.setText(self.scrn)

    def press_6(self):
        self.scrn += "6"
        self.lineEdit.setText(self.scrn)

    def press_7(self):
        self.scrn += "7"
        self.lineEdit.setText(self.scrn)

    def press_8(self):
        self.scrn += "8"
        self.lineEdit.setText(self.scrn)

    def press_9(self):
        self.scrn += "9"
        self.lineEdit.setText(self.scrn)

    def press_carp(self):
        self.scrn += "x"
        self.lineEdit.setText(self.scrn)

    def press_bol(self):
        self.scrn += "/"
        self.lineEdit.setText(self.scrn)

    def press_topla(self):
        self.scrn += "+"
        self.lineEdit.setText(self.scrn)

    def press_cikar(self):
        self.scrn += "-"
        self.lineEdit.setText(self.scrn)


app = QtWidgets.QApplication(sys.argv)
pencere = Pencere()
sys.exit(app.exec_())
