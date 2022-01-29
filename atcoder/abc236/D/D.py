#!/usr/bin/env pypy3

import io, os
from sys import stdin, stdout

input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline
# def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

from itertools import permutations, chain, combinations, product
from math import factorial, gcd
from collections import Counter, defaultdict
from heapq import heappush, heappop, heapify
from bisect import bisect_left
from functools import lru_cache

### CODE HERE

def subsets(iterable, low=0, high=None):
    "subsets([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    if high is None:
        high = len(s)
    return chain.from_iterable(combinations(s, r) for r in range(low, high+1))


def ans(N, A):
    @lru_cache(None)
    def dp(ss):
        if len(ss) == 0:
            return [0]

        ret = []
        ss = list(ss)
        for i in range(1, len(ss)):
            for val in dp(frozenset(ss) - frozenset([ss[0], ss[i]])):
                ret += [val^score(ss[0], ss[i])]

        return ret

    peeps = list(range(1, 2*N+1))

    def score(a, b):
        [a, b] = sorted([a, b])
        return A[a-1][b-a-1]

    return dp(frozenset(peeps))
    # return max(dp(frozenset(peeps)))

def ans_slow(N, A):
    ret = 0

    peeps = list(range(1, 2*N+1))

    for p in subsets(peeps, low=N, high=N):
        q = set(peeps) - set(p)
        for pp in permutations(p):
            for qq in permutations(q):
                candidate = 0
                for aa, bb in zip(pp, qq):
                    a, b = min(aa, bb), max(aa, bb)
                    candidate = candidate^A[a-1][b-a-1]
                ret = max(ret, candidate)
    return ret

if True:
    N = read_int()
    A = [read_int_list() for _ in range(2*N-1)]
    print(max(ans(N, A)))
else:
    for _ in range(1):
        import random
        N = 8
        M = 2*N-1
        A = [[random.randint(0,5) for _ in range(M-i)] for i in range(M)]
        print(max(ans(N, A)))
