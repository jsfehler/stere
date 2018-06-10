import logging

import pytest
from selenium.webdriver.remote.remote_connection import LOGGER

from pages import dummy_invalid

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


def test_repeating_area(test_page):
    test_page.navigate()

    listings = test_page.repeating_area.areas
    assert listings[0].link.text == "Repeating Link 1"
    assert listings[1].link.text == "Repeating Link 2"


def test_repeating_area_includes(test_page):
        test_page.navigate()

        correct_element = test_page.repeating_area.links.includes(
            "Repeating Link 1"
        )

        assert correct_element.value == "Repeating Link 1"


def test_repeating_area_area_with(test_page):
        test_page.navigate()

        found_area = test_page.repeating_area.area_with(
            'link', 'Repeating Link 2'
        )

        assert found_area.text.value == 'Repeating Area 2'


def test_repeating_area_area_with_invalid_value(test_page):
        test_page.navigate()

        with pytest.raises(ValueError) as e:
            test_page.repeating_area.area_with('link', 'Repeating Link 3')

        assert str(e.value) == 'Could not find Repeating Link 3 in any link.'


def test_repeating_area_area_with_invalid_field_name(test_page):
        test_page.navigate()

        with pytest.raises(AttributeError) as e:
            test_page.repeating_area.area_with('lunk', 'Repeating Link 2')

        assert str(e.value) == "'Area' object has no attribute 'lunk'"
