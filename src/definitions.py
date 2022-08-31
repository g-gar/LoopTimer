
class Loop:
    '''Main class
    '''

    def __init__(self):
        self.__index_generator__ = None
        self.__processors__ = {}

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

    def run(self):
        '''Entry point for running the execution flow assigned in Loop.execution_flow()
        '''

        for index in self.__index_generator__:
            for processor in self.__processors__.get(0, None):
                processor.run(index=index)
        self.__index_generator__.close()
        self.__index_generator__.reset()
