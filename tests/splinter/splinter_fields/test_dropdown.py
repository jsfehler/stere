import logging
import os
import time

import pytest

from selenium.webdriver.remote.remote_connection import LOGGER

LOGGER.setLevel(logging.WARNING)


def test_html_dropdown_default_option_field(test_page):
    """Given the option argument was provided for a Dropdown
    Then the option attribute should match the argument
    """
    assert test_page.dropdown_with_override_option.option.locator == 'foobar'
    assert test_page.dropdown_with_override_option.option.strategy == 'id'


def test_html_dropdown_perform_return_value(test_page):
    """When Dropdown's perform() method is called
    And Dropdown consumes an argument
    Then Dropdown's performer method should return True
    """
    test_page.navigate()
    res = test_page.dropdown_area.dropdown.perform('Banana')

    assert res


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
