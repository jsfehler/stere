import copy

from ..fields import Field

from .area import Area


class RepeatingArea:
    """
    Represents a collection of Fields that appear multiple times on a Page.

    The RepeatingArea objects requires a Root Field in the arguments,
    but otherwise takes any number of Fields as arguments.
    The other Fields will use the Root as a parent.

    Example:

    >>> from stere.areas import RepeatingArea
    >>> from stere.fields import Root, Input
    >>>
    >>> class MyPage():
    >>>     def __init__(self):
    >>>         self.my_repeating_area = RepeatingArea(
    >>>             root=Root('xpath', '//my_xpath_string'),
    >>>             my_input=Input('xpath', '//my_xpath_string')
    >>>         )
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
                    'RepeatingArea arguments can only be Field objects.'
                )
            if k is not 'root':
                self.items[k] = v
                # Field (in plural) can be accessed directly.
                setattr(self, f'{k}s', v)

    @property
    def areas(self):
        """Find all instances of the root,
        then return an array of Areas for each root.

        Returns:
            list: Collection of every Area that was found.

        Raises:
            ValueError: If no Areas were found.

        Example:

        >>> def test_stuff():
        >>>     listings = MyPage().my_repeating_area.areas
        >>>     listings[0].my_input.fill('Hello world')

        """
        created_areas = []
        all_roots = self.root.find()
        if 0 == len(all_roots):
            raise ValueError(
                f'Could not find any Areas with the root: {self.root.locator}'
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
            field_name (str): The name of the field object.
            field_value (str): The value of the field object.

        Returns:
            Area

        Example:

            >>> class Inventory():
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
        for area in self.areas:
            field = getattr(area, field_name)

            if field.value == field_value:
                return area

        raise ValueError(f'Could not find {field_value} in any {field_name}.')
