from src.good_store import GoodStore


class TruckResults(object):
    def __init__(self):
        self.truck_type = ""
        self.truck_name = ""
        self.times = dict()
        self.coming_goods = GoodStore()
        self.going_goods = GoodStore()
