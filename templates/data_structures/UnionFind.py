# the integers in the interval [0, N)
class UnionFind:
    def __init__(self, N):
        self.parent = dict()
        for i in range(N):
            self.parent[i] = i

    def find(self, a):
        acopy = a
        while a != self.parent[a]:
            a = self.parent[a]
        while acopy != a:
            self.parent[acopy], acopy = a, self.parent[acopy]
        return a

    def join(self, a, b):
        self.parent[self.find(b)] = self.find(a)

# a grid of size rxc
class UnionFind:
    def __init__(self, r, c):
        self.parent = dict()
        for x in range(r):
            for y in range(c):
                self.parent[(x,y)] = (x,y)

    def find(self, a):
        acopy = a
        while a != self.parent[a]:
            a = self.parent[a]
        while acopy != a:
            self.parent[acopy], acopy = a, self.parent[acopy]
        return a

    def join(self, a, b):
        self.parent[self.find(b)] = self.find(a)