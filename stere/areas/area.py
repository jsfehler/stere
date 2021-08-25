from typing import Optional, TypeVar, Union

from .repeating import Repeating
from ..fields import Field


T = TypeVar('T', bound='Area')


class Area:
    """A collection of unique objects on a page.

    Area takes any number of the following object types:
        - Field
        - Area
        - Repeating

    Example:

    >>> from stere.areas import Area
    >>> from stere.fields import Button
    >>>
    >>> class Album(Page):
    >>>     def __init__(self):
    >>>         self.genres = Area(
    >>>             jazz=Button('css', '.genreJazz'),
    >>>             metal=Button('css', '.genreMetal'),
    >>>             rock=Button('xpath', '//div[@id="genreRock"]'),
    >>>         )
    >>>
    >>> def test_album_genres():
    >>>     album = Album()
    >>>     album.genres.rock.click()
    """

    def __init__(self, root: Optional[Field] = None, **kwargs: Union[Field, Area, Repeating]):
        self.root = root

        # Store kwargs
        self._items = {}

        for key, value in kwargs.items():
            if not isinstance(value, (Field, Area, Repeating)):
                raise ValueError(
                    (
                        'Areas must only be initialized with: '
                        'Field, Area, Repeating types'
                    ),
                )
            self._items[key] = value

            # Sets the root for the element, if provided.
            if self.root is not None and value is not self.root:
                # Set the Field's _element's root
                if isinstance(value, Field):
                    value._element.root = self.root

                elif isinstance(value, Area):
                    # Area has a root, give that root a root.
                    if value.root is not None:
                        value.root._element.root = self.root
                    # Area has no root, set every Field's _element's root
                    else:
                        for _k, v in value._items.items():
                            v._element.root = self.root

                # Repeating sets its root Field's root.
                elif isinstance(value, Repeating):
                    value.root._element.root = self.root

            # Field can be called directly.
            setattr(self, key, value)

        self._workflow: Optional[str] = None

    def _set_parent_locator(self, element) -> None:
        """For every item in the Area, set a parent_locator.

        Arguments:
            element: The found element belonging to the parent of this object.
        """
        if self.root is not None:
            self.root._set_parent_locator(element)
        else:
            for _, v in self._items.items():
                v._set_parent_locator(element)

    def workflow(self: T, value: str) -> T:
        """Set the current workflow for an Area.

        Designed for chaining before a call to perform().

        Arguments:
            value (str): The name of the workflow to set.

        Returns:
            Area: The calling Area

        Example:

        >>> my_area.workflow('Foobar').perform()

        """
        self._workflow = value
        return self

    def perform(self, *args, **kwargs):
        """For every Field in an Area, "do the right thing"
        by calling the Field's perform() method.

        Fields that require an argument can either be given sequentially
        or with keywords.

        Arguments:
            args: Arguments that will sequentially be sent to Fields
                in this Area.
            kwargs: Arguments that will be sent specifically to the Field
                with a matching name.

        Example:

            Given the following Page Object:

            >>> from stere.areas import Area
            >>> from stere.fields import Button, Input
            >>>
            >>> class Login():
            >>>     def __init__(self):
            >>>         self.form = Area(
            >>>             username=Input('id', 'app-user'),
            >>>             password=Input('id', 'app-pwd'),
            >>>             submit=Button('id', 'app-submit')
            >>>         )

            Any of the following styles are valid:

            >>> def test_login():
            >>>     login = Login()
            >>>     login.my_area.perform('Sven', 'Hoek')

            >>> def test_login():
            >>>     login = Login()
            >>>     login.my_area.perform(username='Sven', password='Hoek')

            >>> def test_login():
            >>>     login = Login()
            >>>     login.my_area.perform('Sven', password='Hoek')
        """
        arg_index = 0
        workflow = self._workflow
        for field_name, field in self._items.items():
            # If the Field isn't in the current workflow, skip it entirely.
            if workflow is not None and workflow not in field.workflows:
                continue

            if field_name in kwargs:
                result = field.perform(kwargs[field_name])
            else:
                if args:
                    result = field.perform(args[arg_index])
                else:
                    result = field.perform()

                # If we've run out of arguments, don't increase the index.
                if field.consumes_arg and len(args) > (arg_index + 1):
                    arg_index += 1

        self._workflow = None

        return result
