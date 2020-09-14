from .clickable import Clickable
from ..decorators import stere_performer


@stere_performer('click', consumes_arg=False)
class Link(Clickable):
    """Convenience Class on top of Field.

    Implements `click()` as its performer.

    Example:

        >>> purchase = Link('id', 'buy_link')
        >>> purchase.click()

    """
