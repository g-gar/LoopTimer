from src.definitions import Loop, IterativeGenerator, Processor
from test.util import PartialFormatter

class LoggingProcessor(Processor):
	def __init__(self, template):
		self.template = template

	def run(self, **kwargs):
		if 'index' in kwargs:
			print(PartialFormatter().format(self.template, **kwargs))

if __name__ == '__main__':
	template = 'current iteration: index={index}'
	loop = Loop() \
		.index_generator(IterativeGenerator(0, 200, 2, lambda idx: idx < 20)) \
		.add_processor(LoggingProcessor(template)) \
		.run() \
		.index_generator(IterativeGenerator(0, 5, 1)) \
		.run()
