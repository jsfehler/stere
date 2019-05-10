from stere.browserenabled import BrowserEnabled


def test_browserenabled_default_browser():
    """Given stere has not been configured at all
    Then the browser attribute should be None.
    """
    browser_enabled = BrowserEnabled()

    assert browser_enabled.browser is None


def test_browserenabled_default_url_navigator():
    """Given stere has not been configured at all
    Then the url navigator attribute should be the default for splinter.
    """
    browser_enabled = BrowserEnabled()

    assert browser_enabled.url_navigator == 'visit'
