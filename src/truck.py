from src.model_element import ModelElement


class Truck(ModelElement):
    def __init__(self):
        ModelElement.__init__(self)
        self.state_functions['coming'] = self.coming
        self.coming_time = 0

    def set_coming_time(self, coming_time):
        self.coming_time = coming_time
        self.time_signal.emit(self.coming_time, self.element_name)

    def coming(self):
        if self.current_time == self.coming_time:
            print("Arrived: ", self.element_name)
            self.state += 1