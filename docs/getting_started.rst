Getting Started
---------------


Requirements
============

Python >= 3.6


Installation
============

Stere is currently in a proof-of-concept stage and is not available on pypi.
It can be installed with pip using the following command:

.. code-block:: bash

  pip install git+git://github.com/jsfehler/stere.git#egg=stere


Setup
=====

Stere requires a browser (aka driver) to work with.
This can be any class that ultimately drives automation.
Pages, Fields, and Areas inherit their functionality from this object.

Here's an example with Splinter:

.. code-block:: python

  from stere import Stere
  from splinter import Browser

  Stere.browser = Browser()


As long as the base Stere object has the browser set, the browser's functionality is passed down to everything else.
