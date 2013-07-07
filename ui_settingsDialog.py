# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/mte90/Desktop/Prog/Penmode-Qt/settingsDialog.ui'
#
# Created: Sun Jul  7 21:35:34 2013
#      by: PyQt4 UI code generator 4.10.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_settingsDialog(object):
    def setupUi(self, settingsDialog):
        settingsDialog.setObjectName(_fromUtf8("settingsDialog"))
        settingsDialog.resize(360, 308)
        self.gridLayout_4 = QtGui.QGridLayout(settingsDialog)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.pushSaveSettings = QtGui.QPushButton(settingsDialog)
        self.pushSaveSettings.setObjectName(_fromUtf8("pushSaveSettings"))
        self.gridLayout.addWidget(self.pushSaveSettings, 3, 0, 1, 1)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.GroupBox = QtGui.QGroupBox(settingsDialog)
        self.GroupBox.setObjectName(_fromUtf8("GroupBox"))
        self.gridLayout_2 = QtGui.QGridLayout(self.GroupBox)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.gridLayout_3 = QtGui.QGridLayout()
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.nmapHistory = QtGui.QCheckBox(self.GroupBox)
        self.nmapHistory.setObjectName(_fromUtf8("nmapHistory"))
        self.gridLayout_3.addWidget(self.nmapHistory, 0, 2, 1, 1)
        self.niktoHistory = QtGui.QCheckBox(self.GroupBox)
        self.niktoHistory.setObjectName(_fromUtf8("niktoHistory"))
        self.gridLayout_3.addWidget(self.niktoHistory, 1, 0, 1, 1)
        self.whatwebHistory = QtGui.QCheckBox(self.GroupBox)
        self.whatwebHistory.setObjectName(_fromUtf8("whatwebHistory"))
        self.gridLayout_3.addWidget(self.whatwebHistory, 0, 0, 1, 1)
        self.wpscanHistory = QtGui.QCheckBox(self.GroupBox)
        self.wpscanHistory.setObjectName(_fromUtf8("wpscanHistory"))
        self.gridLayout_3.addWidget(self.wpscanHistory, 2, 0, 1, 1)
        self.skipfishHistory = QtGui.QCheckBox(self.GroupBox)
        self.skipfishHistory.setObjectName(_fromUtf8("skipfishHistory"))
        self.gridLayout_3.addWidget(self.skipfishHistory, 2, 2, 1, 1)
        self.joomscanHistory = QtGui.QCheckBox(self.GroupBox)
        self.joomscanHistory.setObjectName(_fromUtf8("joomscanHistory"))
        self.gridLayout_3.addWidget(self.joomscanHistory, 1, 2, 1, 1)
        self.slowlorisHistory = QtGui.QCheckBox(self.GroupBox)
        self.slowlorisHistory.setObjectName(_fromUtf8("slowlorisHistory"))
        self.gridLayout_3.addWidget(self.slowlorisHistory, 3, 2, 1, 1)
        self.sqlmapHistory = QtGui.QCheckBox(self.GroupBox)
        self.sqlmapHistory.setObjectName(_fromUtf8("sqlmapHistory"))
        self.gridLayout_3.addWidget(self.sqlmapHistory, 3, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout_3, 0, 0, 1, 1)
        self.resetHistory = QtGui.QPushButton(self.GroupBox)
        self.resetHistory.setObjectName(_fromUtf8("resetHistory"))
        self.gridLayout_2.addWidget(self.resetHistory, 2, 0, 1, 1)
        self.verticalLayout.addWidget(self.GroupBox)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.enableAdvanced = QtGui.QCheckBox(settingsDialog)
        self.enableAdvanced.setObjectName(_fromUtf8("enableAdvanced"))
        self.gridLayout.addWidget(self.enableAdvanced, 2, 0, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.retranslateUi(settingsDialog)
        QtCore.QMetaObject.connectSlotsByName(settingsDialog)

    def retranslateUi(self, settingsDialog):
        settingsDialog.setWindowTitle(_translate("settingsDialog", "Settings", None))
        self.pushSaveSettings.setText(_translate("settingsDialog", "Save Settings", None))
        self.GroupBox.setTitle(_translate("settingsDialog", "History", None))
        self.nmapHistory.setText(_translate("settingsDialog", "Nmap", None))
        self.niktoHistory.setText(_translate("settingsDialog", "Nikto", None))
        self.whatwebHistory.setText(_translate("settingsDialog", "WhatWeb", None))
        self.wpscanHistory.setText(_translate("settingsDialog", "WpScan", None))
        self.skipfishHistory.setText(_translate("settingsDialog", "SkipFish", None))
        self.joomscanHistory.setText(_translate("settingsDialog", "JoomScan", None))
        self.slowlorisHistory.setText(_translate("settingsDialog", "SlowLoris", None))
        self.sqlmapHistory.setText(_translate("settingsDialog", "SqlMap", None))
        self.resetHistory.setText(_translate("settingsDialog", "Reset History", None))
        self.enableAdvanced.setText(_translate("settingsDialog", "Enable field for manual parameter", None))

