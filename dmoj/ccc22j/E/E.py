#!/usr/bin/env pypy3

import io, os
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

N = read_int()
trees = []
for _ in range(read_int()):
    x, y = read_int_tuple()
    trees += [(x-1, y-1)]

def br(a, b):
    return a[0]+1, b[1]+1

def tl(a, b):
    return a[0]-1, b[0]-1

# def ok(px, py, qx, qy):
#     for x, y in trees:
#         if (px <= x <= qx) and (py <= y <= qy): return False
#     return True

def ok(x, y, L):
    if L == 0: return True
    X = x + L - 1
    Y = y + L - 1
    if not (0 <= X < N): return False
    if not (0 <= Y < N): return False
    for xx, yy in trees:
        if (x <= xx <= X) and (y <= yy <= Y): return False
    return True

def max_L(x, y):
    low = 0
    high = N+1

    assert(ok(x, y, low))
    assert(not ok(x, y, high))

    while high - low > 2:
        assert(ok(x, y, low))
        assert(not ok(x, y, high))

        mid = (low + high) // 2
        if ok(x, y, mid):
            low = mid
        else:
            high = mid

    for ret in range(low, low+5):
        if not ok(x, y, ret):
            return ret-1

ret = 0

xs = set([0])
ys = set([0])

for x, y in trees:
    xs.add(x+1)
    ys.add(y+1)

# print(xs, ys)

for x in xs:
    for y in ys:
        if not (0 <= x < N): continue
        if not (0 <= y < N): continue
        ret = max(ret, max_L(x, y))

print(ret)