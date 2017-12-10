Stere
=====

A modular, Page Object oriented approach to browser based test automation.

The goal is to minimize the amount of implementation code visible in Page Objects and reduce
the need for helper methods.

It uses `Splinter <https://github.com/cobrateam/splinter>`_ under the hood.


Requirements
------------

Python >= 3.6


A Brief Introduction to Page Objects
------------------------------------

Page Objects are a common pattern for modelling a web page.
Element locators for a web page are mapped to variables instead of written over and over again in a test.
This reduces the amount of maintenance necessary to keep tests running.


Basic Usage
-----------

A minimal Stere Page Object looks like this:

.. code-block:: python

    from stere.fields import Input

    class MyPage():
        def __init__(self):
            self.my_input=Input('xpath', '//my_xpath_string')


Fundementally, a Page Object is just a Python class.
Stere provides 2 types of objects to model a web page: Fields and Areas.

It could be called in a test like so:

.. code-block:: python

    def test_stuff():
        MyPage().my_input.fill('Hello world')

  
Fields
------

Fields represent individual objects on a web page.
They model general behaviours, not specific HTML elements.

The following Fields are available:

- Button: Clickable object.
- Input: Object that accepts keyboard input.
- Link: Clickable text.
- Root: Parent container.
- Text: Non-interactive text.

Fields take 2 arguments: strategy and locator.

Areas
-----

Areas represent sections on a page.

The following Areas are available:

- Area: A non-hierarchical, unique group of Fields.
- RepeatingArea: A hierarchical, non-unique group of Fields. They require a Root Field.

Areas take any number of Fields as arguments.

