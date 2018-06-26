from .element_builder import build_element


class Field:
    """Base class for objects on a page.

    Arguments:
        strategy (str):
        locator (str):
        workflows (list):
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
            return getattr(element.find(), val)

    @property
    def element(self):
        """Tries to find the element, the returns the results.
        """
        return self._element.find()

    def perform(self, value=None):
        """Will be called by Area.perform()

        Returns:
            bool: True if the action used an argument, else False
        """
        return False

    def includes(self, value):
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
        if len(found_elements) > 2:
            raise ValueError("Expected one element, found multiple")
        return found_elements.first

    def find_all(self):
        """Find all matching elements.

        Returns:
            List
        """
        return self._element.find()
