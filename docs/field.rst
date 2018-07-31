Fields
------

The Field objects represent individual elements on a web page.
Conceptually, they represent general behaviours, not specific HTML elements.

The following Fields are available with the default Splinter implementation:

- :ref:`Button <button>`: Clickable object.
- :ref:`Checkbox <checkbox>`: Object with a set and unset state.
- :ref:`Dropdown <dropdown>`: Object with multiple options to choose from.
- :ref:`Input <input>`: Object that accepts keyboard input.
- Link: Clickable text.
- Root: Parent container.
- Text: Non-interactive text.

Fields take 2 arguments: :ref:`location strategy <location_strategies>` and locator.

.. code-block:: python

    self.some_text = Text('xpath', '//*[@id="js-link-box-pt"]/small/span')


Performer method
~~~~~~~~~~~~~~~~

A Field can have a single method be designated as a performer.
This causes the method to be called when the Field is inside an Area and that Area's perform() method is called.

For example, Input's performer is the fill() method, and Button's performer is the click() method. Given the following:

.. code-block:: python

    self.some_area = Area(
        my_input=Input('id', 'foobar'),
        my_button=Button('id', 'barfoo'), 
    )
    
When some_area.perform() is called, my_input.fill() is called, followed by my_button.click().

Assigning the performer method
++++++++++++++++++++++++++++++

When creating a custom Field, the stere_performer class decorator can be used to assign a performer method.

.. code-block:: python

    from stere.fields.field import stere_performer

    @stere_performer('philosophize', consumes_arg=False)
    class DiogenesButton(Field):
        def philosophize(self):
            print("As a matter of self-preservation, a man needs good friends or ardent enemies, for the former instruct him and the latter take him to task.")

The `consumes arg` argument should be used to specify if the method should use an argument provided by Area.perform() or not.


Field.includes(value)
~~~~~~~~~~~~~~~~~~~~~

Will search every element found by the Field for a value property that matches the given value.
If an element with a matching value is found, it's then returned.

Useful for when you have non-unique elements and know a value is in one of the elements, but don't know which one.

.. code-block:: python

    PetStore().inventory_list.includes("Kittens").click()


Field.before()
~~~~~~~~~~~~~~

This method is called automatically before methods with the `@use_before` decorator are called.
By default it does nothing. It can be overridden to support any desired behaviour.

In this example, Dropdown has been subclassed to hover over the Dropdown before clicking.

.. code-block:: python

    from stere.fields import Dropdown

    class CSSDropdown(Dropdown):
        """A Dropdown that's customized to hover over the element before attempting
        a select.
        """
        def before(self):
            self.element.mouse_over()


Field.after()
~~~~~~~~~~~~~
This method is called automatically after methods with the `@use_after` decorator are called.
By default it does nothing. It can be overridden to support any desired behaviour.


Subclassing Field
~~~~~~~~~~~~~~~~~

Field can be subclassed to suit your own requirements.

If the __init__() method is overwritten, make sure to call super() before your own code.

If your class need specific behaviour when interacting with Areas, it must implement the perform() method.

Button
~~~~~~
.. _button:

A simple wrapper over Field, it implements `click()` as its performer.

Input
~~~~~
.. _input:

A simple wrapper over Field, it implements `fill()` as its performer.

Checkbox
~~~~~~~~
.. _checkbox:

By default, the Checkbox field works against HTML inputs with type="checkbox".

Can be initialized with the `default_checked` argument. If True, the Field assumes the checkbox's default state is checked. 


set_to(state)
+++++++++++++

Set a checkbox to the desired state.

Args:
    state (bool): True for check, False for uncheck

toggle()
++++++++

If the checkbox is checked, uncheck it. If the checkbox is unchecked, check it.

opposite()
++++++++++

Switches the checkbox to the opposite of its default state. Uses the `default_checked` attribute to decide this.


Dropdown
~~~~~~~~
.. _dropdown:

By default, the Dropdown field works against HTML Dropdowns.
However, it's possible to extend Dropdown to work with whatever implementation of a CSS Dropdown you need.

The `option` argument can be provided to override the default implementation.
This argument expects a Field. The Field should be the individual options in the dropdown you wish to target.

.. code-block:: python

    self.languages = Dropdown('id', 'langDrop', option=Button('xpath', '/h4/a/strong'))

options
+++++++

Searches for all the options in the dropdown and returns a list of Fields.


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
