from .browserenabled import BrowserEnabled


class Page(BrowserEnabled):
    """Represents a single Web Page. The Page class is the base which all
    Page Objects should inherit from.

    Inheriting from Page is not required for Fields or Areas to work.

    All attribute calls are tried on the browser attribute.
    This allows classes inheriting from Page to act as a proxy to
    whichever browser/driver is being used.

    Using Splinter's browser.url method as an example, the following methods
    are analogous:

    >>> MyPage.url == MyPage.browser.url == browser.url

    The choice of which syntax to use depends on how you want to write your
    tests.
    """
    def __getattr__(self, val):
        """If an attribute doesn't exist, try getting it from the browser.
        """

        return getattr(self.browser, val)

    def __enter__(self):
        """Page Objects can be used as context managers."""
        return self

    def __exit__(self, *args):
        pass

    def navigate(self):
        """When the base Stere object has been given the `url_navigator`
        attribute, and a Page Object has a `page_url` attribute, the
        `navigate()` method can be called.

        This method will call the method defined in `url_navigator`,
        with `page_url`as the first parameter.

        In the following example, Stere is initialized with Splinter.

        >>> from splinter import Browser
        >>> from stere import Page
        >>>
        >>>
        >>> class Home(Page):
        >>>     def __init__(self):
        >>>         self.page_url = 'https://en.wikipedia.org/'
        >>>
        >>>
        >>> Stere.browser = Browser()
        >>> Stere.url_navigator = 'visit'
        >>>
        >>> home_page = Home()
        >>> home_page.navigate()
        """
        return getattr(self.browser, self.url_navigator)(self.page_url)
