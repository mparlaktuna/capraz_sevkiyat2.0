class ReceivingDoor():

    def __init__(self, name):
        self.element_name = name
        self.truck_list = []
        self.door_empty = True

    def check_door(self, truck_name):
        """
        check if its time for the truck
        """
        if self.door_empty:
            if truck_name == self.truck_list[0]:
                self.door_empty = False
                return True
            else:
                return False
        else:
            return False
