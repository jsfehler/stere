Network Request Spies
=====================

Network Request Spies inject hooks into the web browser to track activity.

The preferred usage is through the default instances on Page objects via the
following attributes:

  ``Page.fetch_spy``

  ``Page.xhr_spy``


.. autoclass:: stere.browser_spy.FetchSpy()

  .. automethod:: stere.browser_spy.FetchSpy.add()

  .. automethod:: stere.browser_spy.FetchSpy.wait_for_no_activity()

  .. autoattribute:: stere.browser_spy.FetchSpy.active()

  .. autoattribute:: stere.browser_spy.FetchSpy.total()


.. autoclass:: stere.browser_spy.XHRSpy()

  .. automethod:: stere.browser_spy.XHRSpy.add()

  .. automethod:: stere.browser_spy.XHRSpy.wait_for_no_activity()

  .. autoattribute:: stere.browser_spy.XHRSpy.active()

  .. autoattribute:: stere.browser_spy.XHRSpy.total()
