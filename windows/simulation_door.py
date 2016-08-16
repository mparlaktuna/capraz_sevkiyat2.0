# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'simulation_door.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_simulation_door(object):
    def setupUi(self, simulation_door):
        simulation_door.setObjectName("simulation_door")
        simulation_door.resize(210, 43)
        self.gridLayout = QtWidgets.QGridLayout(simulation_door)
        self.gridLayout.setObjectName("gridLayout")
        self.door_name = QtWidgets.QLabel(simulation_door)
        self.door_name.setText("")
        self.door_name.setObjectName("door_name")
        self.gridLayout.addWidget(self.door_name, 0, 0, 1, 1)
        self.show_truck_sequence_button = QtWidgets.QPushButton(simulation_door)
        self.show_truck_sequence_button.setObjectName("show_truck_sequence_button")
        self.gridLayout.addWidget(self.show_truck_sequence_button, 0, 1, 1, 1)

        self.retranslateUi(simulation_door)
        QtCore.QMetaObject.connectSlotsByName(simulation_door)

    def retranslateUi(self, simulation_door):
        _translate = QtCore.QCoreApplication.translate
        simulation_door.setWindowTitle(_translate("simulation_door", "Form"))
        self.show_truck_sequence_button.setText(_translate("simulation_door", "Truck Sequence"))

