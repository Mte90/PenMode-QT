#!/usr/bin/python3
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import os,sys,signal,re
from subprocess import Popen, PIPE

from pencore.pencore import penmode
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
		self.ui.pushTor.clicked.connect(self.startStopTor)
		self.ui.pushStartWhatWeb.clicked.connect(self.whatWeb)

		#load pencore
		self.pencore = penmode()
		self.pencore.set_gui(1)
		
		if self.checkSocat() == 1:
			self.ui.pushSocat.setText('Enabled')
			
		if self.checkTor() == 1:
			self.ui.pushTor.setText('Enabled')
		
		signal.signal(signal.SIGINT, signal.SIG_DFL)
		self.show()
	
	def closeEvent(self):
		self.checkSocat = 1
		self.startStopSocat()
	
	def showTerminal(self,cmd,area):
		area.append(cmd)
		p = Popen(cmd + ' | sed -r "s/\x1B\[([0-9]{1,2}(;[0-9]{1,2})?)?[m|K]//g"', shell=True, stdout=PIPE).stdout
		stdout = ''
		while True:
			line = p.readline()
			line2 = str(line).replace("b'",'').replace('\\n\'','').replace('\\t','')
			stdout += line2
			area.append(line2)
			if not line:
				break

	def checkSocat(self):
		return self.pencore.check_socat()
	
	def startStopSocat(self):
		if self.checkSocat() == 1:
			Popen('killall socat', shell=True, stdout=PIPE)
			self.ui.pushSocat.setText('Enable')
		else:
			Popen('socat TCP4-LISTEN:8080,fork SOCKS4a:127.0.0.1:$ip,socksport=9050 &', shell=True, stdout=PIPE)
			self.ui.pushSocat.setText('Disable')
			
	def checkTor(self):
		return self.pencore.check_tor()
	
	def startStopTor(self):
		if self.checkTor() == 1:
			Popen('su-to-root -X -c /etc/init.d/tor stop', shell=True, stdout=PIPE)
			self.ui.pushSocat.setText('Enable')
		else:
			Popen('su-to-root -X -c /etc/init.d/tor start', shell=True, stdout=PIPE)
			self.ui.pushSocat.setText('Disable')
			
	def whatWeb(self):
		self.pencore.set_target(self.ui.whatwebTarget.text())
		self.showTerminal(self.pencore.whatweb(),self.ui.shellWhatWeb)

def main():
	app = QApplication(sys.argv)
	MainWindow_ = QMainWindow()
	ui = MainWindow()
	ui.setupUi(MainWindow_)
	sys.exit(app.exec_())

main()