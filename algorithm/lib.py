from bisect import bisect_left, bisect_right

arr = [1,2,3,4,5,8,9,9,9,9,9,9,9,9,9,11]

# right or equal
print(bisect_left(arr, 7))
print(bisect_left(arr, 10))
print(bisect_left(arr, 9)) # in case of duplicate first index
print(bisect_left(arr, 0))
print(bisect_left(arr, 15))

print("----------")
# next idx where it can be inserted. Add to right side
print(bisect_right(arr, 7))
print(bisect_right(arr, 10))
print(bisect_right(arr, 9)) # in case of duplicate last index
print(bisect_right(arr, 0))
print(bisect_right(arr, 15)) # outside array at right side
print(bisect_right(arr, 11)) # outside array at right side