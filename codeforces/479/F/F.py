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
arr = read_int_list()

dp = dict()
for i, a in enumerate(arr):
    longest = 1

    if a-1 in dp:
        longest = 1 + dp[a-1]

    dp[a] = longest

ret_l = 0
ret_start = None
for k in dp:
    if dp[k] > ret_l:
        ret_l = dp[k]
        ret_start = k

arr = arr[::-1]
target = ret_start
ret = []

for i, a in enumerate(arr):
    if a == target:
        ret += [len(arr) - i]
        target -= 1

assert(ret_l == len(ret))
ret = ret[::-1]
print(ret_l)
print(*ret)