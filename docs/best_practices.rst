Best Practices
==============

A highly opinionated guide. Ignore at your own peril.

Favour adding methods to Fields and Areas over Page Objects
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If a new method is acting on a specific Field, subclass the Field and add the
method there instead of adding the method to the Page Object.


**Wrong:**

.. code-block:: python

    class Inventory(Page):
        def __init__(self):
            self.medals = Field('id', 'medals')

        def count_the_medals(self):
            return len(self.medals.find())


    def test_you_got_the_medals():
        inventory = Inventory()
        assert 3 == inventory.count_the_medals()


**Right:**

.. code-block:: python

    class Medals(Field):
        def count(self):
            return len(self.find())


    class Inventory(Page):
        def __init__(self):
            self.medals = Medals('id', 'medals')


    def test_you_got_the_medals():
        inventory = Inventory()
        assert 3 == inventory.medals.count()


**Explanation:**

Even if a Field or Area initially appears on only one page, subclassing will
lead to code that is more easily reused and/or moved.

In this example, inventory.count_the_medals() may look easier to read than
inventory.medals.count(). However, creating methods with long names and
specific verbiage makes your Page Objects less predictable and more prone to
inconsistency.


Favour page composition over inheritance
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

When building Page Objects for something with many reused pieces
(such as a settings menu) don't build an abstract base Page Object.
Build each component separately and call them in Page Objects that reflect the application.

**Inheritance:**

.. code-block:: python

    class BaseSettings(Page):
        def __init__(self):
            self.settings_menu = Area(...)


    class SpecificSettings(BaseSettings):
        def __init__(self):
            super().__init__()


**Composition:**

.. code-block:: python

    from .another_module import settings_menu

    class SpecificSettings(Page):
        def __init__(self):
            self.menu = settings_menu


**Explanation:**

Doing so maintains the benefits of reusing code, but prevents the creation of
Page Objects that don't reflect actual pages in an application.

Creating abstract Page Objects to inherit from can make it confusing as to
what Fields are available on a page.


Single blank line when changing page object
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Wrong:**

.. code-block:: python

  def test_the_widgets():
      knicknacks = Knicknacks()
      knicknacks.menu.gadgets.click()
      knicknacks.gadgets.click()
      gadgets = Gadgets()
      gadgets.navigate()

      gadgets.add_widgets.click()
      gadgets.add_sprocket.click()


**Right:**

.. code-block:: python

  def test_the_widgets():
      knicknacks = Knicknacks()
      knicknacks.menu.gadgets.click()
      knicknacks.gadgets.click()

      gadgets = Gadgets()
      gadgets.navigate()
      gadgets.add_widgets.click()
      gadgets.add_sprocket.click()


**Explanation:**

Changing pages usually indicates a navigation action.
Using a consistent line break style visually helps to indicate the steps of a test.
