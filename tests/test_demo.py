import time

from stere import Stere, Goto
from pages import google, dummy


def test_button(browser):
    """
    When a button is clicked
    Then the button's action occurs
    """
    Stere.browser = browser

    test_page = dummy.DummyPage()
    browser.visit(test_page.url)

    test_page.button.click()

    # Clicking changes the button's container background colour
    assert 'rgb(255, 0, 0)' == test_page.button_container.element.first._element.value_of_css_property('background-color')  # NOQA: E501


def test_input(browser):
    """
    When an input is filled with the text 'Winamp'
    Then the text in the input should be 'Winamp'
    """
    Stere.browser = browser

    test_page = dummy.DummyPage()
    browser.visit(test_page.url)

    test_page.area.input.fill('Winamp')

    assert 'Winamp' == test_page.area.input.element.value


def test_link(browser):
    """
    When a link is clicked
    Then the link's action occurs
    """
    Stere.browser = browser

    test_page = dummy.DummyPage()
    browser.visit(test_page.url)

    test_page.link.click()

    time.sleep(2)

    # The result of clicking should land the user on google.ca
    assert 'https://www.google.ca' in browser.url


def test_area_perform(browser):
    """
    When an area is performed
    Then each of the Fields inside it is used
    """
    Stere.browser = browser

    test_page = dummy.DummyPage()
    browser.visit(test_page.url)

    test_page.area.perform('Winamp')

    time.sleep(2)

    # The result of the perform should land the user on google.ca
    assert 'https://www.google.ca' in browser.url


def test_repeating_area(browser):

    Stere.browser = browser

    google_home = google.Home()

    Goto(google_home)
    google_home.search.perform("Winamp")

    import time
    time.sleep(5)

    listings = google.Results().listing.areas
    assert listings[1].items["link"].text == "Winamp - Download"
    assert listings[2].items["link"].text == "Download Winamp - free - latest version"  # NOQA: E501
    # assert listings[5].items["link"].text == "Winamp's woes: How the greatest MP3 player undid itself | Ars Technica"  # NOQA: E501
