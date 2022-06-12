from stere.fields import Field


def test_field_repr():
    """Fields should have a useful __repr__ method."""
    field = Field('id', 'foobar')

    assert "Field - Strategy: id, Locator: foobar" == str(field)


def test_field_empty_perform():
    """The default implementation of Field.perform() should return None."""
    f = Field('id', 'foobar')
    assert f.perform() is None


def test_call():
    """When a Field instance is called
    Then the Field's perform method is executed
    """
    f = Field('id', 'foobar')
    assert f() is None
