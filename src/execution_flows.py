from abc import ABCMeta, abstractmethod

from src.processors import Processor

class ExecutionFlow(metaclass=ABCMeta):
    '''Metaclass for execution flows'''

    @abstractmethod
    def run(self, generator, processors : dict[int, list[Processor]]):
        '''Run method'''

class SynchronousExecutionFlow(ExecutionFlow):
    '''Synchronous execution flow'''

    def run(self, generator, processors : dict[int, list[Processor]]):
        for idx in generator:
            for processor in processors.get(0, None):
                processor.run(index=idx)
