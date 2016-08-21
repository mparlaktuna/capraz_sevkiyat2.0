class SolverData:
    def __init__(self):
        self.number_of_iterations = 100
        self.data_set_number = 0
        self.algorithm_name = 'annealing'
        self.annealing_temperature = 100
        self.annealing_decay_factor = 0.9
        self.tabu_number_of_neighbors = 5
        self.tabu_number_of_tabu = 4
        self.function_type = "normal"
        self.time_limit = 0
