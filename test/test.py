from test.util import PartialFormatter

from src.definitions import Loop, IterativeGenerator, Processor

class LoggingProcessor(Processor):
    def __init__(self, template):
        self.template = template

    def run(self, **kwargs):
        if 'index' in kwargs:
            print(PartialFormatter().format(self.template, **kwargs))

if __name__ == '__main__':
    TEMPLATE = 'current iteration: index={index}'
    loop = Loop() \
        .index_generator(IterativeGenerator(0, 200, 2, lambda idx: idx < 20)) \
        .add_processor(LoggingProcessor(TEMPLATE)) \
        .run() \
        .index_generator(IterativeGenerator(0, 5, 1)) \
        .run()
