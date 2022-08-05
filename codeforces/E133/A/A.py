#!/usr/bin/env python3

import io, os, sys
import itertools
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

def ans_slow(n):
    m = (n // 3) + 2

    ret = float("inf")

    for p in itertools.product([0, +3, -3, +2, -2], repeat=m):
        if sum(p) == n:
            ret = min(ret, len([x for x in p if x != 0]))

    return ret

def ans_small(n):
    ret = float("inf")
    for first_step in [+3, -3, +2, -2]:
        new_n = abs(n + first_step)
        if new_n % 3 == 0:
            ret = min(ret, 1 + (new_n // 3))
        if new_n % 2 == 0:
            ret = min(ret, 1 + (new_n // 2))
    return ret

def ans(n):
    if n < 10: return ans_small(n)

    ret = ans_small(n)
    for first_step in itertools.product([+3, +2], repeat=2):
        new_n = n - sum(first_step)
        if new_n % 3 == 0 and new_n > 0:
            ret = min(ret, 2 + (new_n // 3))
    return ret

if False:
    print(ans(10))
elif False:
    for t in range(1, 30):
        assert(ans(t) == ans_slow(t))
else:
    for _ in range(read_int()):
        print(ans(read_int()))