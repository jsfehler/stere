from .strategy import strategy


@strategy('css')
class FindByCss():
    def _find_all(self):
        """Find from page root."""
        return self.browser.find_by_css(self.locator)

    def _find_all_in_parent(self):
        """Find from inside a parent element."""
        return self.parent_locator.find_by_css(self.locator)


@strategy('xpath')
class FindByXPath():
    def _find_all(self):
        """Find from page root."""
        return self.browser.find_by_xpath(self.locator)

    def _find_all_in_parent(self):
        """Find from inside a parent element."""
        return self.parent_locator.find_by_xpath(self.locator)


@strategy('tag')
class FindByTag():
    def _find_all(self):
        """Find from page root."""
        return self.browser.find_by_tag(self.locator)

    def _find_all_in_parent(self):
        """Find from inside a parent element."""
        return self.parent_locator.find_by_tag(self.locator)


@strategy('name')
class FindByName():
    def _find_all(self):
        """Find from page root."""
        return self.browser.find_by_name(self.locator)

    def _find_all_in_parent(self):
        """Find from inside a parent element."""
        return self.parent_locator.find_by_name(self.locator)


@strategy('text')
class FindByText():
    def _find_all(self):
        """Find from page root."""
        return self.browser.find_by_text(self.locator)

    def _find_all_in_parent(self):
        """Find from inside a parent element."""
        return self.parent_locator.find_by_text(self.locator)


@strategy('id')
class FindById():
    def _find_all(self):
        """Find from page root."""
        return self.browser.find_by_id(self.locator)

    def _find_all_in_parent(self):
        """Find from inside a parent element."""
        return self.parent_locator.find_by_id(self.locator)


@strategy('value')
class FindByValue():
    def _find_all(self):
        """Find from page root."""
        return self.browser.find_by_value(self.locator)

    def _find_all_in_parent(self):
        """Find from inside a parent element."""
        return self.parent_locator.find_by_value(self.locator)
