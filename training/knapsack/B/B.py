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
There are 𝑁 objects of masses 𝑚1,…,𝑚𝑁.

Output indexes of objects, for which the sum of masses is maximal, while no more than 𝑀.
"""


def find(arr, x, start):
    for i in range(start, len(arr)):
        if arr[i] == x: return i
    return -1

def is_subsequence(needle, haystack):
    current_pos = 0
    for c in needle:
        current_pos = find(haystack, c, current_pos) + 1
        if current_pos == 0:
            return False
    return True

def subsets(iterable, low=0, high=None):
    "subsets([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    if high is None:
        high = len(s)
    return chain.from_iterable(combinations(s, r) for r in range(low, high+1))

### CODE HERE

def ss_ncp(target, B):
    M = target
    import array
    possible = array.array('b', [1] + [0]*target)
    component = [0]*(target+1)

    for b in B:
        for mass in range(M, -1, -1):
            if possible[mass] == 1 and mass + b <= target and possible[mass+b] == 0:
                possible[mass+b] = 1
                component[mass+b] = b

    for i in range(target, -1, -1):
        if possible[i]: break

    bm = i

    masses = []
    while i != 0:
        masses += [component[i]]
        i -= component[i]

    indexes = defaultdict(list)
    for i, b in enumerate(B):
        indexes[b] += [i]

    masses = Counter(masses)

    ret = []
    for m in masses:
        f = masses[m]
        ret += indexes[m][0:f]

    ret.sort()

    assert(sum(B[i] for i in ret) == bm)
    assert(len(ret) == len(set(ret)))

    return ret



if False:
    target, B = 4, [2, 2]
    print(ss_ncp(target, B))
elif False:
    import random
    for _ in range(10000):
        M = random.randint(1, 1000)
        N = random.randint(1, 10)
        m = [random.randint(1, 100) for _ in range(N)]
        ss_ncp(M, m)
elif True:
    N, M = read_int_tuple()
    m = read_int_list()
    r = ss_ncp(M,m)
    print(len(r))
    print(*[x+1 for x in r])