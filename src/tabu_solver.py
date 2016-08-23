from src.general_solver import GeneralSolver


class TabuSolver(GeneralSolver):

    def __init__(self):
        GeneralSolver.__init__(self)

    def next_iteration(self):
        self.iteration_number += 1
        print(self.iteration_number)

    def generate_next_iteration(self):
        #self.set sequence
        pass