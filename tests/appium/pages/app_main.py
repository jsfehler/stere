from stere import Page
from stere.fields import (
    Button,
    Input,
    Text,
)


class AppMain(Page):
    """Represents the appium test page."""

    def __init__(self):
        self.build_gear = Button('accessibility_id', 'build_gear_button')
        self.number_of_gears = Text('accessibility_id', 'number_of_gears')
        self.build_robot_input = Input('accessibility_id', 'build_robot_input')
        self.build_robot = Button('accessibility_id', 'build_robot_button')
        self.number_of_robots = Text('accessibility_id', 'number_of_robots')
