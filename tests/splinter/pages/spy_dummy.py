from stere import Page
from stere.fields import Text


class XHRDummyPage(Page):
    """Represents the XHR test page."""

    def __init__(self):
        self.url_suffix = 'test_page/xhr_test_page.html'

        self.filled_text = Text('id', 'filledText')


class FetchDummyPage(Page):
    """Represents the Fetch test page."""

    def __init__(self):
        self.url_suffix = 'test_page/fetch_test_page.html'

        self.filled_text = Text('id', 'filledText')
