from PyQt5.QtCore import *
from collections import OrderedDict


class ModelElement(QObject):
    done_signal = pyqtSignal(int, str, name='done')
    time_signal = pyqtSignal(int, str, name='next_time')
    state_finish = pyqtSignal(int, str, str, name='state_finish')
    state_start = pyqtSignal(int, str, str, name='state_start')

    def __init__(self):
        QObject.__init__(self)
        self.element_name = "element"
        self.current_time = 0
        self.state = 0
        self.state_list = []
        self.step_finish = True
        self.state_functions = OrderedDict()
        self.state_functions['done'] = self.done

    def step_forward(self, current_time):
        print(self.element_name, current_time)
        self.current_time = current_time
        state_name = self.state_list[self.state]
        self.state_functions[state_name]()
        self.step_finish = True

    def done(self):
        print(self.element_name, "Done")
        #self.done_signal.emit(self.current_time, self.element_name)