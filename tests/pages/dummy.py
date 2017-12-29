from stere.fields import Area, Button, Input, Link, Root, Dropdown


class DummyPage():
    """A page object for the test page."""

    def __init__(self):
        self.url = 'https://jsfehler.github.io/stere/test_page/test_page.html'

        self.button_container = Root('id', 'test_button_div')
        self.button = Button('id', 'test_button')
        self.area = Area(
            input=Input('id', 'test_input'),
            submit_button=Button('id', 'test_input_submit')
        )
        self.link = Link('id', 'test_link')
        self.dropdown_area = Area(
            dropdown=Dropdown('id', 'test_dropdown'),
            submit=Button('id', 'test_dropdown_submit')
        )
        self.css_dropdown = Dropdown(
            'id',
            'test_css_dropdown',
            option=Link('css', 'a')
        )
