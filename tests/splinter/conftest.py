import os

from pages import dummy

import pytest

from stere import Stere
from stere.strategy import add_data_star_strategy


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
        try:
            name = request.node.name
            browser.execute_script("sauce:job-name={}".format(name))

            res = str(not request.node.rep_call.failed).lower()
            browser.execute_script("sauce:job-result={}".format(res))
        except AttributeError:
            pass

    if os.getenv('USE_SAUCE_LABS') == "True":
        request.addfinalizer(fin)


@pytest.fixture(scope='session')
def splinter_remote_url(request):
    return request.config.option.sauce_remote_url


@pytest.fixture(scope='session')
def browser_name(request, splinter_webdriver) -> str:
    """Get the name of the web browser used."""
    name = splinter_webdriver
    if name == 'remote':
        name = request.config.option.splinter_remote_name

    return name


@pytest.fixture(scope='session')
def current_options(chrome_options, firefox_options, browser_name):
    if browser_name == "chrome":
        return chrome_options

    return firefox_options


@pytest.fixture(scope='session')
def splinter_driver_kwargs(
    splinter_webdriver, request, browser_name, current_options,
):
    """Webdriver kwargs."""
    browser_versions = {
        'chrome': 'latest-1',
        'firefox': 'latest-1',
    }

    version = browser_versions.get(browser_name)
    if version is None:
        raise ValueError('Unknown browser_name provided')

    # Set the Sauce Labs job name
    github_run_id = os.getenv('GITHUB_RUN_ID')
    testrun_name = f"{github_run_id}: {browser_name}"

    if os.environ.get('USE_SAUCE_LABS') == 'True':
        # Sauce Labs settings
        current_options.browser_version = version
        current_options.platform_name = 'Windows 10'

        sauce_options = {
            'username': os.environ['SAUCE_USERNAME'],
            'accessKey': os.environ['SAUCE_ACCESS_KEY'],
            'name': testrun_name,
            'tunnelIdentifier': 'github-action-tunnel',
            'seleniumVersion': '4.1.0',
        }
        current_options.set_capability('sauce:options', sauce_options)

        # Weird sauce labs issue
        if browser_name == 'chrome':
            sauce_options['browserName'] = 'chrome'

    return {}


@pytest.fixture(scope='function', autouse=True)
def setup_stere(browser):
    Stere.browser = browser
    Stere.url_navigator = "visit"
    Stere.base_url = 'https://jsfehler.github.io/stere/'


@pytest.fixture(scope='function')
def test_page():
    return dummy.DummyPage()
