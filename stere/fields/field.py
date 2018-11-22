from functools import wraps

from .element_builder import build_element


def stere_performer(method_name, consumes_arg=False):
    """Wraps a Class that contains a method which should be
    used by Area.perform().
    """

    def wrapper(cls):
        class Performer(cls):
            def perform(self, value=None):
                performer = getattr(self, method_name)
                if consumes_arg:
                    performer(value)
                    return True
                else:
                    performer()
                    return False
        # Preserve original class name
        Performer.__name__ = cls.__name__
        return Performer
    return wrapper


def use_before(func, *args, **kwargs):
    @wraps(func)
    def wrapper(obj, *inner_args, **inner_kwargs):
        obj.before()
        return func(obj, *inner_args, **inner_kwargs)
    return wrapper


def use_after(func, *args, **kwargs):
    @wraps(func)
    def wrapper(obj, *inner_args, **inner_kwargs):
        result = func(obj, *inner_args, **inner_kwargs)
        obj.after()
        return result
    return wrapper


class Field:
    """Field objects represent individual pieces on a page.
    Conceptually, they're modelled after general behaviours, not specific
    HTML elements.

    Arguments:
        strategy (str): The type of strategy to use when locating an element.
        locator (str): The locator for the strategy.
        workflows (list): Any workflows the Field should be included with.


    Example:

        >>> from stere.fields import Field
        >>> my_field = Field('xpath', '//*[@id="js-link-box-pt"]/small/span')

    """
    def __init__(self, strategy, locator, *args, **kwargs):
        self.strategy = strategy
        self.locator = locator
        self._element = build_element(strategy, locator)

        self.workflows = kwargs.get('workflows') or []

    def __getattr__(self, val):
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
            return getattr(self.find(), val)

    def __repr__(self):
        return (
            f'{self.__class__.__name__} - '
            f'Strategy: {self.strategy}, Locator: {self.locator}')

    @property
    def element(self):
        """Tries to find the element, the returns the results.
        """
        return self._element.find()

    def before(self):
        """Called automatically before methods with the `@use_before`
        decorator are called.

        By default it does nothing. Override this method if an action must be
        taken before the method has been called.
        """
        pass

    def after(self):
        """Called automatically before methods with the `@use_after`
        decorator are called.

        By default it does nothing. Override this method if an action must be
        taken after the method has been called.
        """
        pass

    @use_after
    @use_before
    def perform(self, value=None, *args, **kwargs):
        """Will be called by Area.perform()

        Returns:
            bool: True if the action used an argument, else False
        """
        return False

    def includes(self, value):
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

    def find(self):
        """Find the first matching element.

        Returns:
            Element

        Raises:
            ValueError - If more than one element is found.
        """
        found_elements = self._element.find()
        if len(found_elements) >= 2:
            raise ValueError("Expected one element, found multiple")
        return found_elements[0]

    def find_all(self):
        """Find all matching elements.

        Returns:
            list
        """
        return self._element.find()
