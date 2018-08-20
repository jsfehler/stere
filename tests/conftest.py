import os

import pytest

from stere import Stere
from stere.strategy import add_data_star_strategy

from pages import dummy


add_data_star_strategy('data-test-id')


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # execute all other hooks to obtain the report object
    outcome = yield
    rep = outcome.get_result()

    # set a report attribute for each phase of a call, which can
    # be "setup", "call", "teardown"

    setattr(item, "rep_" + rep.when, rep)


@pytest.fixture(autouse=True)
def after(request, browser):

    def fin():
        # Send result to Sauce labs
        res = str(not request.node.rep_call.failed).lower()
        browser.execute_script("sauce:job-result={}".format(res))

    if os.environ.get('REMOTE_RUN') == "True":
        request.addfinalizer(fin)


@pytest.fixture(scope='session')
def splinter_driver_kwargs(splinter_webdriver, request):
    """Webdriver kwargs."""
    browser_name = os.environ['CURRENT_BROWSER_NAME']

    if browser_name == 'firefox':
        version = '60'
    else:
        # TODO: Test latest Chrome
        version = '64'

    if os.environ.get('REMOTE_RUN') == "True":
        # Sauce Labs settings
        return {
             'browserName': browser_name,
             'browser': browser_name,
             'name': browser_name,
             'platform': 'Windows 10',
             'version': version,
             'tunnelIdentifier': os.getenv('TRAVIS_JOB_NUMBER')
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
