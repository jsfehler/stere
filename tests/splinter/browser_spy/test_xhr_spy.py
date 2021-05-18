import time

from pages import spy_dummy

import pytest


@pytest.fixture()
def xhr_test_page():
    return spy_dummy.XHRDummyPage()


def test_xhr_spy(xhr_test_page):
    xhr_test_page.navigate()
    xhr_test_page.xhr_spy.add()

    # We know the page waits 3 seconds before making the request
    time.sleep(4)

    xhr_test_page.xhr_spy.wait_for_no_activity()

    assert "Hello World" == xhr_test_page.filled_text.text


def test_xhr_spy_total_is_accurate(xhr_test_page):
    """
    When I check the total number of xhr requests
    Then the number is accurate.
    """
    xhr_test_page.navigate()
    xhr_test_page.xhr_spy.add()

    # We know the page waits 3 seconds before making the request
    time.sleep(4)

    assert 2 == xhr_test_page.xhr_spy.total


def test_xhr_spy_not_added(xhr_test_page):
    """
    When I wait for no activity without having added the spy
    Then a TimeoutError should be raised
    """
    xhr_test_page.navigate()

    with pytest.raises(TimeoutError):
        xhr_test_page.xhr_spy.wait_for_no_activity()


def test_xhr_spy_multiple_add(xhr_test_page):
    """
    When I add the XHR spy to the page multiple times
    Then the number of total requests is still accurate.
    """
    xhr_test_page.navigate()
    for _ in range(5):
        xhr_test_page.xhr_spy.add()

    # We know the page waits 3 seconds before making the request
    time.sleep(4)

    assert 2 == xhr_test_page.xhr_spy.total


def test_xhr_spy_multiple_add_in_progress(xhr_test_page):
    """
    When I add the XHR spy to the page multiple times
    And a request is in progress
    Then the number of total requests is still accurate.
    """
    xhr_test_page.navigate()
    for _ in range(2):
        xhr_test_page.xhr_spy.add()

    # We know the page waits 3 seconds before making the request
    time.sleep(4)

    for _ in range(2):
        xhr_test_page.xhr_spy.add()

    assert 2 == xhr_test_page.xhr_spy.total
