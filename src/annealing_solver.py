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

    def save_results(self, model):
        self.iteration_results.solution_type = self.solution_type
        self.iteration_results.solution_name = self.solution_name
        self.iteration_results.add_results(model)
        self.iteration_results.best_solution_number = 1

    def generate_next_iteration(self):
        #self.set sequence
        pass