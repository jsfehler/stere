Pages
-----

The Page class is the base which all Page Objects should inherit from.

Although inheriting from Page is not required for Fields or Areas to work,
Page will act as a proxy for calls to the browser attribute.

Using Splinter's browser.url method as an example, the following methods are analogous:

.. code-block:: python

    MyPage.url == MyPage.browser.url == browser.url

The choice of which syntax to use depends on how you want to write your tests.
