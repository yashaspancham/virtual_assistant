from jarvis import Ui_jarvisui
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import QMovie
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt , QTimer ,QDate
from PyQt5.uic import loadUiType
#import v2
#import v1
import os
import sys


class MainThread(QThread):

    def __init__(self):
        super(MainThread,self).__init__()
        
    def run(self):   
        v1

