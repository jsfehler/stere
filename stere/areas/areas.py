from .area import Area
from ..utils import rgetattr


class Areas:
    """Searchable collection of Areas.

    Behaves like a list.
    """

    def __init__(self, container=None):
        self._container = container or []

    def __getattr__(self, item):
        """__getattr__ checks the internal container."""
        return getattr(self._container, item)

    def __len__(self) -> int:
        """__len__ checks the internal container."""
        return len(self._container)

    def __getitem__(self, item):
        """__getitem__ checks the internal container."""
        return self._container[item]

    def append(self, item: Area) -> None:
        """Add a new Area to the container.

        Raises:
            TypeError: If a non-Area object is given.

        """
        if not isinstance(item, Area):
            raise TypeError(
                f"{item} is not an Area. "
                "Only Area objects can be inside Areas.",
            )

        self._container.append(item)

    def containing(self, field_name: str, field_value: str):
        """Search for Areas where the Field's value
        matches the expected value and then returns an Areas object with all
        matches.

        Arguments:
            field_name (str): The name of the Field object.
            field_value (str): The value of the Field object.

        Returns:
            Areas: A new Areas object with matching results

        Example:

            >>> class Inventory(Page):
            >>>     def __init__(self):
            >>>         self.items = RepeatingArea(
            >>>             root=Root('xpath', '//my_xpath_string'),
            >>>             description=Text('xpath', '//my_xpath_string')
            >>>         )
            >>>
            >>> def test_stuff():
            >>>     # Ensure 10 items have a price of $9.99
            >>>     inventory = Inventory()
            >>>     found_areas = inventory.items.areas.containing(
            >>>         "price", "$9.99")
            >>>     assert 10 == len(found_areas)

        """
        containing = Areas()
        for area in self:
            field = rgetattr(area, field_name)

            if field.value == field_value:
                containing.append(area)

        return containing

    def contain(self, field_name: str, field_value: str) -> bool:
        """Check if a Field in any Area contains a specific value.

        Arguments:
            field_name (str): The name of the Field object.
            field_value (str): The value of the Field object.

        Returns:
            bool: True if matching value found, else False

        Example:

            >>> class Inventory(Page):
            >>>     def __init__(self):
            >>>         self.items = RepeatingArea(
            >>>             root=Root('xpath', '//div[@id='inventory']'),
            >>>             description=Text('xpath', './td[1]')
            >>>         )
            >>>
            >>> def test_stuff():
            >>>     inventory = Inventory()
            >>>     assert inventory.items.areas.contain(
            >>>         "description", "Bananas")

        """
        for area in self:
            field = rgetattr(area, field_name)

            if field.value == field_value:
                return True

        return False
