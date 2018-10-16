from ..fields import Field


class Area:
    """A collection of unique fields.

    The Area object takes any number of Fields as arguments.
    Each Field must be unique on the Page and only present in one Area.

    Example:

    >>> from stere.areas import Area
    >>> from stere.fields import Button
    >>>
    >>> class Album(Page):
    >>>     def __init__(self):
    >>>         self.tracks = Area(
    >>>             first_track=Button('xpath', '//my_xpath_string'),
    >>>             second_track=Button('xpath', '//my_xpath_string'),
    >>>             third_track=Button('xpath', '//my_xpath_string'),
    >>>         )
    >>>
    >>> def test_stuff():
    >>>     album = Album()
    >>>     album.tracks.third_track.click()
    """

    def __init__(self, **kwargs):
        if kwargs.get('items') is not None:
            raise ValueError('"items" is a reserved parameter.')

        self.root = kwargs.get('root')

        self.items = {}
        for key, value in kwargs.items():
            if not isinstance(value, Field):
                raise ValueError(
                    'Areas must only be initialized with field objects.',
                )
            self.items[key] = value
            # Sets the root for the element, if provided.
            if self.root is not None and value is not self.root:
                self.items[key]._element.root = self.root

            # Field can be called directly.
            setattr(self, key, value)

        self._workflow = None

    def workflow(self, value):
        """Sets the current workflow for an Area.

        Designed for chaining before a call to perform().
        ie: my_area.workflow('Foobar').perform()

        Returns:
            self
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
        for field_name, field in self.items.items():
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
                if result and len(args) > (arg_index + 1):
                    arg_index += 1

        self._workflow = None
