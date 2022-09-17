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

### ABC Snukes' Coloring 2 (ABC Edit)

W, H, N = read_int_tuple()
ret = []
for _ in range(H):
    ret += [[1]*W]

for _ in range(N):
    X, Y, a = read_int_tuple()
    if a == 1:
        for x in range(H): 
            for y in range(X): 
                ret[x][y] = 0
    elif a == 2:
        for x in range(H): 
            for y in range(X, W): 
                ret[x][y] = 0
    if a == 3:
        for x in range(Y): 
            for y in range(W): 
                ret[x][y] = 0
    elif a == 4:
        for x in range(Y, H): 
            for y in range(W):
                ret[x][y] = 0
# for row in ret:
#     print(*row)

print(sum(map(sum, ret)))