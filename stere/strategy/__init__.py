from stere import Stere

from .strategy import strategies
from .strategy import strategy


__all__ = [
    'strategy',
    'strategies',
]

if Stere.library == 'appium':
    from .appium import FindByAccessibilityId
    from .appium import FindByAndroidUIAutomator
    from .appium import FindByIOSClassChain
    from .appium import FindByIOSUIPredicate
    from .appium import FindByIOSUIAutomation

    __all__ += [
        'FindByAccessibilityId',
        'FindByAndroidUIAutomator',
        'FindByIOSClassChain',
        'FindByIOSUIPredicate',
        'FindByIOSUIAutomation',
    ]

elif Stere.library == 'splinter':
    from .splinter import FindByCss
    from .splinter import FindById
    from .splinter import FindByName
    from .splinter import FindByTag
    from .splinter import FindByText
    from .splinter import FindByValue
    from .splinter import FindByXPath
    from .splinter import add_data_star_strategy

    __all__ += [
        'FindByCss',
        'FindByXPath',
        'FindByTag',
        'FindByName',
        'FindByText',
        'FindById',
        'FindByValue',
        'add_data_star_strategy',
    ]
