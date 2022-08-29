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

MODULUS = 10**9+7

### CODE HERE

def is_good(arr):
    for i in range(len(arr)-1):
        if not (arr[i]+1 < arr[i+1]):
            return False
    return True

@lru_cache(None)
def num_good_slow(N):
    ret = 0
    for sz in range(1, N+1):
        for arr in product(range(sz, N+1), repeat=sz):
            if is_good(arr):
                ret += 1
    return ret % MODULUS

@lru_cache(None)
def a(n):
    if n < 4:
        return num_good_slow(n)
    return (a(n-2) + a(n-3) + a(n-4) + 2) % MODULUS

# for n in range(1, 100):
#     print(n, a(n), num_good_slow(n))
print(a(read_int()))