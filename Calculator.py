from PyQt5 import QtWidgets
from CalcMain import Ui_Calculator

from math import pi,sqrt
from random import uniform
import string


class CalculatorWindow(QtWidgets.QMainWindow, Ui_Calculator):

    # firstNum = None
    # userIsTypingSecondNumber = False # нужно сделать закрытыми

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()
        self._firstNum = None
        self._userIsTypingSecondNumber = False

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

        self.pushButton_plus.setCheckable(True)
        self.pushButton_minus.setCheckable(True)
        self.pushButton_multiply.setCheckable(True)
        self.pushButton_divide.setCheckable(True)


        self.pushButton_bin.setCheckable(True)
        self.pushButton_oct.setCheckable(True)
        self.pushButton_hex.setCheckable(True)



    def outputLabel(self,labelNumber):
        '''Функция для ввода нового значения на экран'''
        if isinstance(labelNumber,float):   
        	newLabel = format(labelNumber, '.15g')
        elif isinstance(labelNumber,str):
        	newLabel = format(labelNumber, '.15s')
        
        return self.label.setText(newLabel)


    def digitClicked(self):
        '''Введены цифры'''
        
        button = self.sender()

        if ((self.pushButton_plus.isChecked() or 
            self.pushButton_minus.isChecked() or 
            self.pushButton_multiply.isChecked() or 
            self.pushButton_divide.isChecked()) and (not self._userIsTypingSecondNumber)):
            newLabel = format(float(button.text()), '.15g')
            self._userIsTypingSecondNumber = True
        elif (('.' in self.label.text()) and button.text() == '0'):
            newLabel = format(self.label.text() + button.text(),'.15')
        elif not self.label.text().isdigit():
            newLabel = format(button.text(), '.15')
        else:
            newLabel = format(float(self.label.text() + button.text()), '.15g')

        self.outputLabel(newLabel)





    
    def decimalClicked(self):
        '''Введена точка'''
        if '.' not in self.label.text():
            self.outputLabel(self.label.text() + '.')



    def unaryOperationsClicked(self):
        '''Унарные операции'''
        button = self.sender()
        labelNumber = float(self.label.text())
        if button.text() == '+/-':
            labelNumber = labelNumber * -1
        else: # button text == '%'
            labelNumber = labelNumber * 0.01
        self.outputLabel(labelNumber)



    def binaryOperationsClicked(self):
        '''Бинарные операции'''
        button = self.sender()
        self.firstNum = float(self.label.text())
        button.setChecked(True)



    def equalsClicked(self):
        secondNum = float(self.label.text())

        if self.pushButton_plus.isChecked():
            labelNumber = self.firstNum + secondNum
            self.outputLabel(labelNumber)
            self.pushButton_plus.setChecked(False)

        elif self.pushButton_minus.isChecked():
            labelNumber = self.firstNum - secondNum
            self.outputLabel(labelNumber)
            self.pushButton_minus.setChecked(False)

        elif self.pushButton_multiply.isChecked():
            labelNumber = self.firstNum * secondNum
            self.outputLabel(labelNumber)
            self.pushButton_multiply.setChecked(False)

        elif self.pushButton_divide.isChecked():
            labelNumber = self.firstNum / secondNum
            self.outputLabel(labelNumber)
            self.pushButton_divide.setChecked(False)

        self._userIsTypingSecondNumber = False



    def clearClicked(self):
        '''Отчистка экрана'''
        self.pushButton_plus.setChecked(False)
        self.pushButton_minus.setChecked(False)
        self.pushButton_multiply.setChecked(False)
        self.pushButton_divide.setChecked(False)
        self._userIsTypingSecondNumber = False
        self.label.setText('0')



    def piClicked(self):
        '''Число Пи'''
        self.label.setText(str(pi))


    def rdClicked(self):
        '''Случайное число от -1 до 1'''
        # self.label.setText(str(uniform(-1,1)))
        self.label.setText(str(uniform(int(self.lineEdit_input1.text()),int(self.lineEdit_input2.text()))))


    def sqrtClicked(self):
        '''Квадратный корень'''
        button = self.sender()
        labelNumber = self.label.text()
        if button.text() == 'sqrt' and float(labelNumber) > 0:
            labelNumber = sqrt(float(labelNumber))
            self.outputLabel(labelNumber)
        else:
            labelNumber = 'Не определенно'
            self.outputLabel(labelNumber)




    def numberSystemsClicked(self):
        '''Перевод в СС'''
        button = self.sender()
        labelNumber = float(self.label.text())
        if button.text() == 'bin':
            labelNumber = bin(int(labelNumber))[2:]
        if button.text() == 'oct':
            labelNumber = oct(int(labelNumber))[2:]
        if button.text() == 'hex':
            labelNumber = hex(int(labelNumber))[2:]
        self.outputLabel(labelNumber)
        

    def convertGetResulst(self):
        '''Конвертер в другие СС'''
        decimal_number = int(self.lineEdit_input1.text())
        base = int(self.lineEdit_input2.text())
        
        STRINGS = string.digits + string.ascii_lowercase 
        remainder_stack = []

        while decimal_number > 0:
            remainder = decimal_number % base
            remainder_stack.append(remainder)
            decimal_number = decimal_number // base

        new_digits = []
        while remainder_stack:
            new_digits.append(STRINGS[remainder_stack.pop()])

        labelNumber = ''.join(new_digits)
        
        self.outputLabel(labelNumber)

        






    




    



