from src.general_solver import GeneralSolver


class AnnealingSolver(GeneralSolver):

    def __init__(self):
        GeneralSolver.__init__(self)


    def next_iteration(self):
        self.iteration_saved = False
        self.model.reset_model()
        if self.iteration_number == 0:
            self.set_sequence(self.sequence_algorithms.start_sequence1())
        else:
            self.set_sequence(self.sequence_algorithms.start_sequence1())
        self.solve_iteration()
        self.iteration_number += 1
        print(self.iteration_number)

    def save_results(self, model):
        print("save annealing")

    def generate_next_iteration(self):
        pass