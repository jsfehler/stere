import copy
import warnings

from .area import Area
from .areas import Areas
from .repeating import Repeating
from ..fields import Field


class RepeatingArea(Repeating):
    """
    Represents multiple identical Areas on a page.

    A root argument is required, which is expected to be a non-unique Field
    on the page.

    A collection of Areas are built from every instance of the root that is
    found. Every other Field provided in the arguments is populated inside
    each Area.

    In the following example, there's a table with 15 rows. Each row has
    two cells. The sixth row in the table should have an item with the
    name "Banana" and a price of "$7.00"

    >>> from stere.areas import RepeatingArea
    >>> from stere.fields import Root, Link, Text
    >>>
    >>> class Inventory(Page):
    >>>     def __init__(self):
    >>>         self.inventory_items = RepeatingArea(
    >>>             root=Root('xpath', '//table/tr'),
    >>>             name=Link('xpath', './td[1]'),
    >>>             price=Text('xpath', './td[2]'),
    >>>         )

    >>> inventory = Inventory()
    >>> assert 15 == len(inventory.areas)
    >>> assert "Banana" == inventory.areas[5].name
    >>> assert "$7.00" == inventory.areas[5].price
    """

    def __init__(self, **kwargs):
        if kwargs.get('root') is None:
            raise ValueError('RepeatingArea requires a Root Field.')

        self.root = kwargs['root']

        if kwargs.get('items') is not None:
            raise ValueError('"items" is a reserved parameter.')

        self.items = {}
        for k, v in kwargs.items():
            if not isinstance(v, Field) and not isinstance(v, Area):
                raise ValueError(
                    'RepeatingArea arguments can only be a Field or Area.',
                )
            if k != 'root':
                self.items[k] = v
                # Field (in plural) can be accessed directly.
                setattr(self, f'{k}s', v)

        self.repeater = Area
        self.repeater_name = self.repeater.__name__

    def new_container(self):
        """Get a new instance of the container this class uses.

        Returns:
            Areas

        """
        return Areas()

    @property
    def areas(self):
        """Find all instances of the root,
        then return a list of Areas: one for each root.

        Returns:
            Areas: list-like collection of every Area that was found.

        Example:

            >>> def test_stuff():
            >>>     listings = MyPage().my_repeating_area.areas
            >>>     listings[0].my_input.fill('Hello world')

        """
        return self.children()

    def children(self):
        """Find all instances of the root,
        then return a list of Areas: one for each root.

        Returns:
            Areas: list-like collection of every Area that was found.

        Example:

            >>> def test_stuff():
            >>>     listings = MyPage().my_repeating_area.areas
            >>>     listings[0].my_input.fill('Hello world')

        """
        all_roots = self._all_roots()
        container = self.new_container()

        for item in all_roots:
            copy_items = copy.deepcopy(self.items)
            for field_name in copy_items.keys():
                child = copy_items[field_name]
                if isinstance(child, Field):
                    child._element.parent_locator = item
                elif isinstance(child, Area):
                    if child.root:
                        child.root._element.parent_locator = item
                    else:
                        child._element.parent_locator = item

            new_area = self.repeater(**copy_items)
            container.append(new_area)
        return container

    def area_with(self, field_name, field_value):
        """Find an Area where the Field's value matches an expected value.

        Arguments:
            field_name (str): The name of the Field object.
            field_value (str): The value of the Field object.

        Returns:
            Area: The Area object that matches the search.

        Example:

            >>> class Inventory(Page):
            >>>     def __init__(self):
            >>>         self.items = RepeatingArea(
            >>>             root=Root('xpath', '//my_xpath_string'),
            >>>             description=Text('xpath', '//my_xpath_string')
            >>>         )
            >>>
            >>> def test_stuff():
            >>>     inventory = Inventory()
            >>>     found_area = inventory.items.area_with(
            >>>         "description", "Bananas")

        """
        warnings.warn(
            'RepeatingArea.areas_with() is deprecated.'
            ' Use RepeatingArea.areas.containing() instead.',
            FutureWarning,
        )
        for area in self.areas:
            field = getattr(area, field_name)

            if field.value == field_value:
                return area

        raise ValueError(f'Could not find {field_value} in any {field_name}.')
