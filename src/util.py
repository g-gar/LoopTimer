from functools import wraps
import string
from src.loop_timer_state_info import LoopTimerStateInfo

#FROM https://kitchingroup.cheme.cmu.edu/blog/2013/06/26/Memoizing-instance-methods-in-a-class/
def memoize(fn):
	cache = {}
	@wraps(fn)
	def wrap(*args):
		if args not in cache:
			print('Running func with ', args)
			cache[args] = fn(*args)
		else:
			print(f'result in cache with args {args} and value {cache[args]}')
		return cache[args]
	return wrap

class SafeExecutor:
	@staticmethod
	def execute(fn, *args, print_exception = False):
		try:
			result = fn(*args)
		except Exception as e:
			if print_exception:
				print(e)
			result = None
		finally:
			return result

#FROM https://stackoverflow.com/a/20250018/13758294
class PartialFormatter(string.Formatter):
	def __init__(self, missing='[NOT FOUND]', bad_fmt='[BAD FORMATTING]'):
		self.missing, self.bad_fmt=missing, bad_fmt

	def get_field(self, field_name, args, kwargs):
		try:
			if isinstance(kwargs, LoopTimerStateInfo):
				val = kwargs.__get__item(field_name)
			val=super().get_field(field_name, args, kwargs)
		except (KeyError, AttributeError):
			val=None,field_name 
		return val

	def format_field(self, value, spec):
		# handle an invalid format
		if value==None: return self.missing
		try:
			return super().format_field(value, spec)
		except ValueError:
			if self.bad_fmt is not None: return self.bad_fmt   
			else: raise
