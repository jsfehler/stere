from .area import Area


class Areas:
    """Searchable collection of Areas.

    Behaves like a list.
    """
    def __init__(self, container=None):
        self._container = container or []

    def __getattr__(self, item):
        return getattr(self._container, item)

    def __len__(self):
        return len(self._container)

    def __getitem__(self, item):
        return self._container[item]

    def append(self, item):
        if not isinstance(item, Area):
            raise TypeError(
                f"{item} is not an Area. "
                "Only Area objects can be inside Areas."
            )

        self._container.append(item)

    def containing(self, field_name, field_value):
        """Searches for Areas where the Field's value
        matches the expected value and then returns an Areas object with all
        matches.

        Arguments:
            field_name (str): The name of the Field object.
            field_value (str): The value of the Field object.

        Returns:
            Area

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
            field = getattr(area, field_name)

            if field.value == field_value:
                containing.append(area)

        return containing

    def contain(self, field_name, field_value):
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
            field = getattr(area, field_name)

            if field.value == field_value:
                return True

        return False
