from PyQt5 import QtWidgets
from CalcMain import Ui_Calculator

from math import pi,sqrt
from random import uniform


class CalculatorWindow(QtWidgets.QMainWindow, Ui_Calculator):

    firstNum = None
    userIsTypingSecondNumber = False

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()

        # fixme: сделать нажатие а не клик
        self.pushButton_0.clicked.connect(self.digitClicked)
        self.pushButton_1.clicked.connect(self.digitClicked)
        self.pushButton_2.clicked.connect(self.digitClicked)
        self.pushButton_3.clicked.connect(self.digitClicked)
        self.pushButton_4.clicked.connect(self.digitClicked)
        self.pushButton_5.clicked.connect(self.digitClicked)
        self.pushButton_6.clicked.connect(self.digitClicked)
        self.pushButton_7.clicked.connect(self.digitClicked)
        self.pushButton_8.clicked.connect(self.digitClicked)
        self.pushButton_9.clicked.connect(self.digitClicked)

        # self.pushButton_A.clicked.connect(self.letterClicked)
        # self.pushButton_B.clicked.connect(self.letterClicked)
        # self.pushButton_C.clicked.connect(self.letterClicked)
        # self.pushButton_D.clicked.connect(self.letterClicked)
        # self.pushButton_E.clicked.connect(self.letterClicked)
        # self.pushButton_F.clicked.connect(self.letterClicked)



        self.pushButton_decimal.clicked.connect(self.decimalClicked)
        self.pushButton_unaryMinus.clicked.connect(self.unaryOperationsClicked)
        self.pushButton_percent.clicked.connect(self.unaryOperationsClicked)

        self.pushButton_plus.clicked.connect(self.binaryOperationsClicked)
        self.pushButton_minus.clicked.connect(self.binaryOperationsClicked)
        self.pushButton_multiply.clicked.connect(self.binaryOperationsClicked)
        self.pushButton_divide.clicked.connect(self.binaryOperationsClicked)
        self.pushButton_equals.clicked.connect(self.equalsClicked)
        self.pushButton_allClear.clicked.connect(self.clearClicked)

        self.pushButton_pi.clicked.connect(self.piClicked)
        self.pushButton_rd.clicked.connect(self.rdClicked)
        self.pushButton_sqrt.clicked.connect(self.sqrtClicked)

        self.pushButton_bin.clicked.connect(self.numberSystemsClicked)
        self.pushButton_oct.clicked.connect(self.numberSystemsClicked)
        self.pushButton_hex.clicked.connect(self.numberSystemsClicked)

        self.pushButton_convert.clicked.connect(self.convertGetResulst)

        # self.pushButton_bin.clicked.connect(self.binSystem)


        self.pushButton_plus.setCheckable(True)
        self.pushButton_minus.setCheckable(True)
        self.pushButton_multiply.setCheckable(True)
        self.pushButton_divide.setCheckable(True)

        # self.pushButton_A.setCheckable(True)
        # self.pushButton_B.setCheckable(True)
        # self.pushButton_C.setCheckable(True)
        # self.pushButton_D.setCheckable(True)
        # self.pushButton_E.setCheckable(True)
        # self.pushButton_F.setCheckable(True)

        self.pushButton_bin.setCheckable(True)
        self.pushButton_oct.setCheckable(True)
        self.pushButton_hex.setCheckable(True)



    def digitClicked(self):
        button = self.sender()

        if ((self.pushButton_plus.isChecked() or 
            self.pushButton_minus.isChecked() or 
            self.pushButton_multiply.isChecked() or 
            self.pushButton_divide.isChecked()) and (not self.userIsTypingSecondNumber)):
            newLabel = format(float(button.text()), '.15g')
            self.userIsTypingSecondNumber = True
        elif (('.' in self.label.text()) and button.text() == '0'):
            newLabel = format(self.label.text() + button.text(),'.15')
        else:
            newLabel = format(float(self.label.text() + button.text()), '.15g')

        self.label.setText(newLabel)
        


    # def letterClicked(self):
    #     button = self.sender()

    #     if ((self.pushButton_A.isChecked() or 
    #         self.pushButton_B.isChecked() or 
    #         self.pushButton_C.isChecked() or 
    #         self.pushButton_D.isChecked() or
    #         self.pushButton_E.isChecked() or
    #         self.pushButton_F.isChecked()) and (not self.userIsTypingSecondNumber)):
    #         newLabel = format(str(button.text()), '.15s')
    #         self.userIsTypingSecondNumber = True
    #     elif (('.' in self.label.text()) and button.text() == '0'):
    #         newLabel = format(self.label.text() + button.text(),'.15')
    #     else:
    #         newLabel = format(str(self.label.text() + button.text()), '.15')

    #     self.label.setText(newLabel)



    def decimalClicked(self):
        if '.' not in self.label.text():
            self.label.setText(self.label.text() + '.')



    def unaryOperationsClicked(self):
        button = self.sender()

        labelNumber = float(self.label.text())

        if button.text() == '+/-':
            labelNumber = labelNumber * -1
        else: # button text == '%'
            labelNumber = labelNumber * 0.01

        newLabel = format(labelNumber, '.15g')
        self.label.setText(newLabel)


    def binaryOperationsClicked(self):
        
        button = self.sender()

        self.firstNum = float(self.label.text())

        button.setChecked(True)



    def equalsClicked(self):
        secondNum = float(self.label.text())

        if self.pushButton_plus.isChecked():
            labelNumber = self.firstNum + secondNum
            newLabel = format(labelNumber,'.15g')
            self.label.setText(newLabel)
            self.pushButton_plus.setChecked(False)

        elif self.pushButton_minus.isChecked():
            labelNumber = self.firstNum - secondNum
            newLabel = format(labelNumber,'.15g')
            self.label.setText(newLabel)
            self.pushButton_minus.setChecked(False)

        elif self.pushButton_multiply.isChecked():
            labelNumber = self.firstNum * secondNum
            newLabel = format(labelNumber,'.15g')
            self.label.setText(newLabel)
            self.pushButton_multiply.setChecked(False)

        elif self.pushButton_divide.isChecked():
            labelNumber = self.firstNum / secondNum
            newLabel = format(labelNumber,'.15g')
            self.label.setText(newLabel)
            self.pushButton_divide.setChecked(False)

        self.userIsTypingSecondNumber = False



    def clearClicked(self):
        self.pushButton_plus.setChecked(False)
        self.pushButton_minus.setChecked(False)
        self.pushButton_multiply.setChecked(False)
        self.pushButton_divide.setChecked(False)

        self.userIsTypingSecondNumber = False
        self.label.setText('0')



    def piClicked(self):

        self.label.setText(str(pi))


    def rdClicked(self):

        self.label.setText(str(uniform(-1,1)))


    def sqrtClicked(self):
        button = self.sender()
        labelNumber = self.label.text()
        if button.text() == 'sqrt' and float(labelNumber) > 0:
            labelNumber = sqrt(float(labelNumber))
            newLabel = format(labelNumber, '.15g')
            self.label.setText(newLabel)
        else:
            self.label.setText('Не определенно')

        


    def numberSystemsClicked(self):

        button = self.sender()

        labelNumber = float(self.label.text())

        if button.text() == 'bin':
            labelNumber = bin(int(labelNumber))[2:]

        if button.text() == 'oct':
            labelNumber = oct(int(labelNumber))[2:]

        if button.text() == 'hex':
            labelNumber = hex(int(labelNumber))[2:]

        newLabel = format(labelNumber, '.15s')
        self.label.setText(newLabel)



    # def binSystem(self):
    #     button = self.sender()
    #     labelNumber = self.label.text()
        
    #     if self.label.text() == 0 and self.pushButton_bin.down():
    #         labelNumber = int(str(labelNumber), 2)
    #     newLabel = format(labelNumber, '.15s')
    #     self.label.setText(newLabel)
        

    def convertGetResulst(self):
        decimal_number = int(self.lineEdit_input1.text())
        base = int(self.lineEdit_input2.text())
        
        STRINGS = '0123456789abcdef'
        remainder_stack = []

        while decimal_number > 0:
            remainder = decimal_number % base
            remainder_stack.append(remainder)
            decimal_number = decimal_number // base

        new_digits = []
        while remainder_stack:
            new_digits.append(STRINGS[remainder_stack.pop()])

        result = ''.join(new_digits)
        

        self.label.setText(result)

           






        # number = self.lineEdit_input1.text()
        # base = int(self.lineEdit_input2.text())
        # result = int(number, base)
        # self.label.setText(str(result))






    




    



