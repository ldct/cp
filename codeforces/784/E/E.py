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

def match(a, b):
    if a[0] == b[0] and a[1] != b[1]: return True
    if a[0] != b[0] and a[1] == b[1]: return True
    return False

def ans(lst):
    s = list(set(lst))
    c = Counter(lst)

    ret = 0

    for i in range(len(s)):
        for j in range(i, len(s)):
            a = s[i]
            b = s[j]
            if not match(a, b): continue
            ret += c[a]*c[b]
    return ret

for _ in range(read_int()):
    print(ans([input() for _ in range(read_int())]))