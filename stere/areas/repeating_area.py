import copy
import warnings

from .area import Area
from .areas import Areas
from ..fields import Field


class RepeatingArea:
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
            if not isinstance(v, Field):
                raise ValueError(
                    'RepeatingArea arguments can only be Field objects.',
                )
            if k is not 'root':
                self.items[k] = v
                # Field (in plural) can be accessed directly.
                setattr(self, f'{k}s', v)

    def __len__(self):
        all_roots = self.root.find_all()
        return len(all_roots)

    @property
    def areas(self):
        """Find all instances of the root,
        then return a list of Areas: one for each root.

        Returns:
            Areas: list-like collection of every Area that was found.

        Raises:
            ValueError: If no Areas were found.

        Example:

            >>> def test_stuff():
            >>>     listings = MyPage().my_repeating_area.areas
            >>>     listings[0].my_input.fill('Hello world')

        """
        created_areas = Areas()

        all_roots = self.root.find_all()
        if 0 == len(all_roots):
            raise ValueError(
                f'Could not find any Areas with the root: {self.root.locator}',
            )

        for item in all_roots:
            copy_items = copy.deepcopy(self.items)
            for field_name in copy_items.keys():
                copy_items[field_name]._element.parent_locator = item

            new_area = Area(**copy_items)
            created_areas.append(new_area)
        return created_areas

    def area_with(self, field_name, field_value):
        """Searches the RepeatingArea for a single Area where the Field's value
        matches the expected value and then returns the entire Area object.

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
