#!/usr/bin/python3
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import os,sys,signal
from subprocess import Popen, PIPE

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
        #Color Shell
        self.ui.shellWhatWeb.setStyleSheet(self.shell_color)
        self.ui.shellWhatWeb.setReadOnly(True)
        self.ui.shellNmap.setStyleSheet(self.shell_color)
        self.ui.shellNmap.setReadOnly(True)
        self.ui.shellNikto.setStyleSheet(self.shell_color)
        self.ui.shellNikto.setReadOnly(True)
        self.ui.shellJoomScan.setStyleSheet(self.shell_color)
        self.ui.shellJoomScan.setReadOnly(True)
        self.ui.shellWpScan.setStyleSheet(self.shell_color)
        self.ui.shellWpScan.setReadOnly(True)
        self.ui.shellSkipFish.setStyleSheet(self.shell_color)
        self.ui.shellSkipFish.setReadOnly(True)
        self.ui.shellSqlmap.setStyleSheet(self.shell_color)
        self.ui.shellSqlmap.setReadOnly(True)
        self.ui.shellSlowLoris.setStyleSheet(self.shell_color)
        self.ui.shellSlowLoris.setReadOnly(True)
        #Slot
        self.ui.pushSocat.clicked.connect(self.startStopSocat)
        signal.signal(signal.SIGINT, signal.SIG_DFL)
        self.show()

    def checkSocat(self):
        stdout = Popen('(ps caux | grep socat)', shell=True, stdout=PIPE).stdout
        stdout = str(stdout.read()).replace("b''",'')
        if stdout != '':
            return 1
        else:
            return 0
    
    def startStopSocat(self):
        if self.checkSocat() == 1:
            print(1)
            Popen('killall socat', shell=True, stdout=PIPE)
            self.ui.pushSocat.setText('Enable')
        else:
            print(2)
            Popen('socat TCP4-LISTEN:8080,fork SOCKS4a:127.0.0.1:$ip,socksport=9050 &', shell=True, stdout=PIPE)
            self.ui.pushSocat.setText('Disable')

def main():
    app = QApplication(sys.argv)
    MainWindow_ = QMainWindow()
    ui = MainWindow()
    ui.setupUi(MainWindow_)
    sys.exit(app.exec_())

main()