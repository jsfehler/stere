import logging
import time

import pytest
from selenium.webdriver.remote.remote_connection import LOGGER

from pages import dummy_invalid

LOGGER.setLevel(logging.WARNING)


def test_area_used_reserved_keyword():
    expected_message = '"items" is a reserved parameter.'

    with pytest.raises(ValueError) as e:
        dummy_invalid.InvalidDummyPageD()

    assert str(e.value) == expected_message


def test_area_non_field_kwarg():
    expected_message = 'Areas must only be initialized with field objects.'

    with pytest.raises(ValueError) as e:
        dummy_invalid.InvalidDummyPageE()

    assert str(e.value) == expected_message


def test_area_with_root(test_page):
    test_page.visit()

    test_page.area_with_root.link.click()


def test_area_items(browser, test_page):
    """
    When an area is created
    Then the items in the area can be accessed with dot notation
    """
    test_page.visit()
    test_page.input_area.input.fill('Winamp')
    test_page.input_area.submit_button.click()

    time.sleep(2)

    # The result of the perform should land the user on google.ca
    assert 'https://www.google.' in browser.url


def test_area_perform(browser, test_page):
    """
    When an area is performed
    Then each of the Fields inside it is used
    """
    test_page.visit()
    test_page.input_area.perform('Winamp')

    time.sleep(2)

    # The result of the perform should land the user on google.ca
    assert 'https://www.google.' in browser.url


def test_area_perform_multiple_args(test_page):
    test_page.visit()
    test_page.many_input_area.perform(
        'Fooman',
        'Barson',
        'foobar@binbaz.net',
        '99'
    )

    time.sleep(2)

    expected = 'Fooman, Barson, foobar@binbaz.net, 99,'
    assert expected == test_page.many_input_result.text
