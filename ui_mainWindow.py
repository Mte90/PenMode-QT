# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/mte90/Desktop/Prog/Penmode-Qt/mainWindow.ui'
#
# Created: Wed Apr 24 23:21:49 2013
#      by: PyQt4 UI code generator 4.9.6
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(649, 336)
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.gridLayout_2.addWidget(self.pushButton, 0, 1, 1, 1)
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout_2.addWidget(self.label_2, 0, 2, 1, 1)
        self.pushButton_2 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_2.setEnabled(True)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.gridLayout_2.addWidget(self.pushButton_2, 0, 3, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_2, 0, 0, 1, 1)
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab_whatweb = QtGui.QWidget()
        self.tab_whatweb.setObjectName(_fromUtf8("tab_whatweb"))
        self.gridLayout_4 = QtGui.QGridLayout(self.tab_whatweb)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.gridLayout_3 = QtGui.QGridLayout()
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.label_3 = QtGui.QLabel(self.tab_whatweb)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout_3.addWidget(self.label_3, 0, 0, 1, 1)
        self.whatwebTarget = QtGui.QLineEdit(self.tab_whatweb)
        self.whatwebTarget.setObjectName(_fromUtf8("whatwebTarget"))
        self.gridLayout_3.addWidget(self.whatwebTarget, 0, 1, 1, 1)
        self.gridLayout_5 = QtGui.QGridLayout()
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem, 0, 1, 1, 1)
        self.pushStartWhatWeb = QtGui.QPushButton(self.tab_whatweb)
        self.pushStartWhatWeb.setObjectName(_fromUtf8("pushStartWhatWeb"))
        self.gridLayout_5.addWidget(self.pushStartWhatWeb, 0, 0, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_5.addItem(spacerItem1, 1, 1, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_5, 1, 1, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_3, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_whatweb, _fromUtf8(""))
        self.tab_nmap = QtGui.QWidget()
        self.tab_nmap.setObjectName(_fromUtf8("tab_nmap"))
        self.gridLayout_8 = QtGui.QGridLayout(self.tab_nmap)
        self.gridLayout_8.setObjectName(_fromUtf8("gridLayout_8"))
        self.gridLayout_6 = QtGui.QGridLayout()
        self.gridLayout_6.setObjectName(_fromUtf8("gridLayout_6"))
        self.label_4 = QtGui.QLabel(self.tab_nmap)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout_6.addWidget(self.label_4, 0, 0, 1, 1)
        self.nmapTarget = QtGui.QLineEdit(self.tab_nmap)
        self.nmapTarget.setObjectName(_fromUtf8("nmapTarget"))
        self.gridLayout_6.addWidget(self.nmapTarget, 0, 1, 1, 1)
        self.gridLayout_7 = QtGui.QGridLayout()
        self.gridLayout_7.setObjectName(_fromUtf8("gridLayout_7"))
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_7.addItem(spacerItem2, 0, 1, 1, 1)
        self.pushStartNmap = QtGui.QPushButton(self.tab_nmap)
        self.pushStartNmap.setObjectName(_fromUtf8("pushStartNmap"))
        self.gridLayout_7.addWidget(self.pushStartNmap, 0, 0, 1, 1)
        spacerItem3 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_7.addItem(spacerItem3, 1, 1, 1, 1)
        self.gridLayout_6.addLayout(self.gridLayout_7, 1, 1, 1, 1)
        self.gridLayout_8.addLayout(self.gridLayout_6, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_nmap, _fromUtf8(""))
        self.tab_nikto = QtGui.QWidget()
        self.tab_nikto.setObjectName(_fromUtf8("tab_nikto"))
        self.gridLayout_11 = QtGui.QGridLayout(self.tab_nikto)
        self.gridLayout_11.setObjectName(_fromUtf8("gridLayout_11"))
        self.gridLayout_9 = QtGui.QGridLayout()
        self.gridLayout_9.setObjectName(_fromUtf8("gridLayout_9"))
        self.label_5 = QtGui.QLabel(self.tab_nikto)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout_9.addWidget(self.label_5, 0, 0, 1, 1)
        self.whatwebTarget_2 = QtGui.QLineEdit(self.tab_nikto)
        self.whatwebTarget_2.setObjectName(_fromUtf8("whatwebTarget_2"))
        self.gridLayout_9.addWidget(self.whatwebTarget_2, 0, 1, 1, 1)
        self.gridLayout_10 = QtGui.QGridLayout()
        self.gridLayout_10.setObjectName(_fromUtf8("gridLayout_10"))
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_10.addItem(spacerItem4, 0, 1, 1, 1)
        self.pushStartNikto = QtGui.QPushButton(self.tab_nikto)
        self.pushStartNikto.setObjectName(_fromUtf8("pushStartNikto"))
        self.gridLayout_10.addWidget(self.pushStartNikto, 0, 0, 1, 1)
        spacerItem5 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_10.addItem(spacerItem5, 1, 1, 1, 1)
        self.gridLayout_9.addLayout(self.gridLayout_10, 1, 1, 1, 1)
        self.gridLayout_11.addLayout(self.gridLayout_9, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_nikto, _fromUtf8(""))
        self.tab_joomscan = QtGui.QWidget()
        self.tab_joomscan.setObjectName(_fromUtf8("tab_joomscan"))
        self.gridLayout_17 = QtGui.QGridLayout(self.tab_joomscan)
        self.gridLayout_17.setObjectName(_fromUtf8("gridLayout_17"))
        self.gridLayout_15 = QtGui.QGridLayout()
        self.gridLayout_15.setObjectName(_fromUtf8("gridLayout_15"))
        self.label_9 = QtGui.QLabel(self.tab_joomscan)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.gridLayout_15.addWidget(self.label_9, 0, 0, 1, 1)
        self.joomscanTarget = QtGui.QLineEdit(self.tab_joomscan)
        self.joomscanTarget.setObjectName(_fromUtf8("joomscanTarget"))
        self.gridLayout_15.addWidget(self.joomscanTarget, 0, 1, 1, 1)
        self.gridLayout_16 = QtGui.QGridLayout()
        self.gridLayout_16.setObjectName(_fromUtf8("gridLayout_16"))
        spacerItem6 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_16.addItem(spacerItem6, 0, 1, 1, 1)
        self.pushStartJoomScan = QtGui.QPushButton(self.tab_joomscan)
        self.pushStartJoomScan.setObjectName(_fromUtf8("pushStartJoomScan"))
        self.gridLayout_16.addWidget(self.pushStartJoomScan, 0, 0, 1, 1)
        spacerItem7 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_16.addItem(spacerItem7, 1, 1, 1, 1)
        self.gridLayout_15.addLayout(self.gridLayout_16, 1, 1, 1, 1)
        self.gridLayout_17.addLayout(self.gridLayout_15, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_joomscan, _fromUtf8(""))
        self.tab_wpscan = QtGui.QWidget()
        self.tab_wpscan.setObjectName(_fromUtf8("tab_wpscan"))
        self.gridLayout_20 = QtGui.QGridLayout(self.tab_wpscan)
        self.gridLayout_20.setObjectName(_fromUtf8("gridLayout_20"))
        self.gridLayout_18 = QtGui.QGridLayout()
        self.gridLayout_18.setObjectName(_fromUtf8("gridLayout_18"))
        self.label_10 = QtGui.QLabel(self.tab_wpscan)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.gridLayout_18.addWidget(self.label_10, 0, 0, 1, 1)
        self.wpscanTarget = QtGui.QLineEdit(self.tab_wpscan)
        self.wpscanTarget.setObjectName(_fromUtf8("wpscanTarget"))
        self.gridLayout_18.addWidget(self.wpscanTarget, 0, 1, 1, 1)
        self.gridLayout_19 = QtGui.QGridLayout()
        self.gridLayout_19.setObjectName(_fromUtf8("gridLayout_19"))
        spacerItem8 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_19.addItem(spacerItem8, 0, 1, 1, 1)
        self.pushStartWpScan = QtGui.QPushButton(self.tab_wpscan)
        self.pushStartWpScan.setObjectName(_fromUtf8("pushStartWpScan"))
        self.gridLayout_19.addWidget(self.pushStartWpScan, 0, 0, 1, 1)
        spacerItem9 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_19.addItem(spacerItem9, 1, 1, 1, 1)
        self.gridLayout_18.addLayout(self.gridLayout_19, 1, 1, 1, 1)
        self.gridLayout_20.addLayout(self.gridLayout_18, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_wpscan, _fromUtf8(""))
        self.tab_skipfish = QtGui.QWidget()
        self.tab_skipfish.setObjectName(_fromUtf8("tab_skipfish"))
        self.gridLayout_23 = QtGui.QGridLayout(self.tab_skipfish)
        self.gridLayout_23.setObjectName(_fromUtf8("gridLayout_23"))
        self.gridLayout_21 = QtGui.QGridLayout()
        self.gridLayout_21.setObjectName(_fromUtf8("gridLayout_21"))
        self.label_11 = QtGui.QLabel(self.tab_skipfish)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.gridLayout_21.addWidget(self.label_11, 0, 0, 1, 1)
        self.skipfishTarget = QtGui.QLineEdit(self.tab_skipfish)
        self.skipfishTarget.setObjectName(_fromUtf8("skipfishTarget"))
        self.gridLayout_21.addWidget(self.skipfishTarget, 0, 1, 1, 1)
        self.gridLayout_22 = QtGui.QGridLayout()
        self.gridLayout_22.setObjectName(_fromUtf8("gridLayout_22"))
        spacerItem10 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_22.addItem(spacerItem10, 0, 1, 1, 1)
        self.pushStartSkipFish = QtGui.QPushButton(self.tab_skipfish)
        self.pushStartSkipFish.setObjectName(_fromUtf8("pushStartSkipFish"))
        self.gridLayout_22.addWidget(self.pushStartSkipFish, 0, 0, 1, 1)
        spacerItem11 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_22.addItem(spacerItem11, 1, 1, 1, 1)
        self.gridLayout_21.addLayout(self.gridLayout_22, 1, 1, 1, 1)
        self.gridLayout_23.addLayout(self.gridLayout_21, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_skipfish, _fromUtf8(""))
        self.tab_sqlmap = QtGui.QWidget()
        self.tab_sqlmap.setObjectName(_fromUtf8("tab_sqlmap"))
        self.gridLayout_26 = QtGui.QGridLayout(self.tab_sqlmap)
        self.gridLayout_26.setObjectName(_fromUtf8("gridLayout_26"))
        self.gridLayout_24 = QtGui.QGridLayout()
        self.gridLayout_24.setObjectName(_fromUtf8("gridLayout_24"))
        self.label_12 = QtGui.QLabel(self.tab_sqlmap)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.gridLayout_24.addWidget(self.label_12, 0, 0, 1, 1)
        self.sqlmapTarget = QtGui.QLineEdit(self.tab_sqlmap)
        self.sqlmapTarget.setObjectName(_fromUtf8("sqlmapTarget"))
        self.gridLayout_24.addWidget(self.sqlmapTarget, 0, 1, 1, 1)
        self.gridLayout_25 = QtGui.QGridLayout()
        self.gridLayout_25.setObjectName(_fromUtf8("gridLayout_25"))
        spacerItem12 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_25.addItem(spacerItem12, 0, 1, 1, 1)
        self.pushStartSqlMap = QtGui.QPushButton(self.tab_sqlmap)
        self.pushStartSqlMap.setObjectName(_fromUtf8("pushStartSqlMap"))
        self.gridLayout_25.addWidget(self.pushStartSqlMap, 0, 0, 1, 1)
        spacerItem13 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_25.addItem(spacerItem13, 1, 1, 1, 1)
        self.gridLayout_24.addLayout(self.gridLayout_25, 1, 1, 1, 1)
        self.gridLayout_26.addLayout(self.gridLayout_24, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_sqlmap, _fromUtf8(""))
        self.tab_slowloris = QtGui.QWidget()
        self.tab_slowloris.setObjectName(_fromUtf8("tab_slowloris"))
        self.gridLayout_14 = QtGui.QGridLayout(self.tab_slowloris)
        self.gridLayout_14.setObjectName(_fromUtf8("gridLayout_14"))
        self.gridLayout_12 = QtGui.QGridLayout()
        self.gridLayout_12.setObjectName(_fromUtf8("gridLayout_12"))
        self.label_6 = QtGui.QLabel(self.tab_slowloris)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout_12.addWidget(self.label_6, 0, 0, 1, 1)
        self.slowlorisTarget = QtGui.QLineEdit(self.tab_slowloris)
        self.slowlorisTarget.setObjectName(_fromUtf8("slowlorisTarget"))
        self.gridLayout_12.addWidget(self.slowlorisTarget, 0, 1, 1, 1)
        self.gridLayout_13 = QtGui.QGridLayout()
        self.gridLayout_13.setObjectName(_fromUtf8("gridLayout_13"))
        spacerItem14 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_13.addItem(spacerItem14, 0, 1, 1, 1)
        self.pushStartSlowLoris = QtGui.QPushButton(self.tab_slowloris)
        self.pushStartSlowLoris.setObjectName(_fromUtf8("pushStartSlowLoris"))
        self.gridLayout_13.addWidget(self.pushStartSlowLoris, 0, 0, 1, 1)
        spacerItem15 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_13.addItem(spacerItem15, 1, 1, 1, 1)
        self.gridLayout_12.addLayout(self.gridLayout_13, 3, 1, 1, 1)
        self.label_7 = QtGui.QLabel(self.tab_slowloris)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.gridLayout_12.addWidget(self.label_7, 1, 0, 1, 1)
        self.label_8 = QtGui.QLabel(self.tab_slowloris)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.gridLayout_12.addWidget(self.label_8, 2, 0, 1, 1)
        self.spinTimeout = QtGui.QSpinBox(self.tab_slowloris)
        self.spinTimeout.setObjectName(_fromUtf8("spinTimeout"))
        self.gridLayout_12.addWidget(self.spinTimeout, 2, 1, 1, 1)
        self.spinRequest = QtGui.QSpinBox(self.tab_slowloris)
        self.spinRequest.setObjectName(_fromUtf8("spinRequest"))
        self.gridLayout_12.addWidget(self.spinRequest, 1, 1, 1, 1)
        self.gridLayout_14.addLayout(self.gridLayout_12, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_slowloris, _fromUtf8(""))
        self.tab_exploit = QtGui.QWidget()
        self.tab_exploit.setObjectName(_fromUtf8("tab_exploit"))
        self.tabWidget.addTab(self.tab_exploit, _fromUtf8(""))
        self.tab_dork = QtGui.QWidget()
        self.tab_dork.setObjectName(_fromUtf8("tab_dork"))
        self.tabWidget.addTab(self.tab_dork, _fromUtf8(""))
        self.gridLayout.addWidget(self.tabWidget, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 649, 22))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        self.menuAbout = QtGui.QMenu(self.menubar)
        self.menuAbout.setObjectName(_fromUtf8("menuAbout"))
        self.menuSettings = QtGui.QMenu(self.menubar)
        self.menuSettings.setObjectName(_fromUtf8("menuSettings"))
        MainWindow.setMenuBar(self.menubar)
        self.actionSocat = QtGui.QAction(MainWindow)
        self.actionSocat.setObjectName(_fromUtf8("actionSocat"))
        self.actionTor = QtGui.QAction(MainWindow)
        self.actionTor.setObjectName(_fromUtf8("actionTor"))
        self.actionWhatWeb = QtGui.QAction(MainWindow)
        self.actionWhatWeb.setObjectName(_fromUtf8("actionWhatWeb"))
        self.actionNmap = QtGui.QAction(MainWindow)
        self.actionNmap.setObjectName(_fromUtf8("actionNmap"))
        self.actionNikto = QtGui.QAction(MainWindow)
        self.actionNikto.setObjectName(_fromUtf8("actionNikto"))
        self.actionJoomScan = QtGui.QAction(MainWindow)
        self.actionJoomScan.setObjectName(_fromUtf8("actionJoomScan"))
        self.actionWpScan = QtGui.QAction(MainWindow)
        self.actionWpScan.setObjectName(_fromUtf8("actionWpScan"))
        self.actionSkipFish = QtGui.QAction(MainWindow)
        self.actionSkipFish.setObjectName(_fromUtf8("actionSkipFish"))
        self.actionSqlmap = QtGui.QAction(MainWindow)
        self.actionSqlmap.setObjectName(_fromUtf8("actionSqlmap"))
        self.actionAbout_Penmode = QtGui.QAction(MainWindow)
        self.actionAbout_Penmode.setObjectName(_fromUtf8("actionAbout_Penmode"))
        self.actionAbout_Phos = QtGui.QAction(MainWindow)
        self.actionAbout_Phos.setObjectName(_fromUtf8("actionAbout_Phos"))
        self.menuHelp.addAction(self.actionSocat)
        self.menuHelp.addAction(self.actionTor)
        self.menuHelp.addAction(self.actionWhatWeb)
        self.menuHelp.addAction(self.actionNmap)
        self.menuHelp.addAction(self.actionNikto)
        self.menuHelp.addAction(self.actionJoomScan)
        self.menuHelp.addAction(self.actionWpScan)
        self.menuHelp.addAction(self.actionSkipFish)
        self.menuHelp.addAction(self.actionSqlmap)
        self.menuAbout.addAction(self.actionAbout_Penmode)
        self.menuAbout.addSeparator()
        self.menuAbout.addAction(self.actionAbout_Phos)
        self.menubar.addAction(self.menuSettings.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(7)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.pushButton.setText(_translate("MainWindow", "Enable", None))
        self.label.setText(_translate("MainWindow", "Socat", None))
        self.label_2.setText(_translate("MainWindow", "Tor", None))
        self.pushButton_2.setText(_translate("MainWindow", "Enable", None))
        self.label_3.setText(_translate("MainWindow", "Target", None))
        self.pushStartWhatWeb.setText(_translate("MainWindow", "Start", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_whatweb), _translate("MainWindow", "WhatWeb", None))
        self.label_4.setText(_translate("MainWindow", "Target", None))
        self.pushStartNmap.setText(_translate("MainWindow", "Start", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_nmap), _translate("MainWindow", "Nmap", None))
        self.label_5.setText(_translate("MainWindow", "Target", None))
        self.pushStartNikto.setText(_translate("MainWindow", "Start", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_nikto), _translate("MainWindow", "Nikto", None))
        self.label_9.setText(_translate("MainWindow", "Target", None))
        self.pushStartJoomScan.setText(_translate("MainWindow", "Start", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_joomscan), _translate("MainWindow", "JoomScan", None))
        self.label_10.setText(_translate("MainWindow", "Target", None))
        self.pushStartWpScan.setText(_translate("MainWindow", "Start", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_wpscan), _translate("MainWindow", "WpScan", None))
        self.label_11.setText(_translate("MainWindow", "Target", None))
        self.pushStartSkipFish.setText(_translate("MainWindow", "Start", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_skipfish), _translate("MainWindow", "SkipFish", None))
        self.label_12.setText(_translate("MainWindow", "Target", None))
        self.pushStartSqlMap.setText(_translate("MainWindow", "Start", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_sqlmap), _translate("MainWindow", "SqlMap", None))
        self.label_6.setText(_translate("MainWindow", "Target", None))
        self.pushStartSlowLoris.setText(_translate("MainWindow", "Start", None))
        self.label_7.setText(_translate("MainWindow", "Requests Number", None))
        self.label_8.setText(_translate("MainWindow", "TimeOut (sec)", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_slowloris), _translate("MainWindow", "SlowLoris", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_exploit), _translate("MainWindow", "Exploit", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_dork), _translate("MainWindow", "Dork", None))
        self.menuHelp.setTitle(_translate("MainWindow", "Help", None))
        self.menuAbout.setTitle(_translate("MainWindow", "About", None))
        self.menuSettings.setTitle(_translate("MainWindow", "Settings", None))
        self.actionSocat.setText(_translate("MainWindow", "Socat", None))
        self.actionTor.setText(_translate("MainWindow", "Tor", None))
        self.actionWhatWeb.setText(_translate("MainWindow", "WhatWeb", None))
        self.actionNmap.setText(_translate("MainWindow", "Nmap", None))
        self.actionNikto.setText(_translate("MainWindow", "Nikto", None))
        self.actionJoomScan.setText(_translate("MainWindow", "JoomScan", None))
        self.actionWpScan.setText(_translate("MainWindow", "WpScan", None))
        self.actionSkipFish.setText(_translate("MainWindow", "SkipFish", None))
        self.actionSqlmap.setText(_translate("MainWindow", "Sqlmap", None))
        self.actionAbout_Penmode.setText(_translate("MainWindow", "About Penmode", None))
        self.actionAbout_Phos.setText(_translate("MainWindow", "About Phos", None))

