import pytest

from stere.areas import Area, Areas


def test_areas_append_wrong_type():
    """Ensure a TypeError is raised when non-Area objects are appended
    to an Areas.
    """
    a = Areas()
    with pytest.raises(TypeError) as e:
        a.append('1')

    assert str(e.value) == (
        '1 is not an Area. Only Area objects can be inside Areas.'
    )


def test_areas_append():
    """Ensure Area objects can be appended to an Areas."""
    a = Areas()

    area = Area()
    a.append(area)

    assert 1 == len(a)


def test_areas_remove():
    """Ensure Areas.remove() behaves like list.remove()."""
    a = Areas()

    area = Area()
    a.append(area)
    a.remove(area)

    assert 0 == len(a)


def test_areas_len():
    """Ensure Areas reports length correctly."""
    a = Areas(['1', '2', '3'])
    assert 3 == len(a)
