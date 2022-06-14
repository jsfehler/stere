import pytest

from stere.areas import Area
from stere.fields import Root


def test_area_non_field_kwarg():
    expected_message = (
        'Areas must only be initialized with: Field, Area, Repeating types'
    )

    with pytest.raises(ValueError) as e:
        Area(
            root=Root('css', '.test_repeating_area_root'),
            link="Foobar",
        )

    assert str(e.value) == expected_message


def test_area_set_workflow():
    area = Area(
        root=Root('css', '.test_repeating_area_root'),
    )

    area.workflow('Foobar')
    assert 'Foobar' == area._workflow
