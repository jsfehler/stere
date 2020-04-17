import time
import typing
from functools import reduce

from stere import Stere


def rgetattr(obj, attr, *args):
    """A nested getattr"""
    def _getattr(obj, attr):
        return getattr(obj, attr, *args)
    return reduce(_getattr, [obj] + attr.split('.'))


def _retry(
    fn: typing.Callable, retry_time: typing.Optional[int] = None,
) -> bool:
    """Retry a function for a specific amount of time.

    Returns:
        True if the function returns a truthy value, else False

    Arguments:
        fn (function): Function to retry
        retry_time: Number of seconds to retry. If not specified,
            Stere.retry_time will be used.

    """
    retry_time = retry_time or Stere.retry_time
    end_time = time.time() + retry_time

    while time.time() < end_time:
        if fn():
            return True
    return False
