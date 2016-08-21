from collections import OrderedDict


class ModelResult:
    """
    results of one solution of a model
    """

    def __init__(self):
        self.errors = OrderedDict()
        self.sequence = 0
        self.truck_times = OrderedDict()
        self.final_goods = OrderedDict()



class IterationResults:

    """
    multiple solutions of an algorithm
    """

    def __init__(self):
        self.algorithm_name = ""
        self.function_name = ""
        self.model_results = list()
        self.number_of_iterations = 0
        self.best_solution_number = 0
        self.solution_type = "simulation"
        self.solution_name = ""

    def add_results(self, model):
        new_model_result = ModelResult()
        new_model_result.errors = model.calculate_errors()
        new_model_result.sequence = model.current_sequence
        new_model_result.truck_times = model.return_truck_times()
        new_model_result.final_goods = model.return_final_goods()
        self.model_results.append(new_model_result)
        self.number_of_iterations += 1