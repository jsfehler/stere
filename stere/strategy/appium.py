import typing

from .element_strategy import ElementStrategy
from .strategy import strategy


class AppiumBase(ElementStrategy):
    def _find_all(self, wait_time: typing.Optional[int] = None):
        """Find from inside a parent element."""
        parent = self.parent_locator or self.browser
        func = getattr(
            parent, f'find_elements_by_{self.strategy}')
        return func(self.locator)


@strategy('accessibility_id')
class FindByAccessibilityId(AppiumBase):
    strategy = 'accessibility_id'


@strategy('android_uiautomator')
class FindByAndroidUIAutomator(AppiumBase):
    strategy = 'android_uiautomator'


@strategy('ios_class_chain')
class FindByIOSClassChain(AppiumBase):
    strategy = 'ios_class_chain'


@strategy('ios_predicate')
class FindByIOSUIPredicate(AppiumBase):
    strategy = 'ios_predicate'


@strategy('ios_uiautomation')
class FindByIOSUIAutomation(AppiumBase):
    strategy = 'ios_uiautomation'
