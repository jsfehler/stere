from stere import Stere

from .field import Field
from .generic.root import Root
from .generic.text import Text

__all = [
    'Field',
    'Root',
    'Text',
]

if Stere.library == 'splinter':
    from .splinter.button import Button
    from .splinter.checkbox import Checkbox
    from .splinter.dropdown import Dropdown
    from .splinter.input import Input
    from .splinter.link import Link

    desired_imports = [
        'Button',
        'Checkbox',
        'Dropdown',
        'Input',
        'Link',
    ]

else:
    desired_imports = []

__all__ = __all + desired_imports
