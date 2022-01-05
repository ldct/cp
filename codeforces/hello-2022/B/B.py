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

def ans(low, high, costs, left, right):
    ret = float("inf")
    if (low, high) in costs:
        ret = costs[(low, high)]

    ret = min(ret,
        left[low] + right[high]
    )

    return ret

def insert(d, k, v):
    if k not in d:
        d[k] = v
    else:
        d[k] = min(d[k], v)

for _ in range(read_int()):
    N = read_int()
    costs = dict()
    left = dict()
    right = dict()

    low = float("inf")
    high = float("-inf")

    for _ in range(N):
        l, r, c = read_int_tuple()

        key = (l, r)
        low = min(l, low)
        high = max(r, high)

        insert(costs, key, c)
        insert(left, l, c)
        insert(right, r, c)

        print(ans(low, high, costs, left, right))
