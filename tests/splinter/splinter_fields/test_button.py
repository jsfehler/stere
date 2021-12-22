import pytest

from stere.fields import Button


button_before_str = 'before'
button_after_str = 'after'


@pytest.fixture(scope='session')
def dummy_button():
    class Dummy(Button):
        def before(self):
            global button_before_str
            button_before_str = 'foo'

        def after(self):
            global button_after_str
            button_after_str = 'bar'

    return Dummy('id', 'test_button')


def test_button_call(browser, request, test_page):
    """When a Button is called
    Then the Button's perform method is called
    """
    test_page.navigate()
    test_page.button()

    # Clicking changes the button's container background colour
    browsers = {
        'firefox': 'rgb(255, 0, 0)',
        'chrome': 'rgba(255, 0, 0, 1)',
    }

    # This works because value_of_css_property is gotten from splinter,
    # which gets it from Selenium
    actual = test_page.button_container.find()._element.value_of_css_property(
        'background-color')

    browser_name = request.config.option.splinter_remote_name
    assert browsers[browser_name] == actual


def test_button(browser, request, test_page):
    """When a Button is clicked
    Then the correct action is sent to Splinter
    """
    test_page.navigate()
    test_page.button.click()

    # Clicking changes the button's container background colour
    browsers = {
        'firefox': 'rgb(255, 0, 0)',
        'chrome': 'rgba(255, 0, 0, 1)',
    }

    # This works because value_of_css_property is gotten from splinter,
    # which gets it from Selenium
    actual = test_page.button_container.find()._element.value_of_css_property(
        'background-color')

    browser_name = request.config.option.splinter_remote_name
    assert browsers[browser_name] == actual


def test_before_click(test_page, dummy_button):
    """Given I have an Button with a before method defined
    When I call Button.click()
    Then Button.before() is called first
    """
    test_page.navigate()
    dummy_button.click()
    assert 'foo' == button_before_str


def test_after_click(test_page, dummy_button):
    """Given I have an Button with an after method defined
    When I call Button.click()
    Then Button.after() is called after
    """
    test_page.navigate()
    dummy_button.click()

    assert 'bar' == button_after_str


def test_performer_returns_attribute_not_present(test_page):
    """Given a Button has a returns attribute set
    When the Button's performer method is called
    Then it returns the returns attribute
    """
    harpoon = Button('id', 'test_button')

    test_page.navigate()
    result = harpoon.perform()

    assert result is None


def test_performer_returns_attribute_present(test_page):
    """Given a Button has a returns attribute set
    When the Button's performer method is called
    Then it returns the returns attribute
    """
    class GetOverHere:
        def __init__(self, target):
            self.target = target

    harpoon = Button('id', 'test_button', returns=GetOverHere('sub-zero'))

    test_page.navigate()
    result = harpoon.perform()

    assert result.target == 'sub-zero'
