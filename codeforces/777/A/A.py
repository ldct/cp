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

def ans(n):
    if n == 1: return 1
    if n == 2: return 2
    ret = [1]
    while sum(ret) <= n:
        ret += [3 - ret[-1]]
    if sum(ret) > n:
        ret = ret[0:-1]

    if n == sum(ret):
        s = ''.join(map(str, ret))
        return max(
            int(s),
            int(s[::-1])
        )

    ret = [3 - r for r in ret]
    assert(sum(ret) == n)

    s = ''.join(map(str, ret))
    return max(
        int(s),
        int(s[::-1])
    )

for _ in range(read_int()):
    print(ans(read_int()))