from abc import abstractmethod

from collections.abc import Generator
import abc

class Processor(metaclass=abc.ABCMeta):
    'Base type for processors'

    def before_start(self, **kwargs):
        'Defines the processor function before starting the executing of the first iteration'

    @classmethod
    @abstractmethod
    def run(cls, **kwargs):
        'Defines the processor function to run on each iteration'

    def after_end(self):
        'Defines the processor function after finishing the execution of the last iteration'

class IterativeGenerator(Generator):
    'Custom Generator class for lineal iterative paths'

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
        super().throw(type, val, tb)

    def reset(self):
        'Sets current index to it\'s starting value'

        self.current = self.start + ((-1 if self.start < self.end else 1) * self.jump)

class Loop:
    'Main class'

    def __init__(self):
        self.__index_generator__ = None
        self.__processors__ = {}

    def index_generator(self, generator):
        'Builder method for setting a generator function'

        self.__index_generator__ = generator
        return self

    def add_processor(self, processor, priority = 0):
        'Builder method for setting a processor with a priority'

        self.__processors__[priority] = [*self.__processors__.get(priority, []), *[processor]]
        return self

    def run(self):
        'Entry point for running the execution flow assigned in Loop.execution_flow()'

        for index in self.__index_generator__:
            for processor in self.__processors__.get(0, None):
                processor.run(index=index)
        self.__index_generator__.close()
        self.__index_generator__.reset()
