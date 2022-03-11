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

def f(a, x):
    return x//a + (x % a)

def ans(l, r, a):
    if l == r: return f(a, l)
    ret = max(f(a, r), f(a, r-1))
    x0 = r - (r % a)

    for x in [x0-1, x0, x0+1]:
        if l <= x <= r: ret = max(ret, f(a, x))
    return ret

def ans_slow(l, r, a):
    return max(f(a, x) for x in range(l, r+1))


# import random
# for _ in range(10000):
#     a = random.randint(1, 10)
#     l = random.randint(1, 10)
#     r = random.randint(l, 10)
#     if not (ans(l, r, a) == ans_slow(l, r, a)):
#         print(l, r, a)
#         break
for _ in range(read_int()):
    print(ans(*read_int_tuple()))