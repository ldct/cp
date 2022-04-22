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

def good(arr):
    return len(set([a % 2 for a in arr])) <= 1

def ans(arr):
    odd = []
    even = []

    for i, a in enumerate(arr):
        if i % 2 == 0:
            even += [a]
        else:
            odd += [a]

    if good(even) and good(odd): return "YES"
    return "NO"

for _ in range(read_int()):
    input()
    print(ans(read_int_list()))