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

def interleve(a: list, b):
    ret = []
    a = list(a)
    b = list(b)
    while len(b):
        ret += [a.pop(), b.pop()]
    ret += [a.pop()]
    return ret

S = list(input())[::-1]
g = len(S) - 1
ret = 0
for scheme in product(["+", ""], repeat=g):
    ret += eval(''.join(interleve(S, scheme)))
print(ret)