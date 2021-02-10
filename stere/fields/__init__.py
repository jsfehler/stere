from stere import Stere

from .field import Field
from .generic.root import Root
from .generic.text import Text

__all__ = [
    'Field',
    'Root',
    'Text',
]

if Stere.library == 'appium':
    from .appium.button import Button
    from .appium.input import Input

    __all__ += [
        'Button',
        'Input',
    ]

elif Stere.library == 'splinter':
    from .splinter.button import Button
    from .splinter.checkbox import Checkbox
    from .splinter.dropdown import Dropdown
    from .splinter.input import Input
    from .splinter.link import Link
    from .splinter.money import Money
    from .splinter.shadow_root import ShadowRoot

    __all__ += [
        'Button',
        'Checkbox',
        'Dropdown',
        'Input',
        'Link',
        'Money',
        'ShadowRoot',
    ]
