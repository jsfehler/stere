def test_button(test_app_main_page):
    """When I click a button to add a gear,
    Then a gear is added
    """
    test_app_main_page.build_gear.click()

    number_of_gears = test_app_main_page.number_of_gears

    assert "Number of Gears: 1" == number_of_gears.text


def test_input(test_app_main_page):
    """Given I have 10 gears
    When I try to build 1 robot
    Then the robot is built
    """
    for _ in range(10):
        test_app_main_page.build_gear.click()

    test_app_main_page.build_robot_input.send_keys('1')

    test_app_main_page.build_robot.click()

    assert 'Number of Robots: 1' == test_app_main_page.number_of_robots.text
