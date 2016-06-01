class SequenceElement():
    def __init__(self, type, number):
        self.sequence_dict = {}
        self.type = type
        self.set_doors(number)

    def set_doors(self, number_of_doors):
        for i in range(number_of_doors):
            t = self.type + str(i)
            self.sequence_dict[t] = []

    def add_sequence_list(self, door_name, sequence_list):
        self.sequence_dict[door_name] = sequence_list

    def get_door_name(self, truck_name):
        for door_name, sequence_list in self.sequence_dict.items():
            if truck_name in sequence_list:
                return door_name

