import os

import pytest

from stere import Stere

from pages import dummy


@pytest.fixture(scope='session')
def splinter_driver_kwargs(splinter_webdriver, request):
    """Webdriver kwargs."""
    if os.environ['CURRENT_BROWSER_NAME'] == 'firefox':
        version = 'dev'
    else:
        version = '64'
    if os.environ['REMOTE_RUN'] == "True":
        # Sauce Labs settings
        return {
             'browserName': os.environ['CURRENT_BROWSER_NAME'],
             'browser': os.environ['CURRENT_BROWSER_NAME'],
             'platform': 'Windows 10',
             'version': version,
             'tunnel-identifier': os.getenv('X_JOB_NUMBER')
            }
    else:
        return {}


@pytest.fixture(scope='function', autouse=True)
def setup_stere(browser):
    Stere.browser = browser


@pytest.fixture(scope='function')
def test_page():
    return dummy.DummyPage()
