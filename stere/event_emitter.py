from typing import Callable, Dict, List


class EventEmitter:
    """A basic Event Emitter.

    Attributes:
        _events_data: A dict of every registered event and the listeners
            attached to them.
    """

    def __init__(self) -> None:
        self._events_data: Dict[str, List[Dict]] = {}

    @property
    def events(self) -> List[str]:
        """Get the names of every registered event."""
        return list(self._events_data.keys())

    def on(self, event: str, listener: Callable) -> List[Dict]:
        """Register a new listener to an event.

        If the event does not exist, it will be created.

        Arguments:
            event (str): The name of the event to register a listener to.
            listener (Callable): The function to run when the event is emitted.

        Returns:
            list: The list of listeners for the event.

        Example:

            >>> def my_event_function(emitter):
            >>>    pass
            >>>
            >>> my_field = Field()
            >>> my_field.on('before', my_event_function)

        """
        if event not in self._events_data:
            self._events_data[event] = []

        listener_data = {'listener': listener}
        self._events_data[event].append(listener_data)

        return self._events_data[event]

    def emit(self, event: str) -> None:
        """Emit an event.

        Every listener registered to the event will be called with the
        emitter class as the first argument.

        Listeners are called in the order of registration.

        Arguments:
            event (str): The name of the event to emit.

        Raises:
            ValueError: If the event has not been registered.
        """
        event_data = self._events_data.get(event)
        if event_data is None:
            raise ValueError(f'{event} is not a registered Event.')

        for ev in event_data:
            ev['listener'](self)
