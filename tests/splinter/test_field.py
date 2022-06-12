import logging

import pytest

from selenium.webdriver.remote.remote_connection import LOGGER


LOGGER.setLevel(logging.WARNING)


def test_value_equals(test_page):
    test_page.navigate()

    assert not test_page.many_input_area.first_name.value_equals('aabbaa')

    test_page.many_input_area.perform(
        "aabbaa",
        "bbccbb",
        "ccddcc",
        "ddeedd",
    )

    assert test_page.many_input_area.first_name.value_equals('aabbaa')


def test_value_contains(test_page):
    test_page.navigate()

    assert not test_page.many_input_area.first_name.value_contains('bbaa')

    test_page.many_input_area.perform(
        "aabbaa",
        "bbccbb",
        "ccddcc",
        "ddeedd",
    )
    assert test_page.many_input_area.first_name.value_contains('bbaa')


def test_field_getattr(test_page):
    """
    When I try to access an element attribute from a Field directly
    Then the attribute is fetched
    """
    test_page.navigate()

    # The is_present method belongs to the element, not the Field directly.
    assert test_page.button.is_present()


def test_field_getattr_should_not_exist(test_page):
    """
    When I try to access an attribute that does not exist from a Field directly
    Then the attribute is not fetched
    """
    test_page.navigate()

    with pytest.raises(AttributeError):
        assert test_page.button.foobar()


def test_field_getattr_find_fails(test_page):
    """
    When I try to access an attribute that does not exist from a Field
    And the element is not found
    Then an error is raised
    And the correct error message is displayed
    """
    test_page.navigate()

    with pytest.raises(AttributeError) as e:
        test_page.missing_button.does_not_exist

    msg = (
        'Failed to get element attribute.'
        'Could not find element with data-test-id: not_on_the_page'
    )

    assert msg == str(e.value)


def test_non_unique_field_find(test_page):
    """
    When I try to use find() on a Field that is found multiple times
     on the page
    Then a ValueError is thrown
    """
    test_page.navigate()
    with pytest.raises(ValueError) as e:
        test_page.purposefully_non_unique_field.find()

    assert "Expected one element, found multiple" == str(e.value)
