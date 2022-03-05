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


def knapsack2(capacity, MAX_VAL, items):

    dp = [float("inf")]*(MAX_VAL+1)
    dp[0] = 0

    for (w, v) in items:
        for curr_value in range(MAX_VAL+1, -1, -1):
            new_value = curr_value + v
            if new_value <= MAX_VAL:
                dp[new_value] = min(dp[new_value], dp[curr_value] + w)

    ret = []
    for v in range(len(dp)):
        if dp[v] <= capacity:
            ret += [v]
    return max(ret)

N, W = read_int_tuple()
MAX_VAL = 0
items = []
for _ in range(N):
    w, v = read_int_tuple()
    items += [(w, v)]
    MAX_VAL += v

p = knapsack2(W, MAX_VAL, items)
print(p)