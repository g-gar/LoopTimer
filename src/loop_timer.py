import time
import json

from src.constants import LoopTimerStates, LoopTimerDefaults
from src.util import SafeExecutor, PartialFormatter, memoize
from src.loop_timer_state_info import LoopTimerStateInfo

def memoizer(fn):
	cache = []
	def actual_memoizer(x):
		if x in cache:
			print(f'{x} already computed, returning... {cache[x]}')
			return cache[x]
		else: return fn(x)
	return actual_memoizer

class LoopTimer:
	def __init__(self):
		self.state = LoopTimerStates.RUNNING
		self.stop_conditions = list()
		self.pause_conditions = list()
		self.iterations_state_info = dict()
		
	def run(self, fn, end, start = 0, step = 1, batch_size = 1, precision = 8, stop_conditions = list(), pause_conditions = list(), template = LoopTimerDefaults.TEMPLATE.value, memoize_enabled = True):
		batch_results = list()
		cache = {}
		if memoize_enabled == True:
			fn = memoizer(fn)
		loop_start_time = time.time_ns()
		for i in range(start, end, batch_size):
			stop_conditions.append(lambda x: (end + 1 == x, lambda: print('stop'), LoopTimerStates.STOPPED))
			batch_result = self.execute_batch(fn, i, batch_size, step, stop_conditions, pause_conditions, template, **{**{
				'precision': precision,
				'loop_start_time': time.time_ns(),
				'loop_start_iteration': start,
				'loop_end_iteration': end,
				'loop_start_time': loop_start_time,
				#'loop_step_size': step #TODO: whyyy
			}, **LoopTimerDefaults.LOOP_TIMER_STATE_INFO.value})
			batch_results.append(batch_result)
			temp = batch_result[max(batch_result.keys())]
			print(PartialFormatter().format(template, **temp))
			if self.state is not LoopTimerStates.RUNNING:
				#TODO: persist some data for resumes or restarts
				break
		return batch_results

	def execute_batch(self, fn, batch_start, batch_size, loop_step_size = LoopTimerDefaults.STEP_SIZE.value, stop_conditions = list(), pause_conditions = list(), template = LoopTimerDefaults.TEMPLATE, **template_args) -> dict:
		states = list()
		last_state = None
		conditions_length = len([*pause_conditions, *stop_conditions])
		batch_start_time = time.time_ns()
		max_iteration = batch_start + batch_size
		for iteration in range(batch_start, max_iteration, loop_step_size):
			if conditions_length > 0 and self.state not in [LoopTimerStates.PAUSED, LoopTimerStates.STOPPED]:
				a = sorted([fn(iteration) for fn in [*pause_conditions, *stop_conditions]], key = lambda x: x[2], reverse = True)
				for _, callback, condition_type in filter(lambda a: a[2] in [LoopTimerStates.PAUSED, LoopTimerStates.STOPPED] and a[0], a):
					if 'batch_end_time' in last_state and last_state['batch_end_time'] is not None:
						last_state['batch_end_time'] = time.time_ns()
					self.state = condition_type
					batch_end_time = time.time_ns()
					for state in states: state['batch_end_time'] = batch_end_time
					SafeExecutor.execute(callback, self)
					iteration = None
					break

			if self.state == LoopTimerStates.RUNNING:
				iteration_execution_metrics = self.execute_single(fn, iteration)
				template_formattings = {
					'current_iteration': iteration,
					'batch_size': batch_size,
					'batch_start_time': batch_start_time,
					'batch_end_time': None
				}
				last_state = LoopTimerStateInfo({**template_args, **template_formattings, **iteration_execution_metrics})
				states.append(last_state)
		batch_end_time = time.time_ns()
		for state in states:
			state.__setitem__('batch_end_time', batch_end_time)
		return {state['current_iteration']:state for state in states}

	def execute_single(self, fn, iteration):
		start, value, end = self.time(fn, iteration)
		return {
			'iteration_start_time': start,
			'value': value,
			'current_iteration': iteration,
			'iteration_end_time': end
		}

	def time(self, fn, *args):
		start = time.time_ns()
		value = self.execute_function(fn, *args)
		end = time.time_ns()
		return start, value, end

	def execute_function(self, fn, *args):
		return fn(*args)

	def compute_total_loop_time(self):
		pass