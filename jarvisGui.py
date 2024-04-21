from JarvisUiNew import Ui_JarvisUI
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, QTimer, QTime, QDate
from PyQt5.uic import loadUiType
import jarvis
import os
import webbrowser as web
import sys


class MainThread(QThread):

    def __init__(self):
        super(MainThread, self).__init__()

    def run(self):
        jarvis.Task_Gui()


startExe = MainThread()


class Gui_Start(QMainWindow):

    def __init__(self):
        super().__init__()

        self.gui = Ui_JarvisUI()
        self.gui.setupUi(self)

        self.gui.StartButton.clicked.connect(self.startTask)
        self.gui.QuitButton.clicked.connect(self.close)
        self.gui.Chrome_Botton.clicked.connect(self.chrome_app)
        self.gui.Whatsapp_Botton.clicked.connect(self.whatsapp_app)
        self.gui.Youtube_Botton.clicked.connect(self.yt_app)
        self.gui.Facebook_Botton.clicked.connect(self.Facebook_app)

    def chrome_app(self):
        jarvis.speak("Opening Chrome")
        os.startfile("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")

    def yt_app(self):
        jarvis.speak("Opening youtube")
        web.open("https://www.youtube.com/")

    def whatsapp_app(self):
        jarvis.speak("Opening whatsapp")
        web.open("https://web.whatsapp.com/")

    def Facebook_app(self):
        jarvis.speak("Opening Facebook")
        web.open("https://www.facebook.com/")

    def startTask(self):
        self.gui.label1 = QtGui.QMovie("D://jarvisGif//ExtraGui//B.G_Template_1.gif")
        self.gui.Gif_1.setMovie(self.gui.label1)
        self.gui.label1.start()

        self.gui.label2 = QtGui.QMovie("D://jarvisGif//ExtraGui//live.gif")
        self.gui.Gif_2.setMovie(self.gui.label2)
        self.gui.label2.start()

        self.gui.label3 = QtGui.QMovie("D://jarvisGif//ExtraGui//Earth.gif")
        self.gui.Gif_3.setMovie(self.gui.label3)
        self.gui.label3.start()

        self.gui.label4 = QtGui.QMovie("D://jarvisGif//VoiceReg//jarvis_jj.gif")
        self.gui.Gif_4.setMovie(self.gui.label4)
        self.gui.label4.start()

    
        # self.gui.label6 = QtGui.QMovie("D://jarvisGif//VoiceReg//Ntuks.gif")
        # self.gui.Gif_6.setMovie(self.gui.label6)
        # self.gui.label6.start()

        self.gui.label7 = QtGui.QMovie("D://jarvisGif//VoiceReg//Listening.gif")
        self.gui.Gif_7.setMovie(self.gui.label7)
        self.gui.label7.start()

        # self.gui.label8 = QtGui.QMovie("D://jarvisGif//VoiceReg//Loading.gif")
        # self.gui.Gif_8.setMovie(self.gui.label8)
        # self.gui.label8.start()


        timer = QTimer(self)
        timer.timeout.connect(self.showTimeLive)
        timer.start(999)
        startExe.start()


    def showTimeLive(self):
        t_ime = QTime.currentTime()
        time = t_ime.toString()
        d_ate = QDate.currentDate()
        date = d_ate.toString()
        label_time = "Time: " + time
        label_date = "Date: " + date

        self.gui.Text_time.setText(label_time)
        self.gui.Text_date.setText(label_date)


GuiApp = QApplication(sys.argv)
jarvis_gui = Gui_Start()
jarvis_gui.show()
exit(GuiApp.exec_())