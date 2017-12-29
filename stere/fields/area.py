from .fields import Button, Input, Link, Text
from .dropdown import Dropdown


class Area():
    """A collection of unique fields."""

    def __init__(self, **kwargs):
        if kwargs.get('items') is not None:
            raise ValueError('"items" is a reserved parameter.')

        self.items = {}
        for key, value in kwargs.items():
            if type(value) not in [Button, Input, Link, Text, Dropdown]:
                raise ValueError(
                    'Areas must only be initialized with field objects.'
                )
            self.items[key] = value
            setattr(self, key, value)

    def perform(self, *args):
        """For every field in the area, sequentially "do the right thing".

        Args:
            args: Array of string that should be equal to the number of
                Input objects in the Area.
        """
        arg_index = 0
        for key, value in self.items.items():
            if type(value) is Input:
                value.fill(args[arg_index])
                arg_index += 1
            elif type(value) is Link:
                value.click()
            elif type(value) is Button:
                value.click()
            elif type(value) is Dropdown:
                value.select(args[arg_index])
                arg_index += 1
