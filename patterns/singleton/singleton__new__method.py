class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = object.__new__(cls, *args, **kwargs)
        return cls._instance


a = Singleton()
b = Singleton()

print(id(a), id(b))
# Cons
# - multiple inheritance - can be override
