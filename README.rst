Stere
=====

A Page Object oriented approach to test automation.

Summary
-------

Stere is a DSL on top of your existing automation library.
No automation abilities are directly built into the project;
it relies on being hooked into other web automation libraries.

The goals of this project are to:

1 - Minimize the amount of implementation code visible in test functions and
Page Objects.

2 - Reduce the need for hand-written helper methods.

3 - Provide a useful syntax for writing maintainable Page Objects.

Out of the box, Stere provides an implementation for
`Splinter <https://github.com/cobrateam/splinter>`_.


Requirements
------------

Python >= 3.6


Basic Usage
-----------

Fundementally, a Page Object is just a Python class.

A minimal Stere Page Object should subclass the Page class:

.. code-block:: python

    from stere import Page
    from stere.fields import Input

    class MyPage(Page):
        def __init__(self):
            self.my_input = Input('xpath', '//my_xpath_string')


There are 2 types of objects to model a web page: Fields and Areas.
Fields represent single web elements, Areas represent groups of elements.

A Page Object's fields can be called in a test function like so:

.. code-block:: python

    def test_stuff():
        MyPage().my_input.fill('Hello world')

Documentation
-------------

`Page <docs/page.rst>`_

`Field <docs/field.rst>`_

`Area <docs/area.rst>`_
