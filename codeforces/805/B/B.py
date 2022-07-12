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

def ans(x):
    i = 0
    ret = 0
    need = set()

    while i < len(x):
        if x[i] in need:
            i += 1
            continue
        if len(need) == 3:
            ret += 1
            need = set()
        need.add(x[i])
        i += 1
    if len(need):
        ret += 1
    return ret

for _ in range(read_int()):
    print(ans(input()))