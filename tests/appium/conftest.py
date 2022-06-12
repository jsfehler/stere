import configparser
import os

from appium import webdriver

import pytest


def pytest_addoption(parser):
    parser.addoption(
        "--browser-name",
        action="store",
        default="",
        help="Name of the browser used",
    )


@pytest.fixture(scope='session')
def appium_capabilities(request):
    """Desired capabilities to use with Appium."""
    browser_name = request.config.option.browser_name

    # Set the Sauce Labs job name
    github_run_id = os.getenv('GITHUB_RUN_ID')
    testrun_name = f"{github_run_id}: {browser_name}"

    sauce_options = {
        'appiumVersion': '1.22.3',
        'name': testrun_name,
    }

    desired_caps = {
        'browserName': '',
        'deviceOrientation': 'portrait',
        'app': 'storage:filename=stere_ios_test_app.zip',
        "sauce:options": sauce_options,
    }

    if browser_name == 'ios':
        platform_caps = {
            'deviceName': 'iPhone X Simulator',
            'platformVersion': '15.4',
            'platformName': 'iOS',
        }
    elif browser_name == 'android':
        platform_caps = {
            'deviceName': 'Android Emulator',
            'platformVersion': '12.0',
            'platformName': 'Android',
        }
    else:
        raise ValueError(f'{browser_name} is not a valid browser name')
    return {**desired_caps, **platform_caps}


@pytest.fixture(scope='session', autouse=True)
def appium_temp_ini(request):
    """Write an appium config file."""
    def fin():
        os.remove('stere.ini')

    request.addfinalizer(fin)

    parser = configparser.ConfigParser()
    parser['stere'] = {'library': 'appium'}
    with open('stere.ini', 'w') as config_file:
        parser.write(config_file)

    return parser


@pytest.fixture(scope='function', autouse=True)
def setup_stere(request, appium_capabilities):
    from stere import Stere  # Place here to avoid conflcts with writing ini
    url = request.config.option.sauce_remote_url
    Stere.browser = webdriver.Remote(url, appium_capabilities)


@pytest.fixture(scope='function')
def test_app_main_page():
    from pages import app_main  # Place here to avoid conflcts with writing ini
    return app_main.AppMain()
