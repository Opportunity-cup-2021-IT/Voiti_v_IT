import sys
import pandas as pd
from PyQt5.QtCore import Qt, QCoreApplication
from PyQt5.QtWidgets import (QApplication, QMainWindow, QToolTip, QPushButton,
                             QLabel, QLineEdit, QTextEdit, QGridLayout, QAction,
                             QFileDialog, QToolBar, QMenu, QMessageBox)
from PyQt5.QtGui import QIcon, QFont


class Window(QMainWindow):

    def __init__(self):
        super().__init__()
        self.textEdit = QTextEdit()
        self.width = 1300
        self.height = 800
        self.Landing()

        self.setGeometry(50, 50, self.width, self.height)
        self.setWindowTitle("Prototype: PAT (predictive analytics tool)")
        self.setWindowIcon(QIcon('LogoT.png'))
        self.show()

    def Landing(self):
        QToolTip.setFont(QFont('SansSerif', 25))
        self.createNavBar()

        qW = 80
        qH = 30

        sW = 200
        sH = 80

        startBtn = QPushButton('START', self)
        # startBtn.clicked.connect(QCoreApplication.instance())
        startBtn.resize(sW, sH)
        startBtn.move((self.width - sW) // 2, (self.height - sH) // 2)

        quitBtn = QPushButton('Quit', self)
        quitBtn.clicked.connect(QCoreApplication.instance().quit)
        quitBtn.resize(qW, qH)
        quitBtn.move((self.width - qW) // 2, self.height // 2 + sH)

        self.show()

    def StartPg(self):
        QToolTip.setFont(QFont('SansSerif', 25))

        ID = QLabel('ID of work')
        Shift = QLabel('Time shift')

        IDEdit = QLineEdit()
        ShiftEdit = QLineEdit()

        grid = QGridLayout()
        grid.setSpacing(10)

        grid.addWidget(ID, 1, 0)
        grid.addWidget(IDEdit, 1, 1)
        grid.addWidget(Shift, 2, 0)
        grid.addWidget(ShiftEdit, 2, 1)

        self.setLayout(grid)
        self.show()
        print("Start")

    def GetFilePg(self):
        self.setCentralWidget(self.textEdit)
        self.statusBar()

        openFile = QAction(QIcon('open.png'), 'Open', self)
        openFile.setShortcut('Ctrl+O')
        openFile.setStatusTip('Open new File')
        openFile.triggered.connect(self.showDialog)

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(openFile)

        self.show()

    def showDialog(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file', '/home')[0]

        f = open(fname, 'r')

        with f:
            data = f.read()
            self.textEdit.setText(data)

    def createNavBar(self):
        navBar = self.menuBar()
        inputMenu = navBar.addMenu("Input")
        resMenu = navBar.addMenu("Result")
        helpMenu = navBar.addMenu("Help")
        aboutMenu = navBar.addMenu("About")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()

    sys.exit(app.exec_())


def CreateWindow():
    app = QApplication(sys.argv)
    window = Window()
    window.GetFilePg()

    sys.exit(app.exec_())


def GetFile(window):
    window.StartPg()
    window.GetFilePg()


def ShowRes():
    pass
