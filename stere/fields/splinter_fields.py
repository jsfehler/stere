from .field import Field, use_before, use_after


def stere_performer(method_name, consumes_arg=False):
    """Wraps a Class that contains a method which should be
    used by Area.perform().
    """
    def wrapper(cls):
        class Performer(cls):
            def perform(self, value=None):
                getattr(self, method_name)(value)
                if consumes_arg:
                    return True
                return False
        return Performer
    return wrapper


@stere_performer('click', consumes_arg=False)
class Button(Field):
    """Convenience Class on top of Field.

    Uses Splinter's click method.
    """
    @use_after
    @use_before
    def click(self, *args, **kwargs):
        self.find().click()


@stere_performer('opposite', consumes_arg=False)
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

    @use_after
    @use_before
    def check(self):
        self.find().check()

    @use_after
    @use_before
    def uncheck(self):
        self.find().uncheck()

    def opposite(self):
        if not self.default_checked:
            self.check()
        else:
            self.uncheck()
        return False


@stere_performer('fill', consumes_arg=True)
class Input(Field):
    """Convenience Class on top of Field.

    Uses Splinter's input method.
    """
    @use_after
    @use_before
    def fill(self, value=None):
        self.find().fill(value)


@stere_performer('click', consumes_arg=False)
class Link(Field):
    """Convenience Class on top of Field.

    Uses Splinter's click method.
    """
    @use_after
    @use_before
    def click(self):
        self.find().click()


class Root(Field):
    """Convenience Class on top of Field."""
    def find(self):
        return self._element.find()


class Text(Field):
    """Convenience Class on top of Field."""
    pass
