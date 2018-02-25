import logging

import pytest
from selenium.webdriver.remote.remote_connection import LOGGER

from pages import dummy, dummy_invalid

LOGGER.setLevel(logging.WARNING)


def test_missing_root():
    expected_message = 'RepeatingArea requires a Root Field.'

    with pytest.raises(ValueError) as e:
        dummy_invalid.InvalidDummyPageA()

    assert str(e.value) == expected_message


def test_used_reserved_keyword():
    expected_message = '"items" is a reserved parameter.'

    with pytest.raises(ValueError) as e:
        dummy_invalid.InvalidDummyPageB()

    assert str(e.value) == expected_message


def test_non_field_kwarg():
    expected_message = 'RepeatingArea arguments can only be Field objects.'

    with pytest.raises(ValueError) as e:
        dummy_invalid.InvalidDummyPageC()

    assert str(e.value) == expected_message


def test_repeating_area(browser):

    test_page = dummy.DummyPage()
    test_page.visit()

    listings = test_page.repeating_area.areas
    assert listings[0].link.text == "Repeating Link 1"
    assert listings[1].link.text == "Repeating Link 2"


def test_repeating_area_includes(browser):
        test_page = dummy.DummyPage()
        test_page.visit()

        correct_element = test_page.repeating_area.links.includes(
            "Repeating Link 1"
        )

        assert correct_element.value == "Repeating Link 1"
