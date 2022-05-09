#!/usr/bin/env pypy3

# https://codeforces.com/gym/380371/problem/B

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

MODULUS = 10**9 + 7

@lru_cache(None)
def ans(n):
    if n == 0: return 1
    if n < 0: return 0
    return (ans(n-1) + ans(n-2)) % MODULUS

n = read_int()
for x in range(1, n):
    ans(x)

print(ans(n))
