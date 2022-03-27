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

def subsets(iterable, low=0, high=None):
    "subsets([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    if high is None:
        high = len(s)
    return chain.from_iterable(combinations(s, r) for r in range(low, high+1))

### CODE HERE

def total(lst):
    X = 0
    Y = 0
    for x, y in lst:
        X += x
        Y += y
    return (X, Y)

N = read_int()
n = N // 2
xg, yg = read_int_list()
instructions1 = []
instructions2 = []

for _ in range(n):
    instructions1 += [read_int_tuple()]
for _ in range(N-n):
    instructions2 += [read_int_tuple()]

achievable = dict()

for ss in subsets(instructions1):
    t = total(ss)
    if t not in achievable:
        achievable[t] = [0]*(N+1)
    achievable[t][len(ss)] += 1

ret = [0]*(N+1)

def bump(lst, l):
    for i in range(N+1):
        if i + l < N+1:
            ret[i+l] += lst[i]

for ss in subsets(instructions2):
    t = total(ss)
    x, y = (xg - t[0], yg - t[1])
    if (x, y) in achievable:
        bump(achievable[(x, y)], len(ss))

for r in ret[1:]:
    print(r)