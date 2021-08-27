import time
from typing import TypeVar

from .fetch_script import js_script
from ..browserenabled import BrowserEnabled


T = TypeVar('T', bound='FetchSpy')


class FetchSpy(BrowserEnabled):
    """Spy for Fetch instances in the browser.

    Allows scripts to block until network activity has stopped.

    Example:
        >>> from stere.browser_spy import FetchSpy
        >>>
        >>> spy = FetchSpy()
        >>> spy.add()
        >>> # Browser interaction
        >>> spy.wait_for_no_activity()
        >>> # More browser interaction

    Can also be used as a context manager, with add() called automatically:

    Example:
        >>> from stere.browser_spy import FetchSpy
        >>>
        >>> with FetchSpy() as spy:
        >>>     # Browser interaction
        >>>     spy.wait_for_no_activity()
        >>>     # More browser interaction

    """

    def __enter__(self: T) -> T:
        """As a context manager, the spy is added on enter."""
        self.add()
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        """Nothing happens on exit."""
        pass

    def add(self) -> None:
        """Inject the spy onto the page.

        Tracks the active and total amount of requests.
        """
        self.browser.execute_script(js_script)

    def wait_for_no_activity(self, timeout: int = 30) -> bool:
        """Until timeout, keep checking if Fetch is done.

        Requires the spy to already be present via FetchSpy.add()

        Arguments:
            timeout (int): Number of seconds to wait

        Raises:
            TimeoutError
        """
        end = time.time() + timeout
        no_active: bool = False

        while not no_active:
            no_active = self.active == 0

            # If no Fetch events, wait and retry.
            # This confirms no new events were added.
            if no_active:
                time.sleep(BrowserEnabled.fetch_spy_sleep_time)
                no_active = self.active == 0

            if time.time() > end:
                raise TimeoutError(
                    f'Fetch events took longer than {timeout} seconds.',
                )

        return no_active

    @property
    def active(self) -> int:
        """Get the number of active Fetch events."""
        return self.browser.execute_script("return document.activeFetchEvents")

    @property
    def total(self) -> int:
        """Get the number of total Fetch events."""
        return self.browser.execute_script("return document.totalFetchEvents")
