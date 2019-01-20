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


def test_button(browser, request, test_page):
    """When a button is clicked
    Then the button's action occurs
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
    assert browsers[request.config.option.browser_name] == actual


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
