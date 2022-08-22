#!/usr/bin/env python3

from email.policy import default
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

MODULUS = 998244353

N, M = read_int_list()
A, B, C, D, E, F = read_int_list()
obstacles = set([read_int_tuple() for _ in range(M)])

paths = {(0, 0): 1}

for _ in range(N):
    next_paths = defaultdict(int)
    for x, y in paths:
        for dx, dy in [(A, B), (C, D), (E, F)]:
            xx = x + dx
            yy = y + dy
            if (xx, yy) in obstacles: continue
            next_paths[(xx, yy)] += paths[x,y]
            next_paths[(xx, yy)] %= MODULUS
    paths = next_paths

ret = 0
for p in paths:
    ret += paths[p]
print(ret % MODULUS)