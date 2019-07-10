# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interface.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1006, 813)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.objectTypesLabel = QtWidgets.QLabel(self.centralwidget)
        self.objectTypesLabel.setObjectName("objectTypesLabel")
        self.verticalLayout.addWidget(self.objectTypesLabel)
        self.objectTypes = QtWidgets.QComboBox(self.centralwidget)
        self.objectTypes.setObjectName("objectTypes")
        self.verticalLayout.addWidget(self.objectTypes)
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.startFeedBtn = QtWidgets.QPushButton(self.groupBox)
        self.startFeedBtn.setObjectName("startFeedBtn")
        self.verticalLayout_2.addWidget(self.startFeedBtn)
        self.stopFeedBtn = QtWidgets.QPushButton(self.groupBox)
        self.stopFeedBtn.setObjectName("stopFeedBtn")
        self.verticalLayout_2.addWidget(self.stopFeedBtn)
        self.captureImageBtn = QtWidgets.QPushButton(self.groupBox)
        self.captureImageBtn.setObjectName("captureImageBtn")
        self.verticalLayout_2.addWidget(self.captureImageBtn)
        self.verticalLayout.addWidget(self.groupBox)
        self.verticalLayout.setStretch(2, 1)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setObjectName("graphicsView")
        self.horizontalLayout.addWidget(self.graphicsView)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1006, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.objectTypesLabel.setText(_translate("MainWindow", "Object Types"))
        self.groupBox.setTitle(_translate("MainWindow", "Control Box"))
        self.startFeedBtn.setText(_translate("MainWindow", "Start Feed"))
        self.stopFeedBtn.setText(_translate("MainWindow", "Stop Feed"))
        self.captureImageBtn.setText(_translate("MainWindow", "Capture Image"))

