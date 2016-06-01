from PyQt5.QtCore import *
from src.data_store import DataStore
from src.solver_data import SolverData
from src.model import Model
from src.sequnce import Sequence
from src.annealing import Annealing


class Solver(QObject):

    def __init__(self, simulator, data=DataStore(), solver_data=SolverData()):
        QObject.__init__(self)
        self.data = data
        self.solver_data = solver_data
        self.simulator = simulator
        self.annealing = Annealing(self.data)
        self.current_iteration = 0

    def solve_data_set(self):
        self.model = Model()
        self.model.set_data(self.solver_data.data_set_number, self.data)
        self.annealing.set_data_set_number(self.solver_data.data_set_number, self.data)
        self.annealing.start_sequence1()
        self.annealing.sequence.set_sequences()

        self.model.current_sequence = self.annealing.next_sequence()
        self.model.set_sequence()
        # calculate sequence
        #self.model.current_sequence = self.current_sequence
        self.model.solve()

    def solve_simluation(self):
        self.model = Model()
        self.model.simulator = self.simulator
        self.model.simulation_on = True
        self.model.set_data(self.solver_data.data_set_number, self.data)
        self.simulator.reset()
        self.simulator.trucks = self.model.all_trucks
        self.simulator.doors = self.model.all_doors
        self.simulator.station = self.model.station
        self.annealing.set_data_set_number(self.solver_data.data_set_number, self.data)
        self.annealing.start_sequence1()
        self.annealing.sequence.set_sequences()

        self.model.current_sequence = self.annealing.next_sequence()
        self.model.set_sequence()

        self.model.solve()

    def simulation_step(self):
        self.model.solve()