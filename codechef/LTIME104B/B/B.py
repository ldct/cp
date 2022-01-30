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
from collections import Counter, defaultdict
from heapq import heappush, heappop, heapify
from bisect import bisect_left
from functools import lru_cache

### CODE HERE

def cost(S):
    S = S[::-1]
    ret = 0
    last = 0
    for c in S:
        gap = (last - c + 10) % 10
        ret += gap
        last = c
    return ret

def ans(K, S):
    S = list(map(int, S))

    def ok(r):
        return cost(S[0:r]) <= K

    if not ok(0): return 0
    if ok(len(S)): return len(S)

    low = 0
    high = len(S)

    assert(ok(low))
    assert(not ok(high))

    while high - low > 2:
        mid = (low + high) // 2
        if ok(mid):
            low = mid
        else:
            high = mid

    for r in range(low, low+10):
        if not ok(r):
            return r-1

    return K, S

for _ in range(read_int()):
    N, K = read_int_tuple()
    S = input()
    print(ans(K, S))