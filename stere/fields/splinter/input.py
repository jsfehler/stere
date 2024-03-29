import platform
from typing import Optional

from selenium.webdriver.common.keys import Keys

from ..decorators import stere_performer, use_after, use_before
from ..field import Field


@stere_performer('fill', consumes_arg=True)
class Input(Field):
    """Convenience Class on top of Field.

    Uses Splinter's input method.

    Arguments:
        default_value (str): When Input.fill() is called with no arguments,
            this value will be used instead.
    """

    def __init__(self, *args, default_value: Optional[str] = None, **kwargs):
        super().__init__(*args, **kwargs)

        self.default_value = default_value

    @use_after
    @use_before
    def fill(self, value: Optional[str] = None) -> None:
        """Use Splinter's fill method.

        Arguments:
            value (str): The text to enter into the input.

        Example:

            >>> first_name = Input('id', 'fillme')
            >>> first_name.fill('Joseph')

        """
        if value is None and self.default_value:
            value = self.default_value
        self.find().fill(value)

    def highlight(self) -> None:
        """Highlight the text content in an input element."""
        system = platform.system()

        if system == 'Darwin':  # OSX
            value = Keys.COMMAND + 'a'
        else:
            value = Keys.CONTROL + 'a'

        self.type(value)
