import time

from src.constants import LoopTimerStates, LoopTimerDefaults
from src.util import SafeExecutor, PartialFormatter, memoize
from src.loop_timer_state_info import LoopTimerStateInfo

class AbstractLoop:
	def __init__(self):
		self.state = LoopTimerStates.CREATED

	def run(self, **args):
		pass

	def start(self):
		pass

	def pause(self):
		pass

	def resume(self):
		pass

	def stop(self):
		pass

	def restart(self):
		pass

class IterativeLoop(AbstractLoop):

	def __init__(self, **args):
		self.state = LoopTimerStates.CREATED

	def before_start(self, fn, *args):
		pass

	def after_end(self, fn, *args):
		pass

	def on_iteration_start(self, fn, *args):
		pass

	def on_iteration_end(self, fn, *args):
		pass

	def on_stop(self, fn, *args):
		pass

	def on_pause(self, fn, *args):
		pass

	def run(self, **args):
		pass

class BatchedIterativeLoop(AbstractLoop):

	def __init__(self, **args):
		self.state = LoopTimerStates.CREATED

	def before_start(self, fn, *args):
		pass

	def after_end(self, fn, *args):
		pass

	def on_iteration_start(self, fn, *args):
		pass

	def on_iteration_end(self, fn, *args):
		pass

	def on_batch_start(self, fn, *args):
		pass

	def on_batch_end(self, fn, *args):
		pass

	def on_stop(self, fn, *args):
		pass

	def on_pause(self, fn, *args):
		pass

	def run(self, **args):
		pass