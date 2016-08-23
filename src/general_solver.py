from src.sequence_list import SequenceList
from src.model import Model
from src.data_store import DataStore
from src.solver import SolverData
from src.sequence import Sequence
from src.results import *
from src.sequence_algorithms import SequenceAlgorithm


class GeneralSolver(object):

    def __init__(self):
        self.iteration_number = 0
        self.solution_type = ""
        self.solution_name = ""
        self.model = Model()
        self.solver_data = SolverData()
        self.data = DataStore()
        self.iteration_results = IterationResults()
        self.sequence_list = SequenceList()
        self.current_sequence = Sequence()
        self.iteration_saved = False

    def new_model(self):
        self.model = Model()

    def set_data(self, solver_data=SolverData(), data=DataStore()):
        self.new_model()
        self.solver_data = solver_data
        self.data = data
        self.model.set_data(solver_data, data)
        self.sequence_algorithms = SequenceAlgorithm(data)
        self.sequence_algorithms.set_data_set_number(solver_data.data_set_number,data)

    def set_sequence(self, sequence=Sequence()):
        self.current_sequence = sequence
        self.sequence_list.add_sequence(self.current_sequence)
        self.model.set_sequence(self.current_sequence)
    # gets a sequence and sets model

    def solve_iteration(self):
        while not self.iteration_saved:
            #print("iteration")
            if not self.model.check_done():
                self.model.next_time()
                #print(self.model.current_time)
            else:
                self.iteration_saved = True
                self.save_results(self.model)


    def start_iteration(self):
        self.model.reset_model()
        # start model solve

    def step_forward(self):
        """
        moves the model forward
        """
        if not self.model.check_done():
            self.model.next_time()
            return True
        else:
            self.save_results(self.model)
            return False

    def save_results(self, model):
        pass

