from src.model_element import ModelElement
from src.good_store import GoodStore
from src.station import Station


class ShippingDoor(ModelElement):
    def __init__(self, name, station=Station()):
        ModelElement.__init__(self)
        self.element_name = name
        self.station = station
        self.state_list = ["door"]
        self.state_functions['door'] = self.door
        self.truck_list = []
        self.door_empty = True

    def door(self):
        pass
