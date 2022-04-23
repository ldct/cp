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

def ans(X, A):
    A.sort()

    a0 = sum(A)
    d = len(A)

    pA = [0]
    for a in A:
        pA += [pA[-1] + a]

    def days(n):
        # for how many days can you buy the first n items
        a0 = pA[0]

        def cost(r):
            return pA[n] + n*r

        r = 0
        def ok(r):
            return cost(r) <= X

        low = r
        high = X
        if not ok(low): return 0

        assert(ok(low))
        assert(not ok(high))

        while high - low > 2:
            mid = (low + high) // 2
            if ok(mid):
                low = mid
            else:
                high = mid

        r = low - 1
        while cost(r) <= X:
            r += 1

        return r

    d = [days(x) for x in range(1, len(A)+1)]

    return sum(d)

for _ in range(read_int()):
    N, X = read_int_tuple()
    A = read_int_list()
    print(ans(X, A))