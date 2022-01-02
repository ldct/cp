#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

from itertools import permutations, chain, combinations
from math import factorial, gcd
from collections import Counter, defaultdict
from heapq import heappush, heappop, heapify
from bisect import bisect_left
from functools import lru_cache

### CODE HERE

MODULUS = 1000000007

N, K, D = read_int_tuple()

@lru_cache(None)
def ans(weight, c):
    if weight < 0: return 0
    if weight == 0:
        if c: return 1
        return 0
    ret = 0
    for k in range(1, K+1):
        ret += ans(weight - k, c or k >= D)
        ret %= MODULUS
    return ret

print(ans(N, False))