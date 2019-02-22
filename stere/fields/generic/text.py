from ..decorators import stere_performer
from ..field import Field


@stere_performer('null_action', consumes_arg=False)
class Text(Field):
    """A simple wrapper over Field, it does not implement a performer method.
    Although Root has no specific behaviour, it can be useful when declaring
    that a Field should just be static Text.

    Example:

        >>> from stere.fields import Text
        >>>
        >>>
        >>> self.price = Text('id', 'item_price')
    """
    pass
