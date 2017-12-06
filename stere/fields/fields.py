from .element_builder import build_element


class Field():
    """Base class for objects on a page."""
    def __init__(self, strategy, locator):
        self.strategy = strategy
        self.locator = locator
        self.element = build_element(strategy, locator)

    def find(self):
        """Find the first matching element.

        Returns:
            Element

        Raises:
            ValueError - If more than one element is found.
        """
        found_elements = self.element.find()
        if len(found_elements) > 2:
            raise ValueError("Expected one element, found multiple")
        return found_elements.first

    def find_all(self):
        """Find all matching elements.

        Returns:
            List
        """
        return self.element.find()


class Button(Field):
    """Convenience Class on top of Field."""
    def click(self):
        self.find().click()


class Input(Field):
    """Convenience Class on top of Field."""
    def fill(self, value):
        self.find().fill(value)


class Link(Field):
    """Convenience Class on top of Field."""
    def click(self):
        self.find().click()

    @property
    def text(self):
        elem = self.find()
        return elem.text


class Text(Field):
    """Convenience Class on top of Field."""
    @property
    def text(self):
        elem = self.find()
        return elem.text


class Area():
    """A collection of unique fields."""

    def __init__(self, **kwargs):
        if kwargs.get('items') is not None:
            raise ValueError('"items" is a reserved parameter.')

        self.items = {}
        for key, value in kwargs.items():
            if type(value) not in [Button, Input, Link, Text]:
                raise ValueError(
                    'Areas must only be initialized with field objects.'
                )
            self.items[key] = value

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
