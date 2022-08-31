from abc import ABCMeta, abstractmethod
from typing import Dict, List

from src.processors import Processor
from src.util import not_none

class ExecutionFlow(metaclass=ABCMeta):
    '''Metaclass for execution flows'''

    def __init__(self, generator = None, processors : Dict[int, List[Processor]] = None):
        self.__generator__ = generator
        self.__processors__ = processors

    @not_none
    def generator(self, generator) -> any:
        '''Generator'''
        self.__generator__ = generator
        return self

    @not_none
    def processors(self, **kwargs : Dict[int, List[Processor]]) -> any:
        '''Processors'''
        self.__processors__ = kwargs
        return self

    @abstractmethod
    def run(self):
        '''Run method'''
