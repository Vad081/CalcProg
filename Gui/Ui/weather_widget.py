# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'weather_widget.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_widget(object):
    def setupUi(self, widget):
        widget.setObjectName("widget")
        widget.resize(315, 166)
        widget.setMinimumSize(QtCore.QSize(315, 166))
        widget.setMaximumSize(QtCore.QSize(315, 166))
        self.label_name = QtWidgets.QLabel(widget)
        self.label_name.setGeometry(QtCore.QRect(10, 10, 121, 21))
        self.label_name.setObjectName("label_name")
        self.lineEdit_city = QtWidgets.QLineEdit(widget)
        self.lineEdit_city.setGeometry(QtCore.QRect(130, 10, 171, 21))
        self.lineEdit_city.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.lineEdit_city.setObjectName("lineEdit_city")
        self.pushButton_weather = QtWidgets.QPushButton(widget)
        self.pushButton_weather.setGeometry(QtCore.QRect(60, 40, 171, 32))
        self.pushButton_weather.setObjectName("pushButton_weather")
        self.label_weather_result = QtWidgets.QLabel(widget)
        self.label_weather_result.setGeometry(QtCore.QRect(10, 70, 291, 81))
        self.label_weather_result.setText("")
        self.label_weather_result.setObjectName("label_weather_result")

        self.retranslateUi(widget)
        QtCore.QMetaObject.connectSlotsByName(widget)

    def retranslateUi(self, widget):
        _translate = QtCore.QCoreApplication.translate
        widget.setWindowTitle(_translate("widget", "Form"))
        self.label_name.setText(_translate("widget", "Название города:"))
        self.pushButton_weather.setText(_translate("widget", "Узнать погоду"))

