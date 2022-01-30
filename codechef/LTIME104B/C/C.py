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

def vau(p, k):
    # p-adic valuation
    for i in range(100, 0, -1):
        if k % (p**i) == 0: return i
    return 0

def ans_GS(N):
    return 2**vau(2, N+1)-1

def ans(N):
    return N*(N+1) - 2*ans_GS(N)

for _ in range(read_int()):
    print(ans(read_int()))