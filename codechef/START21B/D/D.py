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

def med_sum(arr):
    arr.sort()
    return len(arr)*arr[(len(arr)-1)//2]

import random

valid = []
for _ in range(10000):
    arr = [random.randint(0, 5) for _ in range(5)]
    if med_sum(arr) == sum(arr):
        valid += [sorted(arr)]

for arr in valid:
    print(arr)