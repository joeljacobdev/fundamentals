print(id(2000000))
print(id(2000000))
a = 2000000
print(id(2000000))

while True:
    a = 2000000
    print(id(a))
    print(id(2000000))
    a = 3000000
    print(id(a))
    print(id(2000000))
    break

print(id(3000000))

print("Small integers are cached")
print((1 + 2) is (2 + 1))
print(id(1000.0 + 1) == id(1 + 1000.0))
print('-------------------------')
print(id(2))
print(id(2))
a = 2
print(id(2))

while True:
    a = 2
    print(id(a))
    print(id(2))
    a = 3
    print(id(a))
    print(id(2))
    break

print(id(3))
c = [1, 2, 3]
d = c
print(id(c))
print(id(d))
c.append(4)
print(c)
print(d)
print(id(c))
print(id(d))
print('------------------')


def func(list1):
    list1 = [2]
    list1[0] = 1


list2 = [11, 22, 33]
func(list2)
print(list2)


def list_changer(input_list):
    input_list[0] = 10
    input_list = list(range(1, 10))
    print(input_list)
    input_list[0] = 5
    print(input_list)


test_list = [5, 5, 5]
list_changer(test_list)
print(test_list)

import time

start = time.time()
for c in range(1, 100000):
    a = c
print(time.time() - start)

start = time.time()
for c in list(range(1, 100000)):
    a = c
print(time.time() - start)

print('--- string ---')
print('my string' is 'my string')
print(('my string' + 'a') is ('my string' + 'a'))

# values imported changes as object changes
from test.data import my_value, print_my_value, my_val, print_my_val

print(my_value)
my_value[0] = 11
print_my_value()

# but why no changes observed with my_val like in case of my_value?
# from shared_stuff import a would create a new a variable initialized to whatever
# shared_stuff.a referred to at the time of the import, and this new a variable would
# not be affected by assignments to shared_stuff.a
print(my_val)
my_val = 11
print_my_val()
