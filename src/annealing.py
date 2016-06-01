from src.sequence_algorithms import SequenceAlgorithm
from src.data_store import DataStore


class Annealing(SequenceAlgorithm):
    def __init__(self, data=DataStore()):
        SequenceAlgorithm.__init__(self, data)
        self.algorithm_name = "annealing"
