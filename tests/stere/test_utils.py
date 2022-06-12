import time

from stere.utils import _retry


def test_retry():
    """When I call _retry
    Then a function is called until it returns a True value
    """
    now = time.time()

    result = _retry(
        lambda: True if time.time() >= (now + 6) else False,
        retry_time=8,
    )

    assert result


def test_retry_fails():
    """When I call _retry
    And the timeout is hit
    Then it returns False
    """
    now = time.time()

    result = _retry(
        lambda: True if time.time() == (now + 6) else False,
        retry_time=4,
    )

    assert not result
