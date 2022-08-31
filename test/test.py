# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring

from test.util import PartialFormatter

from src.definitions import Loop
from src.generators import IterativeGenerator
from src.processors import Processor

class LoggingProcessor(Processor):
    def __init__(self, template):
        self.template = template

    def run(self, **kwargs):
        if 'index' in kwargs:
            print(PartialFormatter().format(self.template, **kwargs))

if __name__ == '__main__':
    TEMPLATE = 'current iteration: index={index}'

    generator1 = IterativeGenerator(0, 200, 2, lambda idx: idx < 20)
    generator2 = IterativeGenerator(0, 5, 1)
    loop = Loop() \
        .index_generator(generator1) \
        .add_processor(LoggingProcessor(TEMPLATE)) \

    loop.run()

    loop.index_generator(generator2) \
        .run()
