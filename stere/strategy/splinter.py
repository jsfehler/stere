import copy
import typing

from .strategy import strategy
from ..utils import _retry


class SplinterBase:
    def is_clickable(self, wait_time: typing.Optional[int] = None) -> bool:
        """Check if an element is present in the DOM and clickable.

        Arguments:
            wait_time (int): The number of seconds to wait. If not specified,
                Stere.retry_time will be used.
        """
        return _retry(
            lambda: self.find() and self.find()._element.is_enabled(),
            wait_time,
        )

    def is_not_clickable(self, wait_time: typing.Optional[int] = None) -> bool:
        """Check if an element is not clickable in the DOM.

        Arguments:
            wait_time (int): The number of seconds to wait. If not specified,
                Stere.retry_time will be used.
        """
        def search():
            result = self.find(wait_time=0)
            if not result:
                return True
            if result and not result._element.is_enabled():
                return True
            return False

        return _retry(search, wait_time)

    def is_present(self, wait_time: typing.Optional[int] = None) -> bool:
        """Check if an element is present in the DOM.

        Arguments:
            wait_time (int): The number of seconds to wait. If not specified,
                Stere.retry_time will be used.
        """
        return _retry(
            lambda: self.find(),
            wait_time,
        )

    def is_not_present(self, wait_time: typing.Optional[int] = None) -> bool:
        """Check if an element is not present in the DOM.

        Arguments:
            wait_time (int): The number of seconds to wait. If not specified,
                Stere.retry_time will be used.
        """
        return _retry(
            lambda: not self.find(wait_time=0),
            wait_time,
        )

    def is_visible(self, wait_time: typing.Optional[int] = None) -> bool:
        """Check if an element is present in the DOM and visible.

        Arguments:
            wait_time (int): The number of seconds to wait. If not specified,
                Stere.retry_time will be used.
        """
        return _retry(
            lambda: self.find() and self.find().visible,
            wait_time,
        )

    def is_not_visible(self, wait_time: typing.Optional[int] = None) -> bool:
        """Check if an element is not visible in the DOM.

        Arguments:
            wait_time (int): The number of seconds to wait. If not specified,
                Stere.retry_time will be used.
        """
        def search():
            result = self.find(wait_time=0)
            if not result:
                return True
            if result and not result.visible:
                return True
            return False

        return _retry(search, wait_time)

    def _find_all(self, wait_time: typing.Optional[int] = None):
        """Find from page root."""
        func = getattr(self.browser, f'find_by_{self.strategy}')
        return func(self.locator, wait_time=wait_time)

    def _find_all_in_parent(self, wait_time: typing.Optional[int] = None):
        """Find from inside a parent element."""
        func = getattr(self.parent_locator, f'find_by_{self.strategy}')
        return func(self.locator, wait_time=wait_time)


@strategy('css')
class FindByCss(SplinterBase):
    strategy = 'css'


@strategy('xpath')
class FindByXPath(SplinterBase):
    strategy = 'xpath'


@strategy('tag')
class FindByTag(SplinterBase):
    strategy = 'tag'


@strategy('name')
class FindByName(SplinterBase):
    strategy = 'name'


@strategy('text')
class FindByText(SplinterBase):
    strategy = 'text'


@strategy('id')
class FindById(SplinterBase):
    strategy = 'id'


@strategy('value')
class FindByValue(SplinterBase):
    strategy = 'value'


class FindByAttribute(SplinterBase):
    """Strategy to find an element by an arbitrary attribute."""

    def _find_all(self, wait_time=None):
        """Find from page root."""
        return self.browser.find_by_xpath(
            f'//*[@{self._attribute}="{self.locator}"]', wait_time=wait_time,
        )

    def _find_all_in_parent(self, wait_time=None):
        """Find from inside parent element."""
        return self.parent_locator.find_by_xpath(
            f'.//*[@{self._attribute}="{self.locator}"]', wait_time=wait_time,
        )


def add_data_star_strategy(data_star_attribute):
    """Add a new splinter strategy that finds by data_star_attribute.

    Arguments:
        data_star_attribute (str): The data-* attribute to use in the new
            strategy.
    """
    find_by_data_star = copy.deepcopy(FindByAttribute)
    find_by_data_star._attribute = data_star_attribute
    return strategy(data_star_attribute)(find_by_data_star)
