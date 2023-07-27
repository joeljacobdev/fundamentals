import inspect
import functools
import logging

logger = logging.getLogger(__name__)


def logging_decorator(cls):
    # we modify behaviour by dynamically creating subclasses. Parent class here is dynamic.
    class Wrapped(cls):
        def __init__(self, *args, **kwargs):
            logger.info(f'Before {type(cls)}.__init__ {args} {kwargs}')
            super().__init__(*args, **kwargs)
            logger.info(f'After {type(cls)}.__init__')

        def __call__(self, *args, **kwargs):
            logger.info(f"{type(cls)}.__call__")
            result = super().__call__(*args, **kwargs)
            return result

    return Wrapped


def rate_limiter(limit):
    """
    Decorator factory - it will return a decorator.
    As decorator can only take a class or a function.
    """

    def decorator(cls):
        class Wrapper(cls):
            def __init__(self, *args, **kwargs):
                self.rate = 0
                super().__init__(*args, **kwargs)
                for name, method in inspect.getmembers(cls, predicate=inspect.isfunction):
                    setattr(cls, name, self._rate_limit(method))

            def _rate_limit(self, method):
                @functools.wraps(method)
                def wrapper(*args, **kwargs):
                    if self.rate == limit:
                        raise Exception('Rate is limited')
                    self.rate += 1
                    return method(*args, **kwargs)

                return wrapper

        return Wrapper

    return decorator


@rate_limiter(limit=3)
@logging_decorator
class MyClass:
    def __init__(self, a, b=None):
        self.a = a
        logger.info('MyClass ', a, b, type(self))

    def __call__(self):
        logger.info("MyClass.__call__")
        return self.a


# Applying decorator is similar to
# MyClass = logging_decorator(MyClass)
# rate_limiter_decorator = rate_limiter(3)
# MyClass = rate_limiter_decorator(MyClass)
# a = MyClass(1,2)

a = MyClass(1, 2)
a()
a()
a()
# a()
