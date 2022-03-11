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

def ans(d, A):
    old_A = [0] + A + [d+1]

    def ok_after_deleting(mu, old_A, idx):
        if not (0 <= idx < len(old_A)): return False

        A = old_A[:]

        del A[idx]

        for i in range(len(A)-2):
            gap = A[i+1] - A[i] - 1
            if gap < mu: return False

        for i in range(len(A)-2):
            gap = A[i+1] - A[i] - 1
            if gap >= 2*mu+1: return True
        for i in range(len(A)-2, len(A)-1):
            gap = A[i+1] - A[i] - 1
            if gap >= mu+1: return True

        return False

    def ok(mu):
        A = old_A[:]
        # print(A)

        need_to_delete = []
        for i in range(len(A)-2):
            gap = A[i+1] - A[i] - 1
            if gap < mu:
                need_to_delete += [i+1]
        if len(need_to_delete) == 0: return True

        if ok_after_deleting(mu, A, need_to_delete[0]):
            return True

        if ok_after_deleting(mu, A, need_to_delete[0]-1):
            return True

        return False

    low = 0
    high = d + 1

    assert(ok(low))
    assert(not ok(high))

    while high - low > 2:
        mid = (low + high) // 2
        if ok(mid):
            low = mid
        else:
            high = mid

    for mu in range(low, low+10):
        if not ok(mu):
            return mu-1

for _ in range(read_int()):
    input()
    n, d = read_int_tuple()
    A = read_int_list()
    print(ans(d, A))