import time
from functools import reduce
import json

from src.constants import LoopTimerStates, LoopTimerDefaults
from src.util import SafeExecutor, PartialFormatter, memoize
from src.loop_timer_state_info import LoopTimerStateInfo
from src.loop_timer import LoopTimer

def isprime(num):
	'''checks if number is prime

	return type : boolean'''
	if num < 2:
		return False
	if num in [1, 2]:
		return True
	else:
		# check_till - checks till we reach square-root of n.
		check_till = int(num ** 0.5) + 1
		# xrange - fetch number as when required
		# xrange - starts with 3, check for only odd number
		if num % 2 == 0:
			return False
		for div in range(3,check_till, 2):
			if num % div == 0:
				return False
		return True

if __name__ == '__main__':
	
	#LoopTimer.run(lambda x: 2**x, 50, batch_size = 10)

	start, value, end = LoopTimer().time(lambda i: (
		10**100000
	), None)

	result = reduce(int.__and__, [bool(x % 2) for x in range(2,8)])

	conditions = {
		0: lambda x: (True, None, LoopTimerStates.RESUMED),
		1: lambda x: (2 == x, lambda: print('pause'), LoopTimerStates.PAUSED),
		2: lambda x: (2 == x, lambda: print('stop'), LoopTimerStates.STOPPED)
	}

	#LoopTimer().execute_batch(print, 10, 20, 1)
	results = LoopTimer().run(isprime, 100, batch_size=10, stop_conditions = [lambda x: (21 == x, lambda lt: print('stop'), LoopTimerStates.STOPPED)])
	print(len(results))