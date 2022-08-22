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

input()
A = sorted(read_int_list())

def cost(x):
    return sum((a - x)**2 for a in A)

# ternary search for minimum
l = min(A)
r = max(A)
while r - l >= 5:
    m1 = l + (r - l) // 3
    m2 = r - (r - l) // 3
    f1 = cost(m1)      
    f2 = cost(m2)
    if (f1 > f2):
        l = m1
    else:
        r = m2

print(min(cost(x) for x in range(l, r+1)))
# print(A, l, r)