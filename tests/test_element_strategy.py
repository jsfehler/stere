import pytest

from stere.strategy.element_strategy import ElementStrategy


def test_element_strategy_find():
    elem = ElementStrategy('dummy', '//fake')

    with pytest.raises(NotImplementedError):
        elem._find_all()
