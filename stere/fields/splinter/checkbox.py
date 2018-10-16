from ..field import Field, stere_performer, use_after, use_before


@stere_performer('opposite', consumes_arg=False)
class Checkbox(Field):
    """Class with specific methods for handling checkboxes."""
    def __init__(self, *args, default_checked=False, **kwargs):
        super().__init__(*args, **kwargs)

        self.default_checked = default_checked

    def set_to(self, state):
        """Set a checkbox to the desired state.

        Arguments:
            state (bool): True for check, False for uncheck

        Example:

            >>> confirm = Checkbox('id', 'selectme')
            >>> confirm.set_to(True)

        """
        if state:
            self.check()
        else:
            self.uncheck()

    def toggle(self):
        """If the checkbox is checked, uncheck it.
        If the checkbox is unchecked, check it.

        >>> confirm = Checkbox('id', 'selectme')
        >>> confirm.toggle()

        """
        if self.checked:
            self.uncheck()
        else:
            self.check()

    @use_after
    @use_before
    def check(self):
        self.find().check()

    @use_after
    @use_before
    def uncheck(self):
        self.find().uncheck()

    def opposite(self):
        """Switches the checkbox to the opposite of its default state.
        Uses the `default_checked` attribute to decide this.

        >>> confirm = Checkbox('id', 'selectme')
        >>> confirm.opposite()

        """
        if not self.default_checked:
            self.check()
        else:
            self.uncheck()
        return False
