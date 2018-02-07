import logging

from selenium.webdriver.remote.remote_connection import LOGGER

from pages import dummy

LOGGER.setLevel(logging.WARNING)


def test_is_present_args():
    """
    When I send an argument to is_present
    Then it is used by the correct function
    """
    test_page = dummy.DummyPage()
    test_page.visit()
    assert test_page.added_container.is_present(wait_time=6)


def test_is_not_present_args():
    """
    When I send an argument to is_not_present
    Then it is used by the correct function
    """
    test_page = dummy.DummyPage()
    test_page.visit()
    assert test_page.removed_container.is_not_present(wait_time=6)
