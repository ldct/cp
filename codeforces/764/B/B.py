#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

from itertools import permutations, chain, combinations, product
from math import factorial, gcd
from collections import Counter, defaultdict
from heapq import heappush, heappop, heapify
from bisect import bisect_left
from functools import lru_cache

### CODE HERE

def ok(X, x):
    return X >= x and X % x == 0

def ok1(a, b, c):
    A = b - (c - b)
    return ok(A, a)

def ok2(a, b, c):
    B = a + c
    if B % 2 == 1: return False
    B //= 2
    return ok(B, b)

def ok3(a, b, c):
    return ok1(c, b, a)

def ans(a, b, c):
    if ok1(a, b, c): return "YES"
    if ok2(a, b, c): return "YES"
    if ok3(a, b, c): return "YES"

    return "NO"

for _ in range(read_int()):
    print(ans(*read_int_tuple()))