from src.truck import Truck


class InboundTruck(Truck):
    def __init__(self, name):
        Truck.__init__(self)
        self.element_name = name
        self.state_list = ['coming', 'done']
