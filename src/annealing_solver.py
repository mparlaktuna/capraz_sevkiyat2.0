from src.general_solver import GeneralSolver
import math
import random

class AnnealingSolver(GeneralSolver):

    def __init__(self):
        GeneralSolver.__init__(self)

    def next_iteration(self):
        self.iteration_saved = False
        self.model.reset_model()

        if self.iteration_number == 0:
            self.current_sequence = self.sequence_algorithms.start_sequence1()
            self.set_sequence(self.current_sequence)
        else:
            self.generate_next_iteration()
        self.solve_iteration()
        self.iteration_number += 1

    def save_results(self, model):
        self.sequence_list.add_sequence(self.current_sequence)
        self.iteration_results.solution_type = self.solution_type
        self.iteration_results.solution_name = self.solution_name
        self.iteration_results.add_results(model)
        self.sequence_list.add_error(self.iteration_results.model_results[-1].errors[self.solver_data.function_type])
        self.iteration_results.best_solution_number = 1

    def generate_next_iteration(self):
        if len(self.sequence_list.error_list)>2:
            last_error = self.sequence_list.error_list[-1]
            prev_error = self.sequence_list.error_list[-1]
            if last_error < prev_error:
                self.sequence_list.best_sequence.clear()
                self.sequence_list.best_sequence.append(self.iteration_number - 1)
                self.current_sequence = self.sequence_algorithms.generate_next_sequence(self.current_sequence)
                self.set_sequence(self.current_sequence)
            elif last_error == prev_error:
                self.sequence_list.best_sequence.append(self.iteration_number - 1)
                self.current_sequence = self.sequence_algorithms.generate_next_sequence(self.current_sequence)
                self.set_sequence(self.current_sequence)
            else:
                p_accept = math.exp((prev_error - last_error) / self.solver_data.annealing_temperature)
                random_number = random.random()
                if p_accept >= random_number:
                    self.current_sequence = self.sequence_algorithms.generate_next_sequence(self.current_sequence)
                    self.set_sequence(self.current_sequence)
                else:
                    self.current_sequence = self.sequence_list[-1]
                    self.current_sequence = self.sequence_algorithms.generate_next_sequence(self.current_sequence)
                    self.set_sequence(self.current_sequence)

        else:
            self.current_sequence = self.sequence_algorithms.generate_next_sequence(self.current_sequence)
            self.set_sequence(self.current_sequence)