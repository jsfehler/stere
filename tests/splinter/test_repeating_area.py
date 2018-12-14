import logging

from pages import dummy_invalid

import pytest

from selenium.webdriver.remote.remote_connection import LOGGER


LOGGER.setLevel(logging.WARNING)


def test_areas_contain(test_page):
    test_page.navigate()

    assert test_page.repeating_area.areas.contain("link", "Repeating Link 1")


def test_areas_contain_not_found(test_page):
    test_page.navigate()

    assert not test_page.repeating_area.areas.contain(
        "link", "Repeating Link 666"
    )


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


def test_len(test_page):
    """Calling len() on a RepeatingArea should report back how many Areas were
    found.
    """
    test_page.navigate()
    assert 2 == len(test_page.repeating_area)


def test_repeating_area(test_page):
    test_page.navigate()

    listings = test_page.repeating_area.areas
    assert listings[0].link.text == "Repeating Link 1"
    assert listings[1].link.text == "Repeating Link 2"


def test_repeating_area_includes(test_page):
        test_page.navigate()
        elem = test_page.repeating_area.links.includes("Repeating Link 1")
        assert elem.value == "Repeating Link 1"


def test_repeating_area_area_with(test_page):
        test_page.navigate()

        found_area = test_page.repeating_area.area_with(
            'link', 'Repeating Link 2',
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


def test_repeating_area_areas_no_areas_found(test_page):
    """Given I have a RepeatingArea that finds no Areas on the page,
       When I call RepeatingArea.areas(),
       Then I should be informed that no Areas were found.
    """
    test_page.navigate()
    with pytest.raises(ValueError) as e:
        test_page.repeating_area_missing.areas

    assert str(e.value) == (
        "Could not find any Areas with the root: "
        ".test_repeating_area_root_invalid"
    )
