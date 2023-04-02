from jarvis import Ui_jarvisui
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import QMovie
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt , QTimer ,QDate
from PyQt5.uic import loadUiType
import v1
import os
import sys


class MainThread(QThread):

    def __init__(self):
        super(MainThread,self).__init__()
        
    def run(self):   
        v1
startexec=MainThread() 
class Gui_Start(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.gui=Ui_jarvisui()
        self.gui.setupUi(self)
        self.gui.start.clicked.connect(self.starttask)
        self.gui.terminate.clicked.connect(self.close)
    def starttask(self):
        self.gui.label1=QtGui.QMovie("voi.gif")
        self.gui.gif_1.setMovie(self.gui.label1)
        self.gui.label1.start()    
        
        self.gui.label2=QtGui.QMovie("init.gif")
        self.gui.gif_2.setMovie(self.gui.label2)
        self.gui.label2.start()    
        
        timer=QTimer(self)
        timer.timeout.connect(self.showTimeLive)
        timer.start(999)
        startexec.start()
    def showTimeLive(self):
        t=QTime.currentTime()
        time=t.toString()
        d=QDate.currentDate()
        date=d.toString()
        label_time="Time: " + time
        label_date="Date: " + date
        self.gui.text_time.setText(label_time) 
        self.gui.text_date.setText(label_date) 
guiapp=QApplication(sys.argv) 
jarvis_gui=Gui_Start()
jarvis_gui.show()
exit(guiapp.exec_())    
