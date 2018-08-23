Pages
-----

.. autoclass:: stere.Page()

  .. automethod:: stere.Page.navigate()


Using Page as a Context Manager
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Page contains __enter__() and __exit__() methods. This allows any page
to be used as a Context Manager.

Example:

.. code-block:: python

    from pages import Home

    with Home() as p:
        p.login_button.click()
