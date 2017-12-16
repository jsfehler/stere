Stere
=====

A modular, Page Object oriented approach to browser based test automation.

The goal is to minimize the amount of implementation code visible in Page Objects and reduce
the need for helper methods.

It uses `Splinter <https://github.com/cobrateam/splinter>`_ under the hood.


Requirements
------------

Python >= 3.6


Basic Usage
-----------

A minimal Stere Page Object looks like this:

.. code-block:: python

    from stere.fields import Input

    class MyPage():
        def __init__(self):
            self.my_input = Input('xpath', '//my_xpath_string')


Fundementally, a Page Object is just a Python class.
Stere provides 2 types of objects to model a web page: Fields and Areas.

It can be called in a test like so:

.. code-block:: python

    def test_stuff():
        MyPage().my_input.fill('Hello world')


Fields
------

Fields represent individual objects on a web page.
They model general behaviours, not specific HTML elements.

The following Fields are available:

- Button: Clickable object.
- Input: Object that accepts keyboard input.
- Link: Clickable text.
- Root: Parent container.
- Text: Non-interactive text.

Fields take 2 arguments: strategy and locator.

The strategies available by default are:

- css
- xpath
- tag
- name
- text
- id
- value

The locator must be a string that matches the strategy chosen.

Every Field exposes the `find()` and `find_all()` methods. These perform the actual search via Splinter.


Areas
-----

Areas represent sections on a Page.

The following Areas are available:

- Area: A non-hierarchical, unique group of Fields.
- RepeatingArea: A hierarchical, non-unique group of Fields. They require a Root Field.

Areas take any number of Fields as arguments.

.. code-block:: python

    from stere.fields import Area, Input

    class MyPage():
        def __init__(self):
            self.my_area = Area(
                my_input=Input('xpath', '//my_xpath_string')
            )

Fields in an area can be called like so:
            
.. code-block:: python

    def test_stuff():
        MyPage().my_area.my_input.fill('Hello world')


Area.perform()
~~~~~~~~~~~~~~

The perform method will "Do the right thing" sequentially for every Field inside an Area.

For Button and Link, it will click them.

For Input, it will fill them using the text provided.

For Text, it will do nothing.


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
            

Reusing Areas
~~~~~~~~~~~~~

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
~~~~~~~~~~~~~~~~~

If an Area appears on many pages and requires many custom methods,
it may be better to subclass the Area instead of embedding the methods in the Page Object:

.. code-block:: python

    class Header(Area):
        def __init__(self, *args, **kwargs):
            super(Header)

        def my_custom_method(self, *args, **kwargs):
            ...


    class Main(Page):
        def __init__(self, *args, **kwargs):
            self.header = Header()


    class Other(Page):
        def __init__(self, *args, **kwargs):
            self.header = Header()

