from src.truck_results import TruckResults
from src.truck import Truck


class IterationResults(object):

    def __init__(self):
        self.iteration_number = 0
        self.truck_results = dict()
        self.error = 0
        self.error_values = dict()