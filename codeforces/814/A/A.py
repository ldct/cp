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

@lru_cache(None)
def p1_wins_slow(a, b):
    if (a, b) == (1, 1):
        return False

    for x in range(a+1):
        if not (x % 2 == 1): continue
        aa = a - x
        bb = b

        if not p1_wins_slow(aa, bb): return True

    for y in range(b+1):
        if not (y % 2 == 1): continue
        aa = a
        bb = b - y

        if not p1_wins_slow(aa, bb): return True

    return False

def p1_wins(a, b):
    if a == 1:
        if b % 2 == 0: return True
        if b == 1: return False
        if b == 3: return False
        return False

    if a % 2 == 0:
        if a == 2: return not p1_wins(1, b)

        if p1_wins(1, b):
            return False
        else:
            return True

    if a % 2 == 1:
        if p1_wins(1, b):
            return True
        else:
            return False

if False:
    print(p1_wins_slow(1, 5))
    print(p1_wins(1, 5))
elif False:
    for a in range(1, 20):
        for b in range(1, 20):
            if p1_wins_slow(a, b) != p1_wins(a, b):
                print(a, b)
else:
    for _ in range(read_int()):
        x = p1_wins(*read_int_list())
        if x is True:
            print('Burenka')
        elif x is False:
            print("Tonya")
        else:
            print(x)
