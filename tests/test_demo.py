from stere import Stere, Goto
from stere.fields import Input
from pages import google


def test_input(browser):
    Stere.browser = browser

    google_input = Input('xpath', '//*[@id="lst-ib"]')

    browser.visit('http://google.ca')
    google_input.fill('Winamp')


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
    assert listings[5].items["link"].text == "Winamp review and where to download | TechRadar"
