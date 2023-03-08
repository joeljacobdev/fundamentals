class SingletonMeta(type):
    """
    The Singleton class can be implemented in different ways in Python. Some
    possible methods include: base class, decorator, metaclass. We will use the
    metaclass because it is best suited for this purpose.
    """

    # It will store key as class and class instance as value
    _instances = {}

    def __call__(cls, *args, **kwargs):
        """
        Possible changes to the value of the `__init__` argument do not affect
        the returned instance.
        """
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Singleton1(metaclass=SingletonMeta):
    value = 1

    def __str__(self):
        return f'Singleton1 __str__ {self.value}'

    def method1(self):
        return u'singleton 1 method 1'


class Singleton2(metaclass=SingletonMeta):
    value = 2

    def __str__(self):
        return f'Singleton2 __str__ {self.value}'

    def method1(self):
        return u'singleton 2 method 1'


a = Singleton1()
b = Singleton1()
c = Singleton2()
d = Singleton2()

print(a)
print(b)
print(f'a & b are same? {id(a) == id(b)}')
print(c)
print(d)
print(f'c & d are same? {id(c) == id(d)}')
