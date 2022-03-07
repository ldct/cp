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

def neighbours(d):
    if d == 1: return [1, 2]
    if d == 9: return [8, 9]
    return [d-1, d, d+1]

def dp(N, d):
    if N == 1: return 1
    ret = 0
    for n in neighbours(d):
        ret += dp(N-1, n)
        ret %= MODULUS
    return ret

def ans(N):
    ret = 0
    for d in range(1, 10):
        ret += dp(N, d)
        ret %= MODULUS
    return ret
