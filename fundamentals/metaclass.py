class Some:
    pass


# old style classes
class SomeObj(object):
    pass


class SomeType(type):
    def __new__(cls, *args, **kwargs):
        print(args)
        print('__new__ called')
        return super().__new__(cls, *args, **kwargs)
    #
    # def __init__(cls, t, *args, **kwargs):
    #     print('__init__ called')
    #     print(type(cls))
    #     super.__init__(cls, t, *args, **kwargs)


# all three will give class type
print(type(Some))
print(type(SomeObj))
print(type(SomeType))


def some(self):
    print(self.heap)


obj1 = Some()
obj2 = SomeObj()
# object name, base classes, (properties and function)
obj3 = type('some', (object,), {'a': 'a', 'some': some})
obj4 = SomeType('some', (object,), {'a': 'a', 'some': some})

print(type(obj1))
print(type(obj2))
print(type(obj3))
obj3.some(obj3)
obj4.a = 'b'
obj3.some(obj3)
obj4.some(obj4)


print(Some().__class__.__name__)
print(SomeObj.__class__.__name__)
print(SomeType.__class__.__name__)
print(type.__class__.__name__)
print(object.__class__.__name__)
print(obj3())
print(SomeObj())

# singleton using __new__
# https://howto.lintel.in/python-__new__-magic-method-explained/
# meta class
# https://blog.ionelmc.ro/2015/02/09/understanding-python-metaclasses/

# Everything in python is object
# __class__ of a class is type
obj = type('some', (object,), {'a': 'a', 'some': some})
print(obj.__class__)
# will give 'type'
print(obj().__class__)
# will give '__main__.some'
# type is a metaclass, of which classes are instances

# for t in int, float, dict, list, tuple:
#     print(type(t))

# in most languages like C we assume that variable are used to store data

print((10).__class__)

__name__ = '__main__'
