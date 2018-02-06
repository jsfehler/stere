import pytest

from stere import Stere


@pytest.fixture(scope='function', autouse=True)
def setup_stere(browser):
    Stere.browser = browser
