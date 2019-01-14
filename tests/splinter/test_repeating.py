import logging

import pytest

from selenium.webdriver.remote.remote_connection import LOGGER

from stere.areas import Repeating, RepeatingArea
from stere.fields import Root, Text

LOGGER.setLevel(logging.WARNING)


def test_all_roots(test_page):
    test_page.navigate()
    r = test_page.repeating
    all_roots = r._all_roots()
    assert 2 == len(all_roots)


def test_all_roots_not_found(test_page):
    test_page.navigate()

    r = Repeating(
        root=Root('id', 'notFound'),
        repeater=RepeatingArea(
            root=Root('id', 'alsoNotFound'),
            text=Text('id', 'neverFound'),
        ),
    )

    with pytest.raises(ValueError) as e:
        r._all_roots()
        assert str(e.value) == (
            'Could not find any RepeatingArea using the root: '
            '.repeatingRepeating',
        )
