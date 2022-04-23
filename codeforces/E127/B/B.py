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

def ans(arr):
    left = arr[0] + 1
    right = arr[-1] - 1

    if not (left <= right): return "YES"
    sz = right - left + 1

    if sz <= len(arr): return "YES"
    return "NO"

for _ in range(read_int()):
    input()
    print(ans(read_int_list()))