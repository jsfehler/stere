strategies = {}


def strategy(strategy_name: str):
    """Register a strategy name and strategy Class.

    Use as a decorator.

    Example:
        @strategy('id')
        class FindById:
            ...

    Strategy Classes are used to build Elements Objects.

    Arguments:
        strategy_name (str): Name of the strategy to be registered.
    """
    def wrapper(finder_class):
        global strategies
        strategies[strategy_name] = finder_class
        return finder_class
    return wrapper
