from typing import List
from collections import deque


class list_queue:
    __slots__ = ('list_queue',)

    def __init__(self):
        self.list_queue: List[int] = []

    def append(self, val):
        self.list_queue.append(val)

    def popleft(self) -> int:
        try:
            return self.list_queue.pop(0)
        except:
            return -1

    def __str__(self):
        return ', '.join(map(str, self.list_queue))


q1 = list_queue()
q1.append(1)
q1.append(2)
q1.append(3)
q1.append(4)
print(q1)

print(q1.popleft())
print(q1)
print(q1.popleft())
print(q1.popleft())
print(q1.popleft())
print(q1.popleft())

q2 = deque()
q2.append(1)
