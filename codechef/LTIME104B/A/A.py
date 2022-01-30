#!/usr/bin/env pypy3

import io, os
from sys import stdin, stdout

input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline
# def input(): return stdin.readline().strip()
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

def ans(N, K):
    if N == 1: return [1]
    if K == 1: return [-1]
    if K > N: return [-1]
    if N == 3:
        if K == 1: return [3, 2, 1]
        if K == 2: return [1, 3, 2]
        if K == 3: return [1, 2, 3]
        assert(False)
    ret = list(range(1, K)) + list(range(K, N+1))[::-1]
    return ret

for _ in range(read_int()):
    N, K = read_int_tuple()
    print(*ans(N, K))