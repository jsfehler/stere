Areas
=====

Areas represent groupings of Fields on a Page.

The following Area objects are available:

- Area: A non-hierarchical, unique group of Fields.
- RepeatingArea: A hierarchical, non-unique group of Areas. They require a Root Field.


Area()
------

The Area object takes any number of Fields as arguments.
Each Field must be unique on the Page and only present in one Area.

.. code-block:: python

    from stere.fields import Area, Input

    class MyPage():
        def __init__(self):
            self.my_area = Area(
                my_input=Input('xpath', '//my_xpath_string')
            )

Fields in an Area can be called as attributes of the Area:

.. code-block:: python

    def test_stuff():
        MyPage().my_area.my_input.fill('Hello world')


Area.perform()
~~~~~~~~~~~~~~

The perform method will "Do the right thing" sequentially for every Field inside an Area.

- For Button and Link, it will click them.

- For Input, it will fill them using the text arguments provided.

- For Text, it will do nothing.


.. code-block:: python

    from stere.fields import Area, Input

    class MyPage():
        def __init__(self):
            self.my_area = Area(
                my_input=Input('xpath', '//my_xpath_string'),
                my_input_2=Input('xpath', '//my_xpath_string'),
                my_button=Button('xpath', '//my_xpath_string')
            )


    def test_stuff():
        MyPage().my_area.perform('Hello', 'World')


RepeatingArea()
---------------

A RepeatingArea represents a collection of Fields that appear multiple times on a Page.

The RepeatingArea objects requires a Root Field in the arguments, but otherwise takes any number of Fields as arguments.
The other Fields will use the Root as a parent.

.. code-block:: python

    from stere.fields import RepeatingArea, Root, Input

    class MyPage():
        def __init__(self):
            self.my_repeating_area = RepeatingArea(
                my_root=Root('xpath', '//my_xpath_string'),
                my_input=Input('xpath', '//my_xpath_string')
            )


RepeatingArea().areas
~~~~~~~~~~~~~~~~~~~~~

A list of all the Area objects found can be accessed with the areas attribute.

.. code-block:: python

    def test_stuff():
        listings = MyPage().my_repeating_area.areas
        listings[0].my_input.fill('Hello world')


Reusing Areas
-------------

Sometimes an identical Area may be present on multiple pages.
Areas do not need to be created inside a page object, they can be created outside and then called from inside a page.

.. code-block:: python

    header = Area(
        ...
    )

    class Items(Page):
        def __init__(self, *args, **kwargs):
            self.header = header


Subclassing Areas
-----------------

If an Area appears on many pages and requires many custom methods,
it may be better to subclass the Area instead of embedding the methods in the Page Object:

.. code-block:: python

    class Header(Area):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)

        def my_custom_method(self, *args, **kwargs):
            ...


    class Main(Page):
        def __init__(self, *args, **kwargs):
            self.header = Header()


    class Other(Page):
        def __init__(self, *args, **kwargs):
            self.header = Header()
