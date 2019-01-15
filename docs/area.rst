Areas
=====

Areas represent groupings of Fields on a Page.

The following Area objects are available:

- Area: A non-hierarchical, unique group of Fields.
- RepeatingArea: A hierarchical, non-unique group of Areas. They require a Root Field.


.. autoclass:: stere.areas.Area()

  .. automethod:: stere.areas.Area.perform()

  .. automethod:: stere.areas.Area.workflow()


.. autoclass:: stere.areas.RepeatingArea()

  .. autoattribute:: stere.areas.RepeatingArea.areas()

  .. automethod:: stere.areas.RepeatingArea.area_with()


.. autoclass:: stere.areas.Areas()

  .. automethod:: stere.areas.Areas.containing()

  .. automethod:: stere.areas.Areas.contain()


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
