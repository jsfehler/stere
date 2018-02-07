import logging
import time

import pytest
from selenium.webdriver.remote.remote_connection import LOGGER

from pages import dummy

LOGGER.setLevel(logging.WARNING)


def test_button(browser):
    """
    When a button is clicked
    Then the button's action occurs
    """

    test_page = dummy.DummyPage()
    test_page.visit()
    test_page.button.click()

    # Clicking changes the button's container background colour
    browsers = {
     "Firefox": 'rgb(255, 0, 0)',
     "Chrome": 'rgba(255, 0, 0, 1)'
    }

    # This works because value_of_css_property is gotten from splinter,
    # which gets it from Selenium
    actual = test_page.button_container.first._element.value_of_css_property(
        'background-color')
    assert browsers[browser.driver_name] == actual


def test_input():
    """
    When an input is filled with the text 'Winamp'
    Then the text in the input should be 'Winamp'
    """

    test_page = dummy.DummyPage()
    test_page.visit()
    test_page.area.input.fill('Winamp')

    assert 'Winamp' == test_page.area.input.element.value


def test_link(browser):
    """
    When a link is clicked
    Then the link's action occurs
    """

    test_page = dummy.DummyPage()
    test_page.visit()
    test_page.link.click()

    time.sleep(2)

    # The result of clicking should land the user on google.ca
    assert 'https://www.google.ca' in browser.url


def test_html_dropdown(browser):

    test_page = dummy.DummyPage()
    test_page.visit()
    test_page.dropdown_area.dropdown.select('Banana')
    test_page.dropdown_area.submit.click()

    time.sleep(2)

    # The result of clicking should land the user on google.ca
    assert 'search?q=banana' in str.lower(browser.url)


def test_css_dropdown(browser):

    test_page = dummy.DummyPage()
    test_page.visit()
    test_page.css_dropdown.select('Dog')

    time.sleep(2)

    # The result of clicking should land the user on google.ca
    assert 'test_page.html#dog' in browser.url


def test_area_items(browser):
    """
    When an area is created
    Then the items in the area can be accessed with dot notation
    """

    test_page = dummy.DummyPage()
    test_page.visit()
    test_page.area.input.fill('Winamp')
    test_page.area.submit_button.click()

    time.sleep(2)

    # The result of the perform should land the user on google.ca
    assert 'https://www.google.ca' in browser.url


def test_area_perform(browser):
    """
    When an area is performed
    Then each of the Fields inside it is used
    """

    test_page = dummy.DummyPage()
    test_page.visit()
    test_page.area.perform('Winamp')

    time.sleep(2)

    # The result of the perform should land the user on google.ca
    assert 'https://www.google.ca' in browser.url


def test_repeating_area(browser):

    test_page = dummy.DummyPage()
    test_page.visit()

    listings = test_page.repeating_area.areas
    assert listings[0].link.text == "Repeating Link 1"
    assert listings[1].link.text == "Repeating Link 2"


def test_is_present_args():
    """
    When I send an argument to is_present
    Then it is used by the correct function
    """
    test_page = dummy.DummyPage()
    test_page.visit()
    assert test_page.added_container.is_present(wait_time=6)


def test_is_not_present_args():
    """
    When I send an argument to is_not_present
    Then it is used by the correct function
    """
    test_page = dummy.DummyPage()
    test_page.visit()
    assert test_page.removed_container.is_not_present(wait_time=6)
