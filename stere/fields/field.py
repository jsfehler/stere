from typing import Optional

import splinter

from stere import Stere

from .build_element import build_element
from .decorators import stere_performer
from ..event_emitter import EventEmitter
from ..utils import _retry
from ..value_comparator import ValueComparator


@stere_performer('null_action', consumes_arg=False)
class Field(EventEmitter):
    """The representation of individual page components.

    Conceptually, they're modelled after general behaviours, not specific
    HTML tags.

    Arguments:
        strategy (str): The type of strategy to use when locating an element.
        locator (str): The locator for the strategy.
        workflows (list): Any workflows the Field should be included with.

    Example:

        >>> from stere.fields import Field
        >>> my_field = Field('xpath', '//*[@id="js-link-box-pt"]/small/span')

    Attributes:
        element: The result of a search operation on the page.
            All attribute calls on the Field that fail are then tried on the
            element.

            This allows classes inheriting from Field to act as a proxy to the
            underlying automation library.

            Using Splinter's `visible` attribute as an example, the following
            methods are analogous:

            >>> Field.visible == Field.find().visible == Field.element.visible

    """

    def __init__(self, strategy: str, locator: str, *args, **kwargs):
        super().__init__()

        # Ensure before and after events are valid.
        self._events_data['before'] = []
        self._events_data['after'] = []

        self.strategy = strategy
        self.locator = locator
        self._element = build_element(strategy, locator)

        self.workflows = kwargs.get('workflows') or []
        self.returns = kwargs.get('returns') or None

    def __call__(self, *args, **kwargs):
        """When a Field instance is called, run the perform() method."""
        return self.perform(*args, **kwargs)

    def __getattr__(self, val: str):
        """If an attribute doesn't exist, try getting it from the element.

        If it still doesn't exist, do a find() on the element and see if the
        attribute exists there.
        """
        element = super().__getattribute__('_element')
        try:
            return getattr(element, val)
        except AttributeError:
            # Allows deepcopy not to get into infinite recursion.
            if val in ['__deepcopy__', '__getstate__']:
                raise AttributeError

            # Try getting the attribute from the found element.
            try:
                elem = self.find(Stere.retry_time)
            except splinter.exceptions.ElementDoesNotExist as e:
                msg = (
                    'Failed to get element attribute.'
                    f'Could not find element with {self.strategy}: {self.locator}'  # NOQA E501
                )
                raise AttributeError(msg) from e

            return getattr(elem, val)

    def __repr__(self) -> str:
        """Provide a string representation of this class."""
        return (
            f'{self.__class__.__name__} - '
            f'Strategy: {self.strategy}, Locator: {self.locator}')

    def _set_parent_locator(self, element) -> None:
        """Set the parent locator of this Field's element."""
        self._element.parent_locator = element

    @property
    def element(self):
        """Tries to find the element, then returns the results."""
        return self._element.find()

    def null_action(self) -> None:
        """Empty method used as the performer for Field.

        Allows the base Field object to be used in an Area.
        """
        pass

    def before(self) -> None:
        """Called automatically before methods with the `@use_before`
        decorator are called.

        Performer methods are decorated with @use_before.

        By default it does nothing. Override this method if an action must be
        taken before a method is called.

        In the following example, Dropdown has been subclassed to hover over
        the element before clicking.

        Example:

            >>> from stere.fields import Dropdown
            >>>
            >>> class CSSDropdown(Dropdown):
            >>>     def before(self):
            >>>         self.element.mouse_over()
        """
        pass

    def after(self) -> None:
        """Called automatically before methods with the `@use_after`
        decorator are called.

        Performer methods are decorated with @use_after.

        By default it does nothing. Override this method if an action must be
        taken after the method has been called.
        """
        pass

    def includes(self, value: str):
        """Will search every element found by the Field for a value property
        that matches the given value.
        If an element with a matching value is found, it's then returned.

        Useful for when you have non-unique elements and know a value is in
        one of the elements, but don't know which one.

        Arguments:
            value (str): A text string inside an element you want to find.

        Returns:
            element

        Example:

            >>> class PetStore(Page):
            >>>     def __init__(self):
            >>>         self.inventory = Link('xpath', '//li[@class="inv"]')
            >>>
            >>> pet_store = PetStore()
            >>> pet_store.inventory_list.includes("Kittens").click()

        """
        for item in self.element:
            if item.value == value:
                return item

    def value_contains(
        self, expected: str, wait_time: Optional[int] = None,
    ) -> ValueComparator:
        """Check if the value of the Field contains an expected value.

        Arguments:
            expected (str): The expected value of the Field
            wait_time (int): The number of seconds to search.
                Default is Stere.retry_time.

        Returns:
            ValueComparator: Object with the boolean result of the comparison.

        Example:

            >>> class PetStore(Page):
            >>>     def __init__(self):
            >>>         self.price = Link('xpath', '//li[@class="price"]')
            >>>
            >>> pet_store = PetStore()
            >>> assert pet_store.price.value_contains("19.19", wait_time=6)

        """
        result = _retry(
            lambda: expected in self.value,
            retry_time=wait_time,
        )

        value = ValueComparator(result, expected=expected, actual=self.value)
        return value

    def value_equals(
        self, expected: str, wait_time: Optional[int] = None,
    ) -> ValueComparator:
        """Check if the value of the Field equals an expected value.

        Arguments:
            expected (str): The expected value of the Field
            wait_time (int): The number of seconds to search.
                Default is Stere.retry_time.

        Returns:
            ValueComparator: Object with the boolean result of the comparison.

        Example:

            >>> class PetStore(Page):
            >>>     def __init__(self):
            >>>         self.price = Link('xpath', '//li[@class="price"]')
            >>>
            >>> pet_store = PetStore()
            >>> assert pet_store.price.value_equals("$19.19", wait_time=6)

        """
        result = _retry(
            lambda: expected == self.value,
            retry_time=wait_time,
        )

        value = ValueComparator(result, expected=expected, actual=self.value)
        return value

    def find(self, wait_time: Optional[int] = None):
        """Find the first matching element.

        Returns:
            Element

        Raises:
            ValueError - If more than one element is found.

        """
        found_elements = self.find_all(wait_time)
        if len(found_elements) >= 2:
            raise ValueError("Expected one element, found multiple")
        return found_elements[0]

    def find_all(self, wait_time: Optional[int] = None):
        """Find all matching elements.

        Returns:
            list

        """
        return self._element.find(wait_time)
