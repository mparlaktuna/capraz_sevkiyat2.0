import sys

from PyQt5.QtWidgets import *
from PyQt5 import QtGui, QtCore
from src.mainwindow import MainWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)

    mainWindow = MainWindow()
    mainWindow.show()
    app.exec_()
    sys.exit(0)