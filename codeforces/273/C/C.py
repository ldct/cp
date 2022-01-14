#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
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

@lru_cache(None)
def ans_slow(r, g, b):
    ret = 0
    if r > 0 and g > 0 and b > 0:
        ret = max(ret, 1 + ans_slow(r-1, g-1, b-1))
    for p in permutations([r, g, b]):
        x, y, z = p
        if x >= 1 and y >= 2:
            ret = max(ret, 1 + ans_slow(x-1, y-2, z))
    return ret

def ans_greedy(r, g, b):
    if r == g and g == b: return r
    [r, g, b] = sorted([r, g, b])
    ret = 0
    if b >= 2 and g >= 1:
        ret = max(ret, 1 + ans_slow(r, g-1, b-2))
    return ret

for r in range(50):
    for g in range(50):
        for b in range(50):
            if not (ans_greedy(r, g, b) == ans_slow(r, g, b)):
                print(r, g, b)
