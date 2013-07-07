# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/mte90/Desktop/Prog/Penmode-Qt/settingsDialog.ui'
#
# Created: Sun Jul  7 17:54:55 2013
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
        self.pushButton = QtGui.QPushButton(settingsDialog)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.gridLayout.addWidget(self.pushButton, 3, 0, 1, 1)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.GroupBox = QtGui.QGroupBox(settingsDialog)
        self.GroupBox.setObjectName(_fromUtf8("GroupBox"))
        self.gridLayout_2 = QtGui.QGridLayout(self.GroupBox)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.gridLayout_3 = QtGui.QGridLayout()
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.checkBox_2 = QtGui.QCheckBox(self.GroupBox)
        self.checkBox_2.setObjectName(_fromUtf8("checkBox_2"))
        self.gridLayout_3.addWidget(self.checkBox_2, 0, 2, 1, 1)
        self.niktoHistory = QtGui.QCheckBox(self.GroupBox)
        self.niktoHistory.setObjectName(_fromUtf8("niktoHistory"))
        self.gridLayout_3.addWidget(self.niktoHistory, 1, 0, 1, 1)
        self.checkBox_3 = QtGui.QCheckBox(self.GroupBox)
        self.checkBox_3.setObjectName(_fromUtf8("checkBox_3"))
        self.gridLayout_3.addWidget(self.checkBox_3, 0, 0, 1, 1)
        self.checkBox_5 = QtGui.QCheckBox(self.GroupBox)
        self.checkBox_5.setObjectName(_fromUtf8("checkBox_5"))
        self.gridLayout_3.addWidget(self.checkBox_5, 2, 0, 1, 1)
        self.checkBox_6 = QtGui.QCheckBox(self.GroupBox)
        self.checkBox_6.setObjectName(_fromUtf8("checkBox_6"))
        self.gridLayout_3.addWidget(self.checkBox_6, 2, 2, 1, 1)
        self.checkBox_4 = QtGui.QCheckBox(self.GroupBox)
        self.checkBox_4.setObjectName(_fromUtf8("checkBox_4"))
        self.gridLayout_3.addWidget(self.checkBox_4, 1, 2, 1, 1)
        self.checkBox_8 = QtGui.QCheckBox(self.GroupBox)
        self.checkBox_8.setObjectName(_fromUtf8("checkBox_8"))
        self.gridLayout_3.addWidget(self.checkBox_8, 3, 2, 1, 1)
        self.checkBox_7 = QtGui.QCheckBox(self.GroupBox)
        self.checkBox_7.setObjectName(_fromUtf8("checkBox_7"))
        self.gridLayout_3.addWidget(self.checkBox_7, 3, 0, 1, 1)
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
        self.pushButton.setText(_translate("settingsDialog", "Save Settings", None))
        self.GroupBox.setTitle(_translate("settingsDialog", "History", None))
        self.checkBox_2.setText(_translate("settingsDialog", "Nmap", None))
        self.niktoHistory.setText(_translate("settingsDialog", "Nikto", None))
        self.checkBox_3.setText(_translate("settingsDialog", "WhatWeb", None))
        self.checkBox_5.setText(_translate("settingsDialog", "WpScan", None))
        self.checkBox_6.setText(_translate("settingsDialog", "SkipFish", None))
        self.checkBox_4.setText(_translate("settingsDialog", "JoomScan", None))
        self.checkBox_8.setText(_translate("settingsDialog", "SlowLoris", None))
        self.checkBox_7.setText(_translate("settingsDialog", "SqlMap", None))
        self.resetHistory.setText(_translate("settingsDialog", "Reset History", None))
        self.enableAdvanced.setText(_translate("settingsDialog", "Enable field for manual parameter", None))

