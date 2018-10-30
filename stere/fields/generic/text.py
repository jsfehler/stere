from ..field import Field


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
