import logging

import pytest

from selenium.webdriver.remote.remote_connection import LOGGER

LOGGER.setLevel(logging.WARNING)


def test_checkbox_set_to_true(test_page):
    test_page.navigate()
    test_page.checkbox.set_to(True)

    assert test_page.checkbox.checked


def test_checkbox_set_to_false(test_page):
    test_page.navigate()
    test_page.checkbox.check()

    assert test_page.checkbox.checked

    test_page.checkbox.set_to(False)

    assert test_page.checkbox.checked is False


def test_checkbox_toggle_on(test_page):
    test_page.navigate()
    test_page.checkbox.toggle()

    assert test_page.checkbox.checked


def test_checkbox_toggle_off(test_page):
    test_page.navigate()
    test_page.checkbox.toggle()
    test_page.checkbox.toggle()

    assert test_page.checkbox.checked is False


def test_checkbox_default_checked(test_page):
    test_page.navigate()
    test_page.checkbox.perform()

    assert test_page.checkbox.checked


def test_checkbox_opposite_default_unchecked(test_page):
    test_page.navigate()
    test_page.checkbox_checked.opposite()

    assert test_page.checkbox.checked is False


def test_field_name(py_version, test_page):
    """Fields should report their intended class name, not 'Performer'."""
    if py_version in [6, 7]:
        error_msg = 'object does not support indexing'
    else:
        error_msg = 'object is not subscriptable'

    with pytest.raises(TypeError) as e:
        test_page.button[0]

    assert f"'Button' {error_msg}" == str(e.value)

    with pytest.raises(TypeError) as e:
        test_page.input_area.input[0]

    assert f"'Input' {error_msg}" == str(e.value)

    with pytest.raises(TypeError) as e:
        test_page.link[0]

    assert f"'Link' {error_msg}" == str(e.value)
