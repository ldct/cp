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

def f(a):
    if a % 10 == 0: return a
    while a % 10 != 8:
        if a % 10 == 0: return a
        a += a % 10
    return a

def ans(arr):
    arr = [f(a) for a in arr]
    
    ZEROES = [a//10 for a in arr if a % 10 == 0]
    EIGHTS = [(a - 8) // 10 for a in arr if a % 10 == 8]

    if len(EIGHTS) > 0 and len(ZEROES) > 0: return "NO"

    if len(EIGHTS) == 0:
        return "YES" if len(set(ZEROES)) <= 1 else "NO"

    if len(ZEROES) == 0:
        EIGHTS = [x % 2 for x in EIGHTS]
        return "YES" if len(set(EIGHTS)) <= 1 else "NO"

    assert(False)
    return arr

def loop(x):
    x += x % 10
    while x % 10 != 9:
        x += x % 10
    return x

print(loop(9))

for _ in range(read_int()):
    input()
    print(ans(read_int_list()))