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

def ans(n, points):
    idx_of = dict()
    for i, p in enumerate(points):
        idx_of[p[0]] = i

    points = [(p[1], p[0]) for p in points]
    points.sort()
    points = points[0:2*n]
    total = sum(p[0] for p in points)
    points = [(p[1], p[0]) for p in points]
    points.sort()
    print(total)
    for i in range(n):
        a, b = points[i], points[len(points)-1-i]
        a, b = a[0], b[0]
        print(idx_of[a]+1, idx_of[b]+1)
    print()

for _ in range(read_int()):
    input()
    points = []
    n, m = read_int_tuple()
    for _ in range(m):
        points += [read_int_tuple()]

    ans(n, points)