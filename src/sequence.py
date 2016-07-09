from src.sequence_element import SequenceElement
from src.data_store import DataStore

class Sequence():
    def __init__(self, data=DataStore()):
        self.data = data
        self.coming_sequence = []
        self.going_sequence = []
        self.coming_sequence_element = SequenceElement('receiving', self.data.number_of_receiving_doors)
        self.going_sequence_element = SequenceElement('shipping', self.data.number_of_shipping_doors)

    def set_sequences(self, coming_sequence=[], going_sequence=[]):
        self.coming_sequence = coming_sequence
        self.going_sequence = going_sequence
        self.coming_sequence_element.set_doors(self.data.number_of_receiving_doors)
        self.going_sequence_element.set_doors(self.data.number_of_shipping_doors)
        coming_index = []
        going_index = []
        for i, j in enumerate(self.coming_sequence):
            if j == '0':
                coming_index.append(i)
        for i, j in enumerate(self.going_sequence):
            if j == '0':
                going_index.append(i)
        coming_index.append(len(self.coming_sequence))
        going_index.append(len(self.going_sequence))
        prev_point = 0
        for i, j in enumerate(coming_index):
            name = 'receiving' + str(i)
            self.coming_sequence_element.add_sequence_list(name, self.coming_sequence[prev_point:j])
            prev_point = j + 1
        prev_point = 0
        for i, j in enumerate(going_index):
            name = 'shipping' + str(i)
            self.going_sequence_element.add_sequence_list(name, self.going_sequence[prev_point:j])
            prev_point = j + 1

    def print_sequence(self):
        print("Coming Sequence:", self.coming_sequence)
        print("Going Sequence:", self.going_sequence)
