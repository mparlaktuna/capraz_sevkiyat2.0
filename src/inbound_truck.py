from src.truck import Truck


class InboundTruck(Truck):
    def __init__(self, name):
        Truck.__init__(self)
        self.element_name = name
        self.state_list = ['coming', 'waiting_to_deploy', 'changeover_deploy', 'deploying', 'changeover_fin', 'done']
        self.state_functions['coming'] = self.coming
