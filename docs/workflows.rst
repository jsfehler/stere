Workflows
=========

When working with an Area that has multiple possible routes, there may be Fields which you do not want
the .perform() method to call under certain circumstances.

Take the following example Page Object:

.. code-block:: python

    class AddSomething(Page):
        def __init__(self):
            self.form = Area(
                item_name=Input('id', 'itemName'),
                item_quantity=Input('id', 'itemQty'),
                save=Button('id', 'saveButton'),
                cancel=Button('id', 'cancelButton')
            )

Calling `AddSomething().form.perform()` would cause the save button and then the cancel button to be acted on.

In these sorts of cases, Workflows can be used to manage which Fields are called.

.. code-block:: python

    class AddSomething(Page):
        def __init__(self):
            self.form = Area(
                item_name=Input('id', 'itemName', workflows=["success", "failure"]),
                item_quantity=Input('id', 'itemQty', workflows=["success", "failure"]),
                save=Button('id', 'saveButton', workflows=["success"]),
                cancel=Button('id', 'cancelButton', workflows=["failure"])
            )


Calling `AddSomething().form.workflow("success").perform()` will ensure that only Fields with a matching workflow are called.
