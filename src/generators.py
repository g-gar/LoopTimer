# pylint: disable=useless-super-delegation

from collections.abc import Generator

class IterativeGenerator(Generator):
    '''Custom Generator class for lineal iterative paths
    '''

    def __init__(self, start, end, jump=1, stop_condition = lambda idx: True):
        self.start = start
        self.jump = abs(jump)
        self.end = end
        self.stop_condition = stop_condition
        self.continue_condition = int.__lt__ if start < end else int.__gt__
        self.reset()

    def send(self, value):
        increment = self.jump * (1 if self.start < self.end else -1)
        continue_loop = self.stop_condition(self.current + increment) & \
            self.continue_condition(self.current + increment, self.end)
        while continue_loop:
            self.current += increment
            return self.current
        raise StopIteration

    def throw(self, typ, val=None, tb=None):
        return super().throw(typ, val, tb)

    def reset(self):
        '''Sets current index to it\'s starting value
        '''

        self.current = self.start + (-1 if self.start < self.end else 1) * self.jump
