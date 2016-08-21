from src.good_store import GoodStore
from src.truck_results import TruckResults
from PyQt5.QtWidgets import *
from PyQt5 import QtGui, QtCore
from collections import OrderedDict


class Truck():
    def __init__(self):
        self.element_name = ""
        self.truck_type = ""
        self.truck_times = OrderedDict()
        self.state_functions = OrderedDict()
        self.truck_states = []
        self.state_change = False
        self.coming_time = 0
        self.changeover_time = 0
        self.good_loading_time = 0
        self.good_unloading_time = 0
        self.good_transfer_time = 0
        self.station = 0
        self.coming_good_store = GoodStore()
        self.going_good_store = GoodStore()
        self.coming_good_dict = dict()
        self.going_good_dict = dict()
        self.state = 0
        self.current_time = 0
        self.truck_results = TruckResults()
        self.first_door = ""
        self.second_door = ""
        self.current_door = ""
        self.next_state_time = 0
        self.simulation_state = 0

        # define state functions
        self.state_functions["coming"] = self.coming
        self.state_functions["waiting_to_deploy"] = self.waiting_to_deploy
        self.state_functions["waiting_to_load"] = self.waiting_to_load
        self.state_functions["changeover_load"] = self.changeover_load
        self.state_functions["changeover_deploy"] = self.changeover_deploy
        self.state_functions["deploying"] = self.deploying
        self.state_functions["changeover_fin"] = self.changeover_fin
        self.state_functions["changeover_mid"] = self.changeover_mid
        self.state_functions["not_enough_goods"] = self.not_enough_goods
        self.state_functions["loading"] = self.loading
        self.state_functions["done"] = self.done

    def add_good_types(self, number_of_goods):
        for i in range(number_of_goods):
            self.coming_good_store.add_good_type(i)

    def add_start_goods(self, start_goods):
        for i in range(len(start_goods)):
            self.coming_good_dict[str(i)] = start_goods[i]
            self.coming_good_store.add_good(start_goods[i], str(i), self.element_name)

    def add_last_goods(self, last_goods):
        for i in range(len(last_goods)):
            self.going_good_dict[str(i)] = last_goods[i]
            self.going_good_store.add_good_type(str(i))

    def show_goods(self):
        """shows goods of the truck in a dialog"""
        print("show goods: ", self.element_name)
        good_dialog = QMessageBox()
        good_dialog.setWindowTitle("Goods of " + self.element_name)
        message = "Current Coming Goods:\n"
        message += self.coming_good_store.print_goods()
        message +=  "\nCurrent Going Goods:\n"
        message += self.going_good_store.print_goods()
        
        message += "\nPlanned Going Goods:\n"
        message += str(self.going_good_dict)
        
        good_dialog.setText(message)
        good_dialog.exec_()

    def show_times (self):
        """shows the times of the truck"""
        good_dialog = QMessageBox()
        good_dialog.setWindowTitle("Times of " + self.element_name)
        message = ""
        for state_name, state_time in self.truck_times.items():
            message += state_name 
            message += ": "
            message += str(state_time)
            message += "\n"
            
        message += "\n"
        message += "Current State: "
        message += self.state_list[self.state]
        message += "\n"

        message += "Next State: "
        message += self.state_list[self.state + 1]
        message += "\n"
        message += "Next state Time: "
        message += str(self.next_state_time)
        message += "\n"
        good_dialog.setText(message)
        good_dialog.exec_()
                
    def return_truck_results(self):
        self.truck_results.truck_name = self.element_name
        self.truck_results.truck_type = self.truck_type
        self.truck_results.times = self.truck_times
        self.truck_results.coming_goods = self.coming_good_store
        self.truck_results.going_goods = self.going_good_store
        return self.truck_results

    def step(self):
        """
        one tep forward
        """
        print("step:", self.element_name, self.state)
        state_name = self.state_list[self.state]
        self.state_change = False        
        self.state_functions[state_name]()

        if self.state_change:
            return self.next_state_time
        else:
            return 0

    def check_next_state_time (self):
        """check next if time for next state has come"""

        if self.current_time == self.next_state_time:
            return True
        else:
            return False
            
    def coming (self):
        """truck coming"""
        if self.check_next_state_time():
            print("truck has come")
            self.truck_times["arrival"] = self.current_time

            if self.current_door.check_door(self.element_name):
                self.state += 2
                self.next_state_time = self.current_time + self.changeover_time
            else:
                self.state += 1
                self.next_state_time = -1
            self.state_change = True
        else:
            print("truck is coming")

    def next_state(self):
        """
        called at every next state
        """
        self.state += 1
        self.state_change = True

    def waiting_to_deploy (self):
        """waiting to deploy goods for inboudn and compound trucks"""
        self.simulation_state = 1
        if self.current_door.check_door(self.element_name):
            self.truck_times["started entering receiving door"] = self.current_time
            self.next_state()
            self.next_state_time = self.current_time + self.changeover_time

    def waiting_to_load (self):
        """
        waiting to load for outbound and compound trucks
        """
        self.simulation_state = 2
        if self.current_door.check_door(self.element_name):
            self.truck_times["started entering shipping door"] = self.current_time
            self.next_state()
            self.next_state_time = self.current_time + self.changeover_time

    def changeover_load(self):
        """
        changeover time for inbound and compound while loading
        """
        self.simulation_state = 2
        if self.check_next_state_time():
            self.truck_times["at the shipping door"] = self.current_time
            if self.station.good_store.check_enough(self.going_good_dict):
                self.state += 2
                total_good = 0
                self.truck_times["started loading"] = self.current_time
                for good_amount in self.going_good_dict.values():
                    total_good += good_amount
                self.next_state_time = self.current_time + self.good_loading_time * total_good
            else:
                self.state += 1
                self.truck_times["not enough goods"] = self.current_time
                self.next_state_time = -1
            self.state_change = True

    def changeover_deploy(self):
        """
        changeover time for outbound and compound while deploying
        """
        self.simulation_state = 1
        if self.check_next_state_time():
            self.truck_times["started deploying goods"] = self.current_time
            self.next_state()
            self.next_state_time = self.current_time + self.coming_good_store.calculate_total() * self.good_unloading_time

    def changeover_fin(self):
        """
        changeover after process finished for all trucks
        """
        if self.check_next_state_time():
            self.current_door.door_empty = True
            self.truck_times["departed from the door"] = self.current_time
            self.next_state()           

    def changeover_mid(self):
        """
        changeover at mid for compound trucks
        """
        if self.check_next_state_time():
            self.current_door.door_empty = True
            self.current_door = self.second_door
            self.truck_times["started going to shipping side"] = self.current_time
            self.next_state_time = self.current_time + self.truck_transfer_time
            self.next_state()

    def not_enough_goods(self):
        """
        waiting for enough goods to load
        """
        if self.station.good_store.check_enough(self.going_good_dict):
            total_good = 0
            for good_amount in self.going_good_dict.values():
                total_good += good_amount
            self.next_state_time = self.current_time + self.good_loading_time * total_good
            self.truck_times["started loading"] = self.current_time
            self.next_state()

    def loading(self):
        """
        waiting to load goods
        """
        if self.check_next_state_time():
            if self.station.good_store.check_enough(self.going_good_dict):
                removed = self.station.good_store.remove_good(self.going_good_dict)

                self.going_good_store.add_good_dict(removed)
                self.next_state_time = self.current_time + self.changeover_time
                self.truck_times["finished loading"] = self.current_time
                self.next_state()

    def deploying(self):
        """
        deploying for inbound and compound trucks
        """
        if self.check_next_state_time():
            self.current_door.transfer_finished = True
            self.current_door.good_store.add_good_dict(self.coming_good_store.good_dictionary)
            self.current_door.good_transfer_time = self.current_time + self.good_transfer_time
            self.coming_good_store.reset_goods()
            self.next_state_time = self.current_time + self.changeover_time
            self.truck_times["finished deploying"] = self.current_time
            self.next_state()

    def done(self):
        """
        done for all trucks set the done signal 
        """
        self.simulation_state = 3
