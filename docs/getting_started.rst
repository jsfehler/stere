Getting Started
---------------


Requirements
============

Python >= 3.6


Installation
============

Stere can be installed with pip using the following command:

.. code-block:: bash

    pip install stere


Setup
=====

Stere.browser
~~~~~~~~~~~~~

Stere requires a browser (aka driver) to work with.
This can be any class that ultimately drives automation.
Pages, Fields, and Areas inherit their functionality from this object.

Here's an example with Splinter:

.. code-block:: python

    from stere import Stere
    from splinter import Browser

    Stere.browser = Browser()


As long as the base Stere object has the browser set, the browser's functionality is passed down to everything else.

Stere.url_navigator
~~~~~~~~~~~~~~~~~~~

Optionally, an attribute called `url_navigator` can be provided a string that maps to the method in the browser that opens a page.

In Splinter's case, this is the `visit` method.

.. code-block:: python

    from stere import Stere
    from splinter import Browser

    Stere.browser = Browser()
    Stere.url_navigator = 'visit'

This attribute is used by the `Page` class to make url navigation easier.
