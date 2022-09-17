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

ratios = [read_int_tuple() for _ in range(read_int())]

def cdiv(x, y):
    # ceil(x / y)
    return x // y if x % y == 0 else x // y + 1

def cmod(x, M):
    # starting from x, search for the smallest multiple of M
    return M*cdiv(x, M)

a, b = ratios[0]
for x, y in ratios[1:]:
    if a/b <= x/y:
        b = cmod(b, y)
        a = b*x//y
    else:
        a = cmod(a, x)
        b = a*y//x
print(a+b)
