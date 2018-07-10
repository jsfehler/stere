import os

import pytest

from stere import Stere
from stere.strategy import add_data_star_strategy

from pages import dummy


add_data_star_strategy('data-test-id')


@pytest.fixture(scope='session')
def splinter_driver_kwargs(splinter_webdriver, request):
    """Webdriver kwargs."""
    browser_name = os.environ['CURRENT_BROWSER_NAME']

    if browser_name == 'firefox':
        version = 'dev'
    else:
        version = '64'

    if os.environ['REMOTE_RUN'] == "True":
        # Sauce Labs settings
        return {
             'browserName': browser_name,
             'browser': browser_name,
             'platform': 'Windows 10',
             'version': version,
             'tunnel-identifier': os.getenv('X_JOB_NUMBER')
            }
    else:
        return {}


@pytest.fixture(scope='function', autouse=True)
def setup_stere(browser):
    Stere.browser = browser
    Stere.url_navigator = "visit"


@pytest.fixture(scope='function')
def test_page():
    return dummy.DummyPage()
