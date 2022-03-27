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

def ok(arr, t):
    if t < 0: return False
    arr = arr[:]
    for i in range(len(arr)-1):
        sub = arr[i] - t
        if sub < 0: return False
        arr[i] -= sub
        arr[i+1] -= sub

    for a in arr:
        if a != t: return False
    return True

def ans_even(arr):
    high = max(arr)+1
    low = 0

    if not ok(arr, low): return -1
    assert not ok(arr, high)

    while high - low > 2:
        mid = (low + high) // 2
        if ok(arr, mid):
            low = mid
        else:
            high = mid

    for t in range(high, high-10, -1):
        if (ok(arr, t)):
            return sum(arr) - t*len(arr)
    return -1

def ans_odd(arr):
    t = 0
    for i, a in enumerate(arr[0:-1]):
        t += (-1)**((i+1) % 2)*a
    g = arr[-1] - t
    if ok(arr, g):
        return sum(arr) - g*len(arr)
    return -1

def ans(arr):
    if len(arr) % 2 == 1:
        return ans_odd(arr)
    return ans_even(arr)

for _ in range(read_int()):
    input()
    print(ans(read_int_list()))