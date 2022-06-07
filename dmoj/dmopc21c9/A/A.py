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

input()
A = read_int_list()

constraints = [0, float("inf")]

def constrain(c, d):
    if d == -1:
        constraints[1] = min(constraints[1], c)
    else:
        constraints[0] = max(constraints[0], -c)

c = A[0]
d = -1
constrain(c, d)

for a in A[1:]:
    c = a - c
    d *= -1
    constrain(c, d)

[c, d] = constraints
print(max(0, d - c - 1))
