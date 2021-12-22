#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

from itertools import permutations, chain, combinations
from math import factorial, gcd
from collections import Counter, defaultdict
from heapq import heappush, heappop, heapify
from bisect import bisect_left

def subsets(iterable, low=0, high=None):
    "subsets([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    if high is None:
        high = len(s)
    return chain.from_iterable(combinations(s, r) for r in range(low, high+1))

### CODE HERE

def gen(a, b, c):
    return sorted([a, b, c, a+b, b+c, a+c, a+b+c])

lst = sorted(read_int_list())
for candidate in permutations(lst):
    a, b, c = candidate[0:3]
    if not (a <= b <= c): continue
    if lst == gen(a, b, c):
        print(a, b, c)
        break
