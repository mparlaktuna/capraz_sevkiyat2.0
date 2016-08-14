from src.general_solver import GeneralSolver


class SequenceSolver(GeneralSolver):

    def __init__(self):
        GeneralSolver.__init__(self)

    def step_forward(self):
        """
        moves the model forward
        """
        self.model.next_time()
        print("Times: ", self.model.time_list)
        print("Finished: ", self.model.check_done())
