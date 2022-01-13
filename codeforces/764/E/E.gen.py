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

import random

### CODE HERE

N = 300

print(1)
print(N, N)

for _ in range(N):
    print(''.join(map(str, [random.randint(0, 9) for _ in range(N)])))
print(''.join(map(str, [random.randint(0, 9) for _ in range(N)])))
