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

N, Q = read_int_tuple()

succ = []
prev = []

for i in range(N+1):
    succ += [i+1]
succ += [-1]
prev += [-1]
for i in range(N+1):
    prev += [i]

for _ in range(Q):
    L, R, J = read_int_tuple()
    l = prev[L]
    r = succ[R]

    assert(l != -1)
    assert(r != -1)

    succ[l] = r
    prev[r] = l

    K = succ[J]

    succ[J] = L
    prev[L] = J
    succ[R] = K
    prev[K] = R


ret = []
i = succ[0]
for _ in range(N):
    ret += [i]
    i = succ[i]
# assert(i == N+1)
print(*ret)