Pages
-----

The Page class is the base which all Page Objects should inherit from.

Although inheriting from Page is not required for Fields or Areas to work,
Page will act as a proxy for calls to the browser attribute.

Using Splinter's browser.url method as an example, the following methods are analogous:

.. code-block:: python

    MyPage.url == MyPage.browser.url == browser.url

The choice of which syntax to use depends on how you want to write your tests.


Page.navigate()
~~~~~~~~~~~~~~~

When the base Stere object has been given the `url_navigator` attribute, and
a Page Object has a `page_url` attribute, the `navigate()` method can be called.

This method will call the method defined in `url_navigator`, with `page_url`
as the first parameter.

In the following example, Stere is initialized with Splinter.

.. code-block:: python

    from splinter import Browser
    from stere import Page


    class Home(Page):
        def __init__(self):
            self.page_url = 'https://en.wikipedia.org/'


    Stere.browser = Browser()
    Stere.url_navigator = 'visit'

    home_page = Home()
    home_page.navigate()
