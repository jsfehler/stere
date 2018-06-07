import pytest


import logging
from selenium.webdriver.remote.remote_connection import LOGGER
LOGGER.setLevel(logging.WARNING)


def test_page_getattr(test_page):
    """
    When I try to access a browser attribute from a Page directly
    Then the attribute is fetched
    """
    test_page.navigate()

    expected = 'https://jsfehler.github.io/stere/test_page/test_page.html'
    # The url attribute belongs to the browser, not Page directly.
    assert expected == test_page.url


def test_page_getattr_should_not_exist(test_page):
    """
    When I try to access an attribute that does not exist from a Page directly
    Then the attribute is not fetched
    """
    test_page.navigate()

    with pytest.raises(AttributeError):
        assert test_page.foobar()
