from stere import Page
from stere.areas import Area, RepeatingArea
from stere.fields import (
    Link,
    Root,
    Text,
)


class InvalidDummyPageB(Page):
    """Represents a page that shouldn't work."""

    def __init__(self):
        self.reserved_kwarg = RepeatingArea(
            root=Root('css', '.test_repeating_area_root'),
            link=Link('xpath', './/a'),
            items=Text('css', '.test_repeating_area_test'),
        )


class InvalidDummyPageC(Page):
    """Represents a page that shouldn't work."""

    def __init__(self):
        self.non_field_kwargs = RepeatingArea(
            root=Root('css', '.test_repeating_area_root'),
            link="Foobar",
        )


class InvalidDummyPageE(Page):
    """Represents a page that shouldn't work."""

    def __init__(self):
        self.non_field_kwargs = Area(
            root=Root('css', '.test_repeating_area_root'),
            link="Foobar",
        )
