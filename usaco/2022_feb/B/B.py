#!/usr/bin/env pypy3

import io, os
from sys import stdin, stdout

input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline
# def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

from itertools import permutations, chain, combinations, product
from math import factorial, gcd, ceil
from collections import Counter, defaultdict, deque
from heapq import heappush, heappop, heapify
from bisect import bisect_left
from functools import lru_cache
from fractions import *

### CODE HERE

def comb(n, r):
    return factorial(n) / (factorial(r) * factorial(n-r))

def ans_fast(T, K):
    T -= 1
    weight = []
    wap = []

    for score in range(T+1):
        weight += [comb(T, score)]
        wap += [score*weight[-1]]

    pw = [0]
    pwap = [0]
    for w in weight:
        pw += [pw[-1] + w]

    for w in wap:
        pwap += [pwap[-1] + w]

    def next_state(state):

        en = 0

        c = ceil(state)

        assert(c <= T)

        en += pw[c]*state
        en += pwap[-1] - pwap[c]

        en /= (2**T)

        return en

    state = 0
    for _ in range(K):
        state = next_state(state)
    return 1+state

print(ans_fast(*read_int_tuple()))
# print(ans_fast(20, 1000000))
# print(ans_fast(20, 100000000))