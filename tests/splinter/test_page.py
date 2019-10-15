import logging

import pytest

from selenium.webdriver.remote.remote_connection import LOGGER

LOGGER.setLevel(logging.WARNING)


def test_page_navigate_return_value(test_page):
    """
    When I use Page.navigate()
    Then the returned value from the method is the Page instance
    """
    rv = test_page.navigate()

    assert rv == test_page


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


def test_page_context_manager(test_page):
    with test_page as t:
        assert t == test_page


def test_page_base_url(test_page):
    assert test_page.base_url == 'https://jsfehler.github.io/stere/'


def test_page_url_suffix(test_page):
    assert test_page.url_suffix == 'test_page/test_page.html'


def test_page_page_url(test_page):
    expected = 'https://jsfehler.github.io/stere/test_page/test_page.html'
    assert test_page.page_url == expected
