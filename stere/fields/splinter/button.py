from ..decorators import stere_performer, use_after, use_before
from .clickable import Clickable


@stere_performer('click', consumes_arg=False)
class Button(Clickable):
    """Convenience Class on top of Field.

    Implements `click()` as its performer.

    Example:

        >>> purchase = Button('id', 'buy_button')
        >>> purchase.click()

    """
