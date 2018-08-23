from .splinter_strategies import FindByCss
from .splinter_strategies import FindById
from .splinter_strategies import FindByName
from .splinter_strategies import FindByTag
from .splinter_strategies import FindByText
from .splinter_strategies import FindByValue
from .splinter_strategies import FindByXPath
from .splinter_strategies import add_data_star_strategy
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
