import pytest

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


def test_after_fill(test_page, dummy_input):
    """Given I have an Input with an after method defined
    When I call Input.fill()
    Then Input.after() is called after
    """
    test_page.navigate()
    dummy_input.fill('Input this')

    assert 'bar' == input_after_str
