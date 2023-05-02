from PyQt6 import QtWidgets, uic
from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox
import rocket_fixed

import sys, os, math

_scriptdir = os.path.dirname(os.path.realpath(__file__))
uifile = os.path.join(_scriptdir, 'ui', 'main.ui')


class Window(*uic.loadUiType(uifile)):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.bindEvents()
    
    def bindEvents(self):
        self.btn_calc.clicked.connect(self.calc)
        self.btn_reset.clicked.connect(self.reset)
        self.btn_exit.clicked.connect(self.close)
        self.btn_default.clicked.connect(self.default)
        

    def calc(self):
        try:
            mass = float(self.textEdit_mass.toPlainText())        
            angle = float(self.textEdit_angle.toPlainText())
            fuel_cons = float(self.textEdit_fuelcons.toPlainText())
            fuel_v = float(self.textEdit_fuelv.toPlainText())
            fuel_vol = float(self.textEdit_fuelvol.toPlainText())
            time = int(self.textEdit_time.toPlainText())
        except ValueError:
            error = QMessageBox()
            error.setWindowTitle('Ошибка формата')
            error.setText('Введенное значение имеет неверный формат')
            error.exec()
            return

        answer = rocket_fixed.RocketFlight(mass, angle, fuel_cons, fuel_v, fuel_vol, time)
        self.label_resX.setText(str(answer[0]))
        self.label_resY.setText(str(answer[1]))
        self.label_resVX.setText(str(answer[2]))
        self.label_resVY.setText(str(answer[3]))
        self.label_resV.setText(str(math.sqrt(answer[2]**2 + answer[3]**2)))

    def reset(self):
        self.label_resX.setText('')
        self.label_resY.setText('')
        self.label_resVX.setText('')
        self.label_resVY.setText('')
        self.label_resV.setText('')

    def default(self):
        self.textEdit_mass.setPlainText('12500')
        self.textEdit_angle.setPlainText('0.78')
        self.textEdit_fuelcons.setPlainText('127')
        self.textEdit_fuelv.setPlainText('2050')
        self.textEdit_fuelvol.setPlainText('8500')
        self.textEdit_time.setPlainText('10')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()

    sys.exit(app.exec())
