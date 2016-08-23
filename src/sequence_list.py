from src.sequence import Sequence


class SequenceList():
    # list of sequences

    def __init__(self):
        self.sequence_list = []
        self.best_sequence = list()
        self.previous_sequence = Sequence()
        self.next_sequence = Sequence()
        self.error_list = []

    def add_sequence(self, sequence):
        self.sequence_list.append(sequence)

    def add_error(self, error):
        self.error_list.append(error)

    def last_sequence(self):
        if self.sequence_list:
            return self.sequence_list[-1]