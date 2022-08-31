# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring

from test.util import PartialFormatter

from src.definitions import Loop, IterativeGenerator, Processor

class LoggingProcessor(Processor):
    def __init__(self, template):
        self.template = template

    @classmethod
    def run(cls, **kwargs):
        if 'index' in kwargs:
            print(PartialFormatter().format(cls.template, **kwargs))

if __name__ == '__main__':
    TEMPLATE = 'current iteration: index={index}'
    loop = Loop() \
        .index_generator(IterativeGenerator(0, 200, 2, lambda idx: idx < 20)) \
        .add_processor(LoggingProcessor(TEMPLATE)) \
        .run() \
        .index_generator(IterativeGenerator(0, 5, 1)) \
        .run()
