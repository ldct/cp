#!/usr/bin/env pypy3

from collections import defaultdict

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

def make_fill(N, M, val=0):
    ret = []
    for _ in range(N):
        ret += [[val]*M]
    return ret

def latestDayToCross(row, col, cells):
    def ok_grid(grid):
        uf = UnionFind(row, col)
        uf.parent["start"] = "start"
        uf.parent["end"] = "end"
        for x in range(row):
            for y in range(col):
                if grid[x][y] == 1: continue
                if x+1 < row and grid[x+1][y] == 0: uf.join((x,y),(x+1,y))
                if y+1 < col and grid[x][y+1] == 0: uf.join((x,y),(x,y+1))

        for y in range(col):
            if grid[0][y] == 0: uf.join("start", (0,y))
            if grid[row-1][y] == 0: uf.join("end", (row-1,y))


        return uf.find("start") == uf.find("end")

    def ok(day):
        grid = make_fill(row, col)
        for i in range(day):
            x,y = cells[i]
            x -= 1
            y -= 1
            grid[x][y] = 1

        return ok_grid(grid)

    low = 0
    high = len(cells)

    while high - low > 2:
        # assert(ok(low))
        # assert(not ok(high))

        mid = (low + high) // 2
        if ok(mid):
            low = mid
        else:
            high = mid

    for i in range(low, low+10):
        if not ok(i):
            return i-1


print(latestDayToCross(
    3, 3,
    [[1,2],[2,1],[3,3],[2,2],[1,1],[1,3],[2,3],[3,2],[3,1]]
))