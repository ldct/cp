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

"""
You are given 𝑁 objects of mass 𝑚1,…,𝑚𝑁 and cost 𝑐1,…,𝑐𝑁 respectively.

Output the indexes of objects, for which the sum of costs is maximal, while the sum of masses is no more than 𝑀.
"""

def argmax(arr):
	ret = 0
	for i, e in enumerate(arr):
		if e > arr[ret]:  ret = i
	return ret

def subsets(iterable, low=0, high=None):
    "subsets([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    if high is None:
        high = len(s)
    return chain.from_iterable(combinations(s, r) for r in range(low, high+1))

### CODE HERE

def bv_slow(m, v, M):
    ret = 0
    elems = list(zip(m, v))
    for ss in subsets(elems, low=1):
        [masses, vals] = list(zip(*ss))
        if sum(masses) <= M:
            ret = max(ret, sum(vals))
    return ret
def bv(m, v, M):
    N = len(m)
    best_value_at_mass = [float("-inf")]*(M+1)
    best_value_at_mass[0] = 0

    made_with = [None]*(M+1)
    made_with[0] = []

    for i in range(N):
        for mass in range(M, -1, -1):
            next_mass = mass + m[i]
            next_value = best_value_at_mass[mass] + v[i]

            if next_mass <= M:
                if next_value > best_value_at_mass[next_mass]:
                    best_value_at_mass[next_mass] = next_value
                    made_with[next_mass] = made_with[mass] + [i]

    ret = max(best_value_at_mass)

    mass = argmax(best_value_at_mass)
    indexes = made_with[mass]

    vals = [v[i] for i in indexes]

    if not (ret == sum(vals)):
        assert(False)

    return indexes
    return ret

if False:
    m, v, M = [1, 1], [1, 2], 3
    print(bv_slow(m, v, M))
    print(bv(m, v, M))
elif False:
    import random
    for _ in range(10000):
        M = random.randint(1, 1000)
        N = random.randint(1, 10)
        m = [random.randint(1, 10) for _ in range(N)]
        v = [random.randint(1, 10) for _ in range(N)]
        assert(bv(m, v, M) == bv_slow(m, v, M))
elif True:
    N, M = read_int_tuple()
    m = read_int_list()
    v = read_int_list()
    r = bv(m, v, M)
    r = sorted([x+1 for x in r])
    print(len(r))
    print(*r)
    # print(bv_slow(m, v, M))
