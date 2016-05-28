from PyQt5.QtCore import *
from src.data_store import DataStore
from src.solver_data import SolverData
from src.model import Model


class Solver(QObject):

    def __init__(self, data=DataStore(), solver_data=SolverData()):
        QObject.__init__(self)
        self.data = data
        self.solver_data = solver_data

    def new_model(self):
        #create model from data
        self.model = Model()
        self.model.set_data(self.solver_data.data_set_number, self.data)

    def solve_one_iteration(self):
        pass

    def solve_data_set(self):
        self.new_model()
        self.model.solve()

    def solve_simulator(self):
        pass