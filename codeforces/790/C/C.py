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

def dc(a, b):
    a = ord(a)
    b = ord(b)
    return abs(a - b)

def dist(A, B):
    return sum(dc(a, b) for (a, b) in zip(A, B))

def ans(strings):
    ret = float("inf")
    for i in range(len(strings)):
        for j in range(i+1, len(strings)):
            ret = min(ret, dist(strings[i], strings[j]))

    return ret

for _ in range(read_int()):
    n, m = read_int_tuple()
    strings = [input() for _ in range(n)]
    print(ans(strings))
