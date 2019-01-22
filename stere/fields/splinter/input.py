from ..decorators import stere_performer, use_after, use_before
from ..field import Field


@stere_performer('fill', consumes_arg=True)
class Input(Field):
    """Convenience Class on top of Field.

    Uses Splinter's input method.
    """
    @use_after
    @use_before
    def fill(self, value=None):
        """Uses Splinter's fill method.

        Arguments:
            value (str): The text to enter into the input.

        Example:

            >>> first_name = Input('id', 'fillme')
            >>> first_name.fill('Joseph')

        """
        self.find().fill(value)
