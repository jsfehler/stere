import logging
import os
import time

import pytest

from selenium.webdriver.remote.remote_connection import LOGGER

LOGGER.setLevel(logging.WARNING)


def test_button(browser, test_page):
    """
    When a button is clicked
    Then the button's action occurs
    """
    test_page.navigate()
    test_page.button.click()

    # Clicking changes the button's container background colour
    browsers = {
     'firefox': 'rgb(255, 0, 0)',
     'chrome': 'rgba(255, 0, 0, 1)',
    }

    # This works because value_of_css_property is gotten from splinter,
    # which gets it from Selenium
    actual = test_page.button_container.first._element.value_of_css_property(
        'background-color')
    assert browsers[os.environ["CURRENT_BROWSER_NAME"]] == actual


def test_input(test_page):
    """
    When an input is filled with the text 'Winamp'
    Then the text in the input should be 'Winamp'
    """
    test_page.navigate()
    test_page.input_area.input.fill('Winamp')

    assert 'Winamp' == test_page.input_area.input.element.value


def test_link(browser, test_page):
    """
    When a link is clicked
    Then the link's action occurs
    """
    test_page.navigate()
    test_page.link.click()

    time.sleep(2)

    # The result of clicking should land the user on google.ca
    assert 'https://www.google.ca' in browser.url


def test_html_dropdown(browser, test_page):
    test_page.navigate()
    test_page.dropdown_area.dropdown.select('Banana')
    test_page.dropdown_area.submit.click()

    time.sleep(2)

    # The result of clicking should land the user on google.ca
    assert 'search?q=banana' in str.lower(browser.url)


@pytest.mark.skipif(os.environ["REMOTE_RUN"])
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
