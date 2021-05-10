import configparser
import os

import pytest


@pytest.fixture
def invalid_ini():
    """Write an invalid config file."""
    parser = configparser.ConfigParser()
    parser['stere'] = {'library': 'invalid'}
    with open('stere.ini', 'w') as config_file:
        parser.write(config_file)

    return parser


def test_field_with_invalid_config(request, py_version, invalid_ini):
    """Ensure library specific Fields don't work with a different library."""
    def fin():
        os.remove('stere.ini')

    request.addfinalizer(fin)

    with pytest.raises(ImportError) as e:
        from stere.fields import Button  # NOQA: F401

    # ImportError message is different between py36 and py37
    if py_version.minor == 6:
        msg = "cannot import name 'Button'"

    else:
        msg = "cannot import name 'Button' from 'stere.fields'"
    assert msg in str(e.value)


def test_stategy_with_invalid_config(request, py_version, invalid_ini):
    """Library specific stategies shouldn't work with a different library."""
    def fin():
        os.remove('stere.ini')

    request.addfinalizer(fin)

    with pytest.raises(ImportError) as e:
        from stere.strategy import FindByCss  # NOQA: F401

    # ImportError message is different between py36 and py37
    if py_version.minor == 6:
        msg = "cannot import name 'FindByCss'"

    else:
        msg = "cannot import name 'FindByCss' from 'stere.strategy'"
    assert msg in str(e.value)
