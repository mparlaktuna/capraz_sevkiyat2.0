from src.model_element import ModelElement
from src.station import Station


class ReceivingDoor(ModelElement):
    def __init__(self, name, station=Station()):
        ModelElement.__init__(self)
        self.element_name = name
        self.station = station
        self.state_list = ["door"]
        self.state_functions['door'] = self.door
        self.truck_list = []
        self.door_empty = True

    def door(self):
        if self.check_next_time():
            self.station.good_store.add_good_dict(self.good_store.good_dictionary)
            self.good_store.reset_goods()

