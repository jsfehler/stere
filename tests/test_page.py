import pytest

from pages import dummy


import logging
from selenium.webdriver.remote.remote_connection import LOGGER
LOGGER.setLevel(logging.WARNING)


def test_page_getattr():
    """
    When I try to access a browser attribute from a Page directly
    Then the attribute is fetched
    """

    test_page = dummy.DummyPage()
    test_page.visit()

    expected = 'https://jsfehler.github.io/stere/test_page/test_page.html'
    # The url attribute belongs to the browser, not Page directly.
    assert expected == test_page.url


def test_page_getattr_should_not_exist():
    """
    When I try to access an attribute that does not exist from a Page directly
    Then the attribute is not fetched
    """

    test_page = dummy.DummyPage()
    test_page.visit()

    with pytest.raises(AttributeError):
        assert test_page.foobar()
