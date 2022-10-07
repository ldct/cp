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

def ss_ncp(target, B):
    import array
    possible = array.array('b', [1] + [0]*target)

    for b in B:
        for mass in range(target, -1, -1):
            if possible[mass] == 1 and mass + b <= target:
                possible[mass+b] = 1
    return possible

### CODE HERE

def ans(K, A):
    A.sort()
    mA = max(A)

    def ok(i):
        # print("ok", i)
        if i >= len(A): return False

        T = K + 1
        x = A[i]
        B = list(A)
        del B[i]
        p = ss_ncp(T, B)
        good = False
        for w in range(len(p)):
            if not p[w]: continue
            if w < K <= w+x:
                good = True
        return not good

    for i in range(len(A)):
        print(i, ok(i))

    low = 0
    high = len(A)

    if not ok(low):
        return 0

    assert(ok(low))
    assert(not ok(high))


    while high - low > 2:
        mid = (low + high) // 2
        if ok(mid):
            low = mid
        else:
            high = mid

    while ok(low):
        low += 1

    return low

def assert_is_monotonic(arr):
    check = True
    for x in arr:
        if check and not x:
            check = False
        assert(check == x)

if True:
    N, K = read_int_tuple()
    A = read_int_list()

    A = [min(a, K+1) for a in A]

    ret = ans(K, A)
    print(ret)

else:
    import random
    for _ in range(10000):
        N = random.randint(2, 10)
        K = random.randint(1, 100)
        A = [random.randint(1, K+1) for _ in range(N)]
        A = [min(a, K+1) for a in A]
        sng = set(ans(K, A))
        arr = [x in sng for x in A]
        print(arr)
        assert_is_monotonic(arr)