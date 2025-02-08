import heapq

heap = [2, 5, 3, 6, 8, 7]
heapq.heapify(heap)
print(heap)  # [2, 5, 3, 6, 8, 7]

heapq.heappush(heap, 4)
print(heap)  # [2, 5, 3, 6, 8, 7, 4]
print(heapq.heappop(heap))  # 2
print(heap)  # [3, 5, 4, 6, 8, 7]
print(heapq.heappop(heap))  # 3
print(heap)  # [4, 5, 7, 6, 8]


class Employee:
    def __init__(self, name, yos):
        self.name = name
        self.yos = yos

    def __repr__(self):
        return f'{self.name} {self.yos}'

    def __lt__(self, nxt):
        # it should return true if this is smaller than the next element
        # as heapq provide min heap impl. we override this.
        return self.yos < nxt.yos


emp = [
    Employee('Anish', 3),
    Employee('kathy', 2),
    Employee('Rina', 5),
    Employee('Vinay', 1)
]

heapq.heapify(emp)
print(emp)
heapq.heappushpop(emp, Employee('Zebra', 2))
print(emp)
