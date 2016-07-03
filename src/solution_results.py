from src.iteration_results import IterationResults


class SolutionResults(object):
    def __init__(self):
        self.results = dict()
        self.best_result = IterationResults()

    def add_result(self, iteration_result):
        oass