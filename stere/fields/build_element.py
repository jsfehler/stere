from stere.strategy import strategies


def build_element(desired_strategy: str, locator: str, parent_locator=None):
    """Get an element strategy instance."""
    known = strategies.keys()

    if desired_strategy in known:
        element_class = strategies[desired_strategy]
        return element_class(desired_strategy, locator, parent_locator)

    raise ValueError(
        f'The strategy "{desired_strategy}" is not in {list(known)}.')
