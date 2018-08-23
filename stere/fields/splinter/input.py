from ..field import Field, stere_performer, use_after, use_before


@stere_performer('fill', consumes_arg=True)
class Input(Field):
    """Convenience Class on top of Field.

    Uses Splinter's input method.
    """
    @use_after
    @use_before
    def fill(self, value=None):
        self.find().fill(value)
