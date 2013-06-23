# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/mte90/Desktop/Prog/Penmode-Qt/settingsWindow.ui'
#
# Created: Sun Jun 23 22:30:58 2013
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

class Ui_settingsWindow(object):
    def setupUi(self, settingsWindow):
        settingsWindow.setObjectName(_fromUtf8("settingsWindow"))
        settingsWindow.resize(360, 454)
        self.centralwidget = QtGui.QWidget(settingsWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.GroupBox = QtGui.QGroupBox(self.centralwidget)
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
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.gridLayout.addWidget(self.pushButton, 1, 0, 1, 1)
        settingsWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(settingsWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 360, 22))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        settingsWindow.setMenuBar(self.menubar)

        self.retranslateUi(settingsWindow)
        QtCore.QMetaObject.connectSlotsByName(settingsWindow)

    def retranslateUi(self, settingsWindow):
        settingsWindow.setWindowTitle(_translate("settingsWindow", "Settings", None))
        self.GroupBox.setTitle(_translate("settingsWindow", "History", None))
        self.checkBox_2.setText(_translate("settingsWindow", "Nmap", None))
        self.niktoHistory.setText(_translate("settingsWindow", "Nikto", None))
        self.checkBox_3.setText(_translate("settingsWindow", "WhatWeb", None))
        self.checkBox_5.setText(_translate("settingsWindow", "WpScan", None))
        self.checkBox_6.setText(_translate("settingsWindow", "SkipFish", None))
        self.checkBox_4.setText(_translate("settingsWindow", "JoomScan", None))
        self.checkBox_8.setText(_translate("settingsWindow", "SlowLoris", None))
        self.checkBox_7.setText(_translate("settingsWindow", "SqlMap", None))
        self.resetHistory.setText(_translate("settingsWindow", "Reset History", None))
        self.pushButton.setText(_translate("settingsWindow", "Save Settings", None))

