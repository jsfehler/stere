from ..fields import Field


class Area:
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

            # Field can be called directly.
            setattr(self, key, value)

        self._workflow = None

    def workflow(self, value):
        """Sets the current workflow for an Area.

        Designed for chaining before a call to perform().
        ie: my_area.workflow('Foobar').perform()

        Returns:
            self
        """
        self._workflow = value
        return self

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
        workflow = self._workflow
        for field in self.items.values():
            if workflow is not None and workflow not in field.workflows:
                continue
            result = field.perform(args[arg_index])
            # If we've run out of arguments, don't increase the index.
            if result and len(args) > (arg_index + 1):
                arg_index += 1

        self._workflow = None
