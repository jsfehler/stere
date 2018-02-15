import os

import pytest

from stere import Stere


@pytest.fixture(scope='session')
def splinter_driver_kwargs(splinter_webdriver, request):
    """Webdriver kwargs."""
    if os.environ['CURRENT_BROWSER_NAME'] == 'firefox':
        version = 'dev'
    else:
        version = '64'

    return {
         'browserName': os.environ['CURRENT_BROWSER_NAME'],
         'browser': os.environ['CURRENT_BROWSER_NAME'],
         'platform': 'Windows 10',
         'version': version,
         'tunnel-identifier': os.getenv('X_JOB_NUMBER')
        }


@pytest.fixture(scope='function', autouse=True)
def setup_stere(browser):
    Stere.browser = browser
