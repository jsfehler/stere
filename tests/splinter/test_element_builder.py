import pytest

from stere.fields.element_builder import build_element


def test_build_element_invalid_key():
    """
    When an invalid strategy is used
    Then a ValueError should be thrown
    """
    strategies = [
        'css', 'xpath', 'tag', 'name', 'text', 'id', 'value', 'data-test-id',
    ]
    expected_message = (
        f'The strategy "invalid_strategy" is not in {strategies}.'
    )

    with pytest.raises(ValueError) as e:
        build_element("invalid_strategy", "invalid_locator")

    assert str(e.value) == expected_message
