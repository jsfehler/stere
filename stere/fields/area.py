from .fields import Field


class Area():
    """A collection of unique fields."""

    def __init__(self, **kwargs):
        if kwargs.get('items') is not None:
            raise ValueError('"items" is a reserved parameter.')

        self.root = kwargs.get('root')

        self.items = {}
        for key, value in kwargs.items():
            if not isinstance(value, Field):
                raise ValueError(
                    'Areas must only be initialized with field objects.'
                )
            self.items[key] = value
            # Sets the root for the element, if provided.
            if self.root is not None and value is not self.root:
                self.items[key]._element.root = self.root
            setattr(self, key, value)

    def perform(self, *args):
        """For every Field in an Area, sequentially "do the right thing"
        by calling the Field's perform() method.

        Args:
            args: Array that should be equal to the number of
                Fields in the Area that take an argument.
        """
        arg_index = 0
        for key, value in self.items.items():
            result = value.perform(args[arg_index])
            if result:
                arg_index += 1
