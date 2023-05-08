import re
import sys

from PySide6 import QtGui, QtWidgets, QtCore
from ui import Ui_Form
import math
import numexpr


class Main(QtWidgets.QWidget, Ui_Form):
    def __init__(self):

        super().__init__()
        self.setupUi(self)
        self.setupButtons()
        self.setupShortcuts()

    def setupButtons(self):

        self.n0_btn.clicked.connect(lambda: self.addS(0))
        self.n1_btn.clicked.connect(lambda: self.addS(1))
        self.n2_btn.clicked.connect(lambda: self.addS(2))
        self.n3_btn.clicked.connect(lambda: self.addS(3))
        self.n4_btn.clicked.connect(lambda: self.addS(4))
        self.n5_btn.clicked.connect(lambda: self.addS(5))
        self.n6_btn.clicked.connect(lambda: self.addS(6))
        self.n7_btn.clicked.connect(lambda: self.addS(7))
        self.n8_btn.clicked.connect(lambda: self.addS(8))
        self.n9_btn.clicked.connect(lambda: self.addS(9))
        self.add_btn.clicked.connect(lambda: self.addS("+"))
        self.subst_btn.clicked.connect(lambda: self.addS("-"))
        self.multiply_btn.clicked.connect(lambda: self.addS("*"))
        self.division_btn.clicked.connect(lambda: self.addS("/"))
        self.pow_btn.clicked.connect(lambda: self.addS("^"))
        self.equals_btn.clicked.connect(self.result)
        self.ce_btn.clicked.connect(self.ce)
        self.c_btn.clicked.connect(self.c)
        self.sin_btn.clicked.connect(lambda: self.function("sin"))
        self.cos_btn.clicked.connect(lambda: self.function("cos"))
        self.sqrt_btn.clicked.connect(lambda: self.function("sqrt"))
        self.to_num.clicked.connect(self.to_num_f)
        self.dot_btn.clicked.connect(lambda: self.addS('.'))

    def setupShortcuts(self):
        self.n0_btn.setShortcut("0")
        self.n1_btn.setShortcut("1")
        self.n2_btn.setShortcut("2")
        self.n3_btn.setShortcut("3")
        self.n4_btn.setShortcut("4")
        self.n5_btn.setShortcut("5")
        self.n6_btn.setShortcut("6")
        self.n7_btn.setShortcut("7")
        self.n8_btn.setShortcut("8")
        self.n9_btn.setShortcut("9")
        self.add_btn.setShortcut("+")
        self.division_btn.setShortcut("/")
        self.multiply_btn.setShortcut("*")
        self.pow_btn.setShortcut("^")
        self.subst_btn.setShortcut("-")
        self.equals_btn.setShortcut("")
        self.c_btn.setShortcut("Backspace")
        self.equals_btn.setDefault(True)

    def addS(self, string_to_add):
        if self.te_res.text() != "Division by zero" or self.te_res.text() == "0":
            temp = self.te_res.text() + str(string_to_add)
        else:
            temp = str(string_to_add)

        temp = re.sub("^0+.", "", temp)
        temp = re.sub("([\+-/\*])+0", "\g<1>", temp)
        temp = re.sub("([\+-/\*])+[\+-/\*]", "\g<1>", temp)
        temp = re.sub("^[\*/\^]", "", temp)
        temp = re.sub("\.\.", ".", temp)
        self.te_res.setText(temp)

    def ce(self):
        self.te_res.setText("")
        self.label_res.setText("")

    def c(self):
        self.te_res.setText(self.te_res.text()[:-1])

    def result(self):
        t = self.te_res.text()
        if not t == "Division by zero":
            self.label_res.setText(t)
            try:
                self.te_res.setText(str(numexpr.evaluate(t.replace("^", "**"))))
            except ZeroDivisionError:
                self.te_res.setText("Division by zero")

    def function(self, func: str):
        if self.te_res.text():
            if self.te_res.text()[-1] not in ["+", "-", "/", "*", "^", "."]:
                self.te_res.setText(f"{func}({self.te_res.text()})")

    def to_num_f(self):
        w = QtWidgets.QInputDialog()
        w.setInputMode(QtWidgets.QInputDialog.InputMode.DoubleInput)

        self.te_res.setText(self.te_res.text() + str(w.getDouble(self, "Value", "Input value")[0]))


if __name__ == "__main__":
    app = QtWidgets.QApplication()
    x = Main()
    x.show()
    sys.exit(app.exec())
