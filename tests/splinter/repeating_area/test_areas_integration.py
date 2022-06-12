import logging

import pytest

from selenium.webdriver.remote.remote_connection import LOGGER

from stere.areas import Areas


LOGGER.setLevel(logging.WARNING)


def test_areas_containing_type(test_page):
    """Ensure Areas.containing() returns an Areas object."""
    test_page.navigate()

    found_areas = test_page.repeating_area.areas.containing(
        'link', 'Repeating Link 2',
    )

    assert isinstance(found_areas, Areas)


def test_areas_containing(test_page):
    """Ensure Areas.containing() returns valid results."""
    test_page.navigate()

    found_areas = test_page.repeating_area.areas.containing(
        'link', 'Repeating Link 2',
    )

    assert found_areas[0].text.value == 'Repeating Area 2'


def test_areas_containing_nested_attr(test_page):
    """Ensure Areas.containing() handles dot attrs."""
    test_page.navigate()

    found_areas = test_page.repeating_area.areas.containing(
        'nested.ax', 'AX1',
    )

    assert found_areas[0].nested.ax.value == 'AX1'


def test_areas_containing_invalid_field_name(test_page):
    test_page.navigate()

    with pytest.raises(AttributeError) as e:
        test_page.repeating_area.areas.containing(
            'lunk', 'Repeating Link 2')

    assert str(e.value) == "'Area' object has no attribute 'lunk'"


def test_areas_containing_nested_attr_invalid_field_name(test_page):
    test_page.navigate()

    with pytest.raises(AttributeError) as e:
        test_page.repeating_area.areas.containing(
            'nested.cx', 'CX1')

    assert str(e.value) == "'Area' object has no attribute 'cx'"


def test_areas_contain(test_page):
    """Ensure Areas.contain() returns True when a result is found."""
    test_page.navigate()

    assert test_page.repeating_area.areas.contain("link", "Repeating Link 1")


def test_areas_contain_not_found(test_page):
    """Ensure Areas.contain() returns False when a result is not found."""
    test_page.navigate()

    assert not test_page.repeating_area.areas.contain(
        "link", "Repeating Link 666",
    )
