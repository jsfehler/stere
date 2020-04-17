import time
import typing

from stere import Stere

from .button import Button
from ..decorators import stere_performer, use_after, use_before
from ..field import Field


@stere_performer('select', consumes_arg=True)
class Dropdown(Field):
    """Represents a dropdown menu.
    If the "option" argument is provided with a field,
        use that as the dropdown item.
    Else, assume a standard HTML Dropdown and use the option tag.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # If no option arg is given, assume Dropdown is a standard HTML one.
        if kwargs.get('option') is None:
            self.option = Button('tag', 'option')
        else:
            self.option = kwargs.get('option')

    def __getitem__(self, index):
        """Accessing by index will select the option matching the index."""
        return self.options[index].click()

    @property
    def options(self):
        """Search for all the elements that are an option in the dropdown.

        Returns:
            list

        """
        self.option._element.parent_locator = self.find()
        return list(self.option.find_all())

    @use_after
    @use_before
    def select(self, value: str, retry_time: typing.Optional[int] = None):
        """Search for an option by its html content, then clicks the one
        that matches.

        Arguments:
            value (str): The option value to select.
            retry_time (int): The amount of time to try to find the value.
                Default is Stere.retry_time.

        Raises:
            ValueError: The provided value could not be found in the dropdown.

        """
        retry_time = retry_time or Stere.retry_time
        end_time = time.time() + retry_time

        found_options = []

        while time.time() < end_time:
            found_options = self._select(value)
            if not len(found_options):
                return

        raise ValueError(
            f'{value} was not found. Found values are: {found_options}')

    def _select(self, value: str) -> typing.List[str]:
        found_options = []

        for option in self.options:
            found_options.append(option.html)
            if option.html == value:
                option.click()
                return []

        return found_options
