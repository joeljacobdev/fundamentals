class Base(object):
    def __init__(self, val):
        self.val = val

    @classmethod
    def make_obj(cls, val):
        return cls(val + 1)


class Derived(Base):
    def __init__(self, val):
        # In this super call, the second argument "self" is an object.
        # The result acts like an object of the Base class.
        super(Derived, self).__init__(val + 2)

    @classmethod
    def make_obj(cls, val):
        # In this super call, the second argument "cls" is a type.
        # The result acts like the Base class itself.
        return super(Derived, cls).make_obj(val)


b1 = Base(0)
print(b1.val)
# 0
b2 = Base.make_obj(0)
print(b2.val)
# 1
d1 = Derived(0)
print(d1.val)
# 2
d2 = Derived.make_obj(0)
print(d2.val)
# 3

# The 3 result is the combination of the previous modifiers:
# 1 (from Base.make_obj) plus 2 (from Derived.__init__).
#
# Note that it is possible to call super with just one argument to get an "unbound" super object,
# it is apparently not useful for much. There's not really any reason to do this unless you want
# to mess around with Python internals and you really know what you're doing.
