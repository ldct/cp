#!/usr/bin/env pypy3

import io, os
from sys import stdin, stdout

input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline
# def input(): return stdin.readline().strip()
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

def ans_slow(a, b):
    worklist = deque([(a, b, 0)])

    while True:
        a, b, r = worklist[0]
        worklist.popleft()
        if a == b: return r
        worklist.append((a+1, b, r+1))
        worklist.append((a, b+1, r+1))
        worklist.append((a|b, b, r+1))

def ans1(a, b):
    ret = 0
    while a|b != b:
        b += 1
        ret += 1
    if a != b:
        ret += 1
    return ret

def ans2(a, b):
    ret = 0
    while a|b != b:
        a += 1
        ret += 1
    if a != b:
        ret += 1
    return ret

def ans(a, b):
    return min(
        b-a,
        ans1(a, b),
        ans2(a, b)
    )



# for b in range(2, 20):
#     for a in range(1, b):
#         if not (ans(a, b) == ans_slow(a, b)):
#             print(a, b)

for _ in range(read_int()):
    print(ans(*read_int_tuple()))