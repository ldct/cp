#!/usr/bin/env pypy3

import io, os
from sys import stdin, stdout

# input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline
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

recipe = Counter(input())
recipe = (recipe['B'], recipe['S'], recipe['C'])
pieces = read_int_list()
prices = read_int_tuple()
budget = read_int()

ret = 0
while True:
    need = []
    for i in range(3): need += [max(0, recipe[i] - pieces[i])]

    if sum(need) == 0:
        for i in range(3): pieces[i] -= recipe[i]
        ret += 1
    else:
        cost = 0
        for i in range(3): cost += need[i] * prices[i]

        if sum(need) == sum(recipe):
            ret += budget // cost
            break
        elif cost <= budget:
            budget -= cost
            for i in range(3): pieces[i] += need[i]
        else:
            break

print(ret)