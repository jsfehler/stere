from typing import Any, Optional

from stere import Stere


class ElementStrategy(Stere):
    """Base class for a Strategy.

    Elements are used by Fields as the source of what finds the DOM content.

    Arguments:
        strategy (str): The type of strategy to use when locating an element.
        locator (str): The locator for the strategy.
        parent_locator: A parent object to search from. If None,
            search will occur from top of the DOM.
    """

    def __init__(
        self, strategy: str,
        locator: str,
        parent_locator: Optional[Any] = None,
    ):
        self.strategy = strategy
        self.locator = locator
        self.parent_locator = parent_locator

        # A Field that should be searched for and whose element should be set
        # as the parent, but only when .find() is called.
        self.root: Optional[Any] = None

    def _find_all(self, wait_time: Optional[int] = None):
        """Find from inside a parent element."""
        raise NotImplementedError

    def find(self, wait_time: Optional[int] = None):
        """Use ElementStrategy._find_all() to find an element.

        If a root has been set, it will set the parent_locator attribute
        before searching.
        """
        if self.root:
            self.parent_locator = self.root.find(wait_time=wait_time)
        return self._find_all(wait_time=wait_time)
