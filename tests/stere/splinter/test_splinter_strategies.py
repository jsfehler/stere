import pytest

from stere.fields import Field
from stere.strategy.splinter import (
    FindByCss,
    FindById,
    FindByName,
    FindByTag,
    FindByText,
    FindByValue,
    FindByXPath,
)
from stere.strategy.strategy import strategies


def test_unregistered_strategy():
    """When an unregistered strategy is used
    Then a ValueError should be thrown
    """
    strategies = [
        'css', 'xpath', 'tag', 'name', 'text', 'id', 'value',
    ]

    with pytest.raises(ValueError) as e:
        Field('fail', 'foobar')

    expected_message = f'The strategy "fail" is not in {strategies}.'
    assert expected_message == str(e.value)


def test_unexpected_strategy():
    """Given Stere's default splinter strategies
    When an unexpected strategy is found
    Then this test should fail
    """
    assert strategies == {
        'css': FindByCss,
        'xpath': FindByXPath,
        'tag': FindByTag,
        'name': FindByName,
        'text': FindByText,
        'id': FindById,
        'value': FindByValue,
    }


def test_strategy_attribute_correct():
    """The strategy attribute on each Strategy class should be correct."""
    assert 'css' == FindByCss.strategy
    assert 'id' == FindById.strategy
    assert 'name' == FindByName.strategy
    assert 'tag' == FindByTag.strategy
    assert 'text' == FindByText.strategy
    assert 'value' == FindByValue.strategy
    assert 'xpath' == FindByXPath.strategy
