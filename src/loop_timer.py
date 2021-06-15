import time

class LoopTimer:
	template = 'iteration = {current_iteration} \t took {batch_elapsed_time:.8f}s \t total = {total_elapsed_time:.8f}s \t value = {iteration_returned_value}'

	@staticmethod
	def run(fn, end, start = 0, step = 1, batch_size = 1, precision = 8, template = template):
		timer, timer_total = time.process_time(), time.process_time()
		for i in range(start, end, step):
			value = fn(i)
			if i > 0 & i % batch_size == 0:
				timer_end = time.process_time()
				parameters = LoopTimer.get_template_formattings_map(i, start, end, step, batch_size, timer, timer_total, timer_end, value)
				print(template.format_map(parameters))
				timer = time.process_time()

	@staticmethod
	def get_template_formattings_map(current_iteration, start, end, step, batch_size, timer, timer_total, timer_end, value):
		return {
			'current_iteration': current_iteration,
			'batch_elapsed_time': timer_end - timer,
			'total_elapsed_time': timer_end - timer_total,
			'iteration_returned_value': value,
			'batch_start': timer,
			'batch_end': timer_end,
			'loop_start_time': timer_total,
			'loop_start_iteration': start,
			'loop_end_iteration': end,
			'loop_step_size': step,
			'batch_size': batch_size,
			'batch_remaining_iterations': current_iteration % batch_size,
			'loop_remaining_iterations': end - 1 - current_iteration
		}