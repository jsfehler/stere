import types

import pytest

from stere.event_emitter import EventEmitter


def test_event_emitter_register():
    """When I register a new event with the on() method
    Then the return value is a list of all the data for the event.
    """
    emitter = EventEmitter()

    def event_function(instance):
        pass

    listeners = emitter.on('dummy_event', event_function)

    assert listeners == [{'listener': event_function}]


def test_event_emitter_events():
    """When I register a new event
    Then the event is added to the EventEmitter's list of known events
    """
    emitter = EventEmitter()

    def event_function(instance):
        pass

    emitter.on('dummy_event', event_function)

    assert emitter.events == ['dummy_event']

    emitter.on('another_dummy_event', event_function)

    assert emitter.events == ['dummy_event', 'another_dummy_event']


def test_event_emitter_instance():
    """When I register a new event
    And emit the new event
    Then the listener function is called
    And the listener's argument is the instance linked to the EventEmitter
    """
    emitter = EventEmitter()

    x = types.SimpleNamespace()
    x.event_called = False

    def event_function(instance):
        assert isinstance(instance, EventEmitter)
        x.event_called = True

    emitter.on('dummy_event', event_function)

    emitter.emit('dummy_event')

    assert x.event_called


def test_event_emitter_invalid_event():
    """When I register a new event
    And emit the new event
    Then the listener function is called
    And the listener's argument is the instance linked to the EventEmitter
    """
    emitter = EventEmitter()

    def event_function(instance):
        assert isinstance(instance, EventEmitter)

    emitter.on('dummy_event', event_function)

    with pytest.raises(ValueError) as e:
        emitter.emit('invalid_event')

    assert str(e.value) == 'invalid_event is not a registered Event.'
