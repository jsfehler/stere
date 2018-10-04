Appium Fields
~~~~~~~~~~~~~~~

The following Fields are available with the default Appium implementation.
Each implements a specific performer method.

- :ref:`Button <button>`: Clickable object.
- :ref:`Input <input>`: Object that accepts keyboard input.


.. _button:
.. class:: stere.fields.Button()

  Convenience Class on top of Field, it implements `click()` as its performer.

  .. automethod:: stere.fields.Button.click()


.. _input:
.. class:: stere.fields.Input()

  A simple wrapper over Field, it implements `send_keys()` as its performer.

  .. automethod:: stere.fields.Input.send_keys()

  Fills the element with value.


Location Strategies
-------------------
.. _location_strategies:

These represent the way a locator will be searched for.

By default, the strategies available are:

- accessibility_id
- android_uiautomator
- ios_class_chain
- ios_predicate
- ios_uiautomation

These strategies can be overridden with a custom strategy (ie: You can create a custom accessibility_id strategy with different behaviour).
