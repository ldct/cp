#!/usr/bin/env python3

import io, os, sys
from random import random, randint
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

HASH_SPACE = 32

@lru_cache(None)
def hash(e):
    return randint(1, 1 << HASH_SPACE)

# Zobrist set
class ApproximateEqualitySet:
    def __init__(self):
        self.raw_value = 0
        self.elems = set()

    def insert(self, e):
        if e in self.elems: return
        self.elems.add(e)
        self.raw_value ^= hash(e)

input()
A = read_int_list()
B = read_int_list()

s = ApproximateEqualitySet()
valuesA = [0]
for a in A:
    s.insert(a)
    valuesA += [s.raw_value]

s = ApproximateEqualitySet()
valuesB = [0]
for a in B:
    s.insert(a)
    valuesB += [s.raw_value]

for _ in range(read_int()):
    l, r = read_int_list()
    print("Yes" if valuesA[l] == valuesB[r] else "No")