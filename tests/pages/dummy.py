from stere import Page

from stere.areas import Area, RepeatingArea
from stere.fields import (
    Field,
    Button,
    Input,
    Link,
    Root,
    Text,
    Dropdown
)


class CSSDropdown(Dropdown):
    """A Dropdown that's customized to hover over the element before attempting
    a select.
    """
    def before_select(self):
        self.element.mouse_over()


class DummyPage(Page):
    """Represents the test page."""

    def __init__(self):
        self.url = 'https://jsfehler.github.io/stere/test_page/test_page.html'

        self.button_container = Root('id', 'test_button_div')
        self.button = Button('id', 'test_button')
        self.input_area = Area(
            input=Input('id', 'test_input'),
            submit_button=Button('id', 'test_input_submit')
        )
        self.link = Link('id', 'test_link')
        self.dropdown_area = Area(
            dropdown=Dropdown('id', 'test_dropdown'),
            submit=Button('id', 'test_dropdown_submit')
        )
        self.css_dropdown = CSSDropdown(
            'id',
            'test_css_dropdown',
            option=Link('css', 'a')
        )

        self.repeating_area = RepeatingArea(
            root=Root('css', '.test_repeating_area_root'),
            link=Link('xpath', './/a'),
            text=Text('css', '.test_repeating_area_test')
        )

        self.added_container = Field('id', 'added_container')
        self.removed_container = Field('id', 'removed_container')

        self.area_with_root = Area(
            root=Root('id', 'area_root'),
            link=Link('xpath', './a')
        )

        self.many_input_area = Area(
            first_name=Input('id', 'test_input_first_name'),
            last_name=Input('id', 'test_input_last_name'),
            email=Input('id', 'test_input_email'),
            age=Input('id', 'test_input_age'),
            submit=Button('id', 'test_many_input_submit')
        )
        self.many_input_result = Text('id', 'many_input_result')
