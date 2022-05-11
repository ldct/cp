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

def ans(n, m, grid):
    score_pos = defaultdict(int)
    score_neg = defaultdict(int)

    for i in range(n):
        for j in range(m):
            score_pos[i+j] += grid[i][j]
            score_neg[i-j] += grid[i][j]

    ret = 0

    for i in range(n):
        for j in range(m):
            candidate = score_pos[i+j] + score_neg[i-j] - grid[i][j]
            ret = max(ret, candidate)

    return ret

for _ in range(read_int()):
    n, m = read_int_tuple()
    grid = [read_int_list() for _ in range(n)]
    print(ans(n, m, grid))