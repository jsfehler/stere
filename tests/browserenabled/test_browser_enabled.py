import pytest

from stere.browserenabled import BrowserEnabled


@pytest.fixture
def browser_enabled():
    return BrowserEnabled()


def test_browserenabled_default_browser(browser_enabled):
    """Given stere has not been configured at all
    Then the browser attribute should be None.
    """
    assert browser_enabled.browser is None


def test_browserenabled_base_url(browser_enabled):
    """Given stere has not been configured at all
    Then the url_suffix attribute should be None.
    """
    assert browser_enabled.base_url == ''


def test_browserenabled_url_suffix(browser_enabled):
    """Given stere has not been configured at all
    Then the url_suffix attribute should be None.
    """
    assert browser_enabled.url_suffix == ''


def test_browserenabled_default_url_navigator(browser_enabled):
    """Given stere has not been configured at all
    Then the url_navigator attribute should be the default for splinter.
    """
    assert browser_enabled.url_navigator == 'visit'


def test_browserenabled_default_retry_time(browser_enabled):
    """Given stere has not been configured at all
    Then the retry_time attribute should have a default value of 5.
    """
    assert browser_enabled.retry_time == 5
