from PyQt5.QtCore import *
from collections import OrderedDict
from src.station import Station
from src.data_store import DataStore
from src.inbound_truck import InboundTruck
from src.outbound_truck import OutboundTruck
from src.compound_truck import CompoundTruck
from src.receiving_doors import ReceivingDoor
from src.shipping_door import ShippingDoor
from src.sequence import Sequence
from src.solver_data import SolverData
from src.iteration_results import IterationResults


class Model(QThread):
    finished = pyqtSignal(int, name='time')

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
        self.errors = OrderedDict()
        self.all_doors = OrderedDict()
        self.element_list = []
        self.current_time = 0
        self.current_sequence = Sequence()
        self.done = False
        self.time_list = []
        self.simulation_on = False
        self.simulator = None

    def set_data(self, solver_data=SolverData(), data=DataStore()):
        self.data = data
        self.solver_data = solver_data
        self.data_set_number = self.solver_data.data_set_number
        print("Setting Data Set:", self.data_set_number)
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
            door.station = self.station
            self.all_doors[name] = door
            self.element_list.append(door)

        for i in range(self.data.number_of_shipping_doors):
            name = 'shipping' + str(i)
            door = ShippingDoor(name)
            self.shipping_doors[name] = door
            self.element_list.append(door)
            self.all_doors[name] = door

        for truck in self.all_trucks.values():
            self.element_list.append(truck)

        self.set_coming_times()
        self.set_states()
        self.set_goods()

    def set_sequence(self, sequence):
        self.current_sequence = sequence
        try:
            for truck in self.inbound_trucks.values():
                coming_door_name = self.current_sequence.coming_sequence_element.get_door_name(truck.element_name)
                truck.first_door = self.all_doors[coming_door_name]
                truck.current_door = truck.first_door
                truck.second_door = truck.first_door

            for truck in self.outbound_trucks.values():
                going_door_name = self.current_sequence.going_sequence_element.get_door_name(truck.element_name)
                truck.second_door = self.all_doors[going_door_name]
                truck.current_door = truck.second_door
                truck.first_door = truck.second_door

            for truck in self.compound_trucks.values():
                coming_door_name = self.current_sequence.coming_sequence_element.get_door_name(truck.element_name)
                going_door_name = self.current_sequence.going_sequence_element.get_door_name(truck.element_name)
                truck.first_door = self.all_doors[coming_door_name]
                truck.second_door = self.all_doors[going_door_name]
                truck.current_door = truck.first_door

            for door in self.receiving_doors.values():
                door.truck_list = self.current_sequence.coming_sequence_element.sequence_dict[door.element_name]
                for i in range(self.data.number_of_goods):
                    door.good_store.add_good_type(str(i))

            for door in self.shipping_doors.values():
                door.truck_list = self.current_sequence.going_sequence_element.sequence_dict[door.element_name]
        except:
            print("Girilen Sirada Hata Mevcut")

    def set_coming_times(self):
        for truck in self.all_trucks.values():
            truck.coming_time = self.data.arrival_times[self.data_set_number][truck.element_name]
            truck.next_state_time = truck.coming_time
            truck.truck_times["coming_time"] = truck.coming_time
            truck.changeover_time = self.data.changeover_time
            truck.good_loading_time = self.data.loading_time
            truck.good_unloading_time = self.data.unloading_time
            truck.good_transfer_time = self.data.good_transfer_time
            self.add_time(truck.coming_time)
            truck.station = self.station

    def set_goods(self):
        for i, truck in enumerate(self.inbound_trucks.values()):
            truck.add_start_goods(self.data.inbound_goods[i])

        for i, truck in enumerate(self.outbound_trucks.values()):
            truck.add_last_goods(self.data.outbound_goods[i])

        for i, truck in enumerate(self.compound_trucks.values()):
            truck.add_start_goods(self.data.compound_coming_goods[i])
            truck.add_last_goods(self.data.compound_going_goods[i])
            truck.truck_transfer = self.data.truck_transfer_time

        for i in range(self.data.number_of_goods):
            self.station.good_store.add_good_type(str(i))

    def set_states(self):
        for truck in self.all_trucks.values():
            truck.state = 0
            truck.current_time = 0

    def reset_model(self):
        print("Model Reset")
        self.current_time = 0
        self.time_list = []
        self.set_states()
        self.set_goods()

    def check_done(self):
        """
        check if all the trucks are finished
        """
        finished = True
        for truck in self.all_trucks.values():
            if truck.state_list[truck.state] == 'done':
                finished = True
            else:
                finished = False
                break

        self.done = finished
        return finished

    def add_time(self, new_time):
        if new_time not in self.time_list:
            self.time_list.append(new_time)
            self.time_list.sort()

    def next_time(self):
        if self.time_list:
            self.current_time = self.time_list.pop(0)
            #run trucks doors and station
            if not self.check_done():
                self.update_elements()
                if not self.time_list:
                    self.time_list.append(self.current_time + 1)
                print(self.current_time)
        else:
            print("Finished")

    def calculate_errors(self):
        """
        calculate all error functions
        :return:
        """
        return self.errors
        # return dict of errors

    def return_truck_times(self):
        truck_times = OrderedDict()
        for truck in self.all_trucks.values():
            truck_times[truck.element_name] = truck.truck_times
        return truck_times

    def return_final_goods(self):
        final_goods = OrderedDict()
        return final_goods

    def update_elements(self):
        """
        updates every element (truck, door and station)
        """
        print("update elements")
        for truck in self.all_trucks.values():
            truck.current_time = self.current_time
            result = truck.step()
            if (result and (not result == -1)):
                self.add_time(result)

        for door in self.receiving_doors.values():
            result = door.transfer_goods_to_station(self.current_time)
            if (result and (not result == -1)):
                self.add_time(result)

    def run(self):
        #add timer
        while not self.done:
            self.check_done()
            if self.check_step_finish():
                self.clear_step_finish()
                self.next_time()

    def generate_results(self, results=IterationResults()):
        for truck in self.all_trucks:
            results.truck_results[truck.element_name] = truck.return_truck_results()

        return results
