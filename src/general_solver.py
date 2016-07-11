#from src.sequence_list import SequenceList
from src.model import Model
from src.data_store import DataStore
from src.solver import SolverData
from src.solution_results import SolutionResults
from src.sequence import Sequence

class GeneralSolver(object):

    def __init__(self):
        self.iteration_number = 0
        self.solution_type = ""
        self.model = Model()
        self.solver_data = SolverData()
        self.data = DataStore()
        self.results = SolutionResults()
        #self.sequence_list = SequenceList()
        self.current_sequence = Sequence()

    def new_model(self):
        self.model = Model()

    def set_data(self, solver_data=SolverData(), data=DataStore()):
        self.new_model()
        self.solver_data = solver_data
        self.data = data
        self.model.set_data(solver_data, data)

    def set_sequence(self, sequence=Sequence()):
        self.current_sequence = sequence
        self.model.set_sequence(self.current_sequence)
    # gets a sequence and sets model

    def solve_iteration(self):
        pass
        # solve one iteration

    def start_iteration(self):
        self.model.reset_model()

        pass
    # start model solve

