# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sixth_view.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1280, 570)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Palet = QtWidgets.QLabel(self.centralwidget)
        self.Palet.setGeometry(QtCore.QRect(20, 20, 356, 491))
        self.Palet.setText("")
        self.Palet.setObjectName("Palet")
        self.DictLabel = QtWidgets.QLabel(self.centralwidget)
        self.DictLabel.setGeometry(QtCore.QRect(142, 70, 101, 41))
        font = QtGui.QFont()
        font.setFamily(".Apple SD Gothic NeoI")
        font.setPointSize(26)
        self.DictLabel.setFont(font)
        self.DictLabel.setObjectName("DictLabel")
        self.NackNarrowImage = QtWidgets.QLabel(self.centralwidget)
        self.NackNarrowImage.setGeometry(QtCore.QRect(30, 70, 41, 41))
        self.NackNarrowImage.setText("")
        self.NackNarrowImage.setObjectName("NackNarrowImage")

        self.VocListLabel = QtWidgets.QLabel(self.centralwidget)
        self.VocListLabel.setGeometry(QtCore.QRect(610, 30, 171, 41))
        font = QtGui.QFont()
        font.setFamily(".Apple SD Gothic NeoI")
        font.setPointSize(24)
        self.VocListLabel.setFont(font)
        self.VocListLabel.setObjectName("VocListLabel")
        self.VL_engWord_1 = QtWidgets.QLabel(self.centralwidget)
        self.VL_engWord_1.setGeometry(QtCore.QRect(400, 100, 141, 41))
        font = QtGui.QFont()
        font.setFamily(".Apple SD Gothic NeoI")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.VL_engWord_1.setFont(font)
        self.VL_engWord_1.setObjectName("VL_engWord_1")
        self.VL_rusWord_1 = QtWidgets.QLabel(self.centralwidget)
        self.VL_rusWord_1.setGeometry(QtCore.QRect(550, 100, 141, 41))
        font = QtGui.QFont()
        font.setFamily(".Apple SD Gothic NeoI")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.VL_rusWord_1.setFont(font)
        self.VL_rusWord_1.setObjectName("VL_rusWord_1")
        self.VL_engTransl_1 = QtWidgets.QLabel(self.centralwidget)
        self.VL_engTransl_1.setGeometry(QtCore.QRect(680, 100, 131, 41))
        font = QtGui.QFont()
        font.setFamily(".Apple SD Gothic NeoI")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.VL_engTransl_1.setFont(font)
        self.VL_engTransl_1.setAutoFillBackground(False)
        self.VL_engTransl_1.setObjectName("VL_engTransl_1")
        self.VL_engSinonyms_1 = QtWidgets.QLabel(self.centralwidget)
        self.VL_engSinonyms_1.setGeometry(QtCore.QRect(840, 100, 131, 41))
        font = QtGui.QFont()
        font.setFamily(".Apple SD Gothic NeoI")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.VL_engSinonyms_1.setFont(font)
        self.VL_engSinonyms_1.setAutoFillBackground(False)
        self.VL_engSinonyms_1.setObjectName("VL_engSinonyms_1")
        self.VL_rusWord_2 = QtWidgets.QLabel(self.centralwidget)
        self.VL_rusWord_2.setGeometry(QtCore.QRect(550, 190, 141, 41))
        font = QtGui.QFont()
        font.setFamily(".Apple SD Gothic NeoI")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.VL_rusWord_2.setFont(font)
        self.VL_rusWord_2.setObjectName("VL_rusWord_2")
        self.VL_engTransl_2 = QtWidgets.QLabel(self.centralwidget)
        self.VL_engTransl_2.setGeometry(QtCore.QRect(680, 190, 131, 41))
        font = QtGui.QFont()
        font.setFamily(".Apple SD Gothic NeoI")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.VL_engTransl_2.setFont(font)
        self.VL_engTransl_2.setAutoFillBackground(False)
        self.VL_engTransl_2.setObjectName("VL_engTransl_2")
        self.VL_engSinonyms_2 = QtWidgets.QLabel(self.centralwidget)
        self.VL_engSinonyms_2.setGeometry(QtCore.QRect(840, 190, 131, 41))
        font = QtGui.QFont()
        font.setFamily(".Apple SD Gothic NeoI")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.VL_engSinonyms_2.setFont(font)
        self.VL_engSinonyms_2.setAutoFillBackground(False)
        self.VL_engSinonyms_2.setObjectName("VL_engSinonyms_2")
        self.VL_engWord_2 = QtWidgets.QLabel(self.centralwidget)
        self.VL_engWord_2.setGeometry(QtCore.QRect(400, 190, 141, 41))
        font = QtGui.QFont()
        font.setFamily(".Apple SD Gothic NeoI")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.VL_engWord_2.setFont(font)
        self.VL_engWord_2.setObjectName("VL_engWord_2")
        self.VL_rusWord_3 = QtWidgets.QLabel(self.centralwidget)
        self.VL_rusWord_3.setGeometry(QtCore.QRect(550, 280, 141, 41))
        font = QtGui.QFont()
        font.setFamily(".Apple SD Gothic NeoI")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.VL_rusWord_3.setFont(font)
        self.VL_rusWord_3.setObjectName("VL_rusWord_3")
        self.VL_engTransl_3 = QtWidgets.QLabel(self.centralwidget)
        self.VL_engTransl_3.setGeometry(QtCore.QRect(680, 280, 131, 41))
        font = QtGui.QFont()
        font.setFamily(".Apple SD Gothic NeoI")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.VL_engTransl_3.setFont(font)
        self.VL_engTransl_3.setAutoFillBackground(False)
        self.VL_engTransl_3.setObjectName("VL_engTransl_3")
        self.VL_engSinonyms_3 = QtWidgets.QLabel(self.centralwidget)
        self.VL_engSinonyms_3.setGeometry(QtCore.QRect(840, 280, 131, 41))
        font = QtGui.QFont()
        font.setFamily(".Apple SD Gothic NeoI")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.VL_engSinonyms_3.setFont(font)
        self.VL_engSinonyms_3.setAutoFillBackground(False)
        self.VL_engSinonyms_3.setObjectName("VL_engSinonyms_3")
        self.VL_engWord_3 = QtWidgets.QLabel(self.centralwidget)
        self.VL_engWord_3.setGeometry(QtCore.QRect(400, 280, 141, 41))
        font = QtGui.QFont()
        font.setFamily(".Apple SD Gothic NeoI")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.VL_engWord_3.setFont(font)
        self.VL_engWord_3.setObjectName("VL_engWord_3")
        self.VL_engSinonyms_4 = QtWidgets.QLabel(self.centralwidget)
        self.VL_engSinonyms_4.setGeometry(QtCore.QRect(840, 370, 131, 41))
        font = QtGui.QFont()
        font.setFamily(".Apple SD Gothic NeoI")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.VL_engSinonyms_4.setFont(font)
        self.VL_engSinonyms_4.setAutoFillBackground(False)
        self.VL_engSinonyms_4.setObjectName("VL_engSinonyms_4")
        self.VL_engWord_4 = QtWidgets.QLabel(self.centralwidget)
        self.VL_engWord_4.setGeometry(QtCore.QRect(400, 370, 141, 41))
        font = QtGui.QFont()
        font.setFamily(".Apple SD Gothic NeoI")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.VL_engWord_4.setFont(font)
        self.VL_engWord_4.setObjectName("VL_engWord_4")
        self.VL_engTransl_4 = QtWidgets.QLabel(self.centralwidget)
        self.VL_engTransl_4.setGeometry(QtCore.QRect(680, 370, 131, 41))
        font = QtGui.QFont()
        font.setFamily(".Apple SD Gothic NeoI")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.VL_engTransl_4.setFont(font)
        self.VL_engTransl_4.setAutoFillBackground(False)
        self.VL_engTransl_4.setObjectName("VL_engTransl_4")
        self.VL_rusWord_4 = QtWidgets.QLabel(self.centralwidget)
        self.VL_rusWord_4.setGeometry(QtCore.QRect(550, 370, 141, 41))
        font = QtGui.QFont()
        font.setFamily(".Apple SD Gothic NeoI")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.VL_rusWord_4.setFont(font)
        self.VL_rusWord_4.setObjectName("VL_rusWord_4")

        self.CardsButton = QtWidgets.QPushButton(self.centralwidget)
        self.CardsButton.setGeometry(QtCore.QRect(85, 380, 201, 51))
        font = QtGui.QFont()
        font.setFamily(".Apple SD Gothic NeoI")
        font.setPointSize(24)
        self.CardsButton.setFont(font)
        self.CardsButton.setObjectName("CardsButton")
        self.AddWordButton = QtWidgets.QPushButton(self.centralwidget)
        self.AddWordButton.setGeometry(QtCore.QRect(85, 160, 201, 51))
        font = QtGui.QFont()
        font.setFamily(".Apple SD Gothic NeoI")
        font.setPointSize(24)
        font.setBold(False)
        font.setWeight(50)
        self.AddWordButton.setFont(font)
        self.AddWordButton.setObjectName("AddWordButton")
        self.MyWordsButton = QtWidgets.QPushButton(self.centralwidget)
        self.MyWordsButton.setGeometry(QtCore.QRect(85, 270, 201, 51))
        font = QtGui.QFont()
        font.setFamily(".Apple SD Gothic NeoI")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.MyWordsButton.setFont(font)
        self.MyWordsButton.setObjectName("MyWordsButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1280, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.DictLabel.setText(_translate("MainWindow", "Словарь"))
        self.VocListLabel.setText(_translate("MainWindow", "Vocabulary List"))
        self.VL_engWord_1.setText(_translate("MainWindow", "1. sophisticated"))
        self.VL_rusWord_1.setText(_translate("MainWindow", "утонченный"))
        self.VL_engTransl_1.setText(_translate("MainWindow", "She has a sophisticated telescope"))
        self.VL_engSinonyms_1.setText(_translate("MainWindow", "complex, advanced, complicated"))
        self.VL_rusWord_2.setText(_translate("MainWindow", "утонченный"))
        self.VL_engTransl_2.setText(_translate("MainWindow", "She has a sophisticated telescope"))
        self.VL_engSinonyms_2.setText(_translate("MainWindow", "complex, advanced, complicated"))
        self.VL_engWord_2.setText(_translate("MainWindow", "1. sophisticated"))
        self.VL_rusWord_3.setText(_translate("MainWindow", "утонченный"))
        self.VL_engTransl_3.setText(_translate("MainWindow", "She has a sophisticated telescope"))
        self.VL_engSinonyms_3.setText(_translate("MainWindow", "complex, advanced, complicated"))
        self.VL_engWord_3.setText(_translate("MainWindow", "1. sophisticated"))
        self.VL_engSinonyms_4.setText(_translate("MainWindow", "complex, advanced, complicated"))
        self.VL_engWord_4.setText(_translate("MainWindow", "1. sophisticated"))
        self.VL_engTransl_4.setText(_translate("MainWindow", "She has a sophisticated telescope"))
        self.VL_rusWord_4.setText(_translate("MainWindow", "утонченный"))
        self.CardsButton.setText(_translate("MainWindow", "Карточки"))
        self.AddWordButton.setText(_translate("MainWindow", "Добавить слово"))
        self.MyWordsButton.setText(_translate("MainWindow", "Мои слова"))
