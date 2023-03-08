from abc import ABC, abstractmethod


class Ten:
    def __get__(self, instance, owner):
        return getattr(instance, 'b', 10)


class TestDescriptor:
    a = Ten()


obj = TestDescriptor()
print(obj.a)
obj.b = 12
print(obj.a)


class LoggedAccess:
    def __set_name__(self, owner, name):
        self.public_name = name
        self.private_name = f'_{name}'

    def __get__(self, instance, owner):
        return getattr(instance, self.private_name)

    def __set__(self, instance, value):
        setattr(instance, self.private_name, value)


class TestDescriptor:
    name = LoggedAccess()
    age = LoggedAccess()

    def __init__(self, name, age):
        self.name = name
        self.age = age


obj = TestDescriptor('Joel', 22)
print(obj.name, obj.age)
print(obj.__dict__)


class Validator(ABC):

    def __set_name__(self, owner, name):
        self.private_name = '_' + name

    def __get__(self, obj, objtype=None):
        return getattr(obj, self.private_name)

    def __set__(self, obj, value):
        self.validate(value)
        setattr(obj, self.private_name, value)

    @abstractmethod
    def validate(self, value):
        pass


class OneOf(Validator):

    def __init__(self, options=None):
        self.options = set(options or [])

    def validate(self, value):
        if value not in self.options:
            raise ValueError(f'{value} is not one of {self.options}')


class TestValidator:
    ram_type = OneOf(options=['ddr', 'ddr2', ' ddr3', 'ddr4'])

    def __init__(self, ram_type):
        self.ram_type = ram_type


obj = TestValidator('ddr2')
print(obj.ram_type)
obj._ram_type = 'dd1'
# it is not necessary to have private name, and we can avoid this case
print(obj.ram_type)
