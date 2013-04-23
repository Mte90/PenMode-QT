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
        signal.signal(signal.SIGINT, signal.SIG_DFL)
        self.show()


def main():
    app = QApplication(sys.argv)
    MainWindow_ = QMainWindow()
    ui = MainWindow()
    ui.setupUi(MainWindow_)
    sys.exit(app.exec_())

main()