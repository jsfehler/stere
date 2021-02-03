Stere
=====


.. image:: https://img.shields.io/pypi/v/stere.svg
    :target: https://pypi.org/project/stere
    :alt: PyPI

.. image:: https://img.shields.io/pypi/pyversions/stere.svg
    :alt: PyPI - Python Version
    :target: https://github.com/jsfehler/stere

.. image:: https://img.shields.io/github/license/jsfehler/stere.svg
    :alt: GitHub
    :target: https://github.com/jsfehler/stere/blob/master/LICENSE

.. image:: https://pyup.io/repos/github/jsfehler/stere/shield.svg
    :target: https://pyup.io/repos/github/jsfehler/stere
    :alt: Updates

.. image:: https://github.com/jsfehler/stere/workflows/CI/badge.svg
    :alt: Build status

.. image:: https://coveralls.io/repos/github/jsfehler/stere/badge.svg?branch=master
    :target: https://coveralls.io/github/jsfehler/stere?branch=master

.. image:: https://api.codacy.com/project/badge/Grade/e791ab09e14c4483943a26a2fd180577
    :target: https://www.codacy.com/app/joshua-fehler_2/stere?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=jsfehler/stere&amp;utm_campaign=Badge_Grade

.. image:: https://saucelabs.com/buildstatus/jsfehler
    :target: https://saucelabs.com/u/jsfehler

Stere is a library for writing Page Objects, designed to work on top of an existing automation library.


Design Philosophy
-----------------

Many implementations of the Page Object model focus on removing the duplication of element locators inside tests.
Stere goes one step further, offering a complete wrapper over the code that drives automation.

The goals of this project are to:

1 - Eliminate implementation code in test functions. Tests should read like a description of behaviour, not Selenium commands.

2 - Reduce the need for hand-written helper methods in Page Objects. Common actions should have universal solutions.

3 - Provide a simple pattern for writing maintainable Page Objects.

No automation abilities are built directly into the project; it completely relies on being hooked into other libraries.
However, implementations using `Splinter <https://github.com/cobrateam/splinter>`_ and `Appium <https://github.com/appium/appium>`_ are available out of the box.


Documentation
-------------

https://stere.readthedocs.io/en/latest/


Basic Usage
-----------

Fundamentally, a Page Object is just a Python class.

A minimal Stere Page Object should:

1 - Subclass the Page class

2 - Declare Fields and Areas in the __init__ method

As an example, here's the home page for Wikipedia:

.. code-block:: python

    from stere import Page
    from stere.areas import Area, RepeatingArea
    from stere.fields import Button, Input, Link, Root, Text


    class WikipediaHome(Page):
        def __init__(self):
            self.search_form = Area(
                query=Input('id', 'searchInput'),
                submit=Button('xpath', '//*[@id="search-form"]/fieldset/button')
            )

            self.other_projects = RepeatingArea(
                root=Root('xpath', '//*[@class="other-project"]'),
                title=Link('xpath', '//*[@class="other-project-title"]'),
                tagline=Text('xpath', '//*[@class="other-project-tagline"]')
            )

The search form is represented as an `Area <https://stere.readthedocs.io/en/latest/area.html>`_ with two `Fields <https://stere.readthedocs.io/en/latest/field.html>`_ inside it.

A Field represents a single item, while an Area represents a unique collection of Fields.

The query and submit Fields didn't have to be placed inside an Area.
However, doing so allows you to use Area's `perform() <https://stere.readthedocs.io/en/latest/area.html#stere.areas.Area.perform>`_ method.

The links to other products are represented as a `RepeatingArea <https://stere.readthedocs.io/en/latest/area.html#stere.areas.RepeatingArea>`_ .
A RepeatingArea represents a non-unique collection of Fields on the page.
Using the root argument as the non-unique selector, RepeatingArea will find all instances of said root,
then build the appropriate number of Areas with all the other Fields inside.

It's just as valid to declare each of the other products as a separate Area
one at a time, like so:

.. code-block:: python

    self.commons = Area(
        root=Root('xpath', '//*[@class="other-project"][1]'),
        title=Link('xpath', '//*[@class="other-project-title"]'),
        tagline=Text('xpath', '//*[@class="other-project-tagline"]')
    )

    self.wikivoyage = Area(
        root=Root('xpath', '//*[@class="other-project"][2]'),
        title=Link('xpath', '//*[@class="other-project-title"]'),
        tagline=Text('xpath', '//*[@class="other-project-tagline"]')
    )

Which style you pick depends entirely on how you want to model the page.
RepeatingArea does the most good with collections where the number of areas and/or the contents of the areas
can't be predicted, such as inventory lists.

Using a Page Object in a test can be done like so:

.. code-block:: python

    def test_search_wikipedia():
        home = WikipediaHome()
        home.search_form.perform('kittens')


License
-------

Distributed under the terms of the `MIT`_ license, "Stere" is free and open source software


Issues
------

If you encounter any problems, please `file an issue`_ along with a detailed description.


Thanks
------

Cross-browser Testing Platform and Open Source <3 Provided by `Sauce Labs`_


.. _`file an issue`: https://github.com/jsfehler/stere/issues
.. _`MIT`: http://opensource.org/licenses/MIT
.. _`Sauce labs`: https://saucelabs.com
