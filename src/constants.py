from enum import Enum

class LoopTimerStates(Enum):
	CREATED = 0
	RUNNING = 1
	PAUSED = 2
	RESUMED = 3
	STOPPED = 4

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

class LoopTimerDefaults(Enum):
	TEMPLATE:str = 'iteration = {current_iteration} \t took {batch_elapsed_time:.{precision}f}s \t total = {total_elapsed_time:.{precision}f}s \t value = {value}'
	STEP_SIZE = 1
	LOOP_TIMER_STATE_INFO = {
		'batch_start_iteration': lambda d: d['current_iteration']//d['batch_size']*d['batch_size'],
		'batch_end_iteration': lambda d: d['current_iteration']//d['batch_size']*d['batch_size']+d['batch_size'],
		'batch_remaining_iterations': lambda d: (d['current_iteration']//d['batch_size'])*d['batch_size'],
		'loop_remaining_iterations': lambda d: d['current_iteration']-d['loop_end_iteration'],
		'batch_elapsed_time': lambda d: d['batch_end_time'] - d['batch_start_time']
	}
