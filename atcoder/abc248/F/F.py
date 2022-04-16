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

N, P = read_int_tuple()

def ans(i, d, has_leak):

    # number of subgraphs of [0...i] with given missing edges

    if d < 0: return 0
    if i == 0:
        if d == 1 and has_leak:
            return 1
        if d == 0 and not has_leak:
            return 1
        return 0

    ret = 0

    # add a complete cap
    ret += ans(i-1, d, False)
    # add a _|
    ret += 2*ans(i-1, d-1, False)

    # add a =
    ret += ans(i-1, d-1, has_leak)


    # add a leak
    if has_leak:
        ret += 2*ans(i-1, d-2, True)

    return ret

# print(ans(N-1, 0, True) + ans(N-1, 1, False))

print(ans(N-2, 2, False))
# print(ans(N-1, 1, True) + ans(N-1, 2, False))

# print(ans(N-1, 2, True) + ans(N-1, 3, False))