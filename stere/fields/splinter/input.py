from ..field import Field, use_before, use_after, stere_performer


@stere_performer('fill', consumes_arg=True)
class Input(Field):
    """Convenience Class on top of Field.

    Uses Splinter's input method.
    """
    @use_after
    @use_before
    def fill(self, value=None):
        self.find().fill(value)
