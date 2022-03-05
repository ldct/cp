#!/usr/bin/env pypy3

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

### CODE HERE

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))

    def find(self, a):
        acopy = a
        while a != self.parent[a]:
            a = self.parent[a]
        while acopy != a:
            self.parent[acopy], acopy = a, self.parent[acopy]
        return a

    def merge(self, a, b):
        self.parent[self.find(b)] = self.find(a)


def kruskal(n, U, V, W):
    union = UnionFind(n)
    cost, merge_cnt = 0, 0
    mst_u, mst_v = [], []
    order = sorted(range(len(W)), key=lambda x: W[x])
    for i in range(len(W)):
        u, v = U[order[i]], V[order[i]]
        find_u, find_v = union.find(u), union.find(v)
        if find_u != find_v:
            cost += W[order[i]]
            merge_cnt += 1
            union.parent[find_v] = find_u
            mst_u.append(u), mst_v.append(v)

    return cost, mst_u, mst_v, n == 1 + merge_cnt

points = []
idx_of = dict()
for i in range(read_int()):
    x, y = read_int_tuple()
    points += [(x, y)]
    idx_of[(x, y)] = i

points.sort()
last_x_of_y = dict()

U = []
V = []
W = []

def add_edge(x, y, X, Y):
    global U, V, W
    dx = x - X
    dy = y - Y
    w = dx**2 + dy**2
    U += [idx_of[(x, y)]]
    V += [idx_of[(X, Y)]]
    W += [w]

for x, y in points:
    for Y in last_x_of_y:
        X = last_x_of_y[Y]
        print("added an edge", X, Y, x, y)
        add_edge(x, y, X, Y)
    last_x_of_y[y] = x

print(kruskal(len(points), U, V, W)[0])