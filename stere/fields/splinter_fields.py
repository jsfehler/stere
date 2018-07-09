from .field import Field


class Button(Field):
    """Convenience Class on top of Field.

    Uses Splinter's click method.
    """
    def perform(self, value=None):
        self.find().click()
        return False


class Checkbox(Field):
    """Class with specific methods for handling checkboxes."""
    def __init__(self, *args, default_checked=False, **kwargs):
        super().__init__(*args, **kwargs)

        self.default_checked = default_checked

    def set_to(self, state):
        """Set a checkbox to the desired state.

        Args:
            state (bool): True for check, False for uncheck
        """
        if state:
            self.check()
        else:
            self.uncheck()

    def toggle(self):
        """If the checkbox is checked, uncheck it.
        If the checkbox is unchecked, check it.
        """
        if self.checked:
            self.uncheck()
        else:
            self.check()

    def perform(self, value=None):
        if not self.default_checked:
            self.find().check()
        else:
            self.find().uncheck()
        return False


class Input(Field):
    """Convenience Class on top of Field.

    Uses Splinter's input method.
    """
    def perform(self, value=None):
        self.find().fill(value)
        return True


class Link(Field):
    """Convenience Class on top of Field.

    Uses Splinter's click method.
    """
    def perform(self, value=None):
        self.find().click()
        return False


class Root(Field):
    """Convenience Class on top of Field."""
    def find(self):
        return self._element.find()


class Text(Field):
    """Convenience Class on top of Field."""
    pass
