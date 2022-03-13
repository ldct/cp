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

print(prefs)

Q = read_int()
breeds = []
for _ in range(Q):
    breeds += [input()]

def ok(p):
    for i in range(N):
        if p[i] not in prefs[i]: return False
    return True

ok_permutations = [p for p in permutations(list(range(N))) if ok(p)]

def ok_swap(p, b):
    for i in range(N):
        if b[i] != b[p[i]]: return False
    return True

def count(b):
    ret = 0
    for p in ok_permutations:
        if ok_swap(p, b):
            ret += 1
    return ret

for b in breeds:
    print(count(b))
