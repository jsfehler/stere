import copy

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

    def __init__(self, root: Field, **kwargs):
        self.root = root
        self.repeater = Area
        self.repeater_name = self.repeater.__name__

        self._items = {}
        for k, v in kwargs.items():
            if not isinstance(v, (Field, Area)):
                raise ValueError(
                    'RepeatingArea arguments can only be a Field or Area.',
                )
            if k != 'root':
                self._items[k] = v
                # Field (in plural) can be accessed directly.
                setattr(self, f'{k}s', v)

    def new_container(self) -> Areas:
        """Get a new instance of the container this class uses.

        Returns:
            Areas

        """
        return Areas()

    @property
    def areas(self) -> Areas:
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

    def children(self) -> Areas:
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

        for root in all_roots:
            copy_items = copy.deepcopy(self._items)
            for field_name in copy_items.keys():
                child = copy_items[field_name]

                # Every Field in the Area gets the root set here.
                if isinstance(child, Field):
                    child._element.parent_locator = root
                # Area inside an Area
                elif isinstance(child, Area):
                    # Has root
                    if child.root:
                        child.root._element.parent_locator = root
                    # Has no root
                    else:
                        for _, v in child._items.items():
                            v._element.parent_locator = root

            new_area = self.repeater(**copy_items)
            container.append(new_area)
        return container
