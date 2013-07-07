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

		signal.signal(signal.SIGINT, signal.SIG_DFL)
		self.show()
