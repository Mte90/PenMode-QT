#!/usr/bin/python3
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import os,sys,signal

from ui_mainWindow import Ui_MainWindow

class MainWindow ( QMainWindow , Ui_MainWindow):

    #var initialization
    settings = QSettings('Phos','Penmode')
    settings.setFallbacksEnabled(False)
    version = 'V 0.1 Alpha'

    def __init__ ( self, parent = None ):
        QMainWindow.__init__( self, parent )
        self.ui = Ui_MainWindow()
        self.ui.setupUi( self )
        self.setWindowTitle('PenMode-QT - ' + self.version)
        self.shell_color = 'QTextEdit { background-color: black; color:#18F018; }'
        self.ui.shellWhatWeb.setStyleSheet(self.shell_color)
        self.ui.shellNmap.setStyleSheet(self.shell_color)
        self.ui.shellNikto.setStyleSheet(self.shell_color)
        self.ui.shellJoomScan.setStyleSheet(self.shell_color)
        self.ui.shellWpScan.setStyleSheet(self.shell_color)
        self.ui.shellSkipFish.setStyleSheet(self.shell_color)
        self.ui.shellSqlmap.setStyleSheet(self.shell_color)
        self.ui.shellSlowLoris.setStyleSheet(self.shell_color)
        signal.signal(signal.SIGINT, signal.SIG_DFL)
        self.show()


def main():
    app = QApplication(sys.argv)
    MainWindow_ = QMainWindow()
    ui = MainWindow()
    ui.setupUi(MainWindow_)
    sys.exit(app.exec_())

main()