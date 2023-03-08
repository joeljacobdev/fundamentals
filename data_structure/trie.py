class Trie:
    class Node:
        __slot__ = ('mp', 'is_ended')

        def __init__(self):
            self.is_ended = False
            self.mp = {}

    __slot__ = ('root',)

    def __init__(self):
        self.root = self.Node()

    def insert(self, word: str) -> None:
        node = self.root
        for ch in word:
            if not node.mp.get(ch):
                node.mp[ch] = self.Node()
            node = node.mp[ch]
        node.is_ended = True

    def search(self, word: str) -> bool:
        node = self.root
        for ch in word:
            if not node.mp.get(ch):
                return False
            node = node.mp[ch]
        return node.is_ended

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for ch in prefix:
            if not node.mp.get(ch):
                return False
            node = node.mp[ch]
        return node.is_ended or len(node.mp.keys()) > 0

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
