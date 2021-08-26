from functools import wraps
from typing import Any, Callable, Optional, Type, TypeVar, cast


T = TypeVar('T')
F = TypeVar('F', bound=Callable[..., Any])


def stere_performer(
    method_name: str,
    consumes_arg: bool = False,
) -> Callable[[Type[T]], Type[T]]:
    """Wrap a class to associate method_name with the perform() method.

    Associating a method with perform allows the class to be fully used
    by Area objects via Area.perform().

    Arguments:
        method_name (str): The name of the method to perform
        consumes_args (bool): True if the method takes an argument, else False

    In the following example, when ``Philosophers().diogenes_area.perform()``
    is called, ``DiogenesButton.philosophize()`` is called.

    Example:

        >>> @stere_performer('philosophize', consumes_arg=False)
        >>> class DiogenesButton(Field):
        >>>     def philosophize(self):
        >>>         print("As a matter of self-preservation, ")
        >>>         print("a man needs good friends or ardent enemies, ")
        >>>         print("for the former instruct him and the latter ")
        >>>         print("take him to task.")
        >>>
        >>>
        >>> class Philosophers(Page):
        >>>     def __init__(self):
        >>>         self.diogenes_area = Area(
        >>>             quote_button=DiogenesButton('id', 'idDio'),
        >>>             next_button=Button('id', 'idNext'),
        >>>         )
        >>>
        >>>
        >>> Philosophers().diogenes_area.perform()
    """
    def wrapper(cls: Type[T]) -> Type[T]:
        class Performer(cls):  # type: ignore
            def perform(self, value: Optional[Any] = None) -> Any:
                """Run the method designated as the performer"""
                performer = getattr(self, method_name)
                if consumes_arg:
                    performer(value)
                else:
                    performer()
                return self.returns

        # Preserve original class name and doc
        Performer.__name__ = cls.__name__
        Performer.__doc__ = cls.__doc__
        Performer.consumes_arg = consumes_arg
        return Performer
    return wrapper


def use_before(func: F) -> F:
    """When used on a method in a Field, the following will occur before
    the decorated method is called:
    - The Field's before() method will be called.
    - Any listeners registered to the 'before' event will be called.

    Example:

        >>> class TransformingButton(Field):
        >>>     def before(self):
        >>>         print('Autobots! Transform and...')
        >>>
        >>>     @use_before
        >>>     def roll_out(self):
        >>>         print('roll out!')
        >>>
        >>> tf = TransformingButton()
        >>> tf.roll_out()
        >>>
        >>> "Autobots! Transform and..."
        >>> "roll out!"
    """
    @wraps(func)
    def wrapper(cls: Type[T], *inner_args: Any, **inner_kwargs: Any) -> Any:
        cls.before()
        cls.emit('before')
        return func(cls, *inner_args, **inner_kwargs)
    return cast(F, wrapper)


def use_after(func: F) -> F:
    """When used on a method in a Field, the following will occur after
    the decorated method is called:
    - The Field's after() method will be called.
    - Any listeners registered to the 'after' event will be called.

    Example:

        >>> class TransformingButton(Field):
        >>>     def after(self):
        >>>         print('rise up!')
        >>>
        >>>     @use_after
        >>>     def transform_and(self):
        >>>         print('Decepticons, transform and...')
        >>>
        >>> tf = TransformingButton()
        >>> tf.transform_and()
        >>>
        >>> "Decepticons, transform and..."
        >>> "rise up!"
    """
    @wraps(func)
    def wrapper(cls: Type[T], *inner_args: Any, **inner_kwargs: Any) -> Any:
        result = func(cls, *inner_args, **inner_kwargs)
        cls.after()
        cls.emit('after')
        return result
    return cast(F, wrapper)
