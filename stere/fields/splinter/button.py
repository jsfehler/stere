from ..field import Field, use_before, use_after, stere_performer


@stere_performer('click', consumes_arg=False)
class Button(Field):
    """Convenience Class on top of Field, it implements `click()` as its performer.
    """
    @use_after
    @use_before
    def click(self):
        """Uses Splinter's click method."""
        self.find().click()
