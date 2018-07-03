Best Practices
==============

A highly opinionated guide. Ignore at your own peril.

Favour composition over inheritance
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

When building Page Objects for something with many
reused pieces (such as a settings menu) don't build an abstract base Page Object. Build each component separately
and call them in Page Objects that reflect the application.

**Inheritance:**

.. code-block:: python

    class BaseSettings(Page):
        def __init__(self):
            self.menu = Area(...)


    class SpecificSettings(BaseSettings):
        def __init__(self):
          super()


**Composition:**

.. code-block:: python

    from .another_module import settings_menu

    class SpecificSettings(Page):
        def __init__(self):
            self.menu = settings_menu


**Explanation:**

Doing so maintains the benefits of reusing code,
but prevents the creation of Page Objects that don't reflect actual pages in an application.

Creating abstract Page Objects to inherit from can make it confusing as to what Fields are available on a page.


Single blank line when changing page object
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Wrong:**

.. code-block:: python

  def test_the_widgets():
      Knicknacks.menu.gadgets.click()
      Knicknacks.gadgets.click()
      Gadgets.add_widgets.click()

      Gadgets.add_sprocket.click()


**Right:**

.. code-block:: python

  def test_the_widgets():
      Knicknacks.menu.gadgets.click()
      Knicknacks.gadgets.click()

      Gadgets.add_widgets.click()
      Gadgets.add_sprocket.click()


**Explanation:**

Changing pages usually indicates a navigation action.
Using a consistent line break style visually helps to indicate the steps of a test.
