from ..field import Field, use_before, use_after, stere_performer


@stere_performer('click', consumes_arg=False)
class Link(Field):
    """Convenience Class on top of Field.

    Uses Splinter's click method.
    """
    @use_after
    @use_before
    def click(self):
        self.find().click()
