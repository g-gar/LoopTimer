
from src.execution_flows import ExecutionFlow
from src.processors import Processor


class Loop:
    '''Main class
    '''
    def __init__(self):
        self.__index_generator__ = None
        self.__processors__ = dict[int, list[Processor]]()

    def index_generator(self, generator):
        '''Builder method for setting a generator function
        '''
        self.__index_generator__ = generator
        return self

    def add_processor(self, processor, priority = 0):
        '''Builder method for setting a processor with a priority
        '''
        self.__processors__[priority] = [*self.__processors__.get(priority, []), *[processor]]
        return self

    def run(self, execution_flow:ExecutionFlow):
        '''Entry point for running the execution flow assigned in Loop.execution_flow()
        '''
        execution_flow.run(self.__index_generator__, self.__processors__)
        self.__index_generator__.close()
        self.__index_generator__.reset()
