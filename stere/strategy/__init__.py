from .splinter import FindByCss
from .splinter import FindById
from .splinter import FindByName
from .splinter import FindByTag
from .splinter import FindByText
from .splinter import FindByValue
from .splinter import FindByXPath
from .splinter import add_data_star_strategy
from .strategy import strategies
from .strategy import strategy


__all__ = [
    'strategy',
    'strategies',
    'FindByCss',
    'FindByXPath',
    'FindByTag',
    'FindByName',
    'FindByText',
    'FindById',
    'FindByValue',
    'add_data_star_strategy',
]
