from src.data_store import DataStore
from src.sequence_list import SequenceList
from src.sequence import Sequence
from math import ceil
import operator
import random
import copy


class SequenceAlgorithm():

    def __init__(self, data=DataStore()):
        self.algorithm_name = ""
        self.data_set_number = 0
        self.data = data
        self.arrivals = {}
        self.sequence = Sequence(self.data)

    def set_data_set_number(self, number, data):
        self.data = data
        self.data_set_number = number
        self.arrivals = self.data.arrival_times[self.data_set_number]

    def start_sequence1(self):
        sorted_trucks = sorted(self.arrivals.items(), key=operator.itemgetter(1))
        self.sequence.coming_sequence = [x[0] for x in sorted_trucks if x[0] in self.data.coming_truck_name_list]
        step = ceil(self.data.number_of_coming_trucks / self.data.number_of_receiving_doors)

        for i in range(self.data.number_of_receiving_doors - 1):
            self.sequence.coming_sequence.insert(step * (i+1), '0')



        out_trucks = [('outbound' + str(i)) for i in range(self.data.number_of_outbound_trucks)]
        comp_trucks = [('compound' + str(i)) for i in range(self.data.number_of_compound_trucks)]
        sorted_out = sorted(self.arrivals.items(), key=operator.itemgetter(1))

        self.sequence.going_sequence = [x[0] for x in sorted_out if x[0] in out_trucks]
        self.sequence.going_sequence.extend([x[0] for x in sorted_out if x[0] in comp_trucks])
        step = ceil(self.data.number_of_going_trucks / self.data.number_of_shipping_doors)
        for i in range(self.data.number_of_shipping_doors - 1):
            self.sequence.going_sequence.insert(step * (i+1), '0')

        self.sequence.set_sequences(self.sequence.coming_sequence, self.sequence.going_sequence)
        return self.sequence
