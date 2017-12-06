from stere import Page
from stere.fields import Button, Input, Link, Area, RepeatingArea, Root


class Home(Page):
    def __init__(self):
        self.url = 'http://google.ca'
        self.search = Area(
             input=Input('xpath', '//*[@id="lst-ib"]'),
             submit=Button('name', 'btnK')
        )


class Results(Page):
    def __init__(self):
        self.listing = RepeatingArea(
            root=Root('xpath', '//*[@id="rso"]//*[@class="g"]'),
            link=Link('xpath', './/*[@class="rc"]//*[@class="r"]//a'),
        )
