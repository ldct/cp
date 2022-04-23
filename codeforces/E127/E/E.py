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

MODULUS = 998244353

### CODE HERE

N = read_int()
MISSING = 2**N-1
A = input()

@lru_cache(None)
def signature(r):
    if r >= MISSING: return ""
    i = 2*r+1
    j = 2*r+2
    return A[r] + max(
        signature(i) + signature(j),
        signature(j) + signature(i)
    )

def ans(r):
    i = 2*r+1
    j = 2*r+2
    if j >= MISSING: return 1

    if signature(i) == signature(j):
        return (ans(i)*ans(i)) % MODULUS
    return (2*ans(i)*ans(j)) % MODULUS

print(ans(0))