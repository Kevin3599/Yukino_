# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MP4-player.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#1
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Yukino(object):
    def setupUi(self, Yukino):
        Yukino.setObjectName("Yukino")
        Yukino.resize(800, 600)
        self.centralwidget = videoWidget(Yukino)
        self.centralwidget.setObjectName("centralwidget")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(0, 0, 381, 31))
        self.textEdit.setObjectName("textEdit")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(370, 440, 81, 31))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(70, 440, 91, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(220, 440, 91, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalSlider = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider.setGeometry(QtCore.QRect(69, 386, 381, 20))
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.menubar = QtWidgets.QMenuBar(Yukino)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        Yukino.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Yukino)
        self.statusbar.setObjectName("statusbar")
        Yukino.setStatusBar(self.statusbar)

        self.retranslateUi(Yukino)
        QtCore.QMetaObject.connectSlotsByName(Yukino)

    def retranslateUi(self, Yukino):
        _translate = QtCore.QCoreApplication.translate
        Yukino.setWindowTitle(_translate("Yukino", "MainWindow"))
        self.textEdit.setHtml(_translate("Yukino", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">欢迎使用！这是一个MP4播放器，希望能陪伴各位度过美好的时光！😀</p></body></html>"))
        self.pushButton_3.setText(_translate("Yukino", "暂停（pause）"))
        self.pushButton.setText(_translate("Yukino", "打开视频文件"))
        self.pushButton_2.setText(_translate("Yukino", "播放（play）"))
from videowidget import videoWidget
