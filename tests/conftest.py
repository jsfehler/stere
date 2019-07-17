import sys

import pytest


def pytest_addoption(parser):
    # Added to prevent errors when passing arguments from .travis.yml through
    # to tox.ini
    parser.addoption(
        "--sauce-remote-url",
        action="store",
        default="",
        help="Remote URL for Sauce Labs",
    )


@pytest.fixture(scope='session')
def py_version():
    return sys.version_info[1]
