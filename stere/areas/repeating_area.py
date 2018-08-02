import copy

from ..fields import Field

from .area import Area


class RepeatingArea:
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
        then return an array of Area for each root.

        Returns:
            list: Collection of every Area that was found.

        Raises:
            ValueError: If no Areas were found.
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
        """For every Area found, check if the Field matching field_name has
        field_value. If so, return the Area.

        Returns:
            Area
        """
        for area in self.areas:
            field = getattr(area, field_name)

            if field.value == field_value:
                return area

        raise ValueError(f'Could not find {field_value} in any {field_name}.')
