from src.model_element import ModelElement


class Truck(ModelElement):
    def __init__(self):
        ModelElement.__init__(self)
        self.state_functions['coming'] = self.coming
        self.state_functions['waiting_to_deploy'] = self.waiting_for_receiving_door
        self.state_functions['waiting_to_load'] = self.waiting_for_shipping_door
        self.state_functions['deploying'] = self.deploying
        self.state_functions['not_enough_goods'] = self.not_enough_goods
        self.state_functions['loading'] = self.loading
        self.state_functions['changeover_load'] = self.changeover
        self.state_functions['changeover_fin'] = self.changeover
        self.state_functions['changeover_deploy'] = self.changeover
        self.state_functions['changeover_fin'] = self.changeover
        self.changeover_time = 0
        self.good_transfer_time = 0
        self.good_loading_time = 0
        self.good_unloading_time = 0
        self.last_good_dict = {}
        self.first_door = None
        self.second_door = None

    def set_coming_time(self, coming_time):
        self.next_state_time = coming_time
        self.time_signal.emit(self.next_state_time, self.element_name)

    def add_good_types(self, number):
        for i in range(number):
            self.good_store.add_good_type(i)

    def add_start_goods(self, goods):
        for i, amount in enumerate(goods):
            self.good_store.add_good(amount, i, self.element_name)
        #self.good_store.print_goods()

    def add_last_goods(self, goods):
        for i, amount in enumerate(goods):
            self.last_good_dict[i] = amount

    def coming(self):
        if self.check_next_time():
            # print("Arrived: ", self.element_name)
            if self.first_door.door_empty:
                self.first_door.door_empty = False
                self.next_state_time = self.current_time + self.changeover_time
                self.time_signal.emit(self.next_state_time, self.element_name)

                self.state += 2
            else:
                self.state += 1

    def print_info(self):
        t = ''
        if self.first_door:
            t += "Coming Door: {0}\n".format(self.first_door.element_name)
        if self.second_door:
            t += "Going Door: {0}\n".format(self.second_door.element_name)
        return t

    def waiting_for_receiving_door(self):
        if self.first_door.door_empty:
            self.first_door.door_empty = False
            self.next_state_time = self.current_time + self.changeover_time
            self.time_signal.emit(self.next_state_time, self.element_name)
            self.state += 1

    def not_enough_goods(self):
        pass

    def loading(self):
        if self.check_next_time():
            self.next_state_time = self.current_time + self.changeover_time
            self.time_signal.emit(self.next_state_time, self.element_name)
            self.state += 1

    def deploying(self):
        if self.check_next_time():
            self.first_door.good_store.add_good_dict(self.good_store.good_dictionary)
            self.good_store.reset_goods()
            self.first_door.next_state_time = self.current_time + self.good_transfer_time
            self.time_signal.emit(self.first_door.next_state_time, self.first_door.element_name)
            self.next_state_time = self.current_time + self.changeover_time
            self.time_signal.emit(self.next_state_time, self.element_name)
            self.state += 1

    def changeover(self):
        if self.check_next_time():
            print('number of goods:', self.good_store.calculate_total())
            if self.current_state_name == 'changeover_load':
                #check goods
                #check time
                self.next_state_time = self.current_time + self.good_store.calculate_total() * self.good_loading_time
                self.time_signal.emit(self.next_state_time, self.element_name)
                self.state += 1
            if self.current_state_name == 'changeover_fin':
                self.first_door.door_empty = True
                self.next_state_time = self.current_time + 1
                self.time_signal.emit(self.next_state_time, self.element_name)
                self.state += 1
            if self.current_state_name == 'changeover_deploy':
                self.next_state_time = self.current_time + self.good_store.calculate_total() * self.good_unloading_time
                self.time_signal.emit(self.next_state_time, self.element_name)
                self.state += 1
            if self.current_state_name == 'changeover_mid':
                self.first_door = self.second_door


    def waiting_for_shipping_door(self):
        if self.check_next_time():
            if self.first_door.door_empty:
                self.first_door.door_empty = False
                self.next_state_time = self.current_time + self.changeover_time
                self.time_signal.emit(self.next_state_time, self.element_name)
                self.state += 1