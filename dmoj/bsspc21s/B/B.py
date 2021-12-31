#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

from itertools import permutations, chain, combinations
from math import factorial, gcd
from collections import Counter, defaultdict
from heapq import heappush, heappop, heapify
from bisect import bisect_left

### CODE HERE

N, K, Q = read_int_tuple()
ops = [read_int_tuple() for _ in range(K)]
points = [read_int_tuple() for _ in range(Q)]

ops = [(a-1, b-1, c-1, d-1) for a, b, c, d in ops]
points = [(x-1, y-1) for x, y in points]

def apply(x, y, a, b, c, d):
    if not (a <= x <= c): return (x, y)
    if not (b <= y <= d): return (x, y)
    x -= a
    y -= b
    x, y = (c - a - y, x)
    x += a
    y += b
    return x, y

for (a, b, c, d) in ops[::-1]:
    points = [apply(x, y, a, b, c, d) for (x, y) in points]

for (x, y) in points:
    print(x*N + y + 1)