from typing import List, Dict


class UnionFind:
    """
    Map based union find implementation
    """

    def __init__(self):
        self.p: Dict[int, int] = {}

    def find(self, x):
        if x == self.p[x]:
            return x
        self.p[x] = self.find(self.p[x])
        return self.p[x]

    def insert(self, x):
        """
        Allow insert if x is not present in graph
        """
        if self.p.get(x) is None:
            self.p[x] = x

    def union(self, x: int, y: int):
        """
        Connect 2 nodes :x and :y if they are present.
        In case they are not present in add them and connect.
        """
        self.insert(x)
        self.insert(y)
        xp = self.find(x)
        yp = self.find(y)
        if xp == yp:
            return
        if xp < yp:
            self.p[yp] = xp
        else:
            self.p[xp] = yp


class ArrayUnionFind:
    """
    Array based union find implementation.
    """

    def __init__(self, n):
        """
        :param n: size of union find structure. Can't have more than these nodes.
        """
        self.parents: List[int] = [-1] * (n + 1)
        self.sz: List[int] = [0] * (n + 1)
        self.num_component: int = 0

    def insert(self, x) -> None:
        """
        In case there is already some node x, we don't allow re-insert
        """
        if x <= len(self.parents):
            if self.find(x) == -1:
                self.parents[x] = x
                self.sz[x] += 1
                self.num_component += 1
            return
        raise Exception(f'Initialized array is smaller to insert {x}')

    def find(self, x: int) -> int:
        if x > len(self.parents):
            raise Exception(f"Initialized storage is smaller for {x}")
        if self.parents[x] == -1:
            return -1

        root = x
        while root != self.parents[root]:
            root = self.parents[root]

        # lazy path compression - node in path point directly to root.
        while x != root:
            next_x = self.parents[x]
            self.parents[x] = root
            x = next_x

        return root

    def connected(self, x: int, y: int) -> bool:
        fx = self.find(x)
        fy = self.find(y)
        return fx == fy and not ({fx, fx} & {-1})

    def union(self, x: int, y: int) -> None:
        """
        Create union of 2 node - x and y. If they are not present, raise an exception.
        """
        if self.connected(x, y): return
        fx = self.find(x)
        fy = self.find(y)
        if {fx, fx} & {-1}:
            raise Exception(f'Either {x} or {y} is not present in the graph')

        # Merge smaller graph to larger graph.
        if self.sz[fx] > self.sz[fy]:
            self.sz[fx] += self.sz[fy]
            self.parents[fy] = fx
            self.sz[fy] = 0
        else:
            self.sz[fy] += self.sz[fx]
            self.parents[fx] = fy
            self.sz[fx] = 0
        self.num_component -= 1


uf = ArrayUnionFind(10)
uf.insert(1)
uf.insert(5)
uf.insert(6)
uf.insert(8)
uf.insert(9)
uf.union(5, 9)
uf.union(1, 8)
uf.union(1, 6)
uf.union(6, 9)
print(uf.find(9))
print(uf.find(6))
print(uf.find(4))
print(uf.find(1))
print(uf.find(8))
print(uf.num_component)
