import urllib.parse
from typing import TypeVar

from .browser_spy import FetchSpy, XHRSpy
from .browserenabled import BrowserEnabled


T = TypeVar('T', bound='Page')


class Page(BrowserEnabled):
    """Represents a single page in an application.
    The Page class is the base which all Page Objects should inherit from.

    Inheriting from Page is not required for Fields or Areas to work.

    All attribute calls that fail are then tried on the browser attribute.
    This allows classes inheriting from Page to act as a proxy to
    whichever browser/driver is being used.

    Using Splinter's browser.url method as an example, the following methods
    are analogous:

    >>> MyPage.url == MyPage.browser.url == browser.url

    The choice of which syntax to use depends on how you want to write your
    test suite.
    """

    # Allows network requests to be spied on
    fetch_spy = FetchSpy()
    xhr_spy = XHRSpy()

    def __getattr__(self, val):
        """If an attribute doesn't exist, try getting it from the browser."""
        return getattr(self.browser, val)

    def __enter__(self: T) -> T:
        """Page Objects can be used as context managers."""
        return self

    def __exit__(self, *args):
        """Page Objects can be used as context managers."""
        pass

    @property
    def page_url(self) -> str:
        """Get a full URL from Stere's base_url and a Page's url_suffix.

        Uses urllib.parse.urljoin to combine the two.
        """
        return urllib.parse.urljoin(self.base_url, self.url_suffix)

    def navigate(self: T) -> T:
        """When the base Stere object has been given the `url_navigator`
        attribute, the base_url attribute, and a Page Object
        has a `url_suffix` attribute, the `navigate()` method can be called.

        This method will call the method defined in `url_navigator`,
        with `page_url` as the first parameter.

        Returns:
            Page: The instance where navigate() was called from.

        Example:

            >>> from splinter import Browser
            >>> from stere import Page
            >>>
            >>>
            >>> class GuiltyGear(Page):
            >>>     def __init__(self):
            >>>         self.url_suffix = 'Guilty_Gear'
            >>>
            >>>
            >>> Stere.browser = Browser()
            >>> Stere.url_navigator = 'visit'
            >>> Stere.base_url = 'https://en.wikipedia.org/'
            >>>
            >>> guilty_gear_page = GuiltyGear()
            >>> guilty_gear_page.navigate()

        """
        getattr(self.browser, self.url_navigator)(self.page_url)
        return self
