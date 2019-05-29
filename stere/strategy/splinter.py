import copy
import time

from .strategy import strategy


class SplinterBase:
    def is_present(self, *args, **kwargs):
        """Check if an element is present in the DOM.

        Takes the same arguments as Splinter's
        `is_element_present_by_xpath`
        """
        func = getattr(self.browser, f'is_element_present_by_{self.strategy}')
        return func(self.locator, *args, **kwargs)

    def is_not_present(self, *args, **kwargs):
        """Check if an element is not present in the DOM.

        Takes the same arguments as Splinter's
        `is_element_not_present_by_xpath`
        """
        func = getattr(
            self.browser, f'is_element_not_present_by_{self.strategy}')
        return func(self.locator, *args, **kwargs)

    def is_visible(self, wait_time=2):
        """Check if an element is present in the DOM and visible.

        Arguments:
            wait_time (int): The number of seconds to wait
        """
        end_time = time.time() + wait_time

        while time.time() < end_time:
            if self.find() and self.find().visible:
                return True
        return False

    def is_not_visible(self, wait_time=2):
        """Check if an element is present in the DOM but not visible.

        Arguments:
            wait_time (int): The number of seconds to wait
        """
        end_time = time.time() + wait_time

        while time.time() < end_time:
            if not self.find() or (self.find() and not self.find().visible):
                return True
        return False

    def _find_all(self):
        """Find from page root."""
        func = getattr(self.browser, f'find_by_{self.strategy}')
        return func(self.locator)

    def _find_all_in_parent(self):
        """Find from inside a parent element."""
        func = getattr(self.parent_locator, f'find_by_{self.strategy}')
        return func(self.locator)


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


class FindByDataStarAttribute(SplinterBase):
    """Strategy to find an element by an arbitrary data-* attribute."""

    def is_present(self, *args, **kwargs):
        """Check if an element is present in the DOM.

        Takes the same arguments as Splinter's
        `is_element_present_by_xpath`
        """
        return self.browser.is_element_present_by_xpath(
            f'.//*[@{self._data_star_attribute}="{self.locator}"]')

    def is_not_present(self, *args, **kwargs):
        """Check if an element is not present in the DOM.

        Takes the same arguments as Splinter's
        `is_element_not_present_by_xpath`
        """
        return self.browser.is_element_not_present_by_xpath(
            f'.//*[@{self._data_star_attribute}="{self.locator}"]')

    def _find_all(self):
        """Find from page root."""
        return self.browser.find_by_xpath(
            f'.//*[@{self._data_star_attribute}="{self.locator}"]')

    def _find_all_in_parent(self):
        """Find from inside parent element."""
        return self.parent_locator.find_by_xpath(
            f'.//*[@{self._data_star_attribute}="{self.locator}"]')


def add_data_star_strategy(data_star_attribute):
    """Add a new splinter strategy that finds by data_star_attribute.

    Arguments:
        data_star_attribute (str): The data-* attribute to use in the new
            strategy.
    """
    find_by_data_star = copy.deepcopy(FindByDataStarAttribute)
    find_by_data_star._data_star_attribute = data_star_attribute
    return strategy(data_star_attribute)(find_by_data_star)
