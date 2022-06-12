from stere.areas import Repeating, RepeatingArea
from stere.fields import Field, Root


def test_repeater_name():
    """The repeater_name attribute should be the class name of the repeater."""
    repeating = Repeating(
        root=Root('css', '.repeatingRepeating'),
        repeater=RepeatingArea(
            root=Root('css', '.test_repeating_area_root'),
            link=Field('xpath', './/a'),
        ),
    )

    assert type(repeating.repeater).__name__ == repeating.repeater_name
