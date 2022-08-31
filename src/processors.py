from abc import abstractmethod, ABCMeta

class Processor(metaclass=ABCMeta):
    '''Base type for processors
    '''

    def before_start(self, **kwargs):
        '''Defines the processor function before starting the executing of the first iteration
        '''

    @abstractmethod
    def run(self, **kwargs):
        '''Defines the processor function to run on each iteration
        '''

    def after_end(self):
        '''Defines the processor function after finishing the execution of the last iteration
        '''
