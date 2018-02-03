from stere import Stere

from stere.strategy import strategies


def build_element(desired_strategy, locator, parent_locator=None):
    """Build a Field Object out of a BaseElement and a Strategy."""

    if desired_strategy in strategies.keys():
        bases = (BaseElement, strategies[desired_strategy])
        element_class = type('Element', bases, dict())
        return element_class(desired_strategy, locator, parent_locator)

    raise ValueError(f'The strategy "{desired_strategy}" is undefined.')


class BaseElement(Stere):
    """Combined with a Strategy to form an Element.

    Elements are used by Fields as the source of what finds the DOM element.
    """
    def __init__(self, strategy, locator, parent_locator=None):
        self.strategy = strategy
        self.locator = locator
        self.parent_locator = parent_locator

    def find(self):
        if self.parent_locator is None:
            return self._find_all()

        return self._find_all_in_parent()
