from ..decorators import stere_performer, use_after, use_before
from ..field import Field


@stere_performer('send_keys', consumes_arg=True)
class Input(Field):
    """Convenience Class on top of Field.

    Uses Appium's send_keys method.
    """
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
        self.find().send_keys(value)
