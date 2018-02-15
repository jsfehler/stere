import logging

import pytest
from selenium.webdriver.remote.remote_connection import LOGGER

from pages import dummy_invalid

LOGGER.setLevel(logging.WARNING)


def test_used_reserved_keyword():
    expected_message = '"items" is a reserved parameter.'

    with pytest.raises(ValueError) as e:
        dummy_invalid.InvalidDummyPageD()

    assert str(e.value) == expected_message


def test_non_field_kwarg():
    expected_message = 'Area arguments can only be Field objects.'

    with pytest.raises(ValueError) as e:
        dummy_invalid.InvalidDummyPageE()

    assert str(e.value) == expected_message
