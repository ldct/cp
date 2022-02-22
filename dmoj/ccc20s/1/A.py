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

obs = []

for _ in range(read_int()):
    obs += [read_int_tuple()]

ret = 0
obs.sort()

for i in range(len(obs)-1):
    candidate = obs[i+1][1] - obs[i][1]
    candidate = candidate / (obs[i+1][0] - obs[i][0])
    candidate = abs(candidate)
    ret = max(ret, candidate)

print(ret)