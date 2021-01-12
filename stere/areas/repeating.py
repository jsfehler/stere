import copy
import typing

from ..utils import _retry


class Repeating:
    """
    Arguments:
        root (Field): A non-unique root to search for.
        repeater (Repeating): An object that inherits from Repeating.

    Represents abstract non-unique collections that repeat,
    based on a common root.

    This can be used to identify anything that not only appears multiple times,
    but also contains things which appear multiple times.

    Repeating are inherently confusing and should only be used if something
    appears multiple times, contains something else that appears multiple
    times, and is truly non-unique with no other way to target it.

    The last object in a chain of Repeating must be a RepeatingArea.
    This is because ultimately, there must be an end to the number of things
    that repeat.

    Example:

        A page where multiple "project" containers appear, each with a
        table of items.

        >>> from stere.areas import Repeating, RepeatingArea
        >>> from stere.fields import Root, Link, Text
        >>>
        >>> projects = Repeating(
        >>>     root=Root('css', '.projectContainer'),
        >>>     repeater=RepeatingArea(
        >>>         root=Root('xpath', '//table/tr'),
        >>>         description=Link('xpath', './td[1]'),
        >>>         cost=Text('xpath', './td[2]'),
        >>>    )
        >>> )
        >>>
        >>> assert 2 == len(projects.children)
        >>> first_project = projects.children[0]
        >>> assert first_project.areas.contains(
        >>>     'description', 'Solar Panels')
        >>>
        >>> second_project = projects.children[1]
        >>> assert second_project.areas.contains(
        >>>     'description', 'Self-Driving Cars')

    """

    def __init__(self, root, repeater):
        self.root = root
        self.repeater = repeater
        self.repeater_name = type(self.repeater).__name__

    def new_container(self) -> typing.List:
        """Must return an object to contain results from Repeater.children()

        By default a list is returned.

        Returns:
            list

        """
        return []

    def __len__(self) -> int:
        """Return the number of times the root was found.

        Does not actually build the children.

        """
        all_roots = self.root.find_all()
        return len(all_roots)

    def _all_roots(self):
        """Search for all instances of the root.

        Only intended for use inside Repeating.children().
        Otherwise use self.root.find_all().

        Raises:
            ValueError: If no instances of the root were found.

        Returns:
            All instances of the Repeating's root

        """
        all_roots = self.root.find_all()
        if 0 == len(all_roots):
            raise ValueError(
                f'Could not find any {self.repeater_name} using the root: '
                f'{self.root.locator}',
            )
        return all_roots

    def children(self) -> typing.List:
        """Find all instances of the root,
        then return a collection containing children built from those roots.

        The type of collection is determined by the Repeating.new_container()
        method.

        Returns:
            list-like collection of every repeater that was found.

        """
        all_roots = self._all_roots()
        container = self.new_container()

        for root in all_roots:
            copy_repeater = copy.deepcopy(self.repeater)
            # Set the repeater's parent locator to the found root instance
            try:
                copy_repeater.root._element.parent_locator = root
            except AttributeError:
                # Repeater has no 'root' attribute, eg: It's an Area
                for _, v in copy_repeater._items.items():
                    v._element.parent_locator = root

            container.append(copy_repeater)

        return container

    def has_children(self, retry_time: typing.Optional[int] = None) -> bool:
        """Check if any children can be found.

        Arguments:
            retry_time: Number of seconds to check for.

        Returns:
            bool

        """
        return _retry(
            lambda: len(self) > 0,
            retry_time=retry_time,
        )
