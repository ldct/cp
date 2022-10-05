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

N, x = read_int_list()
a = read_int_list()
ret = 0
for i in range(len(a)):
    excess = a[i] - x
    if excess > 0:
        ret += excess
        a[i] -= excess

# print(ret, a)

for j in range(1, len(a)-1):
    i = j-1
    k = j+1
    assert(0 <= j < len(a))
    assert(0 <= k < len(a))
    e1 = a[i] + a[j] - x
    e2 = a[j] + a[k] - x
    if e1 > 0 and e2 > 0:
        a[j] -= min(e1, e2)
        ret += min(e1, e2)

# print(ret, a)

for i in range(len(a)-1):
    j = i+1
    excess = a[i] + a[j] - x
    if excess > 0:
        a[j] -= excess
        ret += excess

for i in range(len(a)-1):
    assert(a[i] + a[i+1] <= x)

print(ret)
