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


def ans_fast(A):
    # https://wyy603.github.io/2019/01/22/NOIP2018-%E6%8F%90%E9%AB%98%E7%BB%84-%E9%A2%98%E8%A7%A3/
    N = len(A)
    lastd = 0

    d_arr = []

    for d in A:
        d_arr += [d - lastd]
        lastd = d

    d_arr += [-lastd]

    assert(sum(d_arr) == 0)
    return sum([d for d in d_arr if d > 0])

### CODE HERE

input()
A = read_int_list()
B = read_int_list()
A = list(a - b for (a, b) in zip(A, B))
print(ans_fast(A))