import sys
from PyQt5 import QtWidgets, QtGui
import ctypes
import design


class ExampleApp(QtWidgets.QMainWindow, design.Ui_Dialog):
    numberOfRounds = 7
    currRound = 0
    currPic = ""
    allChosenPics = []

    def __init__(self):
        super().__init__()
        self.setupUi(self, self.currRound)
        self.setWindowIcon(QtGui.QIcon("icon/icon.png"))
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(u'mycompany.myproduct.subproduct.version')
        self.pushButton_1.setVisible(False)
        self.pushButton_2.setVisible(False)
        self.pushButton_3.setVisible(False)
        self.pushButton_4.setVisible(False)
        self.pushButton_big.setVisible(True)
        self.pushButton_big.setStyleSheet("background-image: url(:/newPrefix/bigpic/start.jpg);")
        self.pushButton_1.clicked.connect(self.f1)
        self.pushButton_2.clicked.connect(self.f2)
        self.pushButton_3.clicked.connect(self.f3)
        self.pushButton_4.clicked.connect(self.f4)
        self.pushButton_next.clicked.connect(self.fNext)

    def enableAll(self):
        self.pushButton_1.setEnabled(True)
        self.pushButton_1.setStyleSheet("background-image: url(:/newPrefix/pics/" + str(self.currRound) + "/1.jpg)")
        self.pushButton_2.setEnabled(True)
        self.pushButton_2.setStyleSheet("background-image: url(:/newPrefix/pics/" + str(self.currRound) + "/2.jpg)")
        self.pushButton_3.setEnabled(True)
        self.pushButton_3.setStyleSheet("background-image: url(:/newPrefix/pics/" + str(self.currRound) + "/3.jpg)")
        self.pushButton_4.setEnabled(True)
        self.pushButton_4.setStyleSheet("background-image: url(:/newPrefix/pics/" + str(self.currRound) + "/4.jpg)")
        self.pushButton_next.setEnabled(True)
        self.pushButton_next.setStyleSheet("color: rgb(255, 255, 255);\n"
                                           "background-color: rgb(0, 0, 255);")

    def f1(self):
        self.enableAll()
        self.pushButton_1.setEnabled(False)
        self.pushButton_1.setStyleSheet("background-image: url(:/newPrefix/pics/" + str(self.currRound) +
                                        "/1.jpg); border: 5px solid blue")
        self.currPic = "1"

    def f2(self):
        self.enableAll()
        self.pushButton_2.setEnabled(False)
        self.pushButton_2.setStyleSheet("background-image: url(:/newPrefix/pics/" + str(self.currRound) +
                                        "/2.jpg); border: 5px solid blue")
        self.currPic = "2"

    def f3(self):
        self.enableAll()
        self.pushButton_3.setEnabled(False)
        self.pushButton_3.setStyleSheet("background-image: url(:/newPrefix/pics/" + str(self.currRound) +
                                        "/3.jpg); border: 5px solid blue")
        self.currPic = "3"

    def f4(self):
        self.enableAll()
        self.pushButton_4.setEnabled(False)
        self.pushButton_4.setStyleSheet("background-image: url(:/newPrefix/pics/" + str(self.currRound) +
                                        "/4.jpg); border: 5px solid blue")
        self.currPic = "4"

    def fNext(self):
        if self.currPic != "":
            self.allChosenPics.append(self.currPic)
        self.currRound += 1
        if self.currRound == 1:
            self.fRun()
            return
        if self.currRound == self.numberOfRounds + 1:
            self.fResult()
            return
        if self.currRound == self.numberOfRounds + 2:
            self.currRound = 1
            self.allChosenPics = []
            self.fRun()
            return
        self.enableAll()
        self.pushButton_next.setEnabled(False)
        self.pushButton_next.setStyleSheet("color: rgb(255, 255, 255);\n"
                                           "background-color: rgb(192, 192, 255);")

    def fRun(self):
        self.setWindowTitle("Выберите наилучший вариант")
        self.pushButton_next.setText("Выбрать")
        self.pushButton_big.setVisible(False)
        self.pushButton_1.setVisible(True)
        self.pushButton_2.setVisible(True)
        self.pushButton_3.setVisible(True)
        self.pushButton_4.setVisible(True)
        self.enableAll()
        self.pushButton_next.setEnabled(False)
        self.pushButton_next.setStyleSheet("color: rgb(255, 255, 255);\n"
                                           "background-color: rgb(192, 192, 255);")

    def fResult(self):
        self.pushButton_1.setVisible(False)
        self.pushButton_2.setVisible(False)
        self.pushButton_3.setVisible(False)
        self.pushButton_4.setVisible(False)
        self.pushButton_next.setEnabled(True)
        self.pushButton_next.setStyleSheet("color: rgb(255, 255, 255);\n"
                                           "background-color: rgb(0, 0, 255);")
        self.pushButton_big.setVisible(True)
        score = self.countScore()
        percentage = score * 100 / self.numberOfRounds
        if percentage > 55:
            self.pushButton_big.setStyleSheet("background-image: url(:/newPrefix/bigpic/final_good.jpg);")
        elif percentage > 27:
            self.pushButton_big.setStyleSheet("background-image: url(:/newPrefix/bigpic/final_average.jpg);")
        else:
            self.pushButton_big.setStyleSheet("background-image: url(:/newPrefix/bigpic/final_bad.jpg);")
        self.setWindowTitle("Ваш результат - " + str(round(percentage)) + "% !")
        self.pushButton_next.setText("Пройти еще раз")

    def countScore(self):
        _score = 0.
        if self.allChosenPics[1-1] == "3":
            _score += 1.
        if self.allChosenPics[2-1] == "1":
            _score += 1.
        if self.allChosenPics[3-1] == "2":
            _score += 1.
        if self.allChosenPics[4-1] == "4":
            _score += 1.
        if self.allChosenPics[5-1] == "2":
            _score += 1.
        if self.allChosenPics[6-1] == "3":
            _score += 1.
        if self.allChosenPics[7-1] == "4":
            _score += 1.
        return _score


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = ExampleApp()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
