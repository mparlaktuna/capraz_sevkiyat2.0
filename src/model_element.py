from PyQt5.QtCore import *
from collections import OrderedDict
from src.good_store import GoodStore


class ModelElement(QObject):

    def __init__(self):
        QObject.__init__(self)
        self.element_name = "element"
        self.current_time = 0
        self.next_state_time = 1000
        self.state = 0
        self.state_list = []
        self.step_finish = True
        self.state_functions = OrderedDict()
        self.state_functions['done'] = self.done
        self.current_state_name = "coming"
        self.good_store = GoodStore()

    def check_next_time(self):
        if self.current_time == self.next_state_time:
            return True
        else:
            return False

    def step_forward(self, current_time):
        self.current_time = current_time
        self.current_state_name = self.state_list[self.state]
        self.state_functions[self.current_state_name]()
        self.current_state_name = self.state_list[self.state]
        self.step_finish = True

    def done(self):
        self.current_state_name = 'done'
