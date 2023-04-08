class LRUCache:
    class Node:
        def __init__(self, key, val, nxt=None, prev=None):
            self.key = key
            self.val = val
            self.next = nxt
            self.prev = prev

    def __init__(self, capacity: int):
        self.head = None
        self.tail = None
        self.storage = {}
        self.capacity = capacity

    def _mark_recently_used(self, key):
        """
        Mark the :key are recently used, by moving it to end of recency list.
        :param key:
        :return:
        """
        if self.tail.key == key or len(self.storage.keys()) <= 1:
            return
        node = self.storage[key]
        if node.key == self.head.key:
            self.head = self.head.next
        else:
            node.prev.next = node.next
        node.next.prev = node.prev

        self.tail.next = node
        node.next = None

        node.prev = self.tail
        self.tail = self.tail.next

    def get(self, key: int) -> int:
        ans = self.storage.get(key)
        if ans:
            self._mark_recently_used(key)

        return ans.val if ans else -1

    def put(self, key: int, value: int) -> None:
        if len(self.storage.keys()) == self.capacity and not self.storage.get(key):
            self._remove_least_recently_used()

        if not self.storage.get(key):
            self.storage[key] = self.Node(key=key, val=value, prev=self.tail)
            if not self.head:
                self.head = self.storage[key]
                self.tail = self.storage[key]
            else:
                self.tail.next = self.storage[key]
                self.tail = self.storage[key]
        else:
            self._mark_recently_used(key)
            self.storage[key].val = value

    def _remove_least_recently_used(self):
        """
        When cache is filled, we remove the least recently used node - i.e.
        first of linkedlist which contain the recency of node's usage. We only need to evict cache when the new entry
        not present in the cache. It is not needed when we overwrite the value.
        :return:
        """
        node_to_remove = self.head.key
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.head = self.head.next
            self.head.prev.next = None
            self.head.prev = None
        del self.storage[node_to_remove]
