Fields Returning Objects
========================

Fields take an optional `returns` argument. This can be any object.
When the Field's perform() method is called, this object will be returned.

This can be used to return another Page Object.

.. code-block:: python

    class Navigation(Page):
        def __init__(self):
            self.goto_settings = Button('id', 'settingsLink', returns=NextPage())

.. code-block:: python

    def test_navigation():
        page = Navigation()
        next_page = page.goto_settings.perform()

Fields inside an Area
+++++++++++++++++++++

When a Field is inside an Area and has the returns argument set, only the
object for the last Field in the Area will be returned when `Area.perform()` is called.


.. code-block:: python

    class Address(Page):
        def __init__(self):
            self.form = Area(
                address=Input('id', 'formAddress'),
                city=Input('id', 'formCity', returns=FooPage()),
                submit=Button('id', 'formsubmit', returns=NextPage()),
            )


.. code-block:: python

    def test_address_form():
        page = Address()
        next_page = page.form.perform()
