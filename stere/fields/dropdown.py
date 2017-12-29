from .fields import Button


class Dropdown(Button):
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
        """Get a dictionary of the options in a Dropdown.

        Returns:
            Dict: option_name: option_element for every option in the dropdown
        """
        self.option._element.parent_locator = self.find()
        rv = {}
        for item in self.option.find_all():
            rv[item.html] = item
        return rv

    def before_select(self):
        """Override this method if an action must be taken prior to the
        dropdown being selectable.
        """
        pass

    def select(self, value):
        self.before_select()
        for option_name, option_element in self.options.items():
            if option_name == value:
                option_element.click()
                break
        else:
            raise ValueError(f'{value} was not found in the dropdown.')
