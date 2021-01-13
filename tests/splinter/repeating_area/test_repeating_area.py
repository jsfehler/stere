import logging

from pages import dummy_invalid

import pytest

from selenium.webdriver.remote.remote_connection import LOGGER


LOGGER.setLevel(logging.WARNING)


def test_non_field_kwarg():
    """When an object that does not inherit from Field is used to instantiate
    a RepeatingArea
    Then a ValueError is thrown
    And it should inform the user that only Field objects can be used
    """
    expected_message = 'RepeatingArea arguments can only be a Field or Area.'

    with pytest.raises(ValueError) as e:
        dummy_invalid.InvalidDummyPageC()

    assert str(e.value) == expected_message


def test_repeating_area_areas_no_areas_found(test_page):
    """Given I have a RepeatingArea that finds no Areas on the page,
    When I call RepeatingArea.areas(),
    Then I should be informed that no Area were found.
    """
    test_page.navigate()
    with pytest.raises(ValueError) as e:
        test_page.repeating_area_missing.areas

    assert str(e.value) == (
        "Could not find any Area using the root: "
        ".test_repeating_area_root_invalid"
    )


def test_len(test_page):
    """When I call len() on a RepeatingArea
    Then it should report back how many Areas were found.
    """
    test_page.navigate()
    assert 2 == len(test_page.repeating_area)


def test_repeating_area(test_page):
    test_page.navigate()

    listings = test_page.repeating_area.areas
    assert listings[0].link.text == "Repeating Link 1"
    assert listings[1].link.text == "Repeating Link 2"


def test_repeating_area_with_area(test_page):
    """When a RepeatingArea has an Area inside it
    Then the Area should have the correct root
    """
    test_page.navigate()

    listings = test_page.repeating_area.areas
    assert listings[0].nested.ax.text == "AX1"
    assert listings[0].nested.bx.text == "BX1"
    assert listings[1].nested.bx.text == "BX2"
    assert listings[1].nested.ax.text == "AX2"


def test_repeating_area_with_area_no_root(test_page):
    """When a RepeatingArea has an Area inside it
    And the Area has no root
    Then the found Area's Fields get a parent_locator set by the RepeatingArea
    """
    test_page.navigate()

    areas = test_page.repeating_area_area_no_root.areas
    assert areas[0].parent_locator is not None


@pytest.mark.skip
def test_repeating_area_includes(test_page):
    test_page.navigate()
    elem = test_page.repeating_area.links.includes("Repeating Link 1")
    assert elem.value == "Repeating Link 1"
