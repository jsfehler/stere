import logging
import os
import time

import pytest

from selenium.webdriver.remote.remote_connection import LOGGER

LOGGER.setLevel(logging.WARNING)


def test_html_dropdown(browser, test_page):
    test_page.navigate()
    test_page.dropdown_area.dropdown.select('Banana')
    test_page.dropdown_area.submit.click()

    time.sleep(2)

    # The result of clicking should land the user on google.ca
    assert 'search?q=banana' in str.lower(browser.url)


@pytest.mark.skipif(os.environ.get('REMOTE_RUN', "True"))
def test_css_dropdown(browser, test_page):
    # Can't be run on Remote Firefox. mouse_over isn't supported.
    # BUG: Supported in Remote Chrome, but:
    # https://github.com/cobrateam/splinter/pull/423

    test_page.navigate()
    test_page.css_dropdown.select('Dog')

    time.sleep(2)

    # The result of clicking should land the user on google.ca
    assert 'test_page.html#dog' in browser.url


def test_dropdown_invalid(test_page):
    test_page.navigate()

    with pytest.raises(ValueError) as e:
        test_page.dropdown_area.dropdown.select('Grape')

    contents = ["Apple", "Banana", "Cranberry"]
    expected_message = f'Grape was not found. Found values are: {contents}'
    assert expected_message == str(e.value)


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


def test_field_name(test_page):
    """Fields should report their intended class name, not 'Performer'
    """
    with pytest.raises(TypeError) as e:
        test_page.button[0]

    assert "'Button' object does not support indexing" == str(e.value)

    with pytest.raises(TypeError) as e:
        test_page.input_area.input[0]

    assert "'Input' object does not support indexing" == str(e.value)

    with pytest.raises(TypeError) as e:
        test_page.link[0]

    assert "'Link' object does not support indexing" == str(e.value)
