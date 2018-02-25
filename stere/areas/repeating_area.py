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
        """
        created_areas = []
        all_roots = self.root.find()
        for item in all_roots:
            copy_items = copy.deepcopy(self.items)
            for key, value in copy_items.items():
                copy_items[key]._element.parent_locator = item

            new_area = Area(**copy_items)
            created_areas.append(new_area)
        return created_areas
