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

sys.setrecursionlimit(10000)

N, X = read_int_list()
Y = read_int_list()
Z = read_int_list()

TARGET = 0
ORIGIN = 1
WALL = 2
KEY = 3

items = [(X, TARGET), (0, ORIGIN)]
for i, y in enumerate(Y):
    items += [(y, WALL, i)]

for i, z in enumerate(Z):
    items += [(z, KEY, i)]

items.sort()

def pos(item):
    return item[0]

def kind(item):
    return item[1]

def sig(item):
    return item[2]

def dist(x, y):
    return abs(pos(items[x]) - pos(items[y]))

idx_of_key = dict()

for i, item in enumerate(items):
    if kind(item) == KEY:
        idx_of_key[sig(item)] = i

@lru_cache(None)
def ans(a, b, is_left):
    curr_pos = b
    if is_left:
        curr_pos = a

    if kind(items[curr_pos]) == TARGET:
        return 0

    ret = float("inf")
    aa = a-1

    if aa >= 0:
        item = items[aa]

        cost = dist(curr_pos, aa)
        assert(cost > 0)

        ok = True
        if kind(item) == WALL and not (a <= idx_of_key[sig(item)] <= b):
            ok = False

        if ok:
            ret = min(ret, cost + ans(aa, b, True))

    bb = b+1
    if bb < len(items):
        item = items[bb]

        cost = dist(curr_pos, bb)
        assert(cost > 0)

        ok = True
        if kind(item) == WALL and not (a <= idx_of_key[sig(item)] <= b):
            ok = False

        if ok:
            ret = min(ret, cost + ans(a, bb, False))

    return ret

i = items.index((0, ORIGIN))
# print("origin i=", i)
ret = ans(i, i, i)

if ret == float("inf"):
    ret = -1

print(ret)