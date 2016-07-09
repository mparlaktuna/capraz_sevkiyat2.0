# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\entersequence.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(660, 244)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.comingTruckSequence = QtWidgets.QHBoxLayout()
        self.comingTruckSequence.setObjectName("comingTruckSequence")
        self.gridLayout.addLayout(self.comingTruckSequence, 0, 0, 1, 1)
        self.goingTruckSequence = QtWidgets.QHBoxLayout()
        self.goingTruckSequence.setObjectName("goingTruckSequence")
        self.gridLayout.addLayout(self.goingTruckSequence, 1, 0, 1, 1)
        self.enterSequenceButton = QtWidgets.QPushButton(Form)
        self.enterSequenceButton.setObjectName("enterSequenceButton")
        self.gridLayout.addWidget(self.enterSequenceButton, 2, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.enterSequenceButton.setText(_translate("Form", "Tamam"))

