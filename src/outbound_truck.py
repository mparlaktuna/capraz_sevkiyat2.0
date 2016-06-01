from src.truck import Truck


class OutboundTruck(Truck):
    def __init__(self, name):
        Truck.__init__(self)
        self.element_name = name
        self.state_list = ['coming', 'waiting_to_load', 'changeover_load', 'not_enough_goods', 'loading', 'changeover_fin', 'done']
