import logging
import time

from pages import dummy_invalid

import pytest

from selenium.webdriver.remote.remote_connection import LOGGER

LOGGER.setLevel(logging.WARNING)


def test_area_root_available(test_page):
    """Given an area has a root Field set,
    Then the root should be accessible.
    """
    test_page.navigate()
    assert test_page.area_with_root.root is not None


def test_area_non_field_kwarg():
    expected_message = (
        'Areas must only be initialized with: Field, Area, Repeating types'
    )

    with pytest.raises(ValueError) as e:
        dummy_invalid.InvalidDummyPageE()

    assert str(e.value) == expected_message


def test_area_with_root(test_page):
    test_page.navigate()
    test_page.area_with_root.link.click()


def test_area_with_root_alt_strategy(test_page):
    test_page.navigate()
    test_page.area_with_root_alt_strategy.link.click()


def test_area_items(browser, test_page):
    """
    When an area is created
    Then the items in the area can be accessed with dot notation
    """
    test_page.navigate()
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
    test_page.navigate()
    test_page.input_area.perform('Winamp')

    time.sleep(2)

    # The result of the perform should land the user on google.ca
    assert 'https://www.google.' in browser.url


def test_area_perform_multiple_args(test_page):
    test_page.navigate()
    test_page.many_input_area.perform(
        'Fooman',
        'Barson',
        'foobar@binbaz.net',
        '99',
    )

    time.sleep(2)

    expected = 'Fooman, Barson, foobar@binbaz.net, 99,'
    assert expected == test_page.many_input_result.text


def test_area_perform_kwargs(test_page):
    """When perform is called with kwargs, parameters should be respected."""
    test_page.navigate()
    test_page.many_input_area.perform(
        first_name='Fooman',
        last_name='Barson',
        email='foobar@binbaz.net',
        age='99',
    )

    time.sleep(2)

    expected = 'Fooman, Barson, foobar@binbaz.net, 99,'
    assert expected == test_page.many_input_result.text


def test_area_set_workflow(test_page):
    test_page.many_input_area.workflow('Foobar')
    assert 'Foobar' == test_page.many_input_area._workflow


def test_area_use_workflow(test_page):
    test_page.navigate()
    test_page.many_input_area.workflow('workflow_test').perform('Fooman')

    time.sleep(2)

    expected = 'Fooman, , , ,'
    assert expected == test_page.many_input_result.text


def test_area_with_repeating_area(test_page):
    """When RepeatingArea is inside an Area, Area root is inherited."""
    test_page.navigate()

    listings = test_page.area_repeating_area.it_repeats.areas
    assert listings[0].link.text == "Repeating Link 1"
    assert listings[1].link.text == "Repeating Link 2"


def test_area_with_area(test_page):
    """Area inside Area"""
    test_page.navigate()

    t = test_page.area_in_area.inner_area.link.text
    assert "I'm just a link in a div." == t


def test_area_with_area_no_root(test_page):
    """Area inside Area"""
    test_page.navigate()

    t = test_page.area_in_area_no_root.inner_area.link.text
    assert "I'm just a link in a div." == t


def test_text_to_dict_area(test_page):
    test_page.navigate()

    t = test_page.area_in_area.text_to_dict()

    assert t == {
        'inner_area': {'link': "I'm just a link in a div."},
    }


def test_text_to_dict_area_repeating_area(test_page):
    test_page.navigate()

    t = test_page.area_repeating_area.text_to_dict()

    assert t == {
        'it_repeats': [
            {'link': 'Repeating Link 1', 'text': 'Repeating Area 1'},
            {'link': 'Repeating Link 2', 'text': 'Repeating Area 2'},
        ],
    }
