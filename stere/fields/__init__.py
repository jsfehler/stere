from stere import Stere

from .field import Field

__all = [
    'Field',
]

if Stere.library == 'splinter':
    from .splinter.button import Button
    from .splinter.checkbox import Checkbox
    from .splinter.dropdown import Dropdown
    from .splinter.input import Input
    from .splinter.link import Link
    from .splinter.root import Root
    from .splinter.text import Text

    desired_imports = [
        'Button',
        'Checkbox',
        'Dropdown',
        'Input',
        'Link',
        'Root',
        'Text',
    ]

else:
    desired_imports = []

__all__ = __all + desired_imports
