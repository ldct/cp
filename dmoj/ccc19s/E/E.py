#!/usr/bin/env pypy3

import io, os
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

TESTING = False

if TESTING:
    import random
    N = 100
    triangle = []
    for _ in range(N):
        triangle += [[random.randint(0, 1) for _ in range(N)]]
else:
    N, K = read_int_tuple()
    triangle = []
    for _ in range(N):
        triangle += [read_int_list()]

    # import sys
    # sys.exit(0)


@lru_cache(None)
def maxSqLg(x, y, lg):
    if lg == 0:
        return triangle[x][y]
    d = 2**(lg-1)
    return max(
        maxSqLg(x, y, lg-1),
        maxSqLg(x+d, y, lg-1),
        maxSqLg(x, y+d, lg-1),
        maxSqLg(x+d, y+d, lg-1)
    )

@lru_cache(None)
def maxTriLg(x, y, lg):
    if lg == 0:
        return triangle[x][y]
    d = 2**(lg-1)
    return max(
        maxTriLg(x, y, lg-1),
        maxSqLg(x+d, y, lg-1),
        maxTriLg(x+d, y+d, lg-1)
    )

def maxSq(x, y, D):
    if D == 1:
        return triangle[x][y]
    assert(D > 1)
    i = 0
    while 2**i <= D:
        i += 1
    i -= 1
    assert(2**i <= D)

    d = D - 2**i

    if d == 0:
        return maxSqLg(x, y, i)

    return max(
        maxSqLg(x, y, i),
        maxSqLg(x + d, y, i),
        maxSqLg(x, y + d, i),
        maxSqLg(x + d, y + d, i)
    )

def maxSqBL(x, y, D):
    return -1

def maxTri(x, y, D):

    if D == 1:
        return triangle[x][y]
    assert(D > 1)
    i = 0
    while 2**i <= D:
        i += 1
    i -= 1
    assert(2**i <= D)

    d = D - 2**i

    if d == 0:
        return maxTriLg(x, y, i)

    return max(
        maxTriLg(x, y, i),
        maxSqBL(x, y, d),
        maxTriLg(x + d, y, i),
    )

if TESTING:
    # x, y, D = 2, 1, 2
    # print(maxSq_slow(x, y, D))
    # print(maxSq(x, y, D))
    for _ in range(1000):
        x = random.randint(1, N//2)
        y = random.randint(1, N//2)
        D = random.randint(1, N//2)
        assert(maxSq_slow(x, y, D) == maxSq(x, y, D))
else:
    ret = 0
    for x in range(N-K+1):
        for y in range(x+1):
            # print(x, y, maxTri(x, y, K))
            ret += maxTri(x, y, K)

    print(ret)