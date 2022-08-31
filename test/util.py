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
            