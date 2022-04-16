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


def collinear(a, b, c):
    x1, y1 = a
    x2, y2 = b
    x3, y3 = c
    return (x2 - x1)*(y3 - y1) == (y2 - y1)*(x3 - x1)

### CODE HERE

N, K = read_int_tuple()
points = [read_int_tuple() for _ in range(N)]

if K == 1:
    print("Infinity")
    sys.exit(0)

points_on_line = []
for _ in range(N):
    row = []
    for _ in range(N):
        row += [[]]
    points_on_line += [row]

for i in range(N):
    for j in range(i+1, N):
        for k in range(N):
            a = points[i]
            b = points[j]
            c = points[k]
            if collinear(a, b, c):
                points_on_line[i][j] += [k]

for i in range(N):
    for j in range(N):
        points_on_line[i][j] = tuple(sorted(points_on_line[i][j]))

ret = set()

for i in range(N):
    for j in range(N):
        if len(points_on_line[i][j]) >= K:
            ret.add(points_on_line[i][j])

print(len(ret))