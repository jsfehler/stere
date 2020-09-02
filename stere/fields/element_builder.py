import typing

from stere import Stere
from stere.strategy import strategies


def build_element(desired_strategy, locator, parent_locator=None):
    """Build a Field Object out of a BaseElement and a Strategy."""
    known = strategies.keys()

    if desired_strategy in known:
        bases = (BaseElement, strategies[desired_strategy])
        element_class = type('Element', bases, {})
        return element_class(desired_strategy, locator, parent_locator)

    raise ValueError(
        f'The strategy "{desired_strategy}" is not in {list(known)}.')


class BaseElement(Stere):
    """Combined with a Strategy to form an Element.

    Elements are used by Fields as the source of what finds the DOM element.

    Arguments:
        strategy (str): The type of strategy to use when locating an element.
        locator (str): The locator for the strategy.
        parent_locator: A parent object to search from. If None,
            search will occur from top of page.
    """

    def __init__(self, strategy: str, locator: str, parent_locator=None):
        self.strategy = strategy
        self.locator = locator
        self.parent_locator = parent_locator

        # A Field that should be searched for and set as the parent, but only
        # when .find() is called.
        self.root = None

    def find(self, wait_time: typing.Optional[int] = None):
        """Use _find_all() or _find_all_in_parent() to find an element."""
        if self.root is None and self.parent_locator is None:
            return self._find_all(wait_time=wait_time)

        if self.root:
            self.parent_locator = self.root.find(wait_time=wait_time)
        return self._find_all_in_parent(wait_time=wait_time)
