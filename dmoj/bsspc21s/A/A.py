#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

from itertools import permutations, chain, combinations
from math import factorial, gcd
from collections import Counter, defaultdict
from heapq import heappush, heappop, heapify
from bisect import bisect_left

### CODE HERE

class UnionFind:
    def key(self, i, j):
        return i*M + j
    def __init__(self, N, M):
        self.parent = dict()
        self.N = N
        self.M = M
        for i in range(N):
            for j in range(M):
                self.parent[self.key(i, j)] = self.key(i, j)

    def find(self, a):
        k = self._find(self.key(*a))
        return (k // M, k % M)

    def _find(self, a):
        acopy = a
        while a != self.parent[a]:
            a = self.parent[a]
        while acopy != a:
            self.parent[acopy], acopy = a, self.parent[acopy]
        return a

    def join(self, a, b):
        a, b = self.key(*a), self.key(*b)
        self.parent[self._find(b)] = self._find(a)

N, M = read_int_tuple()
grid = []
for _ in range(N):
    grid += [list(input())]

uf = UnionFind(N, M)

for x in range(N):
    for y in range(M):
        uf.join((x, y), (x, M-y-1))
        uf.join((x, y), (N-x-1, y))

candidates_of = defaultdict(set)

for x in range(N):
    for y in range(M):
        lx, ly = uf.find((x, y))
        if grid[x][y] != '.':
            candidates_of[(lx, ly)].add(grid[x][y])

ok = True
for x in range(N):
    for y in range(M):
        if len(candidates_of[(x, y)]) == 0:
            candidates_of[(x, y)].add('z')
        elif len(candidates_of[(x, y)]) > 1:
            ok = False

if not ok:
    print(-1)
    import sys
    sys.exit(0)

for x in range(N):
    for y in range(M):
        lx, ly = uf.find((x, y))
        grid[x][y] = list(candidates_of[(lx,ly)])[0]

# print("ok")
for row in grid:
    print(''.join(row))
