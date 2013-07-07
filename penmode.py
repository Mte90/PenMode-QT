#!/usr/bin/python3
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import os,sys,signal
from subprocess import Popen, PIPE

from pencore.pencore import penmode
from ui_mainWindow import Ui_MainWindow
from settings import settingsDialog

class MainWindow ( QMainWindow , Ui_MainWindow):

	#var initialization
	settings = QSettings('Phos','Penmode')
	settings.setFallbacksEnabled(False)
	history = QSettings('Phos','Penmode_History')
	history.setFallbacksEnabled(False)
	version = 'V 0.1 Alpha'
	
	history_target = {}
	history_target['whatweb'] = []
	history_target['nmap'] = []
	history_target['nikto'] = []
	history_target['joomscan'] = []
	history_target['wpscan'] = []
	history_target['skipfish'] = []
	history_target['sqlmap'] = []
	history_target['slowloris'] = []
	
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
		self.ui.pushStartNmap.clicked.connect(self.nmap)
		self.ui.pushStartNikto.clicked.connect(self.nikto)
		self.ui.pushStartJoomScan.clicked.connect(self.joomScan)
		self.ui.pushStartWpScan.clicked.connect(self.wpScan)
		self.ui.pushStartSkipFish.clicked.connect(self.skipFish)
		self.ui.pushStartSqlMap.clicked.connect(self.sqlMap)
		self.ui.pushStartSlowLoris.clicked.connect(self.slowLoris)
		self.ui.actionSettings.triggered.connect(self.openSetting)
		#Load Config
		self.loadSetting()
		#Load History
		self.loadHistory()
		
		#load pencore
		self.pencore = penmode()
		self.pencore.set_gui(1)
		self.pencore.get_params()
		
		if self.pencore.get_target() != None:
			target = self.pencore.get_target()
			target = target.replace('\\n\'','')
			self.ui.whatwebTarget.setText(target)
			self.ui.nmapTarget.setText(target)
			self.ui.niktoTarget.setText(target)
			self.ui.joomscanTarget.setText(target)
			self.ui.wpscanTarget.setText(target)
			self.ui.skipfishTarget.setText(target)
			self.ui.sqlmapTarget.setText(target)
			self.ui.slowlorisTarget.setText(target)
		
		if self.checkTor() == 1:
			self.ui.pushTor.setText('Disable')
		else:
			self.startStopTor()
			
		if self.checkSocat() == 1:
			Popen('killall socat', shell=True, stdout=PIPE)
		signal.signal(signal.SIGINT, signal.SIG_DFL)
		self.show()
		
	def openSetting(self):
		#i need to explain this??
		window = QDialog()
		ui = settingsDialog()
		ui.setupUi(window)
		if ui.exec_() == 0:
			self.loadSetting()
		
	def loadSetting(self):
		#Check Field Parameter
		if self.settings.value('parameter_field') == 'True':
			self.ui.labelParameter_1.setEnabled(True)
			self.ui.whatwebParameter.setEnabled(True)
			self.ui.labelParameter_2.setEnabled(True)
			self.ui.nmapParameter.setEnabled(True)
			self.ui.labelParameter_3.setEnabled(True)
			self.ui.niktoParameter.setEnabled(True)
			self.ui.labelParameter_4.setEnabled(True)
			self.ui.joomscanParameter.setEnabled(True)
			self.ui.labelParameter_5.setEnabled(True)
			self.ui.wpscanParameter.setEnabled(True)
			self.ui.labelParameter_6.setEnabled(True)
			self.ui.skipfishParameter.setEnabled(True)
			self.ui.labelParameter_7.setEnabled(True)
			self.ui.sqlmapParameter.setEnabled(True)
			self.ui.labelParameter_8.setEnabled(True)
			self.ui.slowlorisParameter.setEnabled(True)
		else:
			self.ui.labelParameter_1.setEnabled(False)
			self.ui.whatwebParameter.setEnabled(False)
			self.ui.labelParameter_2.setEnabled(False)
			self.ui.nmapParameter.setEnabled(False)
			self.ui.labelParameter_3.setEnabled(False)
			self.ui.niktoParameter.setEnabled(False)
			self.ui.labelParameter_4.setEnabled(False)
			self.ui.joomscanParameter.setEnabled(False)
			self.ui.labelParameter_5.setEnabled(False)
			self.ui.wpscanParameter.setEnabled(False)
			self.ui.labelParameter_6.setEnabled(False)
			self.ui.skipfishParameter.setEnabled(False)
			self.ui.labelParameter_7.setEnabled(False)
			self.ui.sqlmapParameter.setEnabled(False)
			self.ui.labelParameter_8.setEnabled(False)
			self.ui.slowlorisParameter.setEnabled(False)
	
	def addHistory(self,tool,text):
		if text not in self.history_target[tool]:
			self.history_target[tool].append(text)
			self.history.setValue(tool,';'.join(self.history_target[tool]))
			
	def loadHistory(self):
		self.history_target['whatweb'] = str(self.history.value('whatweb')).split(';')
		self.history_target['nmap'] = str(self.history.value('nma')).split(';')
		self.history_target['nikto'] = str(self.history.value('nikto')).split(';')
		self.history_target['joomscan'] = str(self.history.value('joomscan')).split(';')
		self.history_target['wpscan'] = str(self.history.value('wpscan')).split(';')
		self.history_target['skipfish'] = str(self.history.value('skipfish')).split(';')
		self.history_target['sqlmap'] = str(self.history.value('sqlmap')).split(';')
		self.history_target['slowloris'] = str(self.history.value('slowloris')).split(';')
	
	def showTerminal(self,cmd,area):
		#Start Socat
		self.startSocat()
		#Pint the command in the console
		print(cmd)
		p = Popen(cmd + ' | sed -r "s/\x1B\[([0-9]{1,2}(;[0-9]{1,2})?)?[m|K]//g"', shell=True, stdout=PIPE).stdout
		stdout = ''
		while True:
			#read every line of the tool
			line = p.readline()
			line2 = str(line).replace("b'",'').replace('\\n\'','').replace('\\t','')
			stdout += line2
			area.append(line2)
			if not line:
				break

	def checkSocat(self):
		return self.pencore.check_socat()
	
	def startSocat(self):
		Popen('killall socat', shell=True, stdout=PIPE)
		self.pencore.start_socat()
		self.ui.pushSocat.setText('Disable')
				
	def startStopSocat(self):
		if self.pencore.get_target() != None:
			if self.checkSocat() == 1:
				Popen('killall socat', shell=True, stdout=PIPE)
				self.ui.pushSocat.setText('Enable')
			else:
				self.pencore.start_socat()
				self.ui.pushSocat.setText('Disable')
			
	def checkTor(self):
		return self.pencore.check_tor()
	
	def startStopTor(self):
		if self.checkTor() == 1:
			Popen('/etc/init.d/tor stop', shell=True, stdout=PIPE)
			self.ui.pushTor.setText('Enable')
		else:
			self.pencore.start_tor()
			self.ui.pushTor.setText('Disable')
			
	def checkTarget(self,target):
		if self.checkTor() == 0:
			self.startStopTor()
		if not target:
			QMessageBox.critical(self, "Error", "You have not inserted a target!")
			return False
		else:
			self.pencore.set_target(target)
			return True

	def whatWeb(self):
		if self.checkTarget(self.ui.whatwebTarget.text()):
			self.addHistory('whatweb',self.ui.whatwebTarget.text())
			self.showTerminal(self.pencore.whatweb(),self.ui.shellWhatWeb)
	
	def nmap(self):
		if self.checkTarget(self.ui.nmapTarget.text()):
			self.showTerminal(self.pencore.nmap(),self.ui.shellNmap)
	
	def nikto(self):
		if self.checkTarget(self.ui.niktoTarget.text()):
			self.showTerminal(self.pencore.nikto(),self.ui.shellNikto)

	def joomScan(self):
		if self.checkTarget(self.ui.joomscanTarget.text()):
			self.showTerminal(self.pencore.joomscan(),self.ui.shellJoomScan)
			
	def wpScan(self):
		if self.checkTarget(self.ui.wpscanTarget.text()):
			self.showTerminal(self.pencore.wpscan(),self.ui.shellWpScan)

	def skipFish(self):
		if self.checkTarget(self.ui.skipfishTarget.text()):
			self.showTerminal(self.pencore.skipfish(),self.ui.shellSkipFish)
			
	def sqlMap(self):
		if self.checkTarget(self.ui.sqlmapTarget.text()):
			self.showTerminal(self.pencore.sqlmap(),self.ui.shellSqlMap)
	
	def slowLoris(self):
		if self.checkTarget(self.ui.slowlorisTarget.text()):
			self.pencore.set_params('-timeout '+ str(self.ui.spinTimeout.value()) +' -request '+ str(self.ui.spinRequest.value()))
			self.showTerminal(self.pencore.slowloris(),self.ui.shellSlowLoris)
			
def main():
	app = QApplication(sys.argv)
	MainWindow_ = QMainWindow()
	ui = MainWindow()
	ui.setupUi(MainWindow_)
	sys.exit(app.exec_())

main()