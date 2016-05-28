from PyQt5.QtCore import *
from collections import OrderedDict
from src.station import Station
from src.data_store import DataStore
from src.inbound_truck import InboundTruck
from src.outbound_truck import OutboundTruck
from src.compound_truck import CompoundTruck
from src.receiving_doors import ReceivingDoor
from src.shipping_door import ShippingDoor


class Model(QThread):
    next_time_signal = pyqtSignal(int, name='time')

    def __init__(self):
        QThread.__init__(self)
        self.inbound_trucks = OrderedDict()
        self.outbound_trucks = OrderedDict()
        self.compound_trucks = OrderedDict()
        self.coming_trucks = OrderedDict()
        self.going_trucks = OrderedDict()
        self.all_trucks = OrderedDict()
        self.shipping_doors = OrderedDict()
        self.receiving_doors = OrderedDict()
        self.element_list = []
        self.current_time = 0
        self.done = False
        self.time_list = []

    def set_data(self, data_number, data=DataStore()):
        self.data = data
        self.data_set_number = data_number
        print("Setting Data Set:", data_number)
        self.station = Station()

        for i in range(self.data.number_of_inbound_trucks):
            name = 'inbound' + str(i)
            truck = InboundTruck(name)
            self.inbound_trucks[name] = truck
            self.coming_trucks[name] = truck
            self.all_trucks[name] = truck

        for i in range(self.data.number_of_outbound_trucks):
            name = 'outbound' + str(i)
            truck = OutboundTruck(name)
            self.outbound_trucks[name] = truck
            self.going_trucks[name] = truck
            self.all_trucks[name] = truck

        for i in range(self.data.number_of_compound_trucks):
            name = 'compound' + str(i)
            truck = CompoundTruck(name)
            self.compound_trucks[name] = truck
            self.coming_trucks[name] = truck
            self.going_trucks[name] = truck
            self.all_trucks[name] = truck

        for i in range(self.data.number_of_receiving_doors):
            name = 'receiving' + str(i)
            door = ReceivingDoor(name)
            self.receiving_doors[name] = door
            self.element_list.append(door)
            self.next_time_signal.connect(door.step_forward)

        for i in range(self.data.number_of_shipping_doors):
            name = 'shipping' + str(i)
            door = ShippingDoor(name)
            self.shipping_doors[name] = door
            self.element_list.append(door)
            self.next_time_signal.connect(door.step_forward)

        for truck in self.all_trucks.values():
            self.element_list.append(truck)
            truck.time_signal.connect(self.add_time)
            self.next_time_signal.connect(truck.step_forward)
            truck.set_coming_time(self.data.arrival_times[self.data_set_number][truck.element_name])

        self.set_coming_times()

    def reset_model(self):
        print("Model Reset")
        self.current_time = 0
        self.time_list = []
        self.set_states()
        # self.set_goods()

    def done(self, done_time, object_name):
        pass

    def add_time(self, new_time, object_name):

        if new_time not in self.time_list:
            self.time_list.append(new_time)
            self.time_list.sort()

    def set_coming_times(self):
        for truck in self.all_trucks.values():
            truck.set_coming_time(self.data.arrival_times[self.data_set_number][truck.element_name])

    def set_goods(self):
        pass

    def set_states(self):
        for truck in self.all_trucks.values():
            truck.state = 0
            truck.current_time = 0

    def next_time(self):
        next_time = self.time_list.pop(0)
        print(next_time)
        self.next_time_signal.emit(next_time)

    def run(self):
        while not self.done:
            #print(self.time_list)
            if self.check_step_finish():
                self.clear_step_finish()
                self.next_time()

    def clear_step_finish(self):
        for element in self.element_list:
            element.step_finish = False

    def set_step_finish(self):
        for element in self.element_list:
            element.step_finish = True

    def check_step_finish(self):
        step_finish = False
        for element in self.element_list:
            if element.step_finish:
                step_finish = True
            else:
                return False
        return step_finish

    def solve(self):
        self.set_step_finish()
        self.start()
