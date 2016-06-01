from src.sequnce import Sequence


class SequenceList():
    def __init__(self):
        self.sequence_list = []
        self.best_sequence = Sequence()
        self.previous_sequence = Sequence()
        self.next_sequence = Sequence()
        self.error_list = []

    def add_sequence(self, sequence):
        self.sequence_list.append(sequence)
        self.best_sequence = sequence

    def last_sequence(self):
        return self.sequence_list[-1]