from windows.entersequence import Ui_Form
from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import *
from src.data_store import DataStore
from src.sequence_element import SequenceElement


class EnterSequenceWidget(QWidget, Ui_Form):
    def __init__(self, data):
        super(EnterSequenceWidget, self).__init__()
        self.setupUi(self)
        self.data = data
        self.comingSequenceList = []
        self.goingSequenceList = []
        self.setup_sequence_elements()
        #self.sequence = sequence

        self.enterSequenceButton.clicked.connect(self.get_sequence)

    def setup_sequence_elements(self):
        for i in range(self.data.number_of_coming_trucks + self.data.number_of_receiving_doors - 1):
            new_element = QComboBox()
            for truck_name in self.data.coming_truck_name_list:
                new_element.addItem(truck_name)
            for i in range(self.data.number_of_receiving_doors-1):
                new_element.addItem("0")
            self.comingTruckSequence.addWidget(new_element)
            self.comingSequenceList.append(new_element)

        for i in range(self.data.number_of_going_trucks + self.data.number_of_shipping_doors - 1):
            new_element = QComboBox()
            for truck_name in self.data.going_truck_name_list:
                new_element.addItem(truck_name)
            for i in range(self.data.number_of_shipping_doors-1):
                new_element.addItem("0")

            self.goingTruckSequence.addWidget(new_element)
            self.goingSequenceList.append(new_element)

    def get_sequence(self):
        for element in self.comingSequenceList:
            print(element.currentText())

        self.close()

