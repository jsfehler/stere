import os

from pages import dummy

import pytest

from stere import Stere
from stere.strategy import add_data_star_strategy


add_data_star_strategy('data-test-id')


def pytest_addoption(parser):
    parser.addoption(
        "--browser-name",
        action="store",
        default="",
        help="Name of the browser used",
    )


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
        try:
            res = str(not request.node.rep_call.failed).lower()
            browser.execute_script("sauce:job-result={}".format(res))
        except AttributeError:
            pass

    if os.getenv('REMOTE_RUN') == "True":
        request.addfinalizer(fin)


@pytest.fixture(scope='session')
def splinter_remote_url(request):
    return request.config.option.sauce_remote_url


@pytest.fixture(scope='session')
def splinter_driver_kwargs(splinter_webdriver, request):
    """Webdriver kwargs."""
    browser_name = request.config.option.browser_name

    browser_versions = {
        'chrome': '64',
        'firefox': '60',
    }

    version = browser_versions.get(browser_name)
    if version is None:
        raise ValueError('Unknown browser_name provided')

    # Set the Sauce Labs job name
    travis_job_number = os.getenv('TRAVIS_JOB_NUMBER')
    testrun_name = travis_job_number or browser_name

    if os.environ.get('REMOTE_RUN') == "True":
        # Sauce Labs settings
        return {
            'desired_capabilities': {
                'browserName': browser_name,
                'browser': browser_name,
                'name': testrun_name,
                'platform': 'Windows 10',
                'version': version,
                'tunnelIdentifier': travis_job_number,
            },
        }
    else:
        return {}


@pytest.fixture(scope='function', autouse=True)
def setup_stere(browser):
    Stere.browser = browser
    Stere.url_navigator = "visit"
    Stere.base_url = 'https://jsfehler.github.io/stere/'


@pytest.fixture(scope='function')
def test_page():
    return dummy.DummyPage()
