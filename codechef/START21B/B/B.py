#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

from itertools import permutations, chain, combinations, product
from math import factorial, gcd
from collections import Counter, defaultdict
from heapq import heappush, heappop, heapify
from bisect import bisect_left
from functools import lru_cache

### CODE HERE

def count(A, i):
    ret = 0
    for a in A:
        if a & (1 << i):
            ret += 1
    return ret

def ans(A):
    ret = 0
    for i in range(64):
        if count(A, i) >= 2:
            ret |= (1 << i)
    return ret

for _ in range(read_int()):
    input()
    print(ans(read_int_list()))