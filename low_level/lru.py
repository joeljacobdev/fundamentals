import abc
from typing import Dict


class DLLNode:
    def __init__(self, val, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev


class DoublyLinkedList:

    def __init__(self):
        self.__head = None
        self.__tail = None

    def head(self):
        return self.__head

    def tail(self):
        return self.__tail

    def append(self, node):
        """
        Add to the tail
        """
        curr = self.__tail
        curr.next = node
        node.prev = curr
        node.next = None
        self.__tail = node

    def delete(self, node):
        """
        Handles deletion - at any place. Updates head and tail
        """
        if self.__tail == self.__head == node:
            self.__head = None
            self.__tail = None
        elif node == self.__head:
            self.__head = self.__head.next
            self.__head.prev = None
        elif node == self.__tail:
            self.__tail = self.__tail.prev
            self.__tail.next = None
        else:
            prev = node.prev
            next = node.next
            prev.next = next
            next.prev = prev


class EvictionPolicy(abc.ABC):
    @abc.abstractmethod
    def evict(self):
        raise NotImplementedError()

    @abc.abstractmethod
    def use(self, key):
        raise NotImplementedError()

    @abc.abstractmethod
    def is_full(self):
        raise NotImplementedError()

    @abc.abstractmethod
    def exists(self, key):
        raise NotImplementedError()


class LRUEvictionPolicy(EvictionPolicy):
    def __init__(self, capacity):
        self.capacity = capacity
        self.recency_list = DoublyLinkedList()
        self.__key_to_node_map: Dict[str, DLLNode] = {}

    def evict(self):
        """
        Should be called when cache is full
        """
        head = self.recency_list.head()
        self.recency_list.delete(head)
        del self.__key_to_node_map[head.val]
        return head.val

    def use(self, key):
        if key in self.__key_to_node_map:
            node = self.__key_to_node_map[key]
            self.recency_list.delete(node)
        else:
            node = DLLNode(val=key)
            self.__key_to_node_map[key] = node
        self.recency_list.append(node)

    def is_full(self):
        return len(self.__key_to_node_map.keys()) == self.capacity

    def exists(self, key):
        return self.__key_to_node_map.get(key) is not None


class Cache:

    def __init__(self, capacity, eviction_policy_class):
        self._storage = {}
        self.lock = False
        self.eviction_policy = eviction_policy_class(capacity=capacity)

    def put(self, key: str) -> None:
        if self.lock:
            return
        self.lock = True
        if self.eviction_policy.is_full() and not self.eviction_policy.exists(key):
            evicted_key = self.eviction_policy.evict()
            del self._storage[evicted_key]
        self.eviction_policy.use(key)
        self.lock = False
        self._storage[key] = None

    def get(self, key):
        if key in self._storage:
            self.eviction_policy.use(key)
        return self._storage.get(key)
