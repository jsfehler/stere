Appium Integration
------------------

Stere contains Fields designed specifically for when Appium is connected.
Each implements a specific performer method.


Fields
~~~~~~

Button
++++++

.. class:: stere.fields.Button()

  Convenience Class on top of Field, it implements `click()` as its performer.

  .. automethod:: stere.fields.appium.button.Button.click()


Input
+++++

.. class:: stere.fields.Input()

  A simple wrapper over Field, it implements `send_keys()` as its performer.

  .. automethod:: stere.fields.appium.input.Input.send_keys()

  Fills the element with value.


Locator Strategies
~~~~~~~~~~~~~~~~~~
.. _locator_strategies:

These represent the way a locator will be searched for.

By default, the strategies available are:

- accessibility_id
- android_uiautomator
- ios_class_chain
- ios_predicate
- ios_uiautomation

These strategies can be overridden with a custom strategy (ie: You can create a custom accessibility_id strategy with different behaviour).
