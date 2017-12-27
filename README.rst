Stere
=====

A modular, Page Object oriented approach to browser based test automation.

The goal is to minimize the amount of implementation code visible in Page Objects and reduce
the need for helper methods.

It uses `Splinter <https://github.com/cobrateam/splinter>`_ under the hood.


Requirements
------------

Python >= 3.6


Basic Usage
-----------

A minimal Stere Page Object looks like this:

.. code-block:: python

    from stere.fields import Input

    class MyPage():
        def __init__(self):
            self.my_input = Input('xpath', '//my_xpath_string')


Fundementally, a Page Object is just a Python class.
Stere provides 2 types of objects to model a web page: Fields and Areas.

It can be called in a test like so:

.. code-block:: python

    def test_stuff():
        MyPage().my_input.fill('Hello world')

Documentation
-------------

`Field <docs/field.rst>`_

`Area <docs/area.rst>`_
