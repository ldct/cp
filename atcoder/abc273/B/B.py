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

X, K = read_int_list()

def xround(a, b):
    r1 = b*(a // b)
    r2 = r1 + b

    if abs(r1 - a) < abs(r2 - a):
        return r1

    return r2

for k in range(1, K+1):
    X = xround(X, 10**k)
    # print(X)
print(X)
