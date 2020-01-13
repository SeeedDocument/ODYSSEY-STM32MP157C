# -*- coding: utf-8 -*-
"""
This example demonstrates many of the 2D plotting capabilities
in pyqtgraph. All of the plots may be panned/scaled by dragging with 
the left/right mouse buttons. Right click on any plot to show a context menu.
"""

# import initExample ## Add path to library (just for examples; you do not need this)


from pyqtgraph.Qt import QtGui
from PyQt5 import QtWidgets, uic,QtGui
import numpy as np
import pyqtgraph as pg
from PyQt5.QtCore import QTimer
import sys  # We need sys so that we can pass argv to QApplication
import can

app = QtGui.QApplication([])
win = pg.GraphicsLayoutWidget(show=True, title="Basic plotting examples")

Temperature = [0]*100
Humidity = [0]*100
Light = [0]*100

class MainWindow(QtWidgets.QMainWindow):
   
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        win.resize(480,810)
        pg.setConfigOptions(antialias=True)
        self.p1 = win.addPlot(title="Temp(°C)")
        self.curve1 = self.p1.plot(pen=(0,0,255))
        self.p1.showAxis('bottom', False)
        self.p1.setYRange(10,50)
        win.nextRow()
        pg.setConfigOptions(antialias=True)
        self.p2 = win.addPlot(title="Humi(%)")
        self.curve2 = self.p2.plot(pen=(0,255,0))
        self.p2.showAxis('bottom', False)
        self.p2.setYRange(40,90)
        win.nextRow()
        pg.setConfigOptions(antialias=True)
        self.p3 = win.addPlot(title="Light(%)")
        self.curve3 = self.p3.plot(pen=(255,255,0))
        self.p3.showAxis('bottom', False)
        self.p3.setYRange(0,70)        
        
        self.Timer_Init(Time_Ms = 40)
        self.Can_Init()
        
    def Can_Init(self):     
        can_interface = 'can0'
        bustype = 'socketcan_native'
        self.bus = can.interface.Bus(can_interface, bustype=bustype)
        
    def update(self):
        message = self.bus.recv(1.0) # Timeout in seconds.
        print(message)
        if message is None:
            print('Timeout occurred, no message.')
        Temperature.remove(Temperature[0])
        Temperature.append(message.data[7]+message.data[6]*100)
        Humidity.remove(Humidity[0])
        Humidity.append(message.data[5]+message.data[4]*100)  
        Light.remove(Light[0])
        Light.append(message.data[3]+message.data[2]*100)   
        self.curve3.setData(Light)
        self.p3.enableAutoRange('y', False)           
        self.curve2.setData(Humidity)
        self.p2.enableAutoRange('y', False)        
        self.curve1.setData(Temperature)
        self.p1.enableAutoRange('y', False)            

        # self.p2.graphWidget.clear()
        # self.p2 = win.addPlot(title="Humi(%)", pen=(0,255,0),y=Humidity)
        # p1.graphWidget.clear()
        # p1 = win.addPlot(title="Temp(°C)", pen=(0,0,255),y=Temperature) 
    def Timer_Init(self,Time_Ms):
        timer = QTimer(self)
        timer.timeout.connect(self.update)
        timer.start(Time_Ms)
    # def Data_Init(self):
        # sizeTemperature
        
        # Temperature.remove(Temperature[0])
        # Temperature.append(message.data[7]+message.data[6]*100)
        # Humidity.remove(Humidity[0])
        # Humidity.append(message.data[5]+message.data[4]*100) 
        
## Start Qt event loop unless running in interactive mode or using pyside.
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    main = MainWindow()
    sys.exit(app.exec_())
