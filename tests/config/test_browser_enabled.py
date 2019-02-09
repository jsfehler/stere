from stere.browserenabled import BrowserEnabled


def test_browserenabled_browser():
    """Given stere has not been configured at all
    Then the browser attribute should be None."""
    browser_enabled = BrowserEnabled()

    assert browser_enabled.browser is None


def test_browserenabled_url_navigator():
    """Given stere has not been configured at all
    Then the url navigator attribute should be an empty string."""
    browser_enabled = BrowserEnabled()

    assert browser_enabled.urlnavigator == ''
