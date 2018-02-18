import pytest

from stere.fields import Field

from pages import dummy

import logging
from selenium.webdriver.remote.remote_connection import LOGGER
LOGGER.setLevel(logging.WARNING)


def test_field_empty_perform():
    """
    The default implementation of Field.perform() should return False.
    """
    field = Field('id', 'foobar')

    assert field.perform() is False


def test_field_getattr():
    """
    When I try to access an element attribute from a Field directly
    Then the attribute is fetched
    """

    test_page = dummy.DummyPage()
    test_page.visit()

    # The is_present method belongs to the element, not the Field directly.
    assert test_page.button.is_present()


def test_field_getattr_should_not_exist():
    """
    When I try to access an attribute that does not exist from a Field directly
    Then the attribute is not fetched
    """

    test_page = dummy.DummyPage()
    test_page.visit()

    with pytest.raises(AttributeError):
        assert test_page.button.foobar()
