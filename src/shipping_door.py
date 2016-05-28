from src.model_element import ModelElement


class ShippingDoor(ModelElement):
    def __init__(self, name):
        ModelElement.__init__(self)
        self.element_name = name
        self.state_list = ["empty", "full"]
        self.state_functions['empty'] = self.empty
        self.state_functions['full'] = self.full

    def empty(self):
        pass
        #print(self.element_name, "Empty")

    def full(self):
        pass
        #print(self.element_name, "Full")