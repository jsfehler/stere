Fields
------

The Field objects represent individual elements on a web page.
Conceptually, they represent general behaviours, not specific HTML elements.

The following Fields are available by default:

- Button: Clickable object.
- Dropdown: Object with a dropdown menu.
- Input: Object that accepts keyboard input.
- Link: Clickable text.
- Root: Parent container.
- Text: Non-interactive text.

Fields take 2 arguments: location strategy and locator.

.. code-block:: python

    self.some_text = Text('xpath', '//*[@id="js-link-box-pt"]/small/span')


Field.perform(value)
~~~~~~~~~~~~~~~~~~~~

Used by the Area class. When Area.perform() is called, it will trigger the .perform() methods of all its child Fields.

It should implement a standard action taken by the user. For example, Button.perform() will result in a click.

The base Field.perform() does nothing, but can be extended when creating a custom Field.

When creating a custom Field, implementations of .perform() must return a Boolean. If the Field's perform consumes an argument, it should return True. If not, False.


Field.includes(value)
~~~~~~~~~~~~~~~~~~~~~

Will search every element found by the Field for a value property that matches the given value.
If an element with a matching value is found, it's then returned.

Useful for when you have non-unique elements and know a value is in one of the elements, but don't know which one. 

.. code-block:: python

    PetStore().inventory_list.includes("Kittens").click()


Subclassing Field
~~~~~~~~~~~~~~~~~

Field can be subclassed to suit your own requirements.

If the __init__() method is overwritten, make sure to call super() before your own code.

If your class need specific behaviour when interacting with Areas, it must implement the perform() method.


Dropdown
--------

By default, the Dropdown field works against HTML Dropdowns.
However, it's possible to extend Dropdown to work with whatever implementation of a CSS Dropdown you need.

The `option` argument can be provided to override the default implementation.
This argument expects a Field. The Field should be the individual options in the dropdown you wish to target.

before_select()
~~~~~~~~~~~~~~~

This method is called automatically before the select() method.
If an action is required to prepare the dropdown for usage (such as hovering over a button to open it)
then this method can be overridden with the desired behaviour.

In this example, Dropdown has been subclassed to hover over the Dropdown before clicking.

.. code-block:: python

    from stere.fields import Dropdown

    class CSSDropdown(Dropdown):
        """A Dropdown that's customized to hover over the element before attempting
        a select.
        """
        def before_select(self):
            self.element.mouse_over()


Location Strategies
-------------------

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
