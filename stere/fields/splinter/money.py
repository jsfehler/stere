import re

from moneyed import Money as PyMoney

from ..decorators import stere_performer
from ..field import Field


@stere_performer('null_action', consumes_arg=False)
class Money(Field):
    """A simple wrapper over Field, it does not implement a performer method.

    Money has methods for handling Fields where the text is a form of currency.

    Example:

        >>> from stere.fields import Money
        >>>
        >>>
        >>> self.price = Money('id', 'item_price')
    """

    number_regex = r'[^0-9\.]+'

    def money(self, currency: str = 'USD') -> PyMoney:
        """Create a Money object from the Field's text.

        The returned object is an instance of moneyed.Money.
        See: `py-moneyed <https://github.com/limist/py-moneyed>`_

        Arguments:
            currency (str): Name of the currency to use

        Returns:
            moneyed.Money

        """
        return PyMoney(amount=self.number, currency=currency)

    @property
    def number(self) -> str:
        """The Field's text, normalized to look like a number."""
        m = re.compile(self.number_regex, re.IGNORECASE)
        return m.sub('', self.text)
