from src.good_store import GoodStore
from src.truck_results import TruckResults


class Truck():
    def __init__(self):
        self.truck_name = ""
        self.truck_type = ""
        self.truck_times = dict()
        self.truck_states = []
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

    def add_good_types(self, number_of_goods):
        for i in range(number_of_goods):
            self.coming_good_store.add_good_type(i)

    def add_start_goods(self, start_goods):
        for i in range(len(start_goods)):
            self.coming_good_dict[i] = start_goods[i]
            self.coming_good_store.add_good(start_goods[i], str(i), self.truck_name)

    def add_last_goods(self, last_goods):
        for i in range(len(last_goods)):
            self.going_good_dict[i] = last_goods[i]

    def return_truck_results(self):
        self.truck_results.truck_name = self.truck_name
        self.truck_results.truck_type = self.truck_type
        self.truck_results.times = self.truck_times
        self.truck_results.coming_goods = self.coming_good_store
        self.truck_results.going_goods = self.going_good_store
        return self.truck_results
