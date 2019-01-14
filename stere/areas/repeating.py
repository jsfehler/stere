import copy


class Repeating:
    """
    Arguments:
        repeater (Repeating): An object that inherits from Repeating.

    Represents abstract non-unique collections that repeat,
    based on a common root.

    Repeating are inherintly confusing and should only be used if something is
    truly non-unique and cannot be predicted.

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

    def new_container(self):
        """Must return an object to contain results from Repeater.children()

        Returns:
            list
        """
        return []

    def __len__(self):
        """Calling len() returns the number of times the root was found,
        but does not actually build the children.
        """
        all_roots = self.root.find_all()
        return len(all_roots)

    def _all_roots(self):
        """Search for all instances of the root.

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

    def children(self):
        """Find all instances of the root,
        then return a collection containing children built from those roots.

        Returns:
            list-like collection of every Area that was found.
        """

        all_roots = self._all_roots()
        container = self.new_container()

        for item in all_roots:
            copy_items = copy.deepcopy(self.repeater)
            # Set the element's parent locator to the found root instance
            copy_items.root._element.parent_locator = item

            container.append(copy_items)

        return container
