Fields
------

Field
~~~~~

.. autoclass:: stere.fields.Field()

  .. automethod:: stere.fields.Field.includes()

  .. automethod:: stere.fields.Field.before()

  .. automethod:: stere.fields.Field.after()

  .. automethod:: stere.fields.Field.value_contains()

  .. automethod:: stere.fields.Field.value_equals()


Root
~~~~

.. autoclass:: stere.fields.Root()


Text
~~~~

.. autoclass:: stere.fields.Text()


Performer method
~~~~~~~~~~~~~~~~

A Field can have a single method be designated as a performer.
This method will be called when the Field is inside an Area and that Area's perform() method is called.

For example, Input's performer is the fill() method, and Button's performer is the click() method. Given the following Area:

.. code-block:: python

    search = Area(
        query=Input('id', 'xsearch'),
        submit=Button('id', 'xsubmit'),
    )

and the following script:

.. code-block:: python

    search.perform('Orange')


When ``search.perform('Orange')`` is called, ``query.fill('Orange')`` is called, followed by ``submit.click()``.

See the documentation for `Area <https://stere.readthedocs.io/en/latest/area.html>`_ for more details.


Calling the performer method explicitly
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The performer method is available as ``Field.perform()``.
Calling it will run the performer method, but they are not aliases.

No matter what the return value of the performer method is,
the return value from calling Field.perform() will always be the Field.returns attribute.

Using the splinter Button Field as an example, the only difference between
`Button.click()` and `Button.perform()` is that perform will return the object
set in the `Field.returns` attribute.
See `Returning Objects <https://stere.readthedocs.io/en/latest/returning_objects.html>`_ for more details.

Calling the performer method implicitly
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

When a page instance is called directly, the `perform()` method will be executed.

The following code will produce the same results:

.. code-block:: python

    button = Button()
    button.perform()


.. code-block:: python

    button = Button()
    button()


Events
~~~~~~

Fields inherit from an EventEmitter class.

By default, they emit the following events:

- before: Before methods with the `@use_before` decorator are called.
- after: After methods with the `@use_after` decorator are called.

.. automethod:: stere.fields.Field.on()

.. automethod:: stere.fields.Field.emit()

.. autoattribute:: stere.fields.Field.events()


Subclassing Field
~~~~~~~~~~~~~~~~~

Field can be subclassed to suit your own requirements.

If the __init__() method is overwritten, make sure to call super() before your own code.

If your class needs specific behaviour when interacting with Areas, it must be wrapped with the @stere_performer decorator to specify a performer method.

When creating a new type of Field, the stere_performer class decorator should used to assign a performer method.


Field Decorators
~~~~~~~~~~~~~~~~

.. automethod:: stere.fields.decorators.stere_performer()

.. automethod:: stere.fields.decorators.use_before()

.. automethod:: stere.fields.decorators.use_after()
