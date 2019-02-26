from ..decorators import stere_performer, use_after, use_before
from ..field import Field


@stere_performer('send_keys', consumes_arg=True)
class Input(Field):
    """Convenience Class on top of Field.

    Uses Appium's send_keys method.

    Arguments:
        default_value (str): When Input.send_keys() is called with no
            arguments, this value will be used instead.
    """
    def __init__(self, *args, default_value=None, **kwargs):
        super().__init__(*args, **kwargs)

        self.default_value = default_value or None

    @use_after
    @use_before
    def send_keys(self, value=None):
        """Uses Appium's fill method.

        Arguments:
            value (str): The text to enter into the input.

        Example:

        >>> first_name = Input('id', 'fillme')
        >>> first_name.send_keys('Joseph')

        """
        if value is None and self.default_value:
            value = self.default_value
        self.find().send_keys(value)
