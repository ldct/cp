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

A,B,C,D,E,F,X = read_int_tuple()

def f(b, a, c):
    ret = 0

    deltas = ([a]*b + [0]*c) * 100

    return sum(deltas[:X])

if f(A, B, C) == f(D, E, F):
    print("Draw")
elif f(A, B, C) > f(D, E, F):
    print("Takahashi")
else:
    print("Aoki")