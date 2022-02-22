#!/usr/bin/env pypy3

import io, os
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

    def join(self, a, b):
        self.parent[self.find(b)] = self.find(a)

### CODE HERE

import sys

N, M = read_int_list()
D = read_int_list()

uf = UnionFind(N)

sD = sum(D)
if sD % 2 == 1:
    print(-1)
    sys.exit(0)
if sD // 2 != (N-1):
    print(-1)
    sys.exit(0)

for _ in range(M):
    a, b = read_int_tuple()
    a -= 1
    b -= 1
    if uf.find(a) == uf.find(b):
        print(-1)
        sys.exit(0)
    uf.join(a, b)
    D[a] -= 1
    D[b] -= 1

how_many_more = N - M - 1

def find_good_pair():
    for a in range(N):
        for b in range(N):
            if D[a] == 0: continue
            if D[b] == 0: continue
            if uf.find(a) != uf.find(b): return a, b

new_edges = []
for _ in range(how_many_more):
    r = find_good_pair()
    print("found", r)
    if r is None:
        print(-1)
        sys.exit(0)

    new_edges += [r]
    a, b = r
    uf.join(a, b)
    D[a] -= 1
    D[b] -= 1

print(new_edges)