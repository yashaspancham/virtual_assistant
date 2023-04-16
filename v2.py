from jarvis import Ui_jarvisui
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import QMovie
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt , QTimer ,QDate
from PyQt5.uic import loadUiType
import main1
import os
import sys
from processes import process
import speech_recognition as sr
import time
import pyttsx3

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
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Speak now...")
            audio = r.listen(source, timeout=5, phrase_time_limit=5)
            print("Processing")
            said=r.recognize_google(audio)
            said=str(said)

        try:
            print("You said: " + said)
            #process(said)
    
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))
    
        def speak(said):
            engine = pyttsx3.init()
            engine.say(said)
            engine.runAndWait()
        
 #       startexec.start()
        
        
    def showTimeLive(self):
        t=QTime.currentTime()
        time=t.toString()
        d=QDate.currentDate()
        date=d.toString()
        label_time="Time: " + time
        label_date="Date: " + date
        self.gui.text_time.setText(label_time) 
        self.gui.text_date.setText(label_date) 
#startexec=main1
guiapp=QApplication(sys.argv) 
jarvis_gui=Gui_Start()
jarvis_gui.show()
exit(guiapp.exec_())   
 
