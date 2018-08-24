from .button import Button
from ..field import Field, stere_performer, use_after, use_before


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

    @property
    def options(self):
        """Searches for all the elements that are an option in the dropdown.

        Returns:
            list
        """
        self.option._element.parent_locator = self.find()
        return [item for item in self.option.find_all()]

    @use_after
    @use_before
    def select(self, value):
        """Searches for an option by its html content, then clicks the one
        that matches.

        Arguments:
            value (str): The option value to select.

        Raises:
            ValueError: The provided value could not be found in the dropdown.
        """
        found_options = []
        for option in self.options:
            found_options.append(option.html)
            if option.html == value:
                option.click()
                break
        else:
            raise ValueError(
                f'{value} was not found. Found values are: {found_options}')
