strategies = {}


def strategy(strategy_name):
    """Decorator that registers a strategy name and
    strategy Class.

    Strategy Classes are used to build Elements Objects.

    Args:
        strategy_name (str): Name of the strategy to be registered.
    """
    def wrapper(finder_class):
        global strategies
        strategies[strategy_name] = finder_class
        return finder_class
    return wrapper
