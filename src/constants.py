from enum import Enum

class BaseEnum(Enum):
    '''Common enum operations
    '''

    def __ge__(self, other):
        if self.__class__ is other.__class__:
            return self.value >= other.value
        return NotImplemented
    def __gt__(self, other):
        if self.__class__ is other.__class__:
            return self.value > other.value
        return NotImplemented
    def __le__(self, other):
        if self.__class__ is other.__class__:
            return self.value <= other.value
        return NotImplemented
    def __lt__(self, other):
        if self.__class__ is other.__class__:
            return self.value < other.value
        return NotImplemented

class State(BaseEnum):
    '''Workflow execution states
    '''

    CREATED = 0
    RUNNING = 1
    PAUSED  = 2
    STOPPED = 3
    