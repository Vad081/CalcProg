from PyQt5 import QtWidgets
from PyQt5.Qt import Qt
from .Ui.weather_widget import Ui_widget

import pyowm

owm = pyowm.OWM(API_key='ea8c2139b4ac4c3abbe304751c3010c7', language='ru')

class WeatherWidget(QtWidgets.QWidget,Ui_widget):

	def __init__(self):
		super().__init__()
		self.setupUi(self)
		self.show()
		

		self.pushButton_weather.clicked.connect(self.getWeather)


	def keyPressEvent(self, event):
		if event.key() == Qt.Key_Return:
			self.getWeather()


	def getWeather(self):
		city = self.lineEdit_city.text()
		observation = owm.weather_at_place(city)
		w = observation.get_weather()
		temp = w.get_temperature('celsius')['temp']
		status = w.get_detailed_status()

		self.label_weather_result.setText(f'Температура: {temp} C.\nПогодные условия: {status}')