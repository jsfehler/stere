from .browserenabled import BrowserEnabled


class Page(BrowserEnabled):
    def visit(self):
        """Opens the page in the browser, based on the url attribute.
        """
        self.browser.visit(self.url)

    def scroll_to(self, x, y):
        """Scroll to a specific location on the page."""
        self.browser.driver.execute_script(f'window.scrollTo({x}, {y})')
