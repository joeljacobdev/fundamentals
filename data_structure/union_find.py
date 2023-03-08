class UnionFind:
    def __init__(self):
        self.p = {}

    def find(self, x):
        if x == self.p[x]:
            return x
        self.p[x] = self.find(self.p[x])
        return self.p[x]

    def insert(self, x):
        if self.p.get(x) is None:
            self.p[x] = x

    def union(self, x, y):
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
