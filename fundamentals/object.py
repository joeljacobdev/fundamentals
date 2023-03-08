# Some object are mutable and some immutable

a = 1
b = 1
print(id(a) == id(b))

c = 'one'
d = 'one'
print(id(c) == id(d))
# both of them have same memory location
# as string is immutable

e = [1, 2, 3]
f = [1, 2, 3]
print(id(e) == id(f))
# list does not have same id
# as they are immutable

g = (1, 2, 3)
h = (1, 2, 3)
# h = tuple(f) -> (1, 2, 3)
# Why this h will have different memory location
print(id(g) == id(h))


# Implications of passing mutable vs. immutable variables to functions
# passing immutable
def fun(a):
    a = "hello"


a = "holla"
fun(a)
print(a)


# in scope of function fun a has been bound to "hello" while outside the function scope
# we are bound to "holla"

# passing mutable
# passing in a mutable variable causes the local name and the global name to point to the same
# object, and if we modify the mutable object in place (instead of pointing the name a
# to a completely new object), the changes will live beyond the scope of the function
def fun(a):
    a[2] = "nothing"
    a = ['one']


bar = ['You', 'know', 'something', 'Jon', 'Snow']
fun(bar)
print(bar)
