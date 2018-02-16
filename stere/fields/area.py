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

        Every Field that implements perform() must return True or False.
        If True, assume the argument has been used. If False,
        assume the argument is still available.

        Args:
            args: Array that should be equal to the number of
                Fields in the Area that take an argument.
        """
        arg_index = 0
        for field_name, field in self.items.items():
            result = field.perform(args[arg_index])
            # If we've run out of arguments, don't increase the index.
            if result and len(args) > arg_index:
                arg_index += 1
