import logging

from selenium.webdriver.remote.remote_connection import LOGGER


LOGGER.setLevel(logging.WARNING)


def test_is_visible(test_page):
    """When I wait for something to be visible on the page
    Then is_visible() returns True if it becomes visible.
    """
    test_page.navigate()
    assert test_page.added_container_by_id.is_visible(wait_time=10)


def test_is_visible_by_xpath(test_page):
    test_page.navigate()
    assert test_page.added_container_by_xpath.is_visible(wait_time=10)


def test_is_visible_by_css(test_page):
    test_page.navigate()
    assert test_page.added_container_by_css.is_visible(wait_time=10)


def test_is_not_visible(test_page):
    test_page.navigate()
    assert test_page.to_hide_container_by_id.is_not_visible(wait_time=12)


def test_is_not_visible_by_xpath(test_page):
    test_page.navigate()
    assert test_page.to_hide_container_by_xpath.is_not_visible(wait_time=12)


def test_is_not_visible_by_css(test_page):
    test_page.navigate()
    assert test_page.to_hide_container_by_css.is_not_visible(wait_time=12)


def test_is_visible_fails(test_page):
    """When I check if something is visible when it is not,
    Then it should not be found
    """
    test_page.navigate()
    assert not test_page.added_container_by_id.is_visible(wait_time=1)


def test_is_not_visible_fails(test_page):
    """When I check if something is not visible when it is,
    Then it should be found
    """
    test_page.navigate()
    assert not test_page.removed_container_by_id.is_not_visible(wait_time=1)


def test_is_present_args(test_page):
    """
    When I send an argument to is_present
    Then it is used by the correct function
    """
    test_page.navigate()
    assert test_page.added_container_by_id.is_present(wait_time=12)


def test_is_present_repeating_area(test_page):
    """
    Given I have a Field inside a RepeatingArea
    When I send an argument to is_present
    Then it is used by the correct function
    """
    test_page.navigate()
    assert test_page.repeating_area.areas[0].link.is_present()


def test_is_not_present_args(test_page):
    """
    When I send an argument to is_not_present
    Then it is used by the correct function
    """
    test_page.navigate()
    assert test_page.removed_container_by_id.is_not_present(wait_time=12)


def test_button_data_star_strategy(browser, request, browser_name, test_page):
    """When I define a Field using a data-* strategy, it is found."""
    test_page.navigate()
    test_page.button_alt_strategy.click()

    # Clicking changes the button's container background colour
    browsers = {
        'firefox': 'rgb(255, 0, 0)',
        'chrome': 'rgba(255, 0, 0, 1)',
    }

    # This works because value_of_css_property is gotten from splinter,
    # which gets it from Selenium
    actual = test_page.button_container.find()._element.value_of_css_property(
        'background-color')

    assert browsers[browser_name] == actual


def test_data_star_staregy_is_present(browser, test_page):
    test_page.navigate()
    assert test_page.button_alt_strategy.is_present(wait_time=3)


def test_data_star_staregy_is_not_present(browser, test_page):
    test_page.navigate()
    assert test_page.missing_button.is_not_present(wait_time=3)


def test_is_clickable(test_page):
    """
    When I wait for something to be click on the page
    Then is_clickable() returns True if it becomes visible.
    """
    test_page.navigate()
    assert test_page.button.is_clickable(wait_time=1)


def test_is_clickable_element_not_found(test_page):
    """
    When I wait for something to be click on the page
    Then is_clickable() returns True if it becomes visible.
    """
    test_page.navigate()
    assert not test_page.missing_button.is_clickable(wait_time=1)


def test_is_not_clickable(test_page):
    """
    When I wait for something to be click on the page
    Then is_clickable() returns True if it becomes visible.
    """
    test_page.navigate()
    assert test_page.missing_button.is_not_clickable(wait_time=1)


def test_is_not_clickable_element_found(test_page):
    """
    When I wait for something to be click on the page
    Then is_clickable() returns True if it becomes visible.
    """
    test_page.navigate()
    assert not test_page.button.is_not_clickable(wait_time=1)
