import time

from pages import spy_dummy

import pytest


@pytest.fixture()
def xhr_test_page():
    return spy_dummy.XHRDummyPage()


@pytest.fixture()
def fetch_test_page():
    return spy_dummy.FetchDummyPage()


def test_fetch_spy(fetch_test_page):
    fetch_test_page.navigate()
    fetch_test_page.fetch.add()

    # We know the page waits 3 seconds before making the request
    time.sleep(4)

    fetch_test_page.fetch_spy.wait_for_no_activity()

    assert "Hello World" == fetch_test_page.filled_text.text


def test_xhr_fetch_total_is_accurate(fetch_test_page):
    """
    When I check the total number of xhr requests
    Then the number is accurate.
    """
    fetch_test_page.navigate()
    fetch_test_page.fetch_spy.add()

    # We know the page waits 3 seconds before making the request
    time.sleep(4)

    assert 1 == fetch_test_page.fetch_spy.total


def test_fetch_spy_not_added(fetch_test_page):
    """
    When I wait for no activity without having added the spy
    Then a TimeoutError should be raised
    """
    fetch_test_page.navigate()

    with pytest.raises(TimeoutError):
        fetch_test_page.fetch_spy.wait_for_no_activity()


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

    assert 1 == xhr_test_page.xhr_spy.total


def test_xhr_spy_not_added(xhr_test_page):
    """
    When I wait for no activity without having added the spy
    Then a TimeoutError should be raised
    """
    xhr_test_page.navigate()

    with pytest.raises(TimeoutError):
        xhr_test_page.xhr_spy.wait_for_no_activity()
