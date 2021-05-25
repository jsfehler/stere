import types

from stere.fields import Field
from stere.fields.decorators import use_after, use_before


class MockField(Field):
    @use_before
    @use_after
    def click(self):
        """Dummy method for EventEmitter testing."""
        pass


class MockPage:
    def __init__(self):
        self.field = MockField('xpath', '//div')

        self.dummy_namespace = types.SimpleNamespace()
        self.dummy_namespace.after_event_called = False
        self.dummy_namespace.before_event_called = False

        def event_function_after(instance):
            """Dummy event function."""
            self.dummy_namespace.after_event_called = True

        def event_function_before(instance):
            """Dummy event function."""
            self.dummy_namespace.before_event_called = True

        self.field.on('after', event_function_after)
        self.field.on('before', event_function_before)


def test_event_emitter_field_events():
    """When a performer method is called
    Then the correct events should be emitted.
    """
    mock_page = MockPage()

    mock_page.field.click()

    assert mock_page.dummy_namespace.after_event_called
    assert mock_page.dummy_namespace.before_event_called
