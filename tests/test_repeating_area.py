import logging

import pytest
from selenium.webdriver.remote.remote_connection import LOGGER

from pages import dummy_invalid

LOGGER.setLevel(logging.WARNING)


def test_missing_root():
    expected_message = 'RepeatingArea requires a Root Field.'

    with pytest.raises(ValueError) as e:
        dummy_invalid.InvalidDummyPageA()

    assert str(e.value) == expected_message


def test_used_reserved_keyword():
    expected_message = '"items" is a reserved parameter.'

    with pytest.raises(ValueError) as e:
        dummy_invalid.InvalidDummyPageB()

    assert str(e.value) == expected_message


def test_non_field_kwarg():
    expected_message = 'RepeatingArea arguments can only be Field objects.'

    with pytest.raises(ValueError) as e:
        dummy_invalid.InvalidDummyPageC()

    assert str(e.value) == expected_message
