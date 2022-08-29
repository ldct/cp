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

def ans(arr):
    if arr[0] != 1: return [-1]
    last = 0
    for a in arr:
        if a != last and a != last+1:
            return [-1]
        last = a

    c = Counter(arr)

    d = defaultdict(list)

    i = 1
    for a in arr:
        d[a] += [i]
        i += 1

    for k in d:
        d[k] = d[k][::-1]

    ret = []
    for k in sorted(d.keys()):
        ret += d[k]
    return ret

input()
print(*ans(read_int_list()))