import logging

from selenium.webdriver.remote.remote_connection import LOGGER

LOGGER.setLevel(logging.WARNING)


def test_is_present_args(test_page):
    """
    When I send an argument to is_present
    Then it is used by the correct function
    """
    test_page.navigate()
    assert test_page.added_container.is_present(wait_time=6)


def test_is_not_present_args(test_page):
    """
    When I send an argument to is_not_present
    Then it is used by the correct function
    """
    test_page.navigate()
    assert test_page.removed_container.is_not_present(wait_time=6)
