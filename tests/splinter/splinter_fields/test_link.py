import time

import pytest

from stere.fields import Link


link_before_str = 'before'
link_after_str = 'after'


@pytest.fixture(scope='session')
def dummy_link():
    class Dummy(Link):
        def before(self):
            global link_before_str
            link_before_str = 'foo'

        def after(self):
            global link_after_str
            link_after_str = 'bar'

    return Dummy('id', 'test_link')


def test_link(browser, test_page):
    """
    When a link is clicked
    Then the link's action occurs
    """
    test_page.navigate()
    test_page.link.click()

    time.sleep(2)

    # The result of clicking should land the user on google.ca
    assert 'https://www.google.ca' in browser.url


def test_perform_return_value(test_page):
    """
    When Link's perform() method is called
    And Link does not consume an argument
    Then Link's performer method should return False
    """
    test_page.navigate()
    res = test_page.link.perform()

    assert not res


def test_before_fill(test_page, dummy_link):
    """Given I have an Link with a before method defined
    When I call Link.click()
    Then Link.before() is called first
    """
    test_page.navigate()
    dummy_link.click()
    assert 'foo' == link_before_str


def test_after_fill(test_page, dummy_link):
    """Given I have an Link with an after method defined
    When I call Link.click()
    Then Link.after() is called after
    """
    test_page.navigate()
    dummy_link.click()

    assert 'bar' == link_after_str
