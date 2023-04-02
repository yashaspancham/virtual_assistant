


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_jarvisui(object):
    def setupUi(self, jarvisui):
        jarvisui.setObjectName("jarvisui")
        jarvisui.resize(1366, 768)
        self.centralwidget = QtWidgets.QWidget(jarvisui)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(-10, -70, 1381, 861))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("b3.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.gif_1 = QtWidgets.QLabel(self.centralwidget)
        self.gif_1.setGeometry(QtCore.QRect(270, 100, 831, 441))
        self.gif_1.setText("")
        self.gif_1.setPixmap(QtGui.QPixmap("voi.gif"))
        self.gif_1.setObjectName("gif_1")
        self.gif_2 = QtWidgets.QLabel(self.centralwidget)
        self.gif_2.setGeometry(QtCore.QRect(0, 0, 451, 141))
        self.gif_2.setText("")
        self.gif_2.setPixmap(QtGui.QPixmap("init.gif"))
        self.gif_2.setObjectName("gif_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(830, -50, 551, 511))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("dis2.jpg"))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(-50, 120, 501, 151))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("dis2.jpg"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.text_time = QtWidgets.QTextBrowser(self.centralwidget)
        self.text_time.setGeometry(QtCore.QRect(70, 160, 256, 31))
        self.text_time.setStyleSheet("background-color:transparent;\n""color:white;\n""font:14pt;")
        self.text_time.setObjectName("text_time")
        self.text_date = QtWidgets.QTextBrowser(self.centralwidget)
        self.text_date.setGeometry(QtCore.QRect(70, 200, 256, 31))
        self.text_date.setStyleSheet("background-color:transparent;\n"
        "color:white;\n""font:14pt;")
        self.text_date.setObjectName("text_date")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(140, 586, 281, 91))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("buttonbg.jpeg"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(920, 580, 281, 91))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("buttonbg.jpeg"))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")
        self.terminate = QtWidgets.QPushButton(self.centralwidget)
        self.terminate.setGeometry(QtCore.QRect(980, 610, 161, 31))
        self.terminate.setStyleSheet("font: 11pt \"URW Gothic\";\n"
"background-color:Transparent;\n"
"color:blue;")
        
        
        self.terminate.setObjectName("terminate")
        self.start = QtWidgets.QPushButton(self.centralwidget)
        self.start.setGeometry(QtCore.QRect(200, 614, 161, 31))
        self.start.setStyleSheet("background-color:transparent;\n"
"color:blue;\n"
"font: 11pt \"URW Gothic\";")
        
        self.start.setObjectName("start")
        
        
        
        self.text_terminal = QtWidgets.QTextBrowser(self.centralwidget)
        self.text_terminal.setGeometry(QtCore.QRect(960, 100, 351, 211))
        self.text_terminal.setStyleSheet("background-color:transparent;")
        self.text_terminal.setObjectName("text_terminal")
        jarvisui.setCentralWidget(self.centralwidget)

        self.retranslateUi(jarvisui)
        QtCore.QMetaObject.connectSlotsByName(jarvisui)

    def retranslateUi(self, jarvisui):
        _translate = QtCore.QCoreApplication.translate
        jarvisui.setWindowTitle(_translate("jarvisui", "MainWindow"))
        self.terminate.setText(_translate("jarvisui", "TERMINATE"))
        self.start.setText(_translate("jarvisui", "START"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    jarvisui = QtWidgets.QMainWindow()
    ui = Ui_jarvisui()
    ui.setupUi(jarvisui)
    jarvisui.show()
    sys.exit(app.exec_())