import logging

import pytest

from selenium.webdriver.remote.remote_connection import LOGGER

from stere.areas import Repeating, RepeatingArea
from stere.fields import Root, Text

LOGGER.setLevel(logging.WARNING)


def test_repeater_name(test_page):
    """The repeater_name attribute should be the class name of the repeater."""
    test_page.navigate()
    r = test_page.repeating

    assert type(r.repeater).__name__ == r.repeater_name


def test_all_roots(test_page):
    test_page.navigate()
    r = test_page.repeating
    all_roots = r._all_roots()
    assert 2 == len(all_roots)


def test_children(test_page):
    """Given I have a Repeating RepeatingArea
    Then I can search for content inside the Repeating's children.
    """
    test_page.navigate()
    r = test_page.repeating
    children = r.children()
    assert 2 == len(children)

    first_repeating_area = children[0]
    assert 2 == len(first_repeating_area)
    assert first_repeating_area.areas.contain('text', 'Repeating Area A1')

    second_repeating_area = children[1]
    assert 2 == len(second_repeating_area)
    assert second_repeating_area.areas.contain('text', 'Repeating Area B1')


def test_all_roots_not_found(test_page):
    test_page.navigate()

    r = Repeating(
        root=Root('id', 'notFound'),
        repeater=RepeatingArea(
            root=Root('id', 'alsoNotFound'),
            text=Text('id', 'neverFound'),
        ),
    )

    with pytest.raises(ValueError) as e:
        r._all_roots()
        assert str(e.value) == (
            'Could not find any RepeatingArea using the root: '
            '.repeatingRepeating',
        )


def test_has_children(test_page):
    test_page.navigate()

    r = test_page.repeating
    assert r.has_children()


def test_repeating_plus_area(test_page):
    """Repeating with an Area as the repeater.
    Should function identically to a RepeatingArea.
    """
    test_page.navigate()

    listings = test_page.repeating_with_area.children()
    assert listings[0].link.text == "Repeating Link 1"
    assert listings[1].link.text == "Repeating Link 2"


def test_repeating_plus_area_with_repeatingarea(test_page):
    """When Repeating has an Area as the repeater
    And the Area has no root
    And the Area has a RepeatingArea
    Then the RepetingArea should get the root from the Repeating
    """
    test_page.navigate()

    listings = test_page.repeating_area_repeatingarea.children()
    assert listings[0].it_repeats.areas[0].text.text == "Repeating Area A1"
