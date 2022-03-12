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

def ans(N, M, grid):
    if grid[0][0] == '1':
        print(-1)
        return
    points = []
    for i in range(N):
        for j in range(M):
            if grid[i][j] == '1':
                points += [(i, j)]
    points = sorted(points)[::-1]

    ops = []
    for (i, j) in points:
        if j == 0:
            ops += [(i, j+1, i+1, j+1)]
        else:
            ops += [(i+1, j, i+1, j+1)]

    print(len(ops))
    for op in ops:
        print(*op)

for _ in range(read_int()):
    N, M = read_int_list()
    grid = [input() for _ in range(N)]
    ans(N, M, grid)