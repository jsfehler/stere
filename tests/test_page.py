from stere import Stere
from pages import dummy


import logging
from selenium.webdriver.remote.remote_connection import LOGGER
LOGGER.setLevel(logging.WARNING)


def test_page_getattr(browser):
    """
    When I try to access a browser attribute from a Page directly
    Then the attribute is fetched
    """
    Stere.browser = browser

    test_page = dummy.DummyPage()
    test_page.visit()

    expected = 'https://jsfehler.github.io/stere/test_page/test_page.html'
    assert expected == test_page.url
