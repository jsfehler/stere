from functools import wraps


def stere_performer(method_name, consumes_arg=False):
    """Wraps a Class that contains a method which should be
    used by Area.perform().
    """
    def wrapper(cls):
        class Performer(cls):
            def perform(self, value=None):
                """Run the method designated as the performer"""
                performer = getattr(self, method_name)
                if consumes_arg:
                    performer(value)
                else:
                    performer()
                return self.returns

        # Preserve original class name
        Performer.__name__ = cls.__name__
        Performer.consumes_arg = consumes_arg
        return Performer
    return wrapper


def use_before(func, *args, **kwargs):
    """When added to a method in a Field, the Field's before() method will be
    called before the decorated method is called.

    Example:

    class TransformingButton(Field):
        def before(self):
            print('Autobots! Transform and...')

        @use_before
        def roll_out(self):
            print('roll out!')

    """
    @wraps(func)
    def wrapper(obj, *inner_args, **inner_kwargs):
        obj.before()
        return func(obj, *inner_args, **inner_kwargs)
    return wrapper


def use_after(func, *args, **kwargs):
    """When added to a method in a Field, the Field's after() method will be
    called after the decorated method is called.

    Example:

    class TransformingButton(Field):
        def after(self):
            print('roll out!')

        @use_after
        def autobots(self):
            print('Autobots! Transform and...')

    """
    @wraps(func)
    def wrapper(obj, *inner_args, **inner_kwargs):
        result = func(obj, *inner_args, **inner_kwargs)
        obj.after()
        return result
    return wrapper
