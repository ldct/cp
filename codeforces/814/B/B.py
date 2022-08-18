#!/usr/bin/env python3

import io, os, sys
import re
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

def spit(a, b, k):
    if ((a+k)*b) % 4 == 0:
        return a, b
    if ((b+k)*a) % 4 == 0:
        return b, a
def ans(n, k):
    if k % 2 == 1:
        print("YES")
        for i in range(n // 2):
            print(2*i+1, 2*i+2)
        return
    if k % 4 == 0:
        print('NO')
        return
    if k % 2 == 0:
        print('YES')
        for i in range(n // 2):
            a, b = spit(2*i+1, 2*i+2, k)
            print(a, b)
        return
    assert(False)

if True:
    for _ in range(read_int()):
        ans(*read_int_list())