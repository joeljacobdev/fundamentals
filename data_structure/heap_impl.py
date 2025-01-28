class MinHeap:
    def __init__(self):
        self.heap = []

    @staticmethod
    def parent(index):
        return (index - 1) // 2

    @staticmethod
    def left_child(index):
        return 2 * index + 1

    @staticmethod
    def right_child(index):
        return 2 * index + 2

    def insert(self, value):
        # Add the new value at the end
        self.heap.append(value)
        # Heapify up to maintain the heap property
        self.heapify_up(len(self.heap) - 1)

    def heapify_up(self, index):
        while index > 0 and self.heap[index] < self.heap[self.parent(index)]:
            # Swap the current node with its parent
            self.heap[index], self.heap[self.parent(index)] = (
                self.heap[self.parent(index)],
                self.heap[index],
            )
            index = self.parent(index)

    def extract_min(self):
        if not self.heap:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()

        # Replace the root with the last element
        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        # Heapify down to maintain the heap property
        self.heapify_down(0)
        return root

    def heapify_down(self, index):
        smallest = index
        left = MinHeap.left_child(index)
        right = MinHeap.right_child(index)

        # Check if the left child exists and is smaller
        if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
            smallest = left

        # Check if the right child exists and is smaller
        if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
            smallest = right

        # If the smallest is not the current index, swap and continue heapifying
        if smallest != index:
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            self.heapify_down(smallest)

    def get_min(self):
        return self.heap[0] if self.heap else None


# Example Usage
min_heap = MinHeap()
min_heap.insert(10)
min_heap.insert(5)
min_heap.insert(20)
min_heap.insert(2)

print("Heap:", min_heap.heap)  # Heap: [2, 5, 20, 10]
print("Extract Min:", min_heap.extract_min())  # Extract Min: 2
print("Heap after extract:", min_heap.heap)  # Heap after extract: [5, 10, 20]
print("Current Min:", min_heap.get_min())  # Current Min: 5
