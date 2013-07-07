#!/usr/bin/python3
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import os,sys,signal

from ui_settingsDialog import Ui_settingsDialog

class settingsDialog ( QDialog , Ui_settingsDialog):

	#var initialization
	settings = QSettings('Phos','Penmode')
	settings.setFallbacksEnabled(False)

	def __init__ ( self, parent = None ):
		QDialog.__init__( self, parent )
		self.ui = Ui_settingsDialog()
		self.ui.setupUi( self )
		self.ui.buttonBox.accepted.connect(self.saveSettings)
		
		# Load settings
		if self.settings.value('whatweb_history') == 'True':
			self.ui.whatwebHistory.setChecked(True)
		
		if self.settings.value('nmap_history') == 'True':
			self.ui.nmapHistory.setChecked(True)
		
		if self.settings.value('nikto_history') == 'True':
			self.ui.niktoHistory.setChecked(True)
		
		if self.settings.value('joomscan_history') == 'True':
			self.ui.joomscanHistory.setChecked(True)
		
		if self.settings.value('wpscan_history') == 'True':
			self.ui.wpscanHistory.setChecked(True)
		
		if self.settings.value('skipfish_history') == 'True':
			self.ui.skipfishHistory.setChecked(True)
		
		if self.settings.value('sqlmap_history') == 'True':
			self.ui.sqlmapHistory.setChecked(True)
		
		if self.settings.value('slowloris_history') == 'True':
			self.ui.slowlorisHistory.setChecked(True)
		
		if self.settings.value('parameter_field') == 'True':
			self.ui.enableAdvanced.setChecked(True)
		
		if self.settings.value('all_history') == 'True':
			self.ui.historyAll.setChecked(True)

	def saveSettings(self):
		# Tool history
		if self.ui.whatwebHistory.isChecked():
			self.settings.setValue('whatweb_history','True')
		else:
			self.settings.setValue('whatweb_history','False')
			
		if self.ui.nmapHistory.isChecked():
			self.settings.setValue('nmap_history','True')
		else:
			self.settings.setValue('nmap_history','False')
			
		if self.ui.niktoHistory.isChecked():
			self.settings.setValue('nikto_history','True')
		else:
			self.settings.setValue('nikto_history','False')
			
		if self.ui.joomscanHistory.isChecked():
			self.settings.setValue('joomscan_history','True')
		else:
			self.settings.setValue('joomscan_history','False')
		
		if self.ui.wpscanHistory.isChecked():
			self.settings.setValue('wpscan_history','True')
		else:
			self.settings.setValue('wpscan_history','False')
		
		if self.ui.skipfishHistory.isChecked():
			self.settings.setValue('skipfish_history','True')
		else:
			self.settings.setValue('skipfish_history','False')
		
		if self.ui.sqlmapHistory.isChecked():
			self.settings.setValue('sqlmap_history','True')
		else:
			self.settings.setValue('sqlmap_history','False')
		
		if self.ui.slowlorisHistory.isChecked():
			self.settings.setValue('slowloris_history','True')
		else:
			self.settings.setValue('slowloris_history','False')
			
		if self.ui.historyAll.isChecked():
			self.settings.setValue('all_history','True')
		else:
			self.settings.setValue('all_history','False')
		
		# Enable parameter field
		if self.ui.enableAdvanced.isChecked():
			self.settings.setValue('parameter_field','True')
		else:
			self.settings.setValue('parameter_field','False')
			
		self.close()