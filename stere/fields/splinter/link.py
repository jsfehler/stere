from ..decorators import stere_performer, use_after, use_before
from ..field import Field


@stere_performer('click', consumes_arg=False)
class Link(Field):
    """Convenience Class on top of Field.

    Uses Splinter's click method.
    """

    @use_after
    @use_before
    def click(self) -> None:
        """Use Splinter's click method.

        Example:

            >>> login = Link('id', 'loginLink')
            >>> login.click()

        """
        self.find().click()
