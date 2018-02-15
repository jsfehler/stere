from stere import Page

from stere.fields import (
    Area,
    RepeatingArea,
    Link,
    Root,
    Text,
)


class InvalidDummyPageA(Page):
    """Represents a page that shouldn't work."""

    def __init__(self):
        self.missing_root = RepeatingArea(
            link=Link('xpath', './/a'),
            text=Text('css', '.test_repeating_area_test')
        )


class InvalidDummyPageB(Page):
    """Represents a page that shouldn't work."""

    def __init__(self):
        self.reserved_kwarg = RepeatingArea(
            root=Root('css', '.test_repeating_area_root'),
            link=Link('xpath', './/a'),
            items=Text('css', '.test_repeating_area_test')
        )


class InvalidDummyPageC(Page):
    """Represents a page that shouldn't work."""

    def __init__(self):
        self.non_field_kwargs = RepeatingArea(
            root=Root('css', '.test_repeating_area_root'),
            link="Foobar"
        )

    
class InvalidDummyPageD(Page):
    """Represents a page that shouldn't work."""

    def __init__(self):
        self.non_field_kwargs = Area(
            root=Root('css', '.test_repeating_area_root'),
            items=Text('css', '.test_repeating_area_test')
        )
        
        
class InvalidDummyPageE(Page):
    """Represents a page that shouldn't work."""

    def __init__(self):
        self.non_field_kwargs = Area(
            root=Root('css', '.test_repeating_area_root'),
            link="Foobar"
        )
