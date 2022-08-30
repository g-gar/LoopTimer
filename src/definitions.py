from abc import abstractmethod

from collections.abc import Generator
import abc

class Processor(metaclass=abc.ABCMeta):
    def before_start(self, **kwargs):
        pass

    @classmethod
    @abstractmethod
    def run(self, **kwargs):
        pass

    def after_end(self):
        pass

class IterativeGenerator(Generator):
    def __init__(self, start, end, jump=1, stop_condition = lambda idx: True):
        self.start = start
        self.jump = abs(jump)
        self.end = end
        self.stop_condition = stop_condition
        self.continue_condition = int.__lt__ if start < end else int.__gt__
        self.reset()

    def send(self, value):
        increment = self.jump * (1 if self.start < self.end else -1)
        continue_loop = self.stop_condition(self.current + increment)
        continue_loop &= self.continue_condition(self.current + increment, self.end)
        while continue_loop:
            self.current = self.current + increment
            return self.current
        raise StopIteration

    def throw(self, type, value=None, traceback=None):
        super().throw(type, value, traceback)

    def reset(self):
        self.current = self.start + ((-1 if self.start < self.end else 1) * self.jump)

class Loop:
    def __init__(self):
        self.__index_generator__ = None
        self.__processors__ = dict()

    def index_generator(self, generator):
        self.__index_generator__ = generator
        return self

    def add_processor(self, processor, priority = 0):
        self.__processors__[priority] = [*self.__processors__.get(priority, list()), *[processor]]
        return self

    def run(self):
        for index in self.__index_generator__:
            for processor in self.__processors__.get(0, None):
                processor.run(index=index)
        self.__index_generator__.close()
        self.__index_generator__.reset()
        return self
