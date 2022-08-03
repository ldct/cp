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

def f(x):
    MODULUS = 60*24
    x %= MODULUS
    x += MODULUS
    x %= MODULUS
    return x

def ans(H, M, alarms):
    t = H*60 + M
    alarms = [h*60 + m for (h, m) in alarms]
    alarms = [a - t for a in alarms]
    alarms = [f(a) for a in alarms]
    ret = min(alarms)

    return ret // 60, ret % 60
    return alarms

for _ in range(read_int()):
    n, H, M = read_int_list()
    alarms = []
    for _ in range(n):
        alarms += [read_int_tuple()]
    print(*ans(H, M, alarms))