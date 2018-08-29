Fields
------

.. autoclass:: stere.fields.Field()

  .. automethod:: stere.fields.Field.includes()

  .. automethod:: stere.fields.Field.before()

  In this example, Dropdown has been subclassed to hover over the Dropdown before clicking.

  .. code-block:: python

      from stere.fields import Dropdown

      class CSSDropdown(Dropdown):
          """A Dropdown that's customized to hover over the element before attempting
          a select.
          """
          def before(self):
              self.element.mouse_over()

  .. automethod:: stere.fields.Field.after()


Performer method
~~~~~~~~~~~~~~~~

A Field can have a single method be designated as a performer.
This causes the method to be called when the Field is inside an Area and that Area's perform() method is called.

For example, Input's performer is the fill() method, and Button's performer is the click() method. Given the following Area:

.. code-block:: python

    search = Area(
        query=Input('id', 'xsearch'),
        submit=Button('id', 'xsubmit'),
    )

and the following script:

.. code-block:: python
    
    search.perform()


When search.perform() is called, query.fill() is called, followed by submit.click().

See the documentation for `Area <https://stere.readthedocs.io/en/latest/area.html>`_ for more details.


Assigning the performer method
++++++++++++++++++++++++++++++

When creating a new type of Field, the stere_performer class decorator can be used to assign a performer method.

.. code-block:: python

    from stere.fields.field import stere_performer

    @stere_performer('philosophize', consumes_arg=False)
    class DiogenesButton(Field):
        def philosophize(self):
            print("As a matter of self-preservation, a man needs good friends or ardent enemies, for the former instruct him and the latter take him to task.")

The `consumes arg` argument should be used to specify if the method should use an argument provided by Area.perform() or not.


Subclassing Field
~~~~~~~~~~~~~~~~~

Field can be subclassed to suit your own requirements.

If the __init__() method is overwritten, make sure to call super() before your own code.

If your class needs specific behaviour when interacting with Areas, it must use the @stere_performer decorator to specify a performer method.


Splinter Fields
~~~~~~~~~~~~~~~

Fields that rely on Splinter being connected to Stere.

The following Fields are available with the default Splinter implementation:

- :ref:`Button <button>`: Clickable object.
- :ref:`Checkbox <checkbox>`: Object with a set and unset state.
- :ref:`Dropdown <dropdown>`: Object with multiple options to choose from.
- :ref:`Input <input>`: Object that accepts keyboard input.
- :ref:`Link <link>`: Clickable text.
- :ref:`Root <root>`: Parent container.
- :ref:`Text <text>`: Non-interactive text.



.. _button:
.. class:: stere.fields.Button()

  Convenience Class on top of Field, it implements `click()` as its performer.

  .. automethod:: stere.fields.Button.click()


.. _checkbox:
.. class:: stere.fields.Checkbox()

  By default, the Checkbox field works against HTML inputs with type="checkbox".

  Can be initialized with the `default_checked` argument. If True, the Field assumes the checkbox's default state is checked.

  It implements `opposite()` as its performer.

  .. automethod:: stere.fields.Checkbox.set_to()

  .. automethod:: stere.fields.Checkbox.toggle()

  .. automethod:: stere.fields.Checkbox.opposite()


.. _dropdown:
.. class:: stere.fields.Dropdown()

  By default, the Dropdown field works against HTML Dropdowns.
  However, it's possible to extend Dropdown to work with whatever implementation of a CSS Dropdown you need.

  It implements `select()` as its performer.

  The `option` argument can be provided to override the default implementation.
  This argument expects a Field. The Field should be the individual options in the dropdown you wish to target.

  .. code-block:: python

      self.languages = Dropdown('id', 'langDrop', option=Button('xpath', '/h4/a/strong'))


  .. automethod:: stere.fields.Dropdown.options()

  .. automethod:: stere.fields.Dropdown.select()


.. _input:
.. class:: stere.fields.Input()

  A simple wrapper over Field, it implements `fill()` as its performer.

  .. automethod:: stere.fields.Input.fill()

  Fills the element with value.


.. _link:
.. class:: stere.fields.Link()

  A simple wrapper over Field, it implements `click()` as its performer.

  .. automethod:: stere.fields.Link.click()

  Clicks the element.


.. _root:
.. class:: stere.fields.Root()

  A simple wrapper over Field, it does not implement a performer method.


.. _text:
.. class:: stere.fields.Text()

  A simple wrapper over Field, it does not implement a performer method.


Location Strategies
-------------------
.. _location_strategies:

These represent the way a locator will be searched for.

By default, the strategies available are:

- css
- xpath
- tag
- name
- text
- id
- value

These all use Splinter. If you're using a different automation tool, you must create your strategies. These can override the default strategies. (ie: You can create a custom css strategy to replace the default)


Custom Locator Strategies
-------------------------

Custom strategies can be defined using the `@strategy` decorator on top of a Class.

Any class can be decorated with @strategy, as long as the _find_all and _find_all_in_parent methods are implemented.

In the following example, the 'data-test-id' strategy is defined.
It wraps Splinter's find_by_xpath method to simplify the locator required on the Page Object.


.. code-block:: python

    from stere.strategy import strategy


    @strategy('data-test-id')
    class FindByDataTestId():
        def is_present(self, *args, **kwargs):
            return self.browser.is_element_present_by_xpath(f'.//*[@data-test-id="{self.locator}"]')

        def is_not_present(self, *args, **kwargs):
            return self.browser.is_element_not_present_by_xpath(f'.//*[@data-test-id="{self.locator}"]')

        def _find_all(self):
            """Find from page root."""
            return self.browser.find_by_xpath(f'.//*[@data-test-id="{self.locator}"]')

        def _find_all_in_parent(self):
            """Find from inside parent element."""
            return self.parent_locator.find_by_xpath(f'.//*[@data-test-id="{self.locator}"]')


With this implemented, Fields can now be defined like so:

.. code-block:: python

    my_button = Button('data-test-id', 'MyButton')
