import logging
import time

from pages import dummy_invalid

import pytest

from selenium.webdriver.remote.remote_connection import LOGGER

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
    """When perform is called with kwargs, the parameters should be respected.
    """
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
