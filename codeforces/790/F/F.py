#!/usr/bin/env pypy3

# epic misunderstanding

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

def best(good, i):
    # maximum j such that good[j]

    def ok(j):
        return j < len(good) and good[j] == good[i] + (j-i)

    high = len(good)+1
    low = i

    assert(ok(low))
    assert(not ok(high))

    while high - low > 2:
        mid = (low + high) // 2
        if ok(mid):
            low = mid
        else:
            high = mid

    j = low
    while ok(j):
        j += 1
    return j-1

def ans(k, A):
    cA = Counter(A)

    good = [a for a in A if cA[a] >= k]
    good = sorted(set(good))

    if len(good) == 0: return -1

    ret = (0, best(good, 0))

    for i in range(len(good)):

        j = best(good, i)
        if j - i > ret[1] - ret[0]:
            ret = (i, j)

    i, j = ret
    return f"{good[i]} {good[j]}"

for _ in range(read_int()):
    n, k = read_int_tuple()
    A = read_int_list()
    print(ans(k, A))