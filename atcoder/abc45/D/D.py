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

### CODE HERE

H, W, N = read_int_list()
points = []
for _ in range(N):
    x, y = read_int_tuple()
    points += [(x-1, y-1)]

ps = set(points)
scores = dict()

def score(x0, y0):
    ret = 0
    for x in range(x0, x0+3):
        for y in range(y0, y0+3):
            if (x, y) in ps:
                ret += 1
    return ret

def do_square(x, y):
    X = x + 2
    Y = y + 2
    if not (0 <= x < X < H): return
    if not (0 <= y < Y < W): return
    scores[(x, y)] = score(x, y)

def do_point(x, y):
    for dx in [-2, -1, 0]:
        for dy in [-2, -1, 0]:
            do_square(x+dx, y+dy)

for (x, y) in points:
    do_point(x, y)

ret = [0]*10
for s in scores:
    ret[scores[s]] += 1

total = (H-2)*(W-2)
ret[0] = total - sum(ret[1:])

for r in ret:
    print(r)