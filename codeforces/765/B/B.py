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

def ans(arr):
    positions = defaultdict(list)

    for i, a in enumerate(arr):
        positions[a] += [i]

    smallest_gap = float("inf")

    for k in positions:
        if len(positions[k]) == 0: continue
        p = positions[k]
        p.sort()
        for i in range(len(p)-1):
            smallest_gap = min(smallest_gap, p[i+1] - p[i])

    if smallest_gap == float("inf"): return -1
    return len(arr) - smallest_gap

for _ in range(read_int()):
    input()
    print(ans(read_int_list()))