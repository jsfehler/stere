Splinter Fields
~~~~~~~~~~~~~~~

The following Fields are available with the default Splinter implementation.
Each implements a specific performer method.

- :ref:`Button <button>`: Clickable object.
- :ref:`Checkbox <checkbox>`: Object with a set and unset state.
- :ref:`Dropdown <dropdown>`: Object with multiple options to choose from.
- :ref:`Input <input>`: Object that accepts keyboard input.
- :ref:`Link <link>`: Clickable text.
- :ref:`Root <root>`: Parent container.
- :ref:`Text <text>`: Non-interactive text.

All Fields that use Splinter also inherit the following convenience methods:

  .. automethod:: stere.strategy.splinter_strategies.SplinterBase.is_present()
  .. automethod:: stere.strategy.splinter_strategies.SplinterBase.is_not_present()
  .. automethod:: stere.strategy.splinter_strategies.SplinterBase.is_visible()
  .. automethod:: stere.strategy.splinter_strategies.SplinterBase.is_not_visible()

  Example:

  .. code-block:: python

      class Inventory(Page):
          def __init__(self):
              self.price = Link('css', '.priceLink')


      assert Inventory().price.is_present(wait_time=6)


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
