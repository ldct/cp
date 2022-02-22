#!/usr/bin/env pypy3

import io, os
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

A, B, C, D = read_int_list()

@lru_cache(None)
def is_prime(N):
    for i in range(2, N):
        if N % i == 0: return False
    return True

def p1_wins_x(x):
    for y in range(C, D+1):
        if is_prime(x + y): return False
    return True

def p1_wins():
    for x in range(A, B+1):
        if p1_wins_x(x):
            return True
    return False
print("Takahashi" if p1_wins() else "Aoki")