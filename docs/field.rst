Fields
------

Fields represent individual objects on a web page.
They model general behaviours, not specific HTML elements.

The following Fields are available:

- Button: Clickable object.
- Dropdown: Object with a dropdown menu.
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

Dropdown
--------

By default, the Dropdown field works against HTML Dropdowns.
However, it's possible to extend Dropdown to work with whatever implementation of a CSS Dropdown you need.

The `option` argument can be provided to override the default implementation.
This argument expects a Field. The Field should be the individual options in the dropdown you wish to target.

before_select()
~~~~~~~~~~~~~~~

This method is called automatically before the select() method.
If an action is required to prepare the dropdown for usage (such as clicking to open it)
then this method can be overridden with the desired behaviour.


Custom Locator Strategies
-------------------------

Aside from the standard strategies, custom ones can be defined using the `@strategy` decorator.

Any class can be decorated with @strategy, as long as the _find_all and _find_all_in_parent methods are implemented.

In the following example, the 'data-test-id' strategy is defined.
It wraps Splinter's find_by_xpath method to simplify the locator required on the Page Object.


.. code-block:: python

    from stere.strategy import strategy


    @strategy('data-test-id')
    class FindByDataTestId():
        def _find_all(self):
            """Find from page root."""
            return self.browser.find_by_xpath(f'.//*[@data-test-id="{self.locator}"]')

        def _find_all_in_parent(self):
            """Find from inside parent element."""
            return self.parent_locator.find_by_xpath(f'.//*[@data-test-id="{self.locator}"]')


With this implemented, Fields can now be defined like so:

.. code-block:: python

    my_button = Button('data-test-id', 'MyButton')
