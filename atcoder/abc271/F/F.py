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

N = read_int()

grid = [read_int_list() for _ in range(N)]

def dest1(l, x, y):
    if l == 1:
        return [((x, y), grid[x][y])]
    ret = []
    if x+1 < N:
        for endpoint, path_weight in dest1(l-1, x+1, y):
            ret += [(endpoint, path_weight^grid[x][y])]
    if y+1 < N:
        for endpoint, path_weight in dest1(l-1, x, y+1):
            ret += [(endpoint, path_weight^grid[x][y])]
    return ret

def dest2(l, x, y):
    if l == 1:
        return [((x, y), grid[x][y])]
    ret = []
    if 0 <= x-1:
        for endpoint, path_weight in dest2(l-1, x-1, y):
            ret += [(endpoint, path_weight^grid[x][y])]
    if 0 <= y-1:
        for endpoint, path_weight in dest2(l-1, x, y-1):
            ret += [(endpoint, path_weight^grid[x][y])]
    return ret
    
s1 = dest1(N, 0, 0)
s2 = dest2(N, N-1, N-1)

c2 = Counter(s2)

# print(s1)
# print(s2)

ret = 0
for ((x, y), w) in s1:
    target = ((x, y), w^grid[x][y])
    ret += c2[target]

print(ret)