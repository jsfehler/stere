import copy

from .strategy import strategy


class SplinterBase:
    def is_present(self, *args, **kwargs):
        func = getattr(self.browser, f'is_element_present_by_{self.strategy}')
        return func(self.locator, *args, **kwargs)

    def is_not_present(self, *args, **kwargs):
        func = getattr(
            self.browser, f'is_element_not_present_by_{self.strategy}')
        return func(self.locator, *args, **kwargs)

    def is_visible(self, *args, **kwargs):
        func = self.browser.is_element_visible_by_xpath
        xpath = f'.//*[@{self.strategy}="{self.locator}"]'
        return func(xpath, *args, **kwargs)

    def is_not_visible(self, *args, **kwargs):
        func = self.browser.is_element_not_visible_by_xpath
        xpath = f'.//*[@{self.strategy}="{self.locator}"]'
        return func(xpath, *args, **kwargs)

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


class FindByDataStarAttribute:
    """Strategy to find an element by an arbitrary data-* attribute."""
    def is_present(self, *args, **kwargs):
        return self.browser.is_element_present_by_xpath(
            f'.//*[@{self._data_star_attribute}="{self.locator}"]')

    def is_not_present(self, *args, **kwargs):
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
    """Adds a new splinter strategy that finds by data_star_attribute.
    Args:
        data_star_attribute (str): The data-* attribute to use in the new
            strategy.
    """
    find_by_data_star = copy.deepcopy(FindByDataStarAttribute)
    find_by_data_star._data_star_attribute = data_star_attribute
    return strategy(data_star_attribute)(find_by_data_star)
