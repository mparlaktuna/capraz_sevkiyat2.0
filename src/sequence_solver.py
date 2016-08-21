from src.general_solver import GeneralSolver


class SequenceSolver(GeneralSolver):

    def __init__(self):
        GeneralSolver.__init__(self)

    def save_results(self, model):
        """
        save results for one sequence
        :param model:
        :return:
        """
        self.iteration_results.solution_type = self.solution_type
        self.iteration_results.solution_name = self.solution_name
        self.iteration_results.add_results(model)
        self.iteration_results.best_solution_number = 1

