from sortedcontainers import sortedlist

sl = sortedlist.SortedList()
for idx, el in enumerate([2, 7, 4, 2, 1, 8]):
    sl.add((el, idx))

sl.remove((2, 3))
print([s for s in sl])
