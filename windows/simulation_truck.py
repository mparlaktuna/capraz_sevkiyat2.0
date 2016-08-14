# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'simulation_truck.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_simulation_truck(object):
    def setupUi(self, simulation_truck):
        simulation_truck.setObjectName("simulation_truck")
        simulation_truck.resize(811, 34)
        self.horizontalLayout = QtWidgets.QHBoxLayout(simulation_truck)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.truckNameLabel = QtWidgets.QLabel(simulation_truck)
        self.truckNameLabel.setText("")
        self.truckNameLabel.setObjectName("truckNameLabel")
        self.horizontalLayout.addWidget(self.truckNameLabel)
        self.show_goods_button = QtWidgets.QPushButton(simulation_truck)
        self.show_goods_button.setObjectName("show_goods_button")
        self.horizontalLayout.addWidget(self.show_goods_button)
        self.show_times_button = QtWidgets.QPushButton(simulation_truck)
        self.show_times_button.setObjectName("show_times_button")
        self.horizontalLayout.addWidget(self.show_times_button)
        self.currentStateLabel = QtWidgets.QLabel(simulation_truck)
        self.currentStateLabel.setText("")
        self.currentStateLabel.setObjectName("currentStateLabel")
        self.horizontalLayout.addWidget(self.currentStateLabel)
        self.prevTimeLabel = QtWidgets.QLabel(simulation_truck)
        self.prevTimeLabel.setText("")
        self.prevTimeLabel.setObjectName("prevTimeLabel")
        self.horizontalLayout.addWidget(self.prevTimeLabel)
        self.nextStateLabel = QtWidgets.QLabel(simulation_truck)
        self.nextStateLabel.setText("")
        self.nextStateLabel.setObjectName("nextStateLabel")
        self.horizontalLayout.addWidget(self.nextStateLabel)
        self.nextTimeLabel = QtWidgets.QLabel(simulation_truck)
        self.nextTimeLabel.setText("")
        self.nextTimeLabel.setObjectName("nextTimeLabel")
        self.horizontalLayout.addWidget(self.nextTimeLabel)

        self.retranslateUi(simulation_truck)
        QtCore.QMetaObject.connectSlotsByName(simulation_truck)

    def retranslateUi(self, simulation_truck):
        _translate = QtCore.QCoreApplication.translate
        simulation_truck.setWindowTitle(_translate("simulation_truck", "Form"))
        self.show_goods_button.setText(_translate("simulation_truck", "Show Goods"))
        self.show_times_button.setText(_translate("simulation_truck", "Show Times"))

