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

n, k = 100, 1
k -= 1

@lru_cache(None)
def ans(n, s):
    # number of length-n sequences of weight s

    v = n + k

    if n == 1:
        if s == 0: return 0
        if s % v == 0: return 1
        return 0
    if s == 0: return 0
    v = n + k

    ret = 0
    i = 1
    while True:
        if s - i*v < 0: break
        ret += ans(n-1, s - i*v)
        i += 1
    return ret

def f(s):
    return sum([ans(n, s) for n in range(1, s+1)])


print([f(s) for s in range(1, n+1)])