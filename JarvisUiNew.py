# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'JarvisUiNew.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_JarvisUI(object):
    def setupUi(self, JarvisUI):
        JarvisUI.setObjectName("JarvisUI")
        JarvisUI.resize(1937, 1065)
        self.JarvisUi = QtWidgets.QWidget(JarvisUI)
        self.JarvisUi.setObjectName("JarvisUi")
        self.Bg_1 = QtWidgets.QLabel(self.JarvisUi)
        self.Bg_1.setGeometry(QtCore.QRect(-10, -30, 2001, 1101))
        self.Bg_1.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.Bg_1.setText("")
        self.Bg_1.setPixmap(QtGui.QPixmap("D:/jarvisGif/B.G/Black_Template.jpg"))
        self.Bg_1.setScaledContents(True)
        self.Bg_1.setObjectName("Bg_1")
        self.Bg_3 = QtWidgets.QLabel(self.JarvisUi)
        self.Bg_3.setGeometry(QtCore.QRect(570, 10, 821, 581))
        self.Bg_3.setStyleSheet("background-color: rgb(0, 0, 0)")
        self.Bg_3.setText("")
        self.Bg_3.setScaledContents(True)
        self.Bg_3.setObjectName("Bg_3")
        self.Gif_1 = QtWidgets.QLabel(self.JarvisUi)
        self.Gif_1.setGeometry(QtCore.QRect(10, 10, 461, 701))
        self.Gif_1.setText("")
        self.Gif_1.setPixmap(QtGui.QPixmap("D:/jarvisGif/ExtraGui/B.G_Template_1.gif"))
        self.Gif_1.setScaledContents(True)
        self.Gif_1.setObjectName("Gif_1")
        self.Gif_2 = QtWidgets.QLabel(self.JarvisUi)
        self.Gif_2.setGeometry(QtCore.QRect(480, -50, 1091, 711))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setBold(True)
        font.setWeight(75)
        self.Gif_2.setFont(font)
        self.Gif_2.setText("")
        self.Gif_2.setPixmap(QtGui.QPixmap("D:/jarvisGif/ExtraGui/live.gif"))
        self.Gif_2.setScaledContents(True)
        self.Gif_2.setObjectName("Gif_2")
        self.Bg_4 = QtWidgets.QLabel(self.JarvisUi)
        self.Bg_4.setGeometry(QtCore.QRect(0, 750, 361, 231))
        self.Bg_4.setText("")
        self.Bg_4.setPixmap(QtGui.QPixmap("D:/jarvisGif/B.G/gyhf.jpg"))
        self.Bg_4.setScaledContents(True)
        self.Bg_4.setObjectName("Bg_4")
        self.Text_date = QtWidgets.QLabel(self.JarvisUi)
        self.Text_date.setGeometry(QtCore.QRect(50, 900, 261, 51))
        self.Text_date.setStyleSheet("background-color: Transparent;\n"
                                     "border-radius: none;\n"
                                     "color: rgb(0, 255, 255);\n"
                                     "font-size: 23px;")
        self.Text_date.setText("")
        self.Text_date.setObjectName("Text_date")
        self.Text_time = QtWidgets.QLabel(self.JarvisUi)
        self.Text_time.setGeometry(QtCore.QRect(50, 790, 261, 51))
        self.Text_time.setStyleSheet("background-color: Transparent;\n"
                                     "border-radius: none;\n"
                                     "color: rgb(0, 255, 255);\n"
                                     "font-size: 25px;")
        self.Text_time.setText("")
        self.Text_time.setObjectName("Text_time")
        self.StartButton = QtWidgets.QPushButton(self.JarvisUi)
        self.StartButton.setGeometry(QtCore.QRect(1300, 910, 251, 61))
        self.StartButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.StartButton.setStyleSheet("background-color: Transparent;\n"
                                       "border-radius: none;")
        self.StartButton.setText("")
        self.StartButton.setObjectName("StartButton")
        self.Start_bg = QtWidgets.QLabel(self.JarvisUi)
        self.Start_bg.setGeometry(QtCore.QRect(1290, 880, 271, 111))
        self.Start_bg.setText("")
        self.Start_bg.setPixmap(QtGui.QPixmap("D:/jarvisGif/Buttons/Start.png"))
        self.Start_bg.setScaledContents(True)
        self.Start_bg.setObjectName("Start_bg")
        self.Quit_bg = QtWidgets.QLabel(self.JarvisUi)
        self.Quit_bg.setGeometry(QtCore.QRect(1610, 890, 281, 101))
        self.Quit_bg.setText("")
        self.Quit_bg.setPixmap(QtGui.QPixmap("D:/jarvisGif/Buttons/Quit.png"))
        self.Quit_bg.setScaledContents(True)
        self.Quit_bg.setObjectName("Quit_bg")
        self.QuitButton = QtWidgets.QPushButton(self.JarvisUi)
        self.QuitButton.setGeometry(QtCore.QRect(1620, 910, 251, 61))
        self.QuitButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.QuitButton.setStyleSheet("background-color: Transparent;\n"
                                      "border-radius: none;")
        self.QuitButton.setText("")
        self.QuitButton.setObjectName("QuitButton")
        self.Youtube_Botton = QtWidgets.QPushButton(self.JarvisUi)
        self.Youtube_Botton.setGeometry(QtCore.QRect(420, 910, 91, 61))
        self.Youtube_Botton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Youtube_Botton.setStyleSheet("background-color: Transparent;\n"
                                          "border-radius: none;")
        self.Youtube_Botton.setText("")
        self.Youtube_Botton.setObjectName("Youtube_Botton")
        self.Youtube_2 = QtWidgets.QLabel(self.JarvisUi)
        self.Youtube_2.setGeometry(QtCore.QRect(420, 910, 91, 61))
        self.Youtube_2.setText("")
        self.Youtube_2.setPixmap(QtGui.QPixmap("D:/jarvisGif/Social_m/youtube_png.png"))
        self.Youtube_2.setScaledContents(True)
        self.Youtube_2.setObjectName("Youtube_2")
        self.Whatsapp = QtWidgets.QLabel(self.JarvisUi)
        self.Whatsapp.setGeometry(QtCore.QRect(560, 900, 101, 81))
        self.Whatsapp.setText("")
        self.Whatsapp.setPixmap(QtGui.QPixmap("D:/jarvisGif/Social_m/WhatsApp_png.webp"))
        self.Whatsapp.setScaledContents(True)
        self.Whatsapp.setObjectName("Whatsapp")
        self.chrome = QtWidgets.QLabel(self.JarvisUi)
        self.chrome.setGeometry(QtCore.QRect(710, 900, 81, 81))
        self.chrome.setText("")
        self.chrome.setPixmap(QtGui.QPixmap("D:/jarvisGif/Social_m/Google_Chrome_png.png"))
        self.chrome.setScaledContents(True)
        self.chrome.setObjectName("chrome")
        self.Facebook = QtWidgets.QLabel(self.JarvisUi)
        self.Facebook.setGeometry(QtCore.QRect(850, 910, 71, 61))
        self.Facebook.setText("")
        self.Facebook.setPixmap(QtGui.QPixmap("D:/jarvisGif/Social_m/facebook_png.png"))
        self.Facebook.setScaledContents(True)
        self.Facebook.setObjectName("Facebook")
        self.Whatsapp_Botton = QtWidgets.QPushButton(self.JarvisUi)
        self.Whatsapp_Botton.setGeometry(QtCore.QRect(570, 910, 81, 61))
        self.Whatsapp_Botton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Whatsapp_Botton.setStyleSheet("background-color: Transparent;\n"
                                           "border-radius: none;")
        self.Whatsapp_Botton.setText("")
        self.Whatsapp_Botton.setObjectName("Whatsapp_Botton")
        self.Chrome_Botton = QtWidgets.QPushButton(self.JarvisUi)
        self.Chrome_Botton.setGeometry(QtCore.QRect(710, 910, 81, 61))
        self.Chrome_Botton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Chrome_Botton.setStyleSheet("background-color: Transparent;\n"
                                         "border-radius: none;")
        self.Chrome_Botton.setText("")
        self.Chrome_Botton.setObjectName("Chrome_Botton")
        self.Facebook_Botton = QtWidgets.QPushButton(self.JarvisUi)
        self.Facebook_Botton.setGeometry(QtCore.QRect(850, 910, 71, 61))
        self.Facebook_Botton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Facebook_Botton.setStyleSheet("background-color: Transparent;\n"
                                           "border-radius: none;")
        self.Facebook_Botton.setText("")
        self.Facebook_Botton.setObjectName("Facebook_Botton")
        self.Gif_3 = QtWidgets.QLabel(self.JarvisUi)
        self.Gif_3.setGeometry(QtCore.QRect(1520, 60, 461, 331))
        self.Gif_3.setStyleSheet("background-color: Transparent;\n"
                                 "border-radius: none;")
        self.Gif_3.setText("")
        self.Gif_3.setPixmap(QtGui.QPixmap("D:/jarvisGif/ExtraGui/Earth.gif"))
        self.Gif_3.setScaledContents(True)
        self.Gif_3.setObjectName("Gif_3")
        self.Gif_4 = QtWidgets.QLabel(self.JarvisUi)
        self.Gif_4.setGeometry(QtCore.QRect(500, 360, 351, 201))
        self.Gif_4.setStyleSheet("background-color: rgb(115, 115, 115)")
        self.Gif_4.setText("")
        self.Gif_4.setPixmap(QtGui.QPixmap("D:/jarvisGif/VoiceReg/jarvis_jj.gif"))
        self.Gif_4.setScaledContents(True)
        self.Gif_4.setObjectName("Gif_4")
        self.Gif_6 = QtWidgets.QLabel(self.JarvisUi)
        self.Gif_6.setGeometry(QtCore.QRect(870, 590, 321, 241))
        self.Gif_6.setText("")
        self.Gif_6.setPixmap(QtGui.QPixmap("D:/jarvisGif/VoiceReg/Ntuks.gif"))
        self.Gif_6.setScaledContents(True)
        self.Gif_6.setObjectName("Gui_6")
        
        self.frame = QtWidgets.QFrame(self.JarvisUi)
        self.frame.setGeometry(QtCore.QRect(1300, 560, 581, 271))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.TerminalOutputBox = QtWidgets.QPlainTextEdit(self.frame)
        self.TerminalOutputBox.setGeometry(QtCore.QRect(0, 0, 561, 231))
        font = QtGui.QFont()
        font.setFamily("Copperplate Gothic Light")
        self.TerminalOutputBox.setFont(font)
        self.TerminalOutputBox.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.TerminalOutputBox.setMouseTracking(False)
        self.TerminalOutputBox.setAutoFillBackground(False)
        self.TerminalOutputBox.setStyleSheet("background-color: Transparent;\n"
                                             "color: rgb(255, 255, 255);\n"
                                             "border-color:rgb(255, 255, 255);")
        self.TerminalOutputBox.setBackgroundVisible(False)
        self.TerminalOutputBox.setObjectName("TerminalOutputBox")
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setGeometry(QtCore.QRect(0, 230, 491, 41))
        font = QtGui.QFont()
        font.setFamily("Copperplate Gothic Light")
        self.lineEdit.setFont(font)
        self.lineEdit.setMouseTracking(True)
        self.lineEdit.setStyleSheet("background-color: Transparent;\n"
                                    "color: rgb(255, 255, 255);\n"
                                    "border-color:rgb(255, 255, 255);")
        self.lineEdit.setObjectName("lineEdit")
        self.verticalScrollBar = QtWidgets.QScrollBar(self.frame)
        self.verticalScrollBar.setGeometry(QtCore.QRect(560, 0, 20, 231))
        self.verticalScrollBar.setOrientation(QtCore.Qt.Vertical)
        self.verticalScrollBar.setObjectName("verticalScrollBar")
        self.EnterLabel = QtWidgets.QLabel(self.frame)
        self.EnterLabel.setGeometry(QtCore.QRect(490, 230, 91, 41))
        self.EnterLabel.setStyleSheet("")
        self.EnterLabel.setText("")
        self.EnterLabel.setPixmap(QtGui.QPixmap("D:/jarvisGif/Buttons/images.png"))
        self.EnterLabel.setScaledContents(True)
        self.EnterLabel.setObjectName("EnterLabel")
        self.EnterButton = QtWidgets.QPushButton(self.frame)
        self.EnterButton.setGeometry(QtCore.QRect(490, 230, 93, 41))
        self.EnterButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.EnterButton.setStyleSheet("background-color: Transparent;\n"
                                       "border-color:rgb(255, 255, 255)")
        self.EnterButton.setText("")
        self.EnterButton.setObjectName("EnterButton")
        self.Gif_7 = QtWidgets.QLabel(self.JarvisUi)
        self.Gif_7.setGeometry(QtCore.QRect(870, 600, 321, 241))
        self.Gif_7.setText("")
        self.Gif_7.setPixmap(QtGui.QPixmap("D:/jarvisGif/VoiceReg/Listening.gif"))
        self.Gif_7.setScaledContents(True)
        self.Gif_7.setObjectName("Gui_7")
        # self.Gif_8 = QtWidgets.QLabel(self.JarvisUi)
        # self.Gif_8.setGeometry(QtCore.QRect(840, 600, 381, 211))
        # self.Gif_8.setText("")
        # self.Gif_8.setPixmap(QtGui.QPixmap("D:/jarvisGif/VoiceReg/Loading.gif"))
        # self.Gif_8.setScaledContents(True)
        # self.Gif_8.setObjectName("Gui_8")
        self.Bg_1.raise_()
        self.Bg_3.raise_()
        self.Gif_1.raise_()
        self.Bg_4.raise_()
        self.Text_date.raise_()
        self.Text_time.raise_()
        self.Start_bg.raise_()
        self.Quit_bg.raise_()
        self.StartButton.raise_()
        self.QuitButton.raise_()
        self.Youtube_2.raise_()
        self.Whatsapp.raise_()
        self.chrome.raise_()
        self.Facebook.raise_()
        self.Youtube_Botton.raise_()
        self.Whatsapp_Botton.raise_()
        self.Chrome_Botton.raise_()
        self.Facebook_Botton.raise_()
        self.Gif_3.raise_()
        self.Gif_2.raise_()
        self.Gif_4.raise_()
        self.Gif_6.raise_()
        self.frame.raise_()
        self.Gif_7.raise_()
        # self.Gif_8.raise_()
        JarvisUI.setCentralWidget(self.JarvisUi)

        self.retranslateUi(JarvisUI)
        QtCore.QMetaObject.connectSlotsByName(JarvisUI)

    def retranslateUi(self, JarvisUI):
        _translate = QtCore.QCoreApplication.translate
        JarvisUI.setWindowTitle(_translate("JarvisUI", "MainWindow"))
        self.TerminalOutputBox.setPlainText(_translate("JarvisUI", "Terminal Output goes here"))
        self.lineEdit.setText(_translate("JarvisUI", "Enter your command..."))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    JarvisUI = QtWidgets.QMainWindow()
    ui = Ui_JarvisUI()
    ui.setupUi(JarvisUI)
    JarvisUI.show()
    sys.exit(app.exec_())