from .field import Field


class Button(Field):
    """Convenience Class on top of Field.

    Uses Splinter's click method.
    """
    def perform(self, value=None):
        self.find().click()
        return False


class Checkbox(Button):
    """Class with specific methods for handling checkboxes."""
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
        if self.checked():
            self.uncheck()
        else:
            self.check()


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
