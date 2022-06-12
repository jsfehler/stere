import pytest

from stere.value_comparator import ValueComparator


def test_value_comparator_str():
    a = ValueComparator(True, "A", "A")

    assert str(a) == "True. Expected: A, Actual: A"


def test_value_comparator_eq():
    a = ValueComparator(True, "A", "A")

    b = True

    assert b == a


def test_value_comparator_ne():
    a = ValueComparator(False, "A", "AAA")

    assert True != a  # NOQA E712


def test_value_comparator_error_msg():
    a = ValueComparator(False, 100, 101)

    with pytest.raises(AssertionError) as e:
        assert True == a  # NOQA E712

    result = str(e.value)
    expected = "assert True == False. Expected: 100, Actual: 101"
    assert expected == result
