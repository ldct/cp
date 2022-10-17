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

### CODE HERE

import random

def c(t):
    if t == 0:
        return int(20e9) * random.choice([1, -1])
    elif t == 1:
        return random.randint(1, 5e9) * random.choice([1, -1])
    elif t == 2:
        return random.randint(5e9, 10e9) * random.choice([1, -1])

N = 20
X = c(0)
Y = [c(2) for _ in range(N)]
Z = [c(1) for _ in range(N)]

print(N, X)
print(*Y)
print(*Z)