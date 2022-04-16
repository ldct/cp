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

MODULUS = 998244353

def ans(N, M, K):

    @lru_cache(None)
    def dp(N, K):
        if K < 0: return 0
        if N == 0: return 1
        ret = 0
        for a in range(1, M+1):
            ret += dp(N-1, K-a)
            ret %= MODULUS
        return ret

    return dp(N, K)

print(ans(*read_int_tuple()))