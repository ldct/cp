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
from bisect import bisect_left, bisect_right
from functools import lru_cache

# 1091ms on https://judge.yosupo.jp/problem/static_range_frequency

# tag: range frequency query
# query: range frequency

class RangeFreq():
    def __init__(self, arr):
        self.store = defaultdict(list)
        for i, a in enumerate(arr):
            self.store[a] += [i]
    def query(self, left, right, element):
        a = bisect_left(self.store[element], left)
        b = bisect_right(self.store[element], right)
        return b - a

### CODE HERE

N, Q = read_int_tuple()
A = read_int_list()

engine = RangeFreq(A)

for _ in range(Q):
    l, r, x = read_int_tuple()
    print(engine.query(l, r-1, x))