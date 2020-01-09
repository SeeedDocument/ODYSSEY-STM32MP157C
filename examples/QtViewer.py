from PyQt5 import QtWidgets, uic,QtGui,QtCore
from pyqtgraph import PlotWidget, plot
from PyQt5.QtCore import QTimer
import pyqtgraph as pg
import sys  # We need sys so that we can pass argv to QApplication
import os
import random

import can
can_interface = 'can0'
bustype = 'socketcan_native'
bus = can.interface.Bus(can_interface, bustype=bustype)

hour = [1,2,3,4,5,6,7,8,9,10]
temperature_1 = [30,32,34,32,33,31,29,32,35,45]
temperature_2 = [50,35,44,22,38,32,27,38,32,44]

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.graphWidget = pg.PlotWidget()
        self.setCentralWidget(self.graphWidget)
        self.setGeometry(0, 0, 150,150 )
        self.setWindowTitle("Can Bus Data")
        # self.graphWidget.setBackground('w')
        #color = self.palette().color(QtGui.QPalette.Window)
        #self.graphWidget.setBackground(color)
        #self.graphWidget.setBackground((100,50,255))      # RGB each 0-255
       # self.setWindowIcon(QIcon("1.jpg"))
        pen = pg.mkPen(color=(255, 0, 0), width=5, style=QtCore.Qt.SolidLine)
        self.graphWidget.setTitle("<span style=\"color:blue;font-size:15px\">Your Title Here</span>")
        self.graphWidget.setLabel('left', "<span style=\"color:red;font-size:15px\">Temperature (°C)</span>")
        self.graphWidget.setLabel('bottom', "<span style=\"color:red;font-size:15px\">Hour (H)</span>")
        # plot data: x, y values
        self.graphWidget.addLegend()
        self.plot(hour, temperature_1, "Sensor1", 'r')
        self.plot(hour, temperature_2, "Sensor2", 'b')
        
        timer = QTimer(self)
        timer.timeout.connect(self.update)
        timer.start(100)
        
    def plot(self, x, y, plotname, color):
        pen = pg.mkPen(color=color)
        self.graphWidget.plot(x, y, name=plotname, pen=pen, symbol='o', symbolSize=1, symbolBrush=(color))
    def update(self):
        message = bus.recv(1.0) # Timeout in seconds.
        if message is None:
            print('Timeout occurred, no message.')
        temperature_1.remove(temperature_1[0])
        temperature_1.append(message.data[7]+message.data[6]*10)
        temperature_2.remove(temperature_2[0])
        temperature_2.append(message.data[5]+message.data[4]*10)        
        self.graphWidget.clear()
        self.plot(hour, temperature_1, "Sensor1", 'g')
        self.plot(hour, temperature_2, "Sensor2", 'b')
	
def main():
    app = QtWidgets.QApplication(sys.argv)
    main = MainWindow()

    main.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
