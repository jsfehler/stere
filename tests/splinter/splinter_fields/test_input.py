import pytest

from selenium.webdriver.common.keys import Keys

from stere.fields import Input


input_before_str = 'before'
input_after_str = 'after'


@pytest.fixture(scope='session')
def dummy_input():
    class Dummy(Input):
        def before(self):
            global input_before_str
            input_before_str = 'foo'

        def after(self):
            global input_after_str
            input_after_str = 'bar'

    return Dummy('id', 'test_input_first_name')


def test_input_implicit_call(test_page):
    """When an Input is called
    Then the Input's perform method is called
    """
    test_page.navigate()
    test_page.input_area.input('Winamp')


def test_input(test_page):
    """When an input is filled with the text 'Winamp'
    Then the text in the input should be 'Winamp'
    """
    test_page.navigate()
    test_page.input_area.input.fill('Winamp')

    assert 'Winamp' == test_page.input_area.input.element.value


def test_before_fill(test_page, dummy_input):
    """Given I have an Input with a before method defined
    When I call Input.fill()
    Then Input.before() is called first
    """
    test_page.navigate()
    dummy_input.fill('Input this')
    assert 'foo' == input_before_str


def test_input_default_value(test_page):
    """Given I have an Input with a default value
    When I call Input.fill() with no arguments
    Then the default value is filled in
    """
    test_page.navigate()

    i = Input('id', 'test_input_first_name', default_value='Ampwin')
    i.fill()

    assert 'Ampwin' == i.value


def test_after_fill(test_page, dummy_input):
    """Given I have an Input with an after method defined
    When I call Input.fill()
    Then Input.after() is called after
    """
    test_page.navigate()
    dummy_input.fill('Input this')

    assert 'bar' == input_after_str


def test_input_call(test_page):
    test_page.navigate()

    i = Input('id', 'test_input_first_name', returns=10)

    assert 10 == i.perform('alpha')


def test_input_highlight(test_page):
    test_page.navigate()

    test_page.input_area.input.fill('highlight me')
    assert test_page.input_area.input.value == 'highlight me'

    test_page.input_area.input.highlight()

    # Clear text content with delete.
    # Since it's highlighted, all of it should be removed.
    test_page.input_area.input.fill(Keys.DELETE)

    assert test_page.input_area.input.value == ''
