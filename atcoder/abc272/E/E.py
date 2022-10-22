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

def val(A, i, m):
    return A[i] + (i+1)*(m+1)

def mex(A):
    if len(A) == 0:
        return 0
    sA = set(A)
    for i in range(0, max(A+[0])+10):
        if i not in sA:
            return i
    assert(False)

def ans(A, M):
    N = len(A)

    entry_time = [(-a) / (i+1) for (i, a) in enumerate(A)]

    entry_time = [max(0, int(e - 1)) for e in entry_time]

    entries = []
    for _ in range(M+1):
        entries += [[]]

    for i, e in enumerate(entry_time):
        if e < len(entries):
            entries[e] += [i]

    ret = []
    active_indexes = set()
    for m in range(M):
        for idx in entries[m]:
            active_indexes.add(idx)

        ei2 = set(active_indexes)

        for idx in ei2:
            if val(A, idx, m) > N:
                active_indexes.remove(idx)

        print(m, active_indexes)

        active_values = [val(A, i, m) for i in active_indexes]

        ret += [mex(active_values)]

    return ret


def ans_slow(A, M):
    N = len(A)

    ret = []
    for m in range(M):
        active_values = [val(A, i, m) for i in range(N)]
        ret += [mex(active_values)]

    return ret

if False:
    tc = [-4, -4, 10]
    print(ans_slow(tc, 6))
    print(ans(tc, 6))
elif False:
    import random

    for _ in range(10000):
        N = 3
        M = 2*N

        tc = [random.randint(-10, 10) for _ in range(N)]

        if not (ans_slow(tc, M) == ans(tc, M)):
            print(tc)
            assert(False)

elif True:
    N, M = read_int_tuple()
    A = read_int_list()
    for r in ans(A, M):
        print(r)