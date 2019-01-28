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

Specifying the automation library
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Using a `stere.ini` file, the automation library used can be specified.
This determines which library specific Fields are loaded.

While only Splinter and Appium have custom Fields to take advantage of their
specific capabilities, any automation library that implements an API similar to
Selenium should be possible to connect to Stere.

`splinter` is used by default, and `appium` is supported.
Any other value will be accepted, which will result in no specific Fields
being loaded.


.. code-block:: ini

  [stere]
  library = appium


Stere.browser
~~~~~~~~~~~~~

Stere requires a browser (aka driver) to work with.
This can be any class that ultimately drives automation.
Pages, Fields, and Areas inherit their functionality from this object.

Here's an example with `Splinter <https://github.com/cobrateam/splinter>`_:

.. code-block:: python

    from stere import Stere
    from splinter import Browser

    Stere.browser = Browser()


As long as the base Stere object has the browser set, the browser's
functionality is passed down to everything else.

Stere.url_navigator
~~~~~~~~~~~~~~~~~~~

Optionally, an attribute called `url_navigator` can be provided a string that
maps to the method in the browser that opens a page.

In Splinter's case, this is the `visit` method.

.. code-block:: python

    from stere import Stere
    from splinter import Browser

    Stere.browser = Browser()
    Stere.url_navigator = 'visit'

This attribute is used by the `Page` class to make url navigation easier.
