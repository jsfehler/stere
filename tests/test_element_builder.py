import pytest

from stere.fields.element_builder import build_element


def test_build_element_invalid_key():
    """
    When an invalid strategy is used
    Then a ValueError should be thrown
    """
    expected_message = 'The strategy "invalid_strategy" is undefined.'

    with pytest.raises(ValueError) as e:
        build_element("invalid_strategy", "invalid_locator")

    assert str(e.value) == expected_message
