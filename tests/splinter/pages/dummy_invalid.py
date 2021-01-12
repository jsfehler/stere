from stere import Page
from stere.areas import Area, RepeatingArea
from stere.fields import Root


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
