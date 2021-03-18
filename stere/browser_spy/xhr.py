import time

from .xhr_script import js_script
from ..browserenabled import BrowserEnabled


class XHRSpy(BrowserEnabled):
    """Spy for XMLHttpRequest instances in the browser.

    Allows scripts to block until network activity has stopped.

    Example:
        >>> from stere.browser_spy import XHRSpy
        >>>
        >>> spy = XHRSpy()
        >>> spy.add()
        >>> # Browser interaction
        >>> spy.wait_for_no_activity()
        >>> # More browser interaction

    Can also be used as a context manager, with add() called automatically:

    Example:
        >>> from stere.browser_spy import XHRSpy
        >>>
        >>> with XHRSpy() as spy:
        >>>     # Browser interaction
        >>>     spy.wait_for_no_activity()
        >>>     # More browser interaction

    """

    def __enter__(self):
        """As a context manager, the spy is added on enter."""
        self.add()
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        """Nothing happens on exit."""
        pass

    def add(self):
        """Inject the spy onto the page.

        Tracks the active and total amount of requests.
        """
        self.browser.execute_script(js_script)

    def wait_for_no_activity(self, timeout: int = 30) -> bool:
        """Until timeout, keep checking if XHR is done.

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

            # If no XHR events, wait and retry.
            # This confirms no new requests were made.
            if no_active:
                time.sleep(BrowserEnabled.xhr_spy_sleep_time)
                no_active = self.active == 0

            if time.time() > end:
                raise TimeoutError(f'XHR took longer than {timeout} seconds.')

        return no_active

    @property
    def active(self) -> int:
        """Get the number of active XHR requests."""
        return self.browser.execute_script("return document.activeXHRrequests")

    @property
    def total(self) -> int:
        """Get the number of total XHR requests."""
        return self.browser.execute_script("return document.totalXHRrequests")
