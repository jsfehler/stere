from ..decorators import stere_performer, use_after, use_before
from ..field import Field


@stere_performer('click', consumes_arg=False)
class Clickable(Field):
    """Convenience Class on top of Field.

    Implements `click()` as its performer.
    """

    @use_after
    @use_before
    def click(self) -> None:
        """Use Splinter's click method.

        Example:

            >>> purchase = Clickable('id', 'buy_button')
            >>> purchase.click()

        """
        self.is_visible()
        self.is_clickable()
        self.find().click()
