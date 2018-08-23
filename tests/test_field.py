import logging

import pytest

from selenium.webdriver.remote.remote_connection import LOGGER

from stere.fields import Field

LOGGER.setLevel(logging.WARNING)


def test_field_empty_perform():
    """
    The default implementation of Field.perform() should return False.
    """
    field = Field('id', 'foobar')

    assert field.perform() is False


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
