# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring

import string

# FROM https://stackoverflow.com/a/20250018/13758294
class PartialFormatter(string.Formatter):
    def __init__(self, missing='[NOT FOUND]', bad_fmt='[BAD FORMATTING]'):
        self.missing, self.bad_fmt=missing, bad_fmt

    def get_field(self, field_name, args, kwargs):
        try:
            val = super().get_field(field_name, args, kwargs)
        except (KeyError, AttributeError):
            val = None, field_name
        return val

    def format_field(self, value, format_spec):
        # handle an invalid format
        if value is None:
            return self.missing
        try:
            return super().format_field(value, format_spec)
        except ValueError:
            if self.bad_fmt is not None:
                return self.bad_fmt
            raise

# FROM https://stackoverflow.com/a/53639511/19797568
def not_none(nullable_parameters=None):
    def the_actual_test(_f, args, filter_array):
        has_none = False
        bad_parameters = []
        if isinstance(filter_array, str):
            filter_array = [filter_array]
        if not filter_array:
            if any(arg[1] is None for arg in args):
                raise ValueError(f'function {_f.__name__}: Parameters cannot be None. ')
        elif isinstance(filter_array, list):
            for arg in args:
                for _filter in filter_array:
                    if arg[0] != _filter:
                        if arg[1] is None:
                            has_none = True
                            bad_parameters.append(arg[0])
                            break
        if has_none:
            raise ValueError(f'function {_f.__name__}: '
            'Parameters {bad_parameters} cannot be None. ')

    def real_decorator(_f):
        v_names = _f.__code__.co_varnames
        def wrapper(*args, **kwargs):
            n_args = []
            for idx, arg in enumerate(args):
                n_args.append((v_names[idx], arg))
            the_actual_test(_f, n_args, nullable_parameters)
            result = _f(*args, **kwargs)
            return result
        return wrapper
    return real_decorator
