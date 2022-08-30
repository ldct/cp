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

N, C = read_int_list()

events = []

for _ in range(N):
    a, b, c = read_int_tuple()
    events += [(a, c)]
    events += [(b+1, -c)]

events.sort()

last_x = None
curr_cost = 0
ret = 0

for x, delta in events:
    if last_x is not None and x != last_x:
        cost = min(curr_cost, C)
        ret += cost * (x - last_x)
        # print(f"process [{last_x}, {x})", curr_cost)

    curr_cost += delta

    last_x = x

print(ret)