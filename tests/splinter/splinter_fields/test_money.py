from moneyed import Money


def test_money_money_type(test_page):
    """Given I have a field with money in it
    When I call the money method of the field
    Then the object returns is a Money object
    """
    test_page.navigate()
    m = test_page.money_field.money()
    assert isinstance(m, Money)


def test_money_number(test_page):
    """Given I have a field with money in it
    When I call the number attribute of the field
    Then the text in the field is normalized to a number
    """
    test_page.navigate()
    m = test_page.money_field.number
    assert m == '9001'
