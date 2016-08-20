from PyQt5.QtWidgets import *
from PyQt5 import QtGui, QtCore
from src.good_store import GoodStore
from src.station import Station

class ReceivingDoor():

    def __init__(self, name):
        self.element_name = name
        self.truck_list = []
        self.door_empty = True
        self.good_store = GoodStore()
        self.good_transfer_time = 0
        self.transfer_finished = False
        self.station = 0

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

    def transfer_goods_to_station(self, current_time):
        if current_time == self.good_transfer_time:
            self.station.good_store.add_good_dict(self.good_store.good_dictionary)
            self.good_store.reset_goods()

        if self.transfer_finished:
            self.transfer_finished = False
            return self.good_transfer_time
        else:
            return -1

    def show_sequence(self):
        """shows goods of the truck in a dialog"""
        print("show goods: ", self.element_name)
        good_dialog = QMessageBox()
        good_dialog.setWindowTitle("Sequence of " + self.element_name)
        message = str(self.truck_list)

        good_dialog.setText(message)
        good_dialog.exec_()