from src.truck import Truck


class CompoundTruck(Truck):
    def __init__(self, name):
        Truck.__init__(self)
        self.element_name = name
        self.state_list = ['coming', 'waiting_to_deploy', 'changeover_deploy', 'deploying', 'changeover_mid', 'truck_transfer', 'waiting_to_load', 'changeover_load',  'not_enough_goods', 'loading', 'changeover_fin', 'done']
        self.state_functions["truck_transfer"] = self.truck_transfer
        self.truck_transfer_time = 0

    def truck_transfer(self):
        """
        truck transfer time for a compound truck
        """
        self.simulation_state = 4
        if self.check_next_state_time():
            self.truck_times["Arrived to the Shipping Side"] = self.current_time
            self.next_state_time = -1
            self.next_state()







