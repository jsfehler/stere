import logging
import time

import pytest

from selenium.webdriver.remote.remote_connection import LOGGER

from stere.fields import Field
from stere.utils import _retry

LOGGER.setLevel(logging.WARNING)


def test_retry():
    """When I call _retry
    Then a function is called until it returns a True value
    """
    now = time.time()

    result = _retry(
        lambda: True if time.time() >= (now + 6) else False,
        retry_time=8,
    )

    assert result


def test_retry_fails():
    """When I call _retry
    And the timeout is hit
    Then it returns False
    """
    now = time.time()

    result = _retry(
        lambda: True if time.time() == (now + 6) else False,
        retry_time=4,
    )

    assert not result


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


def test_field_repr():
    """Fields should have a useful __repr__ method."""
    field = Field('id', 'foobar')

    assert "Field - Strategy: id, Locator: foobar" == str(field)


def test_field_empty_perform():
    """The default implementation of Field.perform() should return None."""
    f = Field('id', 'foobar')
    assert f.perform() is None


def test_call():
    """When a Field instance is called
    Then the Field's perform method is executed
    """
    f = Field('id', 'foobar')
    assert f() is None


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
