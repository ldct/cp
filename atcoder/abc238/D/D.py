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

def and_span(total):
    ret = set()
    for x in range(total+1):
        y = total-x
        ret.add(x & y)
    return ret

def ans_slow(a, s):
    return a in and_span(s)

def ans(a, s):
    T = s - 2*a
    if T < 0: return False
    if T & a: return False
    return True

for _ in range(read_int()):
    r = ans(*read_int_tuple())
    print("Yes" if r else "No")