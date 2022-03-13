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

def happy(arr, x):
    x = arr.index(x)
    return set(arr[:x+1])

### CODE HERE

N = read_int()
prefs = []
for i in range(N):
    pref = [x-1 for x in read_int_list()]
    prefs += [happy(pref, i)]

Q = read_int()
colours = []
for _ in range(Q):
    colours += [input()]

@lru_cache(None)
def dp(unassigned, colour):
    if len(unassigned) == 0: return 1
    i = N - len(unassigned)
    ret = 0
    for h in prefs[i] & unassigned:
        if colour[h] == colour[i]:
            ret += dp(unassigned - frozenset([h]), colour)
    return ret

for c in colours:
    print(dp(frozenset(range(N)), c))
