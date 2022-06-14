def test_shadow_root_find_all(test_page):
    """When I find the shadow root of an element
    Then the elements in the shadow root can be found.
    """
    test_page.navigate()
    assert test_page.shadow_root_area.data.value == 'Inside a shadow root'
