#!/usr/bin/env pypy3

import io, os, sys
from sys import stdin, stdout

input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline
# def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

from itertools import permutations, chain, combinations, product
from math import factorial, gcd
from collections import Counter, defaultdict, deque
from heapq import heappush, heappop, heapify
from bisect import bisect_left
from functools import lru_cache

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

    def same(self, a, b):
        return self.find(a) == self.find(b)

    def join(self, a, b):
        self.parent[self.find(b)] = self.find(a)

### CODE HERE

N, Q = read_int_list()
succ = list(range(1, N+3))

uf = UnionFind(N+3)

for _ in range(Q):
    t, x, y = read_int_tuple()
    if t == 1:
        uf.join(x, y)
    elif t == 2:
        # print("merge interval", x, y)
        i = x
        while i <= y:
            uf.join(x, i)
            # print("visit", i)
            next_i = succ[i]
            succ[i] = y+1
            i = next_i
    elif t == 3:
        print("YES" if uf.same(x, y) else "NO")
    else:
        assert(False)
