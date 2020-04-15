import sys
from PyQt5.QtWidgets import QApplication 
from Gui.Calculator import CalculatorWindow
from Gui.weather import WeatherWidget


app = QApplication(sys.argv)

calculator = CalculatorWindow()
# weather = WeatherWidget()


sys.exit(app.exec_())
