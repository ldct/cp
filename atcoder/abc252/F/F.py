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

N, L = read_int_list()
A = read_int_list()

if L > sum(A):
    A += [L - sum(A)]

heapify(A)

ret = 0

while len(A) > 1:
    a = heappop(A)
    b = heappop(A)
    # print("merge", a, b)
    ret += (a + b)
    heappush(A, a+b)

print(ret)