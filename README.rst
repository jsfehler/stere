Stere
=====

.. image:: https://pyup.io/repos/github/jsfehler/stere/shield.svg
     :target: https://pyup.io/repos/github/jsfehler/stere/
     :alt: Updates

.. image:: https://travis-ci.org/jsfehler/stere.svg?branch=master
    :target: https://travis-ci.org/jsfehler/stere

.. image:: https://coveralls.io/repos/github/jsfehler/stere/badge.svg?branch=master
    :target: https://coveralls.io/github/jsfehler/stere?branch=master

.. image:: https://api.codacy.com/project/badge/Grade/e791ab09e14c4483943a26a2fd180577
    :target: https://www.codacy.com/app/joshua-fehler_2/stere?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=jsfehler/stere&amp;utm_campaign=Badge_Grade

.. image:: https://saucelabs.com/buildstatus/jsfehler
    :target: https://saucelabs.com/u/jsfehler

Stere is a library for writing Page Objects, designed to work on top of your existing automation library.

Design Philosophy
-----------------

Many implementations of the Page Object model focus on removing the duplication of element locators.
Stere goes one step further, offering a complete wrapper over the code that drives automation.

The goals of this project are to:

1 - Eliminate implementation code in test functions. Tests should read like a set of user actions.

2 - Reduce the need for hand-written helper methods in Page Objects.

3 - Provide a simple pattern for writing maintainable Page Objects.

No automation abilities are built directly into the project; it completely relies on being hooked into other libraries.
However, a default implementation using `Splinter <https://github.com/cobrateam/splinter>`_ is available out of the box.


Basic Usage
-----------

Fundementally, a Page Object is just a Python class.

A minimal Stere Page Object should:

1 - Subclass the Page class

2 - Declare Fields and Areas in the __init__ method

As an example, here's the home page for Wikipedia:

.. code-block:: python

    from stere import Page
    from stere.areas import Area, RepeatingArea
    from stere.fields import Button, Input, Link, Text

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

The search form is represented as an Area with 2 Fields inside it.
An Area represents a unique collection of Fields on the page.

The search query and submit button didn't have to be placed inside an Area.
However, doing so allows you to use Area's perform() method.

The links to other products are represented as a RepeatingArea.
A RepeatingArea represents a non-unique collection of Fields on the page.
Using the root argument, RepeatingArea will find all instances of said root,
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
RepeatingArea does the most good with collections where the number of areas
can't be predicted, such as inventory lists.

Using a Page Object in a test can be done like so:

.. code-block:: python

    def test_search_wikipedia():
        WikipediaHome().search_form.perform('kittens')

Documentation
-------------

https://stere.readthedocs.io/en/latest/
