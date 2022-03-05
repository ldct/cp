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

def knapsack(capacity, items):

    dp = [0]*(capacity+1)

    for (w, v) in items:
        # print(dp, w, v)
        for curr_weight in range(capacity+1, -1, -1):
            new_weight = curr_weight + w
            if new_weight <= capacity:
                dp[new_weight] = max(dp[new_weight], dp[curr_weight] + v)
    return dp

N, W = read_int_tuple()
items = []
for _ in range(N):
    w, v = read_int_tuple()
    items += [(w, v)]

p = knapsack(W, items)
print(max(p))