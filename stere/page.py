from .browserenabled import BrowserEnabled


class Page(BrowserEnabled):
    """Represents a single Web Page. Should be subclassed by Page Objects.

    All attribute calls are tried on the browser attribute.
    This allows classes inheriting from Page to act as a proxy to
    whichever browser/driver is being used.
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
        """Opens the page in the browser, based on the page_url attribute.
        """
        return getattr(self.browser, self.url_navigator)(self.page_url)
