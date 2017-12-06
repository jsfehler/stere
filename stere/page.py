from .browserenabled import BrowserEnabled


class _Goto(BrowserEnabled):
    def __call__(self, page):
        self.browser.visit(page.url)


Goto = _Goto()


class Page(BrowserEnabled):
    def navigate(self):
        """Opens the page in the browser, based on the url attribute.
        """
        self.browser.visit(self.url)

    def scroll_to(self, x, y):
        """Scroll to a specific location on the page."""
        self.browser.driver.execute_script(f'window.scrollTo({x}, {y})')
