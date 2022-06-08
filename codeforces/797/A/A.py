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

def ans(n):

    a, b, c = n+1, n+2, n

    e = ((a + b + c) - n) // 3

    a -= e
    b -= e
    c -= e
    
    while (a + b + c) - n > 3:
        a -= 1
        b -= 1
        c -= 1

    while (a + b + c) != n:
        if c > 1:
            c -= 1
        elif a > 1:
            a -= 1

    print(a, b, c)

for _ in range(read_int()):
    ans(read_int())