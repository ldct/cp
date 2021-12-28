#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

from itertools import permutations, chain, combinations
from math import factorial, gcd
from collections import Counter, defaultdict
from heapq import heappush, heappop, heapify
from bisect import bisect_left
from functools import lru_cache

### CODE HERE

N = read_int()
grid = [input() for _ in range(N)]

@lru_cache(None)
def is_empty(x1, x2, y1, y2):
    for x in range(x1, x2):
        for y in range(y1, y2):
            if grid[x][y] == '#': return False
    return True

@lru_cache(None)
def ans(x1, x2, y1, y2):
    ret = float("inf")
    if x2 - x1 == y2 - y1:
        ret = x2 - x1
    if is_empty(x1, x2, y1, y2):
        return 0
    for x in range(x1+1, x2):
        ret = min(ret,
            ans(x1, x, y1, y2) + ans(x, x2, y1, y2)
        )
    for y in range(y1+1, y2):
        ret = min(ret,
            ans(x1, x2, y1, y) + ans(x1, x2, y, y2)
        )
    return ret

print(ans(0, N, 0, N))