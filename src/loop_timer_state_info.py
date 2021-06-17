import collections

class LoopTimerStateInfo(dict):
	def __init__(self, complex_getters_defaults = dict(), *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.complex_getters = dict()
		for key, fn in complex_getters_defaults.items(): self.__setitem__(key, fn)
		for key, fn in kwargs.items(): self.__setitem__(f'_{key}_', fn)

	def __setitem__(self, key, item):
		subkey = f'_{key}_'
		if subkey not in self.complex_getters and isinstance(item, collections.Callable):
			self.__dict__[key] = None
			self.complex_getters[subkey] = item
		else:
			self.__dict__[key] = item

	def __getitem__(self, key):
		subkey = f'_{key}_'
		if subkey in self.complex_getters and isinstance(self.complex_getters[subkey], collections.Callable):
			return self.complex_getters[subkey](self)
		else:
			return self.__dict__[key]

	def __repr__(self):
		return repr(self.__dict__)

	def __len__(self):
		return len(self.__dict__)

	def __delitem__(self, key):
		del self.__dict__[key]

	def clear(self):
		return self.__dict__.clear()

	def copy(self):
		return self.__dict__.copy()

	def has_key(self, k):
		return k in self.keys()

	def update(self, *args, **kwargs):
		return self.__dict__.update(*args, **kwargs)

	def keys(self):
		return [k for k in self.__dict__.keys() if k not in ['complex_getters']]

	def values(self):
		return [self.__getitem__(key) for key in self.keys()]

	def items(self):
		return [i for i in self.__dict__.items() if i[0] in self.keys()]

	def pop(self, *args):
		return self.__dict__.pop(*args)

	def __cmp__(self, dict_):
		return self.__cmp__(self.__dict__, dict_)

	def __contains__(self, item):
		return item in self.__dict__

	def __iter__(self):
		return iter(self.__dict__)

	def __unicode__(self):
		return unicode(repr(self.__dict__))