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

def ans(A, K):
    N = len(A)

    visited = set()
    curr = 0
    order = []
    while curr not in visited:
        order += [curr]
        visited.add(curr)
        curr += A[curr]
        curr %= N

    lp = curr
    period = len(order) - order.index(curr)

    increment = 0
    curr = lp
    for _ in range(period):
        increment += A[curr]
        curr += A[curr]
        curr %= N

    # print("period=", period, "lp=", lp, "increment=", increment)

    curr = 0
    ret = 0
    while K > 0:
        if curr == lp and (K // period > 0):
            rounds = K // period
            K -= rounds*period
            ret += rounds*increment

            continue

        ret += A[curr]
        curr += A[curr]
        curr %= N

        K -= 1

    return ret

def ans_slow(A, K):
    N = len(A)
    ret = 0
    curr = 0
    for _ in range(K):
        # print("add", A[curr])
        ret += A[curr]
        curr += A[curr]
        curr %= N
    return ret


# print(ans_slow(A, K))
# print(ans(A, K))

N, K = read_int_tuple()
A = read_int_list()

print(ans(A, K))