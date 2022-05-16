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

def sub(tup, d):
    tup = list(tup)
    if tup[d] >= 0: tup[d] -= 1
    return tuple(tup)

@lru_cache(None)
def count_dp(A, r):
    if r == 0:
        if 0 in A: return 0
        return 1

    ret = 0
    for d in range(10):
        ret += count_dp(sub(A, d), r-1)
    return ret

def ans(L, R, A):

    def loves(N):
        N = Counter(map(int, str(N)))
        for d in range(10):
            if N[d] == A[d]:
                return False
        return True

    def num_loves_slow(N):
        ret = 0
        for i in range(1, N):
            if loves(i):
                ret += 1
        return ret

    @lru_cache(None)
    def count0(rest):
        if rest == 0: return 0
        ret = count0(rest-1)
        for d in range(1, 10):
            ret += count([d], rest-1)
        return ret


    def count(prefix, rest):
        if set(prefix) == set([0]):
            return count0(rest)

        _A = A[:]
        for d in prefix:
            if _A[d] >= 0: _A[d] -= 1
        return count_dp(tuple(_A), rest)

    @lru_cache(None)
    def num_loves(N):
        N = list(map(int, str(N)))

        ret = 0
        for i in range(len(N)):
            prefix = N[0:i]
            x = N[i]
            rest = len(N) - len(prefix) - 1

            for j in range(x):
                r = count(prefix + [j], rest)
                ret += r

        return ret

    return num_loves(R+1) - num_loves(L)

for _ in range(read_int()):
    L, R = read_int_tuple()
    A = read_int_list()
    assert(len(A) == 10)

    print(ans(L, R, A))