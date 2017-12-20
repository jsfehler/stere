import time


from stere import Stere, Goto
from stere.fields import Area, Button, Input
from pages import google


class DummyPage():
    """A page object for the test page."""
    
    def __init__(self):
        self.button = Button('id', 'test_button')
        self.area = Area(
            input = Input('id', 'test_input'),
            submit_button = Button('id', 'test_input_submit')
        )


def test_button(browser):
    """
    When a button is clicked
    Then the button's action occurs
    """
    Stere.browser = browser

    browser.visit('https://jsfehler.github.io/stere/test_page/test_page.html')
    
    test_page = DummyPage()
    test_page.button.click()
    
    # Clicking the button turns the button's container background colour
    assert 'red' == test_page.button.element.style.background_color


def test_input(browser):
    """
    When an input is filled with the text 'Winamp'
    Then the text in the input should be 'Winamp'
    """
    Stere.browser = browser

    browser.visit('https://jsfehler.github.io/stere/test_page/test_page.html')
    
    test_page = DummyPage()
    test_page.area.input.fill('Winamp')
    
    assert 'Winamp' == test_page.area.input.element.value


def test_area_perform(browser):
    Stere.browser = browser

    browser.visit('https://jsfehler.github.io/stere/test_page/test_page.html')
    
    test_page = DummyPage()
    test_page.area.perform('Winamp')

    time.sleep(2)
    
    assert 'https://google.ca' == browser.url


def test_stere(browser):

    Stere.browser = browser

    google_home = google.Home()

    Goto(google_home)
    google_home.search.perform("Winamp")

    import time
    time.sleep(5)
    
    listings = google.Results().listing.areas
    assert listings[1].items["link"].text == "Winamp - Download"
    assert listings[2].items["link"].text == "Download Winamp - free - latest version"
    assert listings[5].items["link"].text == "Winamp's woes: How the greatest MP3 player undid itself | Ars Technica"
