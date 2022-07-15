#!/usr/bin/env python3

import io, os, sys
from sys import stdin, stdout

# input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline
def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

from itertools import permutations, chain, combinations, product
from math import factorial, gcd
from collections import Counter, defaultdict, deque
from heapq import heappush, heappop, heapify
from bisect import bisect_left
from functools import lru_cache

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

### CODE HERE

def ans(N, A):
    grid = []
    for i in range(N):
        row = []
        for j in range(N):
            row += [(i, j)]
        grid += [row]

    grid2 = []
    for i in range(N):
        row = []
        for j in range(N):
            row += [(i, j)]
        grid2 += [row]
    
    g = UnionFind(N, N)

    for _ in range(4):
        grid2 = list(zip(*grid[::-1]))

        for i in range(N):
            for j in range(N):
                g.join(
                    (i, j),
                    grid2[i][j]
                )

    elems = defaultdict(list)

    for i in range(N):
        for j in range(N):
            p = g.find((i, j))
            elems[p] += [A[i][j]]

    ret = 0

    for k in elems:
        v = elems[k]
        ret += min(v.count('0'), v.count('1'))

    return ret




    return A

for _ in range(read_int()):
    N = read_int()
    A = [input() for _ in range(N)]
    print(ans(N, A))