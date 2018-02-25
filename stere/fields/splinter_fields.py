from .field import Field


class Button(Field):
    """Convenience Class on top of Field.

    Uses Splinter's click method.
    """
    def perform(self, value=None):
        self.find().click()
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
