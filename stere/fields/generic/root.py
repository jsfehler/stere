from ..decorators import stere_performer
from ..field import Field


@stere_performer('null_action', consumes_arg=False)
class Root(Field):
    """A simple wrapper over Field, it does not implement a performer method.
    Although Root has no specific behaviour, it can be useful when declaring a
    root for an Area or RepeatingArea.

    Example:

        >>> from stere.areas import RepeatingArea
        >>> from stere.fields import Root
        >>>
        >>>
        >>> collections = RepeatingArea(
        >>>     root=Root('xpath', '//table/tr'),
        >>>     quantity=Text('css', '.collection_qty'),
        >>> )
    """

    pass
