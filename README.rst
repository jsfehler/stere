Stere
=====

Stere is a DSL for writing Page Objects, designed to work on top of your existing automation library.
No automation abilities are built directly into the project;
it relies on being hooked into other libraries.

The goals of this project are to:

1 - Minimize the amount of implementation code visible in test functions and
Page Objects.

2 - Reduce the need for hand-written helper methods.

3 - Provide a useful syntax for writing maintainable Page Objects.

Although it's designed to work with any library, a default implementation using `Splinter <https://github.com/cobrateam/splinter>`_ is available out of the box.


Requirements
------------

Python >= 3.6


Installation
--------------

Stere is currently in a proof-of-concept stage and is not available on pypi.
It can be installed with pip using the following command: 

.. code-block:: bash

  pip install git+git://github.com/jsfehler/stere.git#egg=stere


Setup
--------

Stere requires a browser (aka driver) to work with.
This can be any class that ultimately drives automation.
Pages and Fields inherit their functionality from this browser. 

Here's an example with Splinter:

.. code-block:: python
  
  from stere import Stere
  from splinter import Browser

  Stere.browser = Browser()


As long as the base Stere object has the browser set, the browser's functionality is passed down to everything else.


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

    def test_all_the_things():
        MyPage().my_input.fill('Hello world')

Documentation
-------------

`Page <docs/page.rst>`_

`Field <docs/field.rst>`_

`Area <docs/area.rst>`_
