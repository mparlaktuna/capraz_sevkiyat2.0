from PyQt5.QtWidgets import *
from PyQt5 import QtGui, QtCore

class ShippingDoor():

    def __init__(self, name):
        self.element_name = name
        self.truck_list = []
        self.door_empty = True

    def check_door(self, truck_name):
        """
        check if its time for the truck
        """
        if self.door_empty:
            if self.truck_list:
                if truck_name == self.truck_list[0]:
                    self.truck_list.pop(0)
                    self.door_empty = False
                    return True
            else:
                return False
        else:
            return False

    def show_sequence(self):
        """shows goods of the truck in a dialog"""
        print("show goods: ", self.element_name)
        good_dialog = QMessageBox()
        good_dialog.setWindowTitle("Sequence of " + self.element_name)
        message = str(self.truck_list)

        good_dialog.setText(message)
        good_dialog.exec_()