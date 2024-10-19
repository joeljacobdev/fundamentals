from functools import cmp_to_key

def compare_strings(x, y):
    xy = int(x + y)
    yx = int(y + x)
    if xy == yx:
        return 0
    elif xy < yx:
        return -1
    else:
        return 1


class CompareClass:
    def __init__(self, x, cmp):
        self.x = x
        self.cmp = cmp
    def __lt__(self, other):
        return self.cmp(self.x, other.x) < 0
    def __repr__(self):
        return self.x


arr = ['3', '30', '34', '5', '9', '0']
# in python 3, cmp is removed, so we need to use cmp_to_key - to convert cmp function to key function
# cmp function used to take 2 values to compare, while key function takes 1 value to compare
print(sorted(arr, key=cmp_to_key(compare_strings), reverse=True))  # ['9', '5', '34', '3', '30', '0']
# this is equivalent to the above
print(sorted([CompareClass(i, compare_strings) for i in arr], reverse=True))  # ['9', '5', '34', '3', '30', '0']