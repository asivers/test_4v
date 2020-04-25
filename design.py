# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import resource


class Ui_Dialog(object):
    def setupUi(self, Dialog, currRound):
        Dialog.setObjectName("Dialog")
        Dialog.resize(660, 720)
        self.pushButton_1 = QtWidgets.QPushButton(Dialog)
        self.pushButton_1.setGeometry(QtCore.QRect(20, 20, 300, 300))
        self.pushButton_1.setStyleSheet("background-image: url(:/newPrefix/pics/" + str(currRound) + "/1.jpg);")
        self.pushButton_1.setText("")
        self.pushButton_1.setObjectName("pushButton_1")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(340, 20, 300, 300))
        self.pushButton_2.setStyleSheet("background-image: url(:/newPrefix/pics/" + str(currRound) + "/2.jpg);")
        self.pushButton_2.setText("")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(20, 340, 300, 300))
        self.pushButton_3.setStyleSheet("background-image: url(:/newPrefix/pics/" + str(currRound) + "/3.jpg);")
        self.pushButton_3.setText("")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(Dialog)
        self.pushButton_4.setGeometry(QtCore.QRect(340, 340, 300, 300))
        self.pushButton_4.setStyleSheet("background-image: url(:/newPrefix/pics/" + str(currRound) + "/4.jpg);")
        self.pushButton_4.setText("")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_next = QtWidgets.QPushButton(Dialog)
        self.pushButton_next.setGeometry(QtCore.QRect(20, 660, 620, 40))
        self.pushButton_big = QtWidgets.QPushButton(Dialog)
        self.pushButton_big.setGeometry(QtCore.QRect(20, 20, 620, 620))
        self.pushButton_big.setEnabled(False)
        self.pushButton_1.setObjectName("pushButton_big")
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_next.setFont(font)
        self.pushButton_next.setStyleSheet("color: rgb(255, 255, 255);\n"
                                           "background-color: rgb(0, 0, 255);")
        self.pushButton_next.setObjectName("pushButton_next")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Начать тест"))
        self.pushButton_next.setText(_translate("Dialog", "Начать тест"))

