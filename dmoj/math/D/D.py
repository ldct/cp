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

import math

### CODE HERE

N = read_int()

def area(y):
    if y < 0:
        return math.pi - area(-y)
    theta = 2*math.acos(y)
    return 0.5 * (theta - math.sin(theta))

def search(target):
    low = 1.0
    high = -1.0

    while low - high > 10e-10:
        mid = (low + high) / 2
        if area(mid) <= target:
            low = mid
        else:
            high = mid

    return (low + high) / 2

a = math.pi / N
areas = [a*i for i in range(1, N)]

s = [search(a) for a in areas]
s = sorted(s)
for l in s:
    print(l)